---
name: coach
description: |
  24/7 skills learning bot. Searches YouTube tutorials, gathers transcripts,
  extracts skills, and distributes them to other agents based on their niche.
  Other agents communicate with Coach to learn essential skills.
version: 1.0.0
author: Ches (Mark Chester Santos)
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [coach, learning, skills, youtube, composio, agents]
    related_skills: [youtube-content, composio, integration-orchestrator, system-hardening]
---

# Coach — Skills Learning Bot

## Purpose

Coach runs 24/7, continuously learning new skills from YouTube tutorials and
other sources, then distributing those skills to the right agents based on
their niche. Agents ask Coach for skills they need; Coach finds, validates,
and delivers them.

## Agents served (niche → skill mapping)

| Agent | Niche | Skills needed |
|-------|-------|---------------|
| hermes-orchestrator | orchestration | workflow sync, multi-agent coordination |
| Citadel | security | threat detection, zero-trust, audit |
| AI-Ops-Vault | secrets/credentials | API key management, credential sync |
| evelyn-brain | memory/backup | restore points, semantic search |
| PROMPT-GUIDE-AI | prompts | prompt templates, examples |
| github-sync | repo sync | GitHub auth, branch management |
| skill-ecosystem | skill management | skill discovery, versioning |
| integration-orchestrator | cross-bot sync | workflow distribution |
| system-hardening | security fixes | permanent fixes, audit |
| composio | integrations | tool discovery, auth, execution |

## How Coach works

### 1. Continuous learning loop

Coach runs a background loop (every 30 minutes by default) that:
1. Searches YouTube for tutorials relevant to agent niches
2. Fetches transcripts using the `youtube-content` skill
3. Summarizes and extracts actionable skills
4. Matches skills to agents by niche
5. Creates/updates skill files in the target agent's skill directory

### 2. Agent requests

Any agent can request a skill from Coach:

```
Coach, I need a skill for <topic>
```

Coach searches YouTube, extracts the skill, and delivers it.

### 3. Skill delivery

Skills are delivered as SKILL.md files in the target agent's skill directory.
Coach validates each skill before delivery (syntax check, references check).

## Commands

- `coach learn` — run one learning cycle (search, extract, distribute)
- `coach status` — show what skills each agent has and what's missing
- `coach request <agent> <topic>` — request a specific skill for an agent
- `coach sync` — sync all agent skills with GitHub
- `coach stop` — stop the 24/7 loop

## Setup

Dependencies: `uv pip install youtube-transcript-api` (from youtube-content skill)
Composio SDK: already installed (`pip install composio`)

## Workflow

1. **Search**: Use Composio or YouTube API to find tutorials for a topic
2. **Fetch**: Use `youtube-content` skill to get transcript
3. **Extract**: Summarize transcript into skill structure (SKILL.md format)
4. **Match**: Route skill to the agent whose niche matches
5. **Validate**: Check skill syntax and references
6. **Deliver**: Write SKILL.md to agent's skill directory
7. **Sync**: Push updated skills to GitHub

## Error handling

- Transcript unavailable → skip, log, retry next cycle
- Composio key invalid → alert user, stop until fixed
- Agent directory missing → create it, then deliver
- Skill syntax error → quarantine, report to user