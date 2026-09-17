---
name: agent-reach
description: |
  MUST USE when user wants to research/search/look up anything on the internet.
  16 platforms, multi-backend routing, zero config for 6 channels.
  Platforms: Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu, Facebook,
  Instagram, V2EX, LinkedIn, Boss直聘, Xueqiu, Xiaoyuzhou, RSS, web search, Exa AI.
version: 1.5.0
author: Panniantong
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [agent-reach, internet, research, search, social, video, finance, web]
    source: https://github.com/Panniantong/Agent-Reach
    category: research
---

# Agent Reach — Internet Capability Router

## What it does

Gives AI agents read/search access to 16 internet platforms with zero config for 6 channels.
Multi-backend routing — if one backend fails, it falls back to another automatically.

## Platforms

| Category | Platforms |
|----------|-----------|
| Search | Exa AI, web search, GitHub code search |
| Social | Twitter, Reddit, XiaoHongShu, Bilibili, V2EX, Facebook, Instagram |
| Career | LinkedIn, Boss直聘 |
| Dev | GitHub |
| Web | Jina Reader, RSS feeds |
| Video | YouTube, Bilibili, 小宇宙播客 |
| Finance | 雪球/股票行情 |

## Quick start

```bash
# Install
pip install -e .

# Diagnose which platforms work
agent-reach doctor --json

# Search
agent-reach search "query" --platform twitter
agent-reach search "query" --platform youtube
agent-reach search "query" --platform reddit

# Read content
agent-reach read "URL" --platform youtube
```

## Key features

- **Zero config for 6 channels**: web search, GitHub, V2EX, RSS, YouTube (yt-dlp), Bilibili (bili-cli)
- **Cookie-based auth**: Twitter, XiaoHongShu, Reddit (user provides cookies)
- **MCP server**: integrates with Claude Code, Cursor, Windsurf
- **Doctor diagnostics**: `agent-reach doctor` checks all platforms
- **Auto-fallback**: if one backend fails, tries the next
- **Update check**: `agent-reach check-update`

## Integration with PAIOS agents

- **composio**: Tool discovery and execution via Composio
- **hermes-orchestrator**: Coordinate multi-platform research workflows
- **integration-orchestrator**: Cross-bot skill distribution
- **evelyn-brain**: Log research results to memory
- **AI-Ops-Vault**: Store API keys and cookies securely
- **skill-ecosystem**: Manage Agent Reach skill versions

## Setup

```bash
# Clone
git clone https://github.com/Panniantong/Agent-Reach.git
cd Agent-Reach

# Install
pip install -e .

# Check what works
agent-reach doctor --json

# Configure cookies for Twitter/Xiaohongshu (optional)
agent-reach configure twitter-cookies
agent-reach configure xiaohongshu-cookies
```

## Error handling

- Platform not available → run doctor, check backend status
- Cookie expired → re-export cookies from browser
- Rate limited → wait, retry with different backend
- Network error → check proxy settings, retry
- MCP not connecting → check MCP server config