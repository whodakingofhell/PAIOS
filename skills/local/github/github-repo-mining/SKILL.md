---
name: github-repo-mining
description: Large-scale GitHub repository discovery and data collection using agent-browser + execute_code loops. Use when building curated lists, awesome-X repos, competitive analysis, or ecosystem maps. Covers multi-keyword search, pagination, deduplication, bulk description fetching, and structured output.
tags: [github, research, scraping, agent-browser, awesome-list, data-collection]
related_skills: [agent-browser, github-repo-management]
---

# GitHub Repository Mining at Scale

Use when you need to discover 50–200+ repos on a topic, collect their metadata (stars, descriptions), and organize into structured output like an awesome-list.

## Core Approach

Combine `agent-browser` (for GitHub search page scraping) with `execute_code` (for looping, deduplication, and batch processing). Do NOT manually call pages one by one in conversation — use `execute_code` loops.

## Step 1 — Define Search Query Set

GitHub search is noisy. Use **10–30 varied queries** to maximize coverage:

```python
queries = [
    "primary+keyword",                    # Main term, pages 1-8
    "topic:your-topic",                   # GitHub topic tag
    "keyword+tool", "keyword+framework",  # Compound terms
    "keyword+ui", "keyword+config",       # Feature-specific
    "keyword+hooks", "keyword+mcp",       # Ecosystem-specific
    "keyword+tutorial", "keyword+guide",  # Educational
    "keyword+template", "keyword+boilerplate",
    "SomeProperNoun",                     # Related brands/projects
]
```

## Step 2 — Scrape with execute_code Loop

```python
from hermes_tools import terminal
import re, json

def parse_page(raw_text):
    """Extract repos from agent-browser accessibility tree snapshot."""
    repos = []
    lines = raw_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        # Level-3 headings are repo names in GitHub search results
        m = re.search(r'heading "([^/"\s]+/[^"\s]+)".*\[level=3', line)
        if m:
            repo = m.group(1).strip()
            if '/' in repo:
                stars, desc = "", ""
                for j in range(i+1, min(i+30, len(lines))):
                    # Stars: look for "Xk" or plain number pattern
                    sm = re.search(r'StaticText "(\d+\.?\d*[kK]?)"', lines[j])
                    if sm and not stars:
                        stars = sm.group(1)
                    # Description: any long StaticText not matching noise
                    dm = re.search(r'StaticText "([^"]{20,})"', lines[j])
                    if dm and not desc:
                        c = dm.group(1)
                        if not any(x in c for x in ['Updated', ' ago', 'Press', 'Sponsor', 'Read', 'open source', 'every piece']):
                            desc = c
                repos.append((repo, stars, desc))
        i += 1
    return repos

def safe_fetch(url):
    # Include proxy env vars if needed (common in CN/restricted environments)
    r = terminal(f'agent-browser open "{url}" 2>&1 | head -1 && agent-browser snapshot 2>&1')
    return r.get("output", "")

all_repos = {}

# Paginate main keyword (up to 8 pages = ~80 repos)
for p in range(1, 9):
    url = f"https://github.com/search?q=your+keyword&type=repositories&s=stars&o=desc&p={p}"
    raw = safe_fetch(url)
    for repo, stars, desc in parse_page(raw):
        if repo not in all_repos:
            all_repos[repo] = {"stars": stars, "desc": desc}

# Additional queries (first page only, sorted by stars)
for q in queries:
    url = f"https://github.com/search?q={q}&type=repositories&s=stars&o=desc"
    raw = safe_fetch(url)
    for repo, stars, desc in parse_page(raw):
        if repo not in all_repos:
            all_repos[repo] = {"stars": stars, "desc": desc}

print(f"Total unique: {len(all_repos)}")

# Save — execute_code sessions don't share state between calls
with open('/tmp/repos.json', 'w') as f:
    json.dump(all_repos, f, ensure_ascii=False, indent=2)
```

**Critical:** Save to `/tmp/repos.json` after each `execute_code` block — state is NOT shared between calls.

## Step 3 — Fetch Accurate Descriptions (Chunked)

execute_code has a **50 tool-call cap**. Process repos in chunks of 50:

```python
from hermes_tools import terminal
import re, json

with open('/tmp/repos.json') as f:
    all_repos = json.load(f)

def get_repo_desc(repo):
    """GitHub page title format: 'GitHub - owner/repo: description · GitHub'"""
    r = terminal(f'agent-browser open "https://github.com/{repo}" 2>&1 | head -1')
    title = r.get("output", "")
    # Title separator may be · or - before "GitHub"
    m = re.search(r'GitHub - [^:]+: (.+?)(?:\s[·•]\s| - )GitHub', title)
    if m:
        return m.group(1).strip()
    # Fallback: grab everything after colon
    m2 = re.search(r'GitHub - [^:]+: (.+?)$', title.strip())
    return m2.group(1).strip()[:120] if m2 else ""

repos_list = list(all_repos.items())

# Process chunk N (call this block multiple times with different slices)
for repo, info in repos_list[0:50]:    # Change slice each run: [50:100], [100:150]...
    new_desc = get_repo_desc(repo)
    if new_desc:
        all_repos[repo]["desc"] = new_desc

with open('/tmp/repos.json', 'w') as f:
    json.dump(all_repos, f, ensure_ascii=False, indent=2)
print(f"Done chunk. Total: {len(all_repos)}")
```

