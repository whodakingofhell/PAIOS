---
title: "Cost Map — AI Appointment Assistant"
version: "1.0"
status: "Canonical"
date: "2026-07-18"
tags: [integrations, cost, map, budget, paios/knowledge, paios/business]
owner: "OpenCode"
canonical: true
---
related:
  - "Business/01-Business.md"
  - "Business/Tool-Role-Mapping.md"
---

# Cost Map

> Track every tool, its free tier, and when to upgrade. $0/mo baseline enforced.

---

## Tool Costs

| Category | Tool | Free Tier | Limit | Paid Plan | When to Upgrade |
|----------|------|-----------|-------|-----------|-----------------|
| **LLM (brain)** | Claude (Anthropic) | Free tier | Limited messages | $20/mo Pro | >100 bookings/mo |
| **LLM (fallback)** | Gemini | Generous | Flash/Pro quotas | $20/mo | If Claude unavailable |
| **Hosting** | Vercel | Hobby | 100GB bandwidth, 100hrs build | $20/mo Pro | Custom domain or >100GB |
| **Database** | Supabase | Free | 500MB, 50k rows, 500MB bandwidth | $25/mo Pro | >50k bookings or >500MB |
| **Notifications** | Discord Webhook | Free | Unlimited | — | Never |
| **Research** | Perplexity | Free tier | Limited queries | $20/mo Pro | Deep research needs |
| **Tunneling (dev)** | nGrok | Free | 1 tunnel, random URL | $10/mo | Stable URL needed |
| **Version Control** | GitHub | Free | Unlimited repos | — | Never |
| **Knowledge Base** | Obsidian | Free | Local | — | Never |
| **AI Gateway** | Vercel AI Gateway | Included | 200+ models | — | Never |

---

## Monthly Cost Scenarios

| Scenario | LLM | Hosting | DB | Notifications | Total |
|----------|-----|---------|-----|--------------|-------|
| **Dev/testing** | $0 | $0 | $0 | $0 | **$0** |
| **10 bookings/mo** | $0 | $0 | $0 | $0 | **$0** |
| **50 bookings/mo** | $0 | $0 | $0 | $0 | **$0** |
| **100 bookings/mo** | $0–20 | $0 | $0 | $0 | **$0–20** |
| **500 bookings/mo** | $20 | $0 | $0 | $0 | **$20** |
| **1000+ bookings/mo** | $20 | $20 | $25 | $0 | **$65** |

---

## Upgrade Rules

1. **Never upgrade speculatively.** Hit the limit first.
2. **Justify with revenue.** Upgrade only if revenue > 2x the cost.
3. **One tool at a time.** Don't batch upgrades.
4. **Document in MANIFEST.md.** Every upgrade is a tracked decision.

---

## Token Cost Calculator

| Model | Input $/1M tokens | Output $/1M tokens | Per Booking (est.) |
|-------|-------------------|---------------------|-------------------|
| Claude Haiku | $0.25 | $1.25 | ~$0.001 |
| Claude Sonnet | $3.00 | $15.00 | ~$0.01 |
| Claude Opus | $15.00 | $75.00 | ~$0.05 |
| Gemini Flash | $0.075 | $0.30 | ~$0.0003 |

**Recommended:** Claude Haiku for conversations (best cost/quality for short exchanges).

---

## PAIOS Compliance

- **SSoT:** Cost data lives here. Other docs reference this file.
- **DRY:** Not duplicated in Business.md or Vision.md (summary only).
