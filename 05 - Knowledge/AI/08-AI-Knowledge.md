---
tags:
  - paios/knowledge
  - paios/ai
  - knowledge-management
  - prompt-engineering
  - rag
related:
  - "../Knowledge-MOC.md"
  - "AI-Engineering.md"
  - "Claude Master Prompt - Online Seller Support and Retail Assistant.md"
  - "AI/MASTER-FRAMEWORK.md"
  - "AI/Claude-Handoff.md"
  - "Software-Development/09-Documentation.md"
---

# 08 — AI Knowledge

> Section 08 of the AI Engineering OS

---

## Purpose

Defines the **knowledge management strategy, Obsidian vault structure, prompt engineering standards, context engineering, AI memory systems, and RAG approach**. Ensures every AI interaction is grounded, reproducible, and continuously improving from accumulated knowledge.

---

## Owner Team

**AI Engineering Team** (`Team\AI-Engineering.md`) — Prompt Engineer, LLM Engineer, AI Workflow Engineer, RAG Specialist, Knowledge Engineer

---

## Key Responsibilities

- Design and maintain the **Obsidian vault** as the central knowledge base.
- Manage the **prompt library** — versioned, tested, scored prompts for every pipeline stage.
- Engineer **context** for each AI interaction (what goes into the prompt window).
- Implement **RAG (Retrieval-Augmented Generation)** for grounding AI outputs in real data.
- Design **AI memory systems** that persist context across sessions.
- Extract **structured knowledge** from pipeline outputs (videos, scripts, analytics).
- Optimize **token efficiency** — maximum signal per token, minimal waste.

---

## Knowledge Base Architecture (Obsidian Vault)

### Vault Structure

```
Obsidian Vault/
├── 00-Inbox/                    ← quick capture (notes, links, ideas)
│
├── 01-Topics/                   ← knowledge by topic
│   ├── Python/
│   ├── System Design/
│   ├── Cybersecurity/
│   ├── AI & LLMs/
│   ├── DevOps/
│   └── Productivity/
│
├── 02-Projects/                 ← per-project knowledge
│   └── [project-name]/
│       ├── research/
│       ├── decisions/
│       ├── learnings/
│       └── references/
│
├── 03-Content/                  ← content pipeline artifacts
│   ├── scripts/
│   ├── storyboards/
│   ├── metadata/
│   ├── analytics/
│   └── feedback/
│
├── 04-Prompts/                  ← versioned prompt library
│   ├── content-planning/
│   ├── script-generation/
│   ├── research/
│   ├── thumbnail/
│   ├── metadata/
│   ├── seo/
│   └── qa-review/
│
├── 05-Templates/                ← reusable note templates
│
├── 06-References/               ← external references, API docs, guides
│
├── 07-Archives/                 ← completed/deprioritized content
│
└── .obsidian/                   ← Obsidian config (versioned)
```

### Vault Principles

1. **Markdown-first.** Everything is `.md`. No proprietary formats.
2. **Linked, not siloed.** Use `[[wiki-links]]` to connect related notes. A note without links is a dead end.
3. **Atomic notes.** One idea per note. Combine in MOCs (Maps of Content), don't blob.
4. **Tagged, not filed.** Tags for discoverability (`#python`, `#security`, `#pipeline-stage-2`).
5. **Versioned via Git.** Vault is a GitHub repo. Every change is tracked.

---

## Prompt Library Management

### Prompt Versioning

Every prompt in `04-Prompts/` follows this structure:

```markdown
---
id: content-planning-v1.3
stage: 1
model: gemini
tokens_in: ~2000
tokens_out: ~1500
score: 9.2
last_tested: 2026-07-17
status: production
---

# Content Planning Prompt

## Role
...

## Objective
...

## Inputs
...

## Constraints
...

## Output Format
...

## QA Checklist (auto-injected)
...

## Changelog
- v1.3: Added competitive analysis step (2026-07-15)
- v1.2: Improved output format for storyboard compatibility (2026-07-10)
- v1.1: Fixed token overflow in research section (2026-07-05)
```

### Prompt Scoring

Prompts are scored on the same Feature Score Rubric:
- **Accuracy** (does it produce correct output?)
- **Consistency** (does it produce the same quality across runs?)
- **Token Efficiency** (output quality per token — maximize signal, minimize waste)
- **Reproducibility** (does another person/model get the same result?)

Score ≥ 9.0 = production. < 8.0 = revise before use.

---

## Context Engineering

### The Context Window Strategy

Not everything goes into one prompt. Context is layered:

```
Layer 1: System Prompt (always present)
  └─ Role, principles, output format rules

Layer 2: Task Prompt (per stage)
  └─ Stage-specific instructions, input format

Layer 3: Injected Context (variable)
  └─ Intake data, research results, previous stage output

Layer 4: Criticism Framework (auto-injected)
  └─ QA checklist, score rubric

Layer 5: One-shot Examples (when needed)
  └─ 1-2 high-quality examples of desired output
```

### Token Budget per Stage

