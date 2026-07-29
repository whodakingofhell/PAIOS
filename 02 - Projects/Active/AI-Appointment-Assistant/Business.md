---
title: "AI Appointment Assistant — Business"
version: "1.0"
status: "Canonical"
date: "2026-07-18"
tags:
  - project
  - business
  - monetization
  - cost
  - paios/projects
  - paios/project/ai-appointment-assistant
owner: "OpenCode"
canonical: true
related:
  - "Product.md"
  - "Vision.md"
---

# Business Model

---

## Revenue Streams

| # | Stream | Type | Activation | Target |
|---|--------|------|------------|--------|
| 1 | **Direct use** (saves owner time) | Value | Day 1 | $0 — replaces manual work |
| 2 | **SaaS subscription** | Product | Month 6 | $15–30/seller/mo |
| 3 | **Template marketplace** | Product | Year 1 | $10–50/template |
| 4 | **YouTube content** | Content | Day 1 | AdSense + sponsors |
| 5 | **Consulting** | Service | On demand | $50–100/hr |

---

## Cost Structure — $0 First

| Category | Tool | Free Tier | Paid Trigger | Est. Monthly |
|----------|------|-----------|-------------|-------------|
| LLM (brain) | Claude | Limited free | Volume | $0 → $20 |
| Hosting | Vercel | Hobby (100GB) | Custom domain | $0 → $20 |
| Database | Supabase | 500MB, 50k rows | Storage exceeded | $0 → $25 |
| Notifications | Discord webhook | Free | — | $0 |
| Research | Perplexity | Free tier | Deep research | $0 → $20 |
| Knowledge base | Obsidian | Local, free | — | $0 |
| Version control | GitHub | Free repos | — | $0 |
| Tunneling (dev) | nGrok | Free tier | — | $0 |

**Baseline: $0/mo.** Upgrade only when free quota hit AND revenue justifies.

---

## Unit Economics

| Metric | Value | Notes |
|--------|-------|-------|
| Cost per booking (tokens) | <$0.02 | Claude Haiku for conversations |
| Cost per booking (infra) | <$0.001 | Vercel serverless + Supabase free |
| Revenue per booking (SaaS) | $0.50–1.00 | At $15–30/mo for active sellers |
| Break-even | 30 bookings/mo | Per seller at $15/mo plan |

---

## Competitive Positioning

| Competitor | Our Differentiator |
|-----------|-------------------|
| Calendly | We handle short sessions (5–20 min), not 30–60 min meetings |
| Cal.com | We're AI-native chat, not calendar grid |
| Manual scheduling | We automate the entire flow |
| ChatGPT plugins | We're deployed, persistent, with Discord integration |

**Niche:** AI-native appointment booking for short remote support sessions, Philippine-time-anchored.

---

## PAIOS Compliance

- **SSoT:** Business decisions flow from Vision.md
- **DRY:** Cost data referenced from `01-Canonical/Integrations/cost-map.md` when created
