---
tags:
  - paios/knowledge
  - paios/references
  - legacy
  - vault-manifest
related:
  - "[[../README.md]]"
---

# MANIFEST — Single Source of Truth

> Every canonical doc lives here. Every other tool's output is a draft in `00-Inbox/<tool>/`.
> Promote once. Never two tools writing to the same filename.

---

## How It Works

1. **OpenCode/Claude/Codex/Gemini write to** `00-Inbox/<tool>/`
2. **You (or OpenCode as librarian)** review inbox drafts
3. **Promote** approved drafts into `01-Canonical/` — delete the inbox copy
4. **Never** let two tools write to the same canonical filename independently
5. **MANIFEST.md** is the index — update it on every promote/delete

---

## Canonical Files

### Frameworks (`01-Canonical/Frameworks/`)

| File | Owner Tool | Last Updated | Source |
|------|-----------|--------------|--------|
| `QA-Criticism-Framework.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/Frameworks/ |
| `Feature-Score-Rubric.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/Frameworks/ |
| `Product-Lifecycle.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/Frameworks/ |
| `Content-Pipeline.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/Frameworks/ |

### OS Sections (`01-Canonical/OS-Sections/`)

| File | Owner Tool | Last Updated | Source |
|------|-----------|--------------|--------|
| `00-Vision.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/AI-ENGINEERING-OS/ |
| `01-Business.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/AI-ENGINEERING-OS/ |
| `02-Product.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/AI-ENGINEERING-OS/ |
| `03-Architecture.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/AI-ENGINEERING-OS/ |
| `04-Engineering.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/AI-ENGINEERING-OS/ |
| `05-QA-Framework.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/AI-ENGINEERING-OS/ |
| `06-Security.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/AI-ENGINEERING-OS/ |
| `07-Automation.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/AI-ENGINEERING-OS/ |
| `08-AI-Knowledge.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/AI-ENGINEERING-OS/ |
| `09-Documentation.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/AI-ENGINEERING-OS/ |
| `10-Marketing.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |
| `11-Revenue.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |
| `12-Roadmap.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |

### Projects (`01-Canonical/Projects/`)

| File | Owner Tool | Last Updated | Source |
|------|-----------|--------------|--------|
| `MASTER-FRAMEWORK.md` | ZCodeProject | 2026-07-18 | Promoted from ZCodeProject/ |
| `AI-Appointment-Assistant/Vision.md` | OpenCode | 2026-07-18 | Created from AI PROJECTS docs |
| `AI-Appointment-Assistant/Business.md` | OpenCode | 2026-07-18 | Created from AI PROJECTS docs |
| `AI-Appointment-Assistant/Product.md` | OpenCode | 2026-07-18 | Created from AI PROJECTS docs |
| `AI-Appointment-Assistant/Claude-Brain-Prompt.md` | OpenCode | 2026-07-18 | System prompt for appointment brain |
| `AI-Appointment-Assistant/Scheduling-Rules.md` | OpenCode | 2026-07-18 | Business rules for scheduling |
| `AI-Appointment-Assistant/supabase-schema.sql` | OpenCode | 2026-07-18 | Supabase table definition |
| `AI-Appointment-Assistant/Supabase-Connection.md` | OpenCode | 2026-07-18 | Connection guide |
| `AI-Appointment-assistant/Lessons-Learned.md` | Claude | 2026-07-18 | Decision log from Claude sessions 1-3 |
| `AI-Appointment-Assistant/QA-Review-v1.md` | QA Team | 2026-07-18 | Full system audit + scorecard |
| `AI-Appointment-Assistant/README.md` | OpenCode | 2026-07-18 | Deployment guide + API docs |
| `AI-Appointment-Assistant/rls-migration.sql` | OpenCode | 2026-07-18 | Supabase RLS + audit log migration |
| `AI-Appointment-Assistant/appointment-backend/` | OpenCode | 2026-07-18 | Vercel project (API + UI) |

### Team (`01-Canonical/Team/`)

| File | Owner Tool | Last Updated | Source |
|------|-----------|--------------|--------|
| `Executive.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |
| `Architecture.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |
| `Frontend.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |
| `Backend.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |
| `Database.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |
| `DevOps.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |
| `AI-Engineering.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |
| `Automation-Engineering.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |
| `Security.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |
| `QA.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |
| `Claude-Handoff.md` | OpenCode | 2026-07-18 | Claude as second-in-command agent |

### Integrations (`01-Canonical/Integrations/`)

| File | Owner Tool | Last Updated | Source |
|------|-----------|--------------|--------|
| `Tool-Role-Mapping.md` | OpenCode | 2026-07-18 | Generated by architecture agent |
| `cost-map.md` | OpenCode | 2026-07-18 | Created per MASTER-FRAMEWORK |

---

## Inbox Status (`00-Inbox/`)

| Tool | Files Waiting | Last Deposit |
|------|--------------|--------------|
| opencode/ | 0 | — |
| claude/ | 1 | lessons_learned.md |
| codex/ | 0 | — |
| gemini/ | 0 | — |
| zcode/ | 0 | — |
| copilot/ | 0 | — |

---

## Rules

1. **Write to inbox first.** Every tool deposits into `00-Inbox/<tool>/`.
2. **Promote once.** Move approved file to `01-Canonical/`. Delete inbox copy.
3. **Update MANIFEST.** Every promote/delete updates this file.
4. **No parallel writes.** Only one tool owns edit rights to a canonical file at a time.
5. **Archive, don't delete.** Old versions go to `02-Archive/` with date suffix.
6. **OpenCode is librarian.** OpenCode has filesystem access — it handles dedup and cleanup.