| Stage | Model | Input Tokens | Output Tokens | Total Budget |
|---|---|---|---|---|
| 0: Intake | Local (no LLM) | 0 | 0 | — |
| 1: Content Planning | Claude | ~2,000 | ~1,500 | 3,500 |
| 2: Script Gen | Gemini | ~3,000 | ~4,000 | 7,000 |
| 3: Research/Voice | NotebookLM | Variable | Variable | ~10,000 |
| 4: Storyboard | Gemini | ~2,500 | ~2,000 | 4,500 |
| 5: Animation | Image gen | — | — | — |
| 6: Voice | ElevenLabs | — | — | — |
| 7: Video Edit | FFmpeg | — | — | — |
| 8: Thumbnail | Image gen | — | — | — |
| 9: Metadata | Gemini | ~1,500 | ~1,000 | 2,500 |
| 10: SEO | Gemini + Perplexity | ~2,000 | ~1,000 | 3,000 |
| 11: QA Review | Claude | ~5,000 | ~2,000 | 7,000 |
| 12: Upload | YouTube API | — | — | — |
| 13: Analytics | YouTube API | — | — | — |

---

## RAG Approach (Retrieval-Augmented Generation)

### For Content Grounding

When generating scripts or content, ground in real data:

1. **Ingest** intake material → structured JSON (`Pipeline\intake\processed\`).
2. **Research** via Perplexity/NotebookLM → source-annotated findings.
3. **Retrieve** relevant vault notes via keyword/tag search.
4. **Inject** top-5 relevant notes + research findings into the prompt context.
5. **Generate** grounded content that references sources.
6. **Validate** QA stage (11) checks factual grounding.

### For Knowledge Retrieval

When answering questions or planning content:
1. Search Obsidian vault by tags + links.
2. Search analytics history for performance data.
3. Search content history for related/competing topics.
4. Combine into a knowledge context packet.
5. Feed to LLM with the task prompt.

---

## AI Memory Systems

### Short-Term Memory (within a pipeline run)
- Pipeline state JSON passed between stages (script N reads script N-1 output).
- Session context maintained in n8n workflow variables.

### Medium-Term Memory (across pipeline runs)
- Obsidian vault accumulates all scripts, metadata, analytics, feedback.
- Structured indices: topic index, performance index, content calendar.

### Long-Term Memory (across projects)
- Cross-project patterns: what topics perform, what tools work, what prompts score high.
- Archived in `07-Archives/` with searchability maintained via tags.

---

## Token Efficiency (Maximize Signal, Minimize Waste)

1. **Compress context.** Summarize previous stage output before injecting (don't dump raw JSON).
2. **Structured output.** Require JSON or markdown tables — easier to parse, fewer wasted tokens on formatting.
3. **No filler.** Prompts explicitly say: "No preamble. No pleasantries. Output only the requested format."
4. **Cache when possible.** Gemini and Claude support prompt caching — reuse system prompts across calls.
5. **Measure cost per output.** Track tokens per video produced. Optimize prompts that are token-heavy but low-quality.

---

## Inputs

- Content pipeline specifications (`Frameworks\Content-Pipeline.md`)
- Pipeline stage scripts (`Pipeline\scripts\`)
- Analytics data (from stage 13)
- External research (Perplexity, NotebookLM)

---

## Outputs

- Structured knowledge in Obsidian vault
- Versioned prompt library
- Context packets for each pipeline stage
- Token efficiency metrics
- RAG retrieval results

---

## Operating Principles

1. **Knowledge compounds.** Every pipeline run adds to the vault. The system gets smarter over time.
2. **Prompt engineering is engineering.** Prompts are versioned, tested, scored, and iterated like code.
3. **Ground everything.** AI output without sources is speculation. Ground in data, research, and vault knowledge.
4. **Token budget discipline.** Every token costs attention or money. Make each one count.
5. **Searchable by default.** If it's in the vault, it must be findable via tags, links, or search.

---

## Acceptance Criteria

- [ ] Obsidian vault structure is defined with 8 top-level folders.
- [ ] Prompt versioning format is defined with metadata fields.
- [ ] Context layering strategy is documented (5 layers).
- [ ] Token budget is estimated per pipeline stage.
- [ ] RAG approach is defined for content grounding and knowledge retrieval.
- [ ] Token efficiency rules are stated (≤5, concrete).
- [ ] Memory systems are defined for short, medium, and long-term.

---

## Cross-References

| Document | Relationship |
|---|---|
| `07-Automation\Automation.md` | Automation orchestrates knowledge flows |
| `09-Documentation\Documentation.md` | Documentation standards apply to vault notes |
| `Frameworks\Content-Pipeline.md` | Pipeline produces knowledge that feeds back |
| `Pipeline\prompts\` | The actual prompt files used in the pipeline |
| `Pipeline\scripts\` | Scripts that read/write knowledge artifacts |

## Applied in PAIOS Projects

**AI-Appointment-Assistant** — The Claude master prompt (`AI-Appointment-Assistant/Claude Master Prompt - Online Seller Support and Retail Assistant.md`) and its companion `Claude-Brain-Prompt.md` were the first production-grade prompts that informed the prompt versioning standard in this section. The research folder (`AI-Appointment-Assistant/research/`) contains the original RAG experiments where Obsidian vault notes were injected into Claude's context to improve appointment-slot suggestions — directly validating the "Ground everything" principle. The token budget table in this document evolved from tracking actual API consumption during this project's pipeline.

**deploy-v2** — The `MASTER-FRAMEWORK.md` document from this project defined the context layering approach (system → task → injected → criticism → examples) that is now codified as the 5-layer context strategy here. The prompt scoring methodology (accuracy, consistency, token efficiency, reproducibility) was first tested on deploy-v2's deployment-prompting workflows.
