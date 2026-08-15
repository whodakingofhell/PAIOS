# Hermes Skills Reference

> Installed skills and what they do. Last updated: 2026-08-15

## Active Skills (46 enabled, 47 disabled)

### Core AI Agents
- `claude-code` — Delegate coding to Claude Code CLI
- `codex` — Delegate coding to OpenAI Codex CLI
- `opencode` — Delegate coding to OpenCode CLI
- `hermes-agent` — Configure, theme, extend Hermes

### Dev Tools
- `codebase-inspection` — LOC, languages, ratios
- `github-*` — Full GitHub workflow (issues, PRs, repos)
- `plan` — Write markdown plans
- `spike` — Throwaway experiments
- `computer-use` — Drive desktop in background

### Research
- `anysearch` — Real-time web search
- `agent-reach` — YouTube/RSS/GitHub research
- `blogwatcher` — Monitor blogs and feeds
- `ai-news-watcher` — AI news digest for tracked tools

### Obsidian
- `obsidian` — Read, search, create notes
- `obsidian-markdown` — Create/edit Obsidian markdown
- `defuddle` — Extract clean markdown from web pages

### Productivity
- `docx` — Create/edit Word documents
- `pdf` — Create, read, merge, fill PDFs
- `xlsx` — Create/edit Excel workbooks
- `powerpoint` — Create/edit PowerPoint decks
- `nano-pdf` — Edit PDFs via natural language
- `meeting-action-items` — Turn notes into tasks

### Writing
- `avoid-ai-writing` — Audit/rewrite to remove AI patterns
- `prompt-engineering` — Expert prompt crafting

### Orchestration
- `orchestrator` — Multi-agent routing
- `workspace-dispatch` — Single-agent mission orchestrator

### Security
- `citadel` — Zero-trust security integration

### Media
- `youtube-content` — YouTube transcripts to summaries

## Disabled Skills (47)

Trimmed for performance. Includes: ascii-art, comfyui, huggingface-hub, google-workspace, notion, airtable, maps, and others.

## Adding New Skills

```powershell
# From GitHub
hermes skills install https://github.com/user/repo

# From local
cp -r path/to/skill $env:LOCALAPPDATA\hermes\skills\category\skill-name
```

## References

- [Optimization Guide](https://github.com/OnlyTerp/hermes-optimization-guide)
- [Skills Docs](https://hermes-agent.nousresearch.com/docs)
