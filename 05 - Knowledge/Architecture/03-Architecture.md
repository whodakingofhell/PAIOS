# 03 — Architecture

> Section 03 of the AI Engineering OS

---

## Purpose

Defines the **system architecture, technology stack, data flow, integration architecture, and deployment architecture** for the entire operation. Ensures scalability, maintainability, modularity, and fault tolerance across all systems.

---

## Owner Team

**Architecture Team** (`Team\Architecture.md`) — Enterprise, Solution, System, Cloud, Integration Architects

---

## Key Responsibilities

- Design and maintain the **system architecture** across all components.
- Select and justify **technology choices** with cost, capability, and maintainability trade-offs.
- Define **data flow** between tools, services, and storage layers.
- Own the **integration architecture** (how n8n, APIs, AI services, and storage connect).
- Enforce **architectural principles** (separation of concerns, loose coupling, stateless services).
- Maintain **architecture decision records (ADRs)** for every significant technology choice.
- Plan for **scalability and fault tolerance** from day one.

---

## Technology Stack

### Core Stack (the $0/mo backbone)

```
┌─────────────────────────────────────────────────────────────┐
│                      PRESENTATION LAYER                      │
│  YouTube (channel)  │  Vercel (landing/docs)  │  Obsidian   │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    ORCHESTRATION LAYER                       │
│                    n8n (self-hosted Docker)                  │
│         Workflows  │  Triggers  │  Webhooks  │  Queues      │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                     AI / LLM LAYER                          │
│  Gemini (primary)  │  Claude (judgment)  │  NotebookLM     │
│  Perplexity (research)  │  ElevenLabs (voice)                │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    PROCESSING LAYER                          │
│  FFmpeg (video)  │  ComfyUI/SDXL (images)  │  Higgsfield   │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                      DATA LAYER                              │
│  Obsidian Vault (KB)  │  JSON (pipeline state)  │  .env     │
│  GitHub (version control)  │  YouTube API (analytics)       │
└─────────────────────────────────────────────────────────────┘
```

### Technology Justification

| Technology | Role | Why this one |
|---|---|---|
| **n8n (self-hosted)** | Orchestration | Free, visual, 400+ integrations, runs locally — no vendor lock-in |
| **Gemini** | Primary LLM | Most generous free tier, fast, multimodal (text + image) |
| **Claude** | High-judgment LLM | Best at code review, critical analysis, nuanced reasoning |
| **NotebookLM** | Research + voice | Free, Google-grounded, generates audio overviews (reusable as content) |
| **Perplexity** | Research | Real-time web grounding with sources — fact-checking |
| **ElevenLabs** | Voice generation | Best TTS quality; free tier for pilot; NotebookLM audio as $0 fallback |
| **FFmpeg** | Video assembly | Industry standard, free, fully scriptable, no API needed |
| **ComfyUI / SDXL** | Image generation | Free, local, unlimited — no rate limits, no API costs |
| **Higgsfield** | Animation | Free credits for character animation, unique differentiator |
| **Obsidian** | Knowledge base | Local-first, markdown, extensible, free — no cloud dependency |
| **GitHub** | Version control | Free private repos, CI/CD via Actions, collaboration |
| **Vercel** | Hosting | Free hobby tier, instant deploys from GitHub, custom domains |
| **Slack** | Notifications | Free webhook integration — alerts on pipeline events |

---

## Data Flow

```
                    ┌──────────────┐
                    │    INTAKE    │
                    │ (files/text) │
                    └──────┬───────┘
                           │ normalize to JSON
                           ▼
                    ┌──────────────┐
                    │  KNOWLEDGE   │
                    │    BASE      │  ← Obsidian vault + processed JSON
                    │  (Obsidian)  │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │ CONTENT  │ │ PRODUCT  │ │ AUTOMATION│
        │ PIPELINE │ │  BUILD   │ │  n8n      │
        │ 14 stages│ │ CI/CD    │ │ workflows │
        └────┬─────┘ └────┬─────┘ └────┬─────┘
             │            │            │
             ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │ YOUTUBE  │ │ VERCEL/  │ │ SLACK    │
        │  (publish)│ │  GITHUB  │ │ (alerts) │
        └────┬─────┘ └────┬─────┘ └──────────┘
             │            │
             ▼            ▼
        ┌──────────┐ ┌──────────┐
        │ANALYTICS │ │  USERS   │
        │→ KB loop │ │ (audience)│
        └──────────┘ └──────────┘
```

---

## Integration Architecture

### n8n as the Integration Hub

All integrations route through n8n workflows. Each tool has a dedicated node type or HTTP request node:

```
┌───────────────────────────────────────────────────────┐
│                    n8n WORKFLOWS                        │
│                                                        │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐          │
│  │ Watch   │───▶│ Process │───▶│ Publish │          │
│  │ (trigger)│    │ (chain)  │    │ (action)│          │
│  └─────────┘    └─────────┘    └─────────┘          │
│       │              │              │                 │
│  File Watcher   Gemini API     YouTube API           │
│  Cron Schedule  Claude API     GitHub API             │
│  Webhook       ElevenLabs     Slack Webhook          │
│  Manual        FFmpeg cmd     Vercel API             │
│                ComfyUI API                           │
└───────────────────────────────────────────────────────┘
```

### API Key Management

- All keys stored in `Pipeline\.env` (never committed).
- n8n loads env vars via Docker Compose `env_file: .env`.
- Each n8n node references `{{$env.KEY_NAME}}` — no hard-coded secrets.

---

## Architectural Principles

1. **Separation of concerns.** Pipeline stages are independent scripts. n8n orchestrates; scripts execute. Swap tools without rewriting the pipeline.
2. **Stateless services.** Each pipeline stage reads input, writes output, and terminates. No shared mutable state between stages.
3. **JSON as the lingua franca.** All inter-stage communication uses JSON files. Any tool can consume/produce JSON.
4. **Loose coupling.** Swap Gemini for GPT-4, FFmpeg for DaVinci Resolve, ElevenLabs for Azure TTS — without touching other stages.
5. **Fail-forward with alerts.** Each stage logs success/failure. On failure: alert via Slack, mark stage as failed, allow manual retry. Don't crash the whole pipeline.
6. **Local-first, cloud-optional.** Every tool runs locally or via free-tier API. No dependency on a single cloud provider.

---

## Inputs

- Product requirements (`02-Product\Product.md`)
- Business constraints — cost, timeline, team capacity (`01-Business\Business.md`)
- Security requirements (`06-Security\Security.md`)
- Tool evaluations from `integrations\*`

---

## Outputs

- This architecture document (source of truth for all system decisions)
- Architecture Decision Records (ADRs) for each technology choice
- Data flow diagrams
- Integration specifications
- Deployment architecture

---

## Acceptance Criteria

- [ ] Technology stack is fully justified with alternatives considered.
- [ ] Data flow diagram covers intake → processing → output → feedback loop.
- [ ] Every tool has a documented integration method (n8n node or HTTP).
- [ ] API key management strategy is defined (`.env` + n8n env vars).
- [ ] Architectural principles are ≤6, clear, and enforceable.
- [ ] Swapping any one tool doesn't require rewriting the pipeline.

---

## Cross-References

| Document | Relationship |
|---|---|
| `04-Engineering\Engineering.md` | Engineering standards implement this architecture |
| `05-Quality-Assurance\QA-Framework.md` | QA gates validate architectural decisions |
| `06-Security\Security.md` | Security architecture layer |
| `07-Automation\Automation.md` | n8n automation implements this architecture |
| `Project\Architecture.md` | Per-project architecture spec |
| `integrations\*` | Per-tool setup guides |
