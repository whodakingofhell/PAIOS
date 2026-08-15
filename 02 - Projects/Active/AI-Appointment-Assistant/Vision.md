---
title: "AI Appointment Assistant — Vision"
version: "1.0"
status: "Canonical"
date: "2026-07-18"
tags:
  - project
  - vision
  - appointment
  - AI
  - paios/projects
  - paios/project/ai-appointment-assistant
owner: "OpenCode"
canonical: true
related:
  - "Product.md"
  - "Business.md"
---

# Project Vision

## 1. Project Name

**AI Appointment Assistant for Online Sellers**

---

## 2. Problem Statement

Online sellers and service providers (remote PC support, coaching, consulting) spend hours manually scheduling appointments. They face:

- Manual back-and-forth scheduling via chat/email
- Time zone confusion with overseas customers
- Short remote sessions (5–20 min) that need precise timing
- Missed bookings when notifications are delayed

**Who experiences it:** Solo online sellers, small service businesses, remote support providers

**Current alternatives:** Manual scheduling, Calendly (overkill for short sessions), no automation at all

---

## 3. Target Audience

| Persona | Description | Technical Level | Key Need |
|---------|-------------|-----------------|----------|
| Remote PC Support Tech | AnyDesk/TeamViewer sessions, 5–20 min | Low–Medium | Auto-book + notify via Discord |
| Online Coach/Consultant | Short video calls, timezone-sensitive | Low | Handle overseas clients automatically |
| Local Service Business | Appointments based in Philippines | Low | Simple chat-based booking |

---

## 4. Unique Value Proposition

**One-liner:** An AI that talks to your customers in natural language, books short remote appointments in Philippine time, and pings you on Discord instantly.

**Key differentiators:**
1. Philippine-time-anchored (Asia/Manila, UTC+8) — no DST confusion
2. Token-efficient — short questions, short answers, low cost
3. Discord-first notifications — instant booking alerts
4. 5–20 minute session enforcement — matches real remote support constraints

---

## 5. Long-Term Goals

| Timeframe | Goal | Measurable Target |
|-----------|------|-------------------|
| 6 months | MVP live — Claude brain + Discord webhook + Vercel UI | First paying customer using it |
| 12 months | Stable product — email notifications + booking analytics | 10 active sellers, <2% no-show rate |
| 24 months | Multi-platform — WhatsApp, Messenger integration | 50 sellers, $500/mo revenue |
| 36 months | Full SaaS — dashboard, templates, multi-agent support | 200 sellers, $2k/mo revenue |

---

## 6. Success Metrics

| Metric | Baseline | 6-Mo Target | 12-Mo Target | Tool |
|--------|----------|-------------|---------------|------|
| Booking completion rate | 0% | 80% | 90% | Supabase analytics |
| Avg conversation turns | — | ≤6 | ≤5 | Claude logs |
| Discord notification latency | — | <3s | <2s | Vercel function logs |
| Token cost per booking | — | <$0.02 | <$0.01 | Anthropic dashboard |
| Customer satisfaction | — | 4.0/5 | 4.5/5 | Post-booking survey |

---

## 7. Channel / Brand Mission Alignment

**Channel mission:** Designing, building, and improving real-world applications from concept to deployment.

**How this project aligns:**
- Documents the full AI product lifecycle (prompt engineering → backend → deployment)
- Demonstrates practical AI integration for small businesses
- Creates reusable patterns for token-efficient conversational AI
- Generates YouTube content from real build process

**Content opportunities:**
- "Building an AI Appointment Bot from Scratch" series
- "Token Efficiency in Production" deep dive
- "Philippine Time Zone Handling" tutorial

---

## QA Criticism

- [ ] Problem statement backed by user's own experience (not assumption)
- [ ] Target personas specific enough to guide product decisions
- [ ] UVP clearly differentiates from Calendly/Cal.com
- [ ] Long-term goals realistic given solo developer resources
- [ ] Success metrics measurable with Supabase + Vercel tooling
- [ ] Channel alignment explains why this project matters

---

## PAIOS Compliance

- **SSoT:** This file is the canonical vision. All downstream docs derive from it.
- **DRY:** Vision facts referenced here, not duplicated elsewhere.
- **Frontmatter:** Standardized per `Documentation-Standards.md`.
