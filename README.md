---
tags:
  - paios/system
related:
  - "./AGENTS.md"
  - "./ARCHITECTURE.md"
---

# PAIOS — Personal AI Operating System

A portable, Markdown-first knowledge OS for durable knowledge, project management, business operations, and AI-assisted execution. Built on the [Knowledge OS Starter Kit](https://github.com/kravetech/kos-starter-kit) architecture.

**Owner:** PAIOS  
**Timezone:** Asia/Manila  
**Installed:** 2026-07-29  
**Vault path:** Obsidian vault at `PAIOS/PAIOS/`

## Architecture

```
PAIOS/
├── 00 - System/        # Control plane, AI config, automation registry
├── 01 - Business/      # Business operations, team roles, strategy
├── 02 - Projects/      # Active/Incubating/Completed projects
├── 03 - Personal/      # Personal finance, goals, health, learning
├── 04 - Hobbies/       # Creative pursuits and interests
├── 05 - Knowledge/     # Curated knowledge by domain
│   ├── AI/
│   ├── Architecture/
│   ├── Business/
│   ├── DevOps/
│   ├── Product-Design/
│   ├── References/
│   └── Software-Development/
├── 06 - Inbox/         # Capture and processing queue
├── 07 - Daily/         # Daily notes and periodic reviews
├── 08 - Templates/     # Reusable project and review scaffolds
├── 09 - Attachments/   # Non-Markdown assets
└── 99 - Archive/       # Historical material
```

## Active Projects

| Project | Status | Description |
|---------|--------|-------------|
| **AI-Appointment-Assistant** | Active | Full-stack AI scheduling app (Node.js/Supabase/Vercel) |
| **deploy-v2** | Active | Next.js 14 web app with Turnstile, Sentry, Supabase |
| **PhilippineSkyland** | Active | Real estate/development project |

## Knowledge Base (38 docs)

Organized across 7 categories covering the full software product lifecycle:

- **Vision → Roadmap** (12-section methodology framework)
- **Team roles** (Architecture, Engineering, DevOps, QA, Security, etc.)
- **Frameworks** (MASTER-FRAMEWORK, Content-Pipeline, Feature-Score-Rubric, Product-Lifecycle)
- **Security** (SECURITY_ARCHITECTURE, Security.md)
- **AI Operations** (Claude prompts, AI-Engineering, Tool-Role-Mapping)

All documents are reusable across projects — e.g., `Security.md` and `SECURITY_ARCHITECTURE.md` serve as templates for any new project's security posture.

## AI Agent Integration

This vault is designed for use with AI coding agents:

| Tool | Adapter | File |
|------|---------|------|
| **OpenCodeAI** | Canonical router | `AGENTS.md` |
| **Claude Code** | Thin adapter | `CLAUDE.md` |
| **Codex CLI** | Thin adapter | `CODEX.md` |

**Context loading rules:**
- Quick tasks: loads only `AGENTS.md` + `me.md`
- Active work: adds `memory.md` + `handoff.md`
- Project work: loads specific project context only
- Never auto-loads: reports, state, attachments, archives, histories

## Content Origins

This Knowledge OS consolidates content from legacy systems:
- `PROMPT GUIDE AI/` — Full-stack project methodology (45+ docs)
- `AI-Ops-Vault/` — Previous Obsidian knowledge base
- `AI PROJECTS/` — Active development projects

All content was deduplicated and organized into the KOS numbered structure.

## Privacy Model

- Default AI access: **internal**
- Personal data: **restricted**
- Linked sources: **restricted**
- Secrets and credentials: **never committed**
- External integrations: **not configured** by default (see `AUTOMATION-REGISTRY.md`)

## Quick Start

```bash
# Open as Obsidian vault
# File → Open Vault → Manage vaults → Open folder as vault
# Select: C:\Users\...\PAIOS\PAIOS

# For AI agents, start with:
# AGENTS.md  →  me.md  →  memory.md  →  handoff.md
```

## First-Day Checklist

- [ ] Review `me.md` and adjust profile
- [ ] Review privacy defaults in `00 - System/`
- [ ] Process one Inbox item
- [ ] Review `AUTOMATION-REGISTRY.md` for external tools
- [ ] Initialize Git if version tracking is desired
- [ ] Keep remote **private** until content review is complete

## License

System architecture: Apache 2.0 (via KOS-Starter-Kit)  
Content: CC-BY-4.0 unless otherwise noted