## Step 3b — Description Fallback Strategy (3-tier)

When `get_repo_desc()` returns empty for some repos, use this cascade:

1. **Snapshot fallback** — fetch the repo page and scan accessibility tree for long StaticText:
```python
def get_desc_via_snapshot(repo):
    r = terminal(f'agent-browser open "https://github.com/{repo}" 2>&1 | head -1 && agent-browser snapshot 2>&1 | head -80')
    for line in r.get("output","").split('\n'):
        m = re.search(r'StaticText "([^"]{25,120})"', line)
        if m:
            c = m.group(1)
            if not any(x in c for x in ['Star', 'Fork', 'Watch', 'Code', 'Issues', 'Pull', 'Actions']):
                return c
    return ""
```

2. **GitHub REST API** — free, no auth needed for public repos:
```python
def get_desc_via_api(repo):
    r = terminal(f'curl -s "https://api.github.com/repos/{repo}" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get(\'description\',\'\') or \'\')"')
    return r.get("output","").strip()
```

3. **Manual fallback dict** — for repos that resist all scraping:
```python
manual_descs = {"owner/repo": "Hand-written one-liner description"}
for repo, desc in manual_descs.items():
    if repo in all_repos and not all_repos[repo]['desc']:
        all_repos[repo]['desc'] = desc
```

## Step 4 — Classify Repos

**Classify by repo name first, description second.** Descriptions are noisy and sometimes missing; repo names are reliable.

```python
def classify(repo, desc):
    repo_l = repo.lower()
    desc_l = (desc or '').lower()
    # Check repo name FIRST — more reliable than description
    if 'anthropics/' in repo_l: return "Official & Core"
    if 'awesome' in repo_l: return "Awesome Lists"
    if 'mcp' in repo_l: return "MCP Tools"
    if any(x in repo_l for x in ['skill', 'plugin']): return "Skills & Plugins"
    if any(x in repo_l for x in ['router', 'proxy', 'relay']): return "Routing & Proxy"
    if any(x in repo_l for x in ['mem', 'memory', 'context']): return "Memory & Context"
    # Fall through to description keywords
    if 'memory' in desc_l: return "Memory & Context"
    if 'mcp' in desc_l: return "MCP Tools"
    return "Other"
```

Also filter self-referential noise in descriptions (e.g. `owner/repo-name` literally appearing as the description when GitHub shows card header):
```python
noise_patterns = [f'{repo.split("/")[0]}/', 'owner/repo-prefix']
if any(p in desc for p in noise_patterns):
    desc = ""  # treat as missing
```

## Step 5 — Output Format (Awesome List)

**Default: 3-column table, NO rank/sequence column.** Users typically do NOT want sequence numbers — they clutter the view. Only add a rank column if explicitly requested.

**Writing style for Chinese-primary READMEs**: When the user says "按照之前的写作风格" or "no # headings, no sequence numbers", use this pattern:
- Top-level title: plain text on first line (no `#` prefix), e.g. `learn-crypto`
- Section headers: bold text with emoji, e.g. `**⛓️ 公链与底层协议**` — NEVER use `#`, `##`, `###`
- No ordered lists (1. 2. 3.) anywhere in the doc; use `-` bullets for TOC
- Badge row, then `---` dividers between sections
- Footer uses `**贡献**` and `**许可证**` bold headers, not `##`

```markdown
| Repository | Stars | Description |
|-----------|------:|-------------|
| [owner/repo](https://github.com/owner/repo) | 13.5k ⭐ | One-line description |
```

**Removing a rank column from an existing README** (if a user asks to clean it up):
```python
text = text.replace('| # | Repository | Stars | Description |', '| Repository | Stars | Description |')
text = text.replace('|:---:|-----------|------:|-------------|', '|-----------|------:|-------------|')
# Remove rank number from data rows: "| 3 | [repo](...) |" -> "| [repo](...) |"
text = re.sub(r'\|\s*\d+\s*\|\s*(\[)', r'| \1', text)
```

**Incrementally expanding (101-200, etc.)** — insert new rows into existing category sections without rebuilding:
```python
# Find the category header line, then find the last data row in that section,
# insert new rows immediately after it
for cat, new_repos_list in new_classified.items():
    header_idx = next((i for i, l in enumerate(lines) if l.strip() == CAT_HEADER_MAP[cat]), None)
    if header_idx is None: continue
    last_row_idx = None
    for i in range(header_idx + 1, len(lines)):
        if lines[i].startswith('## ') and i != header_idx: break
        if lines[i].startswith('| [') and 'github.com' in lines[i]:
            last_row_idx = i
    if last_row_idx is None: continue
    new_rows = [f"| [{repo}](https://github.com/{repo}) | {stars} | {desc} |" for repo, info in new_repos_list]
    lines = lines[:last_row_idx+1] + new_rows + lines[last_row_idx+1:]
```
Save the second batch to a separate `/tmp/new_repos_101_200.json` to avoid contaminating the first batch. Deduplicate against the original pool when collecting.

