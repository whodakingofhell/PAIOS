# Evelyn Bot Mode Architecture — Deployment Summary

- Generated: 2026-08-19T08:54:39.519695+00:00
- Source: Hermes Bot Mode video (Julian Goldie SEO) + Shorts/QxvzpFUULYk


## Specialist Profiles Deployed

| Profile | Specialist | Name | Model | Core Skills |
|---------|------------|------|-------|-------------|
| `evelyn-research` | Research & Intel | **Athena** | `nemotron-3-ultra-free` | system-intel-scanner, repo-scanner, browser-youtube-scanner, agent-reach, youtube-transcript-pro, evelyn-brain, paios-knowledge |
| `evelyn-content` | Content & Publishing | **Calliope** | `stepfun/step-3.7-flash:free` | writing/avoid-ai-writing, writing/humanizer, youtube-content, obsidian, paios-knowledge |
| `evelyn-expenses` | Finance & Expenses | **Ledger** | `stepfun/step-3.7-flash:free` | ocr-and-documents, pdf, xlsx, document-to-action-items, paios-knowledge |
| `evelyn-gateway-doctor` | Infra & Gateway Health | **Pulse** | `tencent/hy3:free` | windows-bot-operations, free-tier-ai-routing, verified-system-operations, hermes-restore-point, hermes-agent, computer-use, auto-verify |
| `evelyn-unified` | Orchestrator | **Evelyn Prime** | `stepfun/step-3.7-flash:free` | multi-ai-routing, workspace-dispatch, evelyn-brain, paios-knowledge, hermes-agent, auto-verify, session-librarian |

## Architecture Principles (from video)

- Named agents with distinct roles, SOUL.md, model, skills
- Bot Mode: face, chat, schedule in unified panel
- Direct agent-to-agent messaging (delegation)
- Eliminates manual copy-paste handoffs


## Cron Coordination

| Schedule | Specialist | Task |
|----------|------------|------|
| Daily 06:00 | Athena | Intel scan (browser, GitHub, YouTube, web) |
| Daily 07:00 | Ledger | Receipt ingest check |
| Daily 08:00 | Evelyn Prime | Unified brief → Telegram |
| Daily 10:00 PHT | Pulse | Bot health check |
| Every 5 min | Pulse | Gateway watchdog |
| Monday 09:00 | Calliope | Content planning |
| Sunday 10:00 | Ledger | Weekly reconcile |
| 1st of month | Ledger | Monthly audit |
| Friday 17:00 | Calliope | Analytics review |

## Orchestration Skill

- `evelyn-orchestrator` deployed to evelyn-unified profile
- Routing rules: explicit → keyword → parallel → status


## Intel Artifacts Generated

- `browser-history-scan.json` / `intel-brief-*.md` (browser history)
- `web-scan-results.json` / `web-intel-brief-*.md` (GitHub repos)
- `youtube-video-ids.json` / `hermes-youtube-videos.json` (YouTube)
- `short-QxvzpFUULYk.json` (Shorts transcript)

## Vaults Updated

- AI-Ops-Vault: intel briefs pushed, git synced
- PAIOS: intel briefs added
