---
title: "PAIOS Memory"
type: memory
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
  - "./handoff.md"
  - "./CHANGELOG.md"
---

# Purpose

Store durable, reviewed decisions, constraints, terminology, and lessons for PAIOS.

# Durable Decisions

- Markdown and the numbered domain contract are canonical.
- Running work and durable intent remain separate.
- Private and generated operational state is not public context.
- Content from PROMPT GUIDE AI, AI-Ops-Vault, AI PROJECTS consolidated into 05 - Knowledge/
- All knowledge files are reusable across projects (Security.md, SECURITY_ARCHITECTURE.md, etc.)
- AI tools used: OpenCodeAI, Claude Code, ChatGPT, Z.codeAI — all wire through AGENTS.md

# Long-Lived Constraints

- Do not store tasks, transcripts, raw reports, secrets, duplicated project content, speculation, or completed execution history here.
- Target below 3,000 tokens; review at 4,000; hard warning at 6,000.
- Project source code stays in 02 - Projects; knowledge stays in 05 - Knowledge.
- node_modules and build artifacts never committed to vault.