Include a **global rank column** (optional) so readers can compare cross-category popularity:

```python
all_sorted = sorted(all_repos.items(), key=lambda x: parse_stars(x[1]['stars']), reverse=True)
rank_map = {repo: i+1 for i, (repo, _) in enumerate(all_sorted)}
```

Table format with rank:
```markdown
| Rank | Repository | Stars | Description |
|:----:|-----------|------:|-------------|
| #1 | [owner/repo](https://github.com/owner/repo) | 13.5k ⭐ | One-line description |
```

For bilingual (EN + CN) awesome lists:
- Create `README.md` (English, primary) and `README_CN.md` (Chinese)
- Both files start with language toggle badges linking to each other:
  ```markdown
  <a href="README.md">🇺🇸 English</a> | <a href="README_CN.md">🇨🇳 中文</a>
  ```
- Use same category structure in both files
- Chinese descriptions should be natural translations, not verbatim machine translation

## Pitfalls

- **execute_code state loss**: Always save to `/tmp/*.json` — variables vanish between calls
- **50 tool-call cap**: Chunk description fetching into 50-repo batches (one `execute_code` call each)
- **Query overlap**: Use deduplication dict (`if repo not in all_repos`) — same repo appears across many queries
- **Noise in descriptions**: Filter out GitHub UI text ("Updated X ago", "Sponsor", "Press /", etc.). Also filter self-referential noise like `owner/repo-name` appearing as the description
- **Stars parsing**: GitHub shows "13.5k" not "13500" — keep as string for display, parse only if sorting
- **Page 9+ for 101-200**: Main keyword pagination works up to pages 9–17 (after page 17 returns 0 results). Combine with compound queries like `keyword+hooks`, `keyword+config+yaml`, `keyword+subagent` to reach 100+ new repos. Always exclude repos already in the first-batch dict
- **Page 9+ returns empty after 17**: GitHub search caps at ~170 results for main keyword. Quality compound queries add 30–50 more unique repos
- **README badge/stat updates when expanding**: Update `Repos-100` → `Repos-200` badge, recount per-category overview table, update description text (e.g. "These 100 repositories…" → "These 200 repositories…")
- **Rebuild pattern**: If you hit the 50-call cap mid-loop, rebuild from saved JSON in the next call rather than resuming mid-array
- **Title regex variation**: GitHub title separator can be `·` (middle dot U+00B7) or ` - ` — use `(?:\s[·•]\s| - )` to match both
- **Compound keyword searches**: Queries like `keyword+feature` (e.g. `claude+code+hooks`) yield many unique repos not found by the main keyword — always add feature/domain-specific compound queries
- **Proxy in restricted networks**: Prepend `export https_proxy=http://YOUR_PROXY_HOST:PORT http_proxy=http://YOUR_PROXY_HOST:PORT;` to terminal commands when in China or behind a firewall
- **GitHub API rate-limiting with no token**: Unauthenticated requests to `api.github.com/repos/{owner}/{repo}` get rate-limited to 60/hour. When processing 100+ repos in two `execute_code` blocks, the second block will return all zeros. Mitigate by: (1) chunking smaller (30 repos per block), (2) adding `sleep 1` between calls, or (3) hardcoding known star counts for famous repos rather than fetching them all
- **`write_file` uses absolute paths from agent perspective**: On macOS, `write_file("/root/Desktop/...")` writes nowhere useful. Always resolve the real home directory first with `terminal("echo $HOME")` and use that path (e.g. `/Users/username/Desktop/...`). The `execute_code` sandbox assumes Linux paths — use `terminal("mkdir -p ~/Desktop/project")` to create dirs, then write with the real path
- **Description cross-contamination in search results**: When scraping GitHub search pages, repo descriptions sometimes bleed into adjacent repos' parsed data (e.g. `dogecoin/dogecoin` getting monero's description). Always verify descriptions for the top 20 repos manually or via a `known_desc` dict for well-known projects
- **Stars display string vs sort integer**: Keep both `stars` (display string like "13.5k") and `stars_int` (integer for sorting) in the data dict. The search page scraper gives display strings; the API gives integers. When API is rate-limited, maintain a `known_stars` dict for major projects (bitcoin ~83k, ethereum/go-ethereum ~48k, etc.) to ensure correct sort order
- **Repo count inflation from niche queries**: Broad queries like `monero+wallet`, `zcash+privacy`, `lightning+network` add many low-star repos (under 500 stars) that dilute the top-100 list. If the goal is "top 100 by stars globally", prioritize the main keyword's first 8–10 pages over many variant queries, then supplement with topic searches only

## Realistic Scale Expectations

| Queries | Pages | Expected Unique Repos |
|---|---|---|
| 1 keyword × 8 pages | 80 results | ~60–70 unique |
| + 15 variant queries | +150 results | ~100–120 unique |
| + 15 more queries | +150 results | ~150–185 unique |

Diminishing returns kick in after ~150 repos for niche topics.
