#!/usr/bin/env python3
"""
Coach Loop — 24/7 skills learning bot for PAIOS.

Continuously searches YouTube tutorials, extracts skills from transcripts,
and distributes them to agents based on their niche.

Usage:
    python coach_loop.py              # run one cycle
    python coach_loop.py --daemon     # run continuously (24/7)
    python coach_loop.py --status     # show agent skill status
    python coach_loop.py --request <agent> <topic>  # request a skill
"""

import os
import sys
import json
import time
import subprocess
from datetime import datetime
from pathlib import Path

# --- Configuration ---
PAIOS_ROOT = Path(os.environ.get("PAIOS_ROOT", Path.home() / "paios"))
SKILLS_DIR = PAIOS_ROOT / "skills"
COACH_DIR = SKILLS_DIR / "local" / "paios-core" / "coach"
LOG_FILE = COACH_DIR / "coach.log"
CYCLE_INTERVAL = int(os.environ.get("COACH_INTERVAL_MIN", "30"))  # minutes

# Agent niche mapping
AGENTS = {
    "hermes-orchestrator": {"niche": "orchestration", "skills": []},
    "Citadel": {"niche": "security", "skills": []},
    "AI-Ops-Vault": {"niche": "secrets", "skills": []},
    "evelyn-brain": {"niche": "memory", "skills": []},
    "PROMPT-GUIDE-AI": {"niche": "prompts", "skills": []},
    "github-sync": {"niche": "repo-sync", "skills": []},
    "skill-ecosystem": {"niche": "skill-management", "skills": []},
    "integration-orchestrator": {"niche": "cross-bot-sync", "skills": []},
    "system-hardening": {"niche": "security-fixes", "skills": []},
    "composio": {"niche": "integrations", "skills": []},
}

# Known learning sources (repos to pull skills from)
LEARNING_SOURCES = {
    "fleetbase": {
        "repo": "https://github.com/fleetbase/fleetbase",
        "niche": "logistics",
        "agents": ["composio"],
    },
    "youtube-shorts-pipeline": {
        "repo": "https://github.com/rushindrasinha/youtube-shorts-pipeline",
        "niche": "media-content",
        "agents": ["composio", "skill-ecosystem", "integration-orchestrator", "evelyn-brain"],
    },
    "agent-reach": {
        "repo": "https://github.com/Panniantong/Agent-Reach",
        "niche": "research",
        "agents": ["composio", "hermes-orchestrator", "integration-orchestrator", "evelyn-brain", "AI-Ops-Vault", "skill-ecosystem"],
    },
}

# Search topics per niche (YouTube search queries)
SEARCH_QUERIES = {
    "orchestration": ["multi-agent orchestration tutorial", "hermes agent workflow", "AI agent coordination"],
    "security": ["zero trust security tutorial", "threat detection AI", "cybersecurity best practices 2024"],
    "secrets": ["API key management", "credential storage secrets", "encrypted config management"],
    "memory": ["AI memory system tutorial", "vector database RAG", "semantic search AI"],
    "prompts": ["prompt engineering tutorial", "LLM prompt templates", "AI prompt best practices"],
    "repo-sync": ["GitHub CLI automation", "Git submodule management", "repo synchronization"],
    "skill-management": ["AI skill management", "agent skills architecture", "skill orchestration"],
    "cross-bot-sync": ["multi-agent communication", "bot workflow sync", "agent team coordination"],
    "security-fixes": ["system hardening tutorial", "security audit automation", "permanent security fixes"],
    "integrations": ["Composio tutorial", "AI integrations platform", "agent tool integration"],
    "logistics": ["Fleetbase logistics tutorial", "supply chain OS", "fleet management API"],
    "media-content": ["YouTube Shorts pipeline tutorial", "AI content engine", "automated YouTube upload"],
    "research": ["Agent Reach research tool", "internet search AI agent", "web research CLI"],
}


