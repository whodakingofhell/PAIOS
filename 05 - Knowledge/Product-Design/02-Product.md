---
tags: [paios/knowledge, paios/product-design, product-management, lifecycle]
related:
  - "Product-Design/Content-Pipeline.md"
  - "Product-Design/Feature-Score-Rubric.md"
  - "Product-Design/Product-Lifecycle.md"
  - "Software-Development/00-Vision.md"
  - "Business/01-Business.md"
  - "Software-Development/12-Roadmap.md"
---

# 02 — Product

> Section 02 of the AI Engineering OS

---

## Purpose

Defines **what we build** — the YouTube channel itself as a product, plus any software products, tools, and digital assets that emerge from the build-in-public process. Governs product-market fit, feature prioritization, release cadence, and scope management.

---

## Owner Team

**Executive** (`Team\Executive.md`) — Product Director + CTO

---

## Key Responsibilities

- Define the **product portfolio** (channel + software products + digital assets).
- Maintain **product-market fit** through continuous audience feedback analysis.
- Own the **feature prioritization framework** (what we build next and why).
- Enforce **MVP scoping** — ship the minimum that delivers value, then iterate.
- Manage the **release cadence** for both content (videos) and software.
- Ensure every product has a clear **value proposition** and **monetization path**.

---

## Product Portfolio

### Primary Product: The YouTube Channel

| Attribute | Definition |
|---|---|
| **What it is** | A build-in-public engineering journal that turns the development process into educational content |
| **Who it's for** | Developers, IT professionals, students, tech enthusiasts |
| **Core value** | Watch real software get planned, built, tested, deployed, and monetized — learn by observing |
| **Format** | Long-form tutorials (15–30 min), project walkthroughs, tool deep-dives, live coding sessions |
| **Cadence** | 2–4 videos/week (automated pipeline target: daily capable) |
| **Monetization** | AdSense → Affiliates → Sponsorships → Courses → Own products |

### Secondary Products (emerge from build-in-public)

| Product | Type | Trigger | Revenue Model |
|---|---|---|---|
| AI Engineering OS Framework | Open-source repo | When framework is proven internally | Donation + consulting |
| Prompt packs / templates | Digital download | When prompts are validated | One-time purchase |
| Automation workflow packs | Digital download | When n8n workflows are stable | One-time / subscription |
| Video creation masterclass | Course | When 10k+ subs, proven process | Course fee |
| Build tools / CLIs | SaaS or OSS | When internal tools have external demand | Freemium / SaaS |

---

## Feature Prioritization Framework

### RICE Scoring (for products and features)

| Factor | Definition | Scale |
|---|---|---|
| **Reach** | How many viewers/users affected per month | 1–10 (10 = all viewers) |
| **Impact** | How much value it delivers per person | 1–5 (5 = transformative) |
| **Confidence** | How sure we are about Reach and Impact | % (50%–100%) |
| **Effort** | Person-days to build | Days |
| **RICE Score** | (Reach × Impact × Confidence) / Effort | Numeric — higher = prioritize |

### Priority Matrix (for content topics)

| Axis | High | Low |
|---|---|---|
| **Audience Demand** (search volume + comments) | Build immediately | Queue for later |
| **Alignment with Vision** (build-in-public, engineering depth) | Feature in series | Consider if easy |
| **Production Feasibility** (can the pipeline produce it?) | Automate in pipeline | Manual one-off |

---

## MVP Scoping Rules

1. **What's the smallest thing that delivers the stated value?** Build that first.
2. **Cut scope until removing more would break the value proposition.** That's the MVP.
3. **Time-box MVPs to 2 weeks max.** If it's bigger, split it into phases.
4. **Every MVP must have a measurable success metric.** Ship → measure → iterate.
5. **No gold-plating.** Polish is for the iteration phase, not the MVP.

---

## Release Cadence

| Product Type | Cadence | Gate |
|---|---|---|
| YouTube videos | 2–4/week (staging for daily) | QA Review (stage 11 of content pipeline) |
| Software products | Per-milestone in roadmap | QA Gate #1 + Gate #2 |
| Digital assets | As validated | Business value score ≥ 8.0 |
| Framework updates | Monthly or per significant change | Framework stability principle |

---

## Inputs

- Vision and audience definition (`00-Vision\Vision.md`)
- Business model and revenue targets (`01-Business\Business.md`)
- Audience feedback and analytics (`10-Marketing\Marketing.md`)
- Technical feasibility assessment (`03-Architecture\Architecture.md`)
- Available automation capacity (`07-Automation\Automation.md`)

---

## Outputs

- This product document (the source of truth for what we build)
- Product roadmap with prioritized features (`12-Roadmap\Roadmap.md`)
- MVP specifications for each active product
- Feature backlog with RICE scores

---

## Operating Principles

1. **Audience-driven.** Build what the audience asks for (search data, comments, analytics) — not what we assume they want.
2. **Ship fast, iterate faster.** An imperfect product shipped today beats a perfect product shipped never.
3. **Content is product.** Every video is a product with its own scope, MVP, QA gate, and success metric.
4. **Portfolio balance.** At least 60% effort on the primary product (channel). Secondary products get remaining capacity.
5. **Kill ruthlessly.** If a product's metrics don't improve after 2 iterations, sunset it and reallocate.

---

## Acceptance Criteria

- [ ] Product portfolio is defined with primary + secondary products.
- [ ] RICE scoring framework is documented with examples.
- [ ] MVP scoping rules are ≤5, clear, and enforceable.
- [ ] Release cadence is defined per product type with gates.
- [ ] Every active product has a one-sentence value proposition.

---

## Cross-References

| Document | Relationship |
|---|---|
| `00-Vision\Vision.md` | Products serve the vision |
| `01-Business\Business.md` | Products generate the revenue the business needs |
| `03-Architecture\Architecture.md` | Architecture enables the products |
| `12-Roadmap\Roadmap.md` | Roadmap sequences the product builds |
| `Frameworks\Content-Pipeline.md` | Pipeline produces the primary product (videos) |
| `Project\Product.md` | Per-project product spec template |
