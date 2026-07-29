---
title: "PAIOS AI Router"
type: ai-instruction
status: active
owner: "PAIOS"
created: 2026-07-29
updated: 2026-07-29
ai_access: internal
ai_generated: true
review_status: draft
canonical: true
tags:
  - paios/system
related:
  - "./ARCHITECTURE.md"
  - "./CONTEXT-POLICY.md"
  - "./DESIGN.md"
  - "./PRODUCT.md"
---

# PAIOS AI Router

`AGENTS.md` is the canonical shared AI router. `CONTEXT-POLICY.md` is the retrieval and privacy authority.

## Bootstrap

1. Confirm the root by locating this file and `00 - System/Config/ai-context-manifest.yaml`.
2. Read `me.md`.
3. Classify the task.
4. Load only the matching authority or selected project context.
5. Stop loading when enough verified context exists.

## Task Bundles

Refer to `00 - System/Config/ai-context-manifest.yaml` for full bundle definitions. Short-form:

- Quick task: `AGENTS.md`, `me.md`.
- Normal active work: add root `memory.md` and `handoff.md`.
- Active project: load matching project entry from manifest; add project `memory.md`/`handoff.md` only when present.
- New project: load `new_project` bundle from manifest (template + patterns + lessons).
- Architecture/design/product: load only the matching root authority and relevant project context.
- Business: load `01 - Business/Business-MOC.md` and the exact required file.

## Reference Files

- `05 - Knowledge/References/Lessons-Ledger.md` — Cross-project lessons learned
- `05 - Knowledge/References/Project-Patterns.md` — Reusable architecture patterns

## Default Exclusions

Never broadly load reports, state, linked-source inventories, attachments, archives, histories, logs, credentials, secrets, entire daily history, entire project trees, or large generated data.

## Write Rules

- Preserve existing content and use reversible edits.
- Never store credentials in Markdown.
- Treat missing `ai_access` as restricted.
- AI-generated operational knowledge starts as draft.
- `memory.md` is durable and approved; `handoff.md` is current and replace-and-refresh.
- Do not commit, publish, configure remotes, or push without explicit authorization.