def log(msg):
    """Append timestamped message to log file and stdout."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def fetch_transcript(url):
    """Fetch YouTube transcript using the youtube-content skill script."""
    script = SKILLS_DIR / "local" / "media" / "youtube-content" / "scripts" / "fetch_transcript.py"
    if not script.exists():
        log("ERROR: youtube-content fetch_transcript.py not found")
        return None
    try:
        result = subprocess.run(
            [sys.executable, str(script), url, "--text-only"],
            capture_output=True, text=True, timeout=60,
            cwd=str(SKILLS_DIR)
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        log(f"Transcript fetch failed for {url}: {result.stderr[:200]}")
        return None
    except Exception as e:
        log(f"Transcript fetch error: {e}")
        return None


def extract_skills_from_transcript(transcript, topic):
    """Extract actionable skills from a transcript (simple heuristic)."""
    if not transcript:
        return []
    lines = transcript.split("\n")
    skills = []
    current_skill = None
    for line in lines:
        line = line.strip()
        if not line or len(line) < 20:
            continue
        # Look for tutorial-style lines that describe a skill
        if any(kw in line.lower() for kw in ["how to", "step", "first", "next", "then", "finally", "you'll learn", "you will learn"]):
            if current_skill and len(current_skill.get("steps", [])) < 5:
                current_skill["steps"].append(line)
            elif len(line) < 200:
                current_skill = {"topic": topic, "title": line[:100], "steps": [line], "source": "youtube"}
                skills.append(current_skill)
        elif current_skill and len(current_skill.get("steps", [])) < 5:
            current_skill["steps"].append(line)
    return skills[:10]  # Cap at 10 skills per cycle


def generate_skill_md(skill_data):
    """Generate a SKILL.md file from extracted skill data."""
    title = skill_data.get("title", "Unknown Skill")
    steps = skill_data.get("steps", [])
    topic = skill_data.get("topic", "general")

    steps_text = "\n".join(f"- {s}" for s in steps[:5])

    return f"""---
name: {topic}-{title[:30].lower().replace(' ', '-').replace(':', '')}
description: Auto-generated skill from YouTube tutorial: {title}
version: 1.0.0
author: Coach (auto-generated)
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [auto-generated, coach, {topic}]
    source: youtube
    generated: {datetime.now().isoformat()}
---

# {title}

## When to use

Use when the user needs help with {topic}.

{steps_text}

## Workflow

1. Fetch the relevant information
2. Validate the input
3. Execute the steps
4. Verify the result
5. Report back

## Error handling

- If the step fails, retry once
- If still failing, log the error and report to user
- Never skip validation steps
"""


def deliver_skill(agent_name, skill_md):
    """Write a skill file to the target agent's skill directory."""
    agent_dir = SKILLS_DIR / "local" / agent_name.lower().replace("-", "-")
    if not agent_dir.exists():
        agent_dir.mkdir(parents=True, exist_ok=True)

    skill_name = skill_md.split("name: ")[1].split("\n")[0] if "name: " in skill_md else "unknown"
    skill_file = agent_dir / "SKILL.md"

    # Avoid overwriting existing skills — append suffix
    counter = 1
    original_file = skill_file
    while skill_file.exists():
        skill_file = original_file.parent / f"{original_file.stem}-{counter}{original_file.suffix}"
        counter += 1

    skill_file.write_text(skill_md, encoding="utf-8")
    log(f"Delivered skill '{skill_name}' to {agent_name} at {skill_file}")
    return skill_file


def search_youtube(topic, max_results=3):
    """Search YouTube for tutorials on a topic. Returns list of (title, url)."""
    # Try hermes_tools web_search first
    try:
        from hermes_tools import web_search
        results = web_search(f"site:youtube.com {topic}", limit=max_results)
        videos = []
        for item in results.get("data", {}).get("web", []):
            url = item.get("url", "")
            title = item.get("title", "")
            if "youtube.com" in url or "youtu.be" in url:
                videos.append((title, url))
        return videos
    except Exception:
        pass

    # Fallback: direct curl search via YouTube page scrape
    try:
        import urllib.request
        import re
        query = topic.replace(" ", "+")
        url = f"https://www.youtube.com/results?search_query={query}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
        videos = []
        for match in re.finditer(r'href="(/watch\?v=[^"]+)"[^>]*>\s*<h3[^>]*>(.*?)</h3>', html):
            video_url = "https://www.youtube.com" + match.group(1).split("&")[0]
            video_title = re.sub(r'<[^>]+>', '', match.group(2)).strip()
            if video_title and video_url not in [v[1] for v in videos]:
                videos.append((video_title, video_url))
        return videos[:max_results]
    except Exception as e:
        log(f"YouTube search fallback error: {e}")
        return []


