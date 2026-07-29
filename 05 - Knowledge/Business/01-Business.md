# 01 — Business

> Section 01 of the AI Engineering OS

---

## Purpose

Defines the **business model, monetization strategy, cost structure, and competitive positioning** for the channel and any associated products. Ensures every decision has a clear path to sustainability and growth.

---

## Owner Team

**Executive** (`Team\Executive.md`) — CEO, CTO, Product Director

---

## Key Responsibilities

- Define and maintain the **business model** across all revenue streams.
- Enforce the **$0-first cost discipline** — free tiers before paid, upgrades justified by ROI.
- Track **unit economics** (cost per video, cost per subscriber, revenue per video).
- Monitor **competitive positioning** and differentiate in the developer-education space.
- Maintain **monetization compliance** (YouTube policies, FTC affiliate disclosure, GDPR).
- Set **revenue targets** and track actuals against projections.

---

## Business Model

```
                    ┌─────────────────────┐
                    │   CONTENT ENGINE    │
                    │  (YouTube channel)  │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌──────────┐   ┌──────────────┐  ┌───────────┐
        │ AdSense  │   │ Sponsorships │  │ Affiliates│
        │ (passive)│   │  (active)    │  │ (passive) │
        └──────────┘   └──────────────┘  └───────────┘
              │                │                │
              └────────────────┼────────────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌──────────┐   ┌──────────────┐  ┌───────────┐
        │  Courses  │   │  Own Tools/  │  │Consulting│
        │ (digital) │   │  Products     │  │ (services)│
        └──────────┘   └──────────────┘  └───────────┘
```

### Revenue Streams (ordered by activation timeline)

| # | Stream | Type | Activation | Target |
|---|---|---|---|---|
| 1 | **YouTube AdSense** | Passive | Day 1 (YPP at 1k subs/4k hours) | $500–2k/mo at scale |
| 2 | **Affiliate links** | Passive | Month 1 (tool reviews, tutorials) | $200–1k/mo |
| 3 | **Sponsorships** | Active | 5k+ subscribers | $500–5k/video at scale |
| 4 | **Digital courses** | Product | 10k+ subscribers | $2k–10k/mo |
| 5 | **Own tools/templates** | Product | Year 1+ (sell pipeline configs, prompt packs) | $500–3k/mo |
| 6 | **Consulting/coaching** | Service | On demand | $100–300/hr |

---

## Cost Structure

### Principle: $0/mo first. Upgrade only when free quota is exhausted AND measurable ROI justifies it.

| Category | Tool | Free Tier | Paid Trigger | Est. Monthly Cost |
|---|---|---|---|---|
| LLM (primary) | Gemini | Generous (Flash/Pro) | Volume exceeds free | $0 → $20 |
| LLM (judgment) | Claude | Limited free | High-judgment tasks exceed | $0 → $20 |
| Research | NotebookLM | Free | N/A | $0 |
| Research | Perplexity | Free tier | Deep research needs | $0 → $20 |
| Voice | ElevenLabs | 10k chars/mo | Character limit hit | $0 → $5 |
| Voice fallback | NotebookLM audio | Free | N/A | $0 |
| Animation | Higgsfield | Free credits | Credits exhausted | $0 → $10 |
| Images | ComfyUI/SDXL | Local, $0 | N/A | $0 |
| Video assembly | FFmpeg | Local, $0 | N/A | $0 |
| Upload | YouTube API v3 | 10k units/day | N/A | $0 |
| Knowledge base | Obsidian | Local, $0 | N/A | $0 |
| Repo | GitHub | Free | N/A | $0 |
| Hosting | Vercel | Hobby free | Custom domain needs | $0 → $20 |
| Notifications | Slack | Free webhooks | N/A | $0 |
| Orchestration | n8n | Self-hosted, $0 | N/A | $0 |

**Baseline: $0/mo.** Full details in `integrations\cost-map.md`.

---

## Competitive Positioning

| Competitor Type | Example | Our Differentiator |
|---|---|---|
| Big tutorial channels | Fireship, Traversy Media | We build end-to-end projects in public, not just tutorials |
| AI-focused channels | AI Jason, Matthew Berman | We integrate AI into real engineering workflows, not AI demos |
| Dev tool reviewers | Theo, NetworkChuck | We build WITH tools, not just review them |
| Course creators | Colt Steele, Andrei Neagoie | Free content-first; courses are a later revenue layer |

**Our niche:** *The engineering build journal* — raw, real, from concept to deployed product, with AI deeply embedded in the process.

---

## Revenue Targets

| Milestone | Subscribers | Monthly Revenue | Primary Streams |
|---|---|---|---|
| **MVP** | 1,000 | $0–100 | Affiliates only |
| **Growth** | 10,000 | $500–2,000 | AdSense + Affiliates + first sponsorships |
| **Scale** | 50,000 | $3,000–8,000 | All streams active |
| **Brand** | 100,000 | $8,000–20,000 | Courses + tools dominant |

---

## Inputs

- Vision and audience definition (`00-Vision\Vision.md`)
- Channel analytics and audience data
- Market research on competitor channels
- Cost data from `integrations\cost-map.md`

---

## Outputs

- This business document (reference for all financial decisions)
- Revenue model and projections (tracked in `11-Revenue\Revenue.md`)
- Cost baseline and upgrade triggers (fed into automation decisions)
- Competitive analysis (fed into `10-Marketing\Marketing.md`)

---

## Operating Principles

1. **Unit economics discipline.** Every video and product has a cost and an expected return. Track both.
2. **Revenue diversification.** No single stream should exceed 40% of total revenue at scale.
3. **Compliance first.** FTC disclosures on every affiliate link. YouTube policies followed. No black-hat SEO.
4. **Cost-aware automation.** Every n8n workflow has a cost estimate per execution. Free-tier limits are monitored.

---

## Acceptance Criteria

- [ ] Business model diagram is complete with all 6 revenue streams.
- [ ] Cost table lists every tool with free-tier limits and paid triggers.
- [ ] Revenue targets are set at 4 milestone points with subscriber counts.
- [ ] Competitive differentiation is articulated in one sentence.
- [ ] Unit economics formula is defined and trackable.

---

## Cross-References

| Document | Relationship |
|---|---|
| `00-Vision\Vision.md` | Business serves the vision |
| `11-Revenue\Revenue.md` | Detailed revenue tracking per stream |
| `10-Marketing\Marketing.md` | Marketing drives the business metrics |
| `07-Automation\Automation.md` | Automation reduces per-unit costs |
| `integrations\cost-map.md` | Detailed free-tier limits and upgrade triggers |