def process_learning_source(source_name, source_info):
    """Process a known learning source (repo) and deliver skills to its agents."""
    repo = source_info["repo"]
    niche = source_info["niche"]
    target_agents = source_info["agents"]
    log(f"Processing learning source: {source_name} ({repo})")

    # Search web for the source's tools/features
    try:
        from hermes_tools import web_search
        results = web_search(f"{source_name} tools features API", limit=3)
        pages = results.get("data", {}).get("web", [])
    except Exception:
        pages = []

    skills_delivered = 0
    for page in pages[:2]:
        title = page.get("title", "")
        url = page.get("url", "")
        log(f"  Extracting from: {title}")

        # Extract skills from the page content
        skills = extract_skills_from_transcript(f"{title}\n{url}", niche)
        for skill_data in skills:
            skill_md = generate_skill_md(skill_data)
            for agent_name in target_agents:
                deliver_skill(agent_name, skill_md)
                skills_delivered += 1

    return skills_delivered


def learn_cycle():
    """Run one full learning cycle: search, fetch, extract, distribute."""
    log("=== Coach learning cycle started ===")
    skills_delivered = 0

    # Process known learning sources first
    for source_name, source_info in LEARNING_SOURCES.items():
        skills_delivered += process_learning_source(source_name, source_info)

    # Then search YouTube for each agent's niche
    for agent_name, agent_info in AGENTS.items():
        niche = agent_info["niche"]
        queries = SEARCH_QUERIES.get(niche, [niche])

        for query in queries[:1]:  # One query per agent per cycle to stay rate-friendly
            log(f"Searching YouTube for: {query} (agent: {agent_name})")
            videos = search_youtube(query)

            if not videos:
                log(f"No videos found for '{query}'")
                continue

            for title, url in videos[:1]:  # Process one video per query
                log(f"Fetching transcript: {title}")
                transcript = fetch_transcript(url)

                if not transcript:
                    log(f"No transcript for {url}")
                    continue

                skills = extract_skills_from_transcript(transcript, query)
                for skill_data in skills:
                    skill_md = generate_skill_md(skill_data)
                    deliver_skill(agent_name, skill_md)
                    skills_delivered += 1

    log(f"=== Coach cycle complete: {skills_delivered} skills delivered ===")
    return skills_delivered


def status():
    """Show current skill status for all agents."""
    log("=== Agent Skill Status ===")
    for agent_name, agent_info in AGENTS.items():
        agent_dir = SKILLS_DIR / "local" / agent_name.lower().replace("-", "-")
        skill_count = len(list(agent_dir.glob("SKILL.md"))) if agent_dir.exists() else 0
        log(f"  {agent_name} ({agent_info['niche']}): {skill_count} skills")
    log("=== End Status ===")


def handle_request(agent_name, topic):
    """Handle a skill request from an agent."""
    log(f"Skill request: {agent_name} needs '{topic}'")

    # Search YouTube for the topic
    videos = search_youtube(topic, max_results=3)
    if not videos:
        log(f"No YouTube videos found for '{topic}'")
        return 0

    skills_delivered = 0
    for title, url in videos[:2]:
        log(f"Fetching transcript for: {title}")
        transcript = fetch_transcript(url)
        if not transcript:
            continue
        skills = extract_skills_from_transcript(transcript, topic)
        for skill_data in skills:
            skill_md = generate_skill_md(skill_data)
            deliver_skill(agent_name, skill_md)
            skills_delivered += 1

    log(f"Request fulfilled: {skills_delivered} skills delivered to {agent_name}")
    return skills_delivered


def daemon_loop():
    """Run the learning loop continuously (24/7)."""
    log(f"Coach daemon started — cycle every {CYCLE_INTERVAL} minutes")
    cycle = 0
    try:
        while True:
            cycle += 1
            log(f"--- Cycle {cycle} ---")
            try:
                learn_cycle()
            except Exception as e:
                log(f"Cycle error: {e}")
            log(f"Sleeping {CYCLE_INTERVAL} minutes...")
            time.sleep(CYCLE_INTERVAL * 60)
    except KeyboardInterrupt:
        log("Coach daemon stopped by user")


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python coach_loop.py <command> [args]")
        print("Commands: learn, status, request <agent> <topic>, daemon, stop")
        sys.exit(1)

    command = sys.argv[1]

    if command == "learn":
        learn_cycle()
    elif command == "status":
        status()
    elif command == "request" and len(sys.argv) >= 4:
        handle_request(sys.argv[2], " ".join(sys.argv[3:]))
    elif command == "daemon":
        daemon_loop()
    elif command == "stop":
        log("Coach stop requested")
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()