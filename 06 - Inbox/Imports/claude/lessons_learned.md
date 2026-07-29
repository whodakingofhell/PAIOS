---
title: "Lessons Learned / Decision Log — Sessions 1-3"
version: "1.0"
status: "Inbox — pending promotion"
date: "2026-07-18"
tags: [project, lessons, decisions, log]
owner: "Claude"
canonical: false
source: "Claude Anthropic (second-in-command agent)"
---

# Lessons Learned / Decision Log — Session 1 (2026-07-15)

## What was reviewed
All prior docs: Vision, Product Brief, Timezone, Should_know_and_do, Pipeline_v1, Architecture, Claude Appointment Brain v1, Claude Master Prompt, Token Efficiency, What good AI schedulers do, Decision Support Tool.

## What was wrong / missing
1. `Claude Appointment Brain – v1.md` internally contradicted itself: 5–20 min duration rule vs. a leftover 30/60-min "slot length" reference. **Fixed** in v2.
2. Working hours, minimum notice, and daily cap were never finalized — only placeholder examples existed across multiple docs. **Fixed**: see `scheduling_rules.md`.
3. No database was ever specified, which silently broke the claimed features (conflict-checking, cancellation, daily caps). **Fixed**: added Supabase schema in `integration_spec_discord.md`.
4. Two parallel system prompts (Appointment Brain v1 and Master Prompt) had no stated precedence. **Fixed**: Master Prompt is parked for v2; Appointment Brain v2 is the sole active prompt.
5. No security requirements existed for the webhook/backend (auth, validation, rate limiting, idempotency). **Fixed**: added to `integration_spec_discord.md`.
6. Timezone date resolution ("today/tomorrow") wasn't anchored — risk of off-by-one-day errors for customers far behind Manila. **Fixed**: resolve against customer's local date first.

## Decisions made this session
- Working hours: **Mon–Sun 9AM–6PM PH time.**
- Min notice: 2 hours. Max/day: 12. Buffer: 5 min (proposed, adjustable).
- Storage: Supabase free tier.
- Error-handling loop capped at 2 retries before human handoff.

## Session 2 — backend build
- Bug caught and fixed: `book-appointment.js` originally only validated the appointment *start* time against working hours, allowing bookings to run past 6 PM close if started near the boundary. **Now validates both start and end.**
- Known limitation (not a bug, but fragile): daily-cap and conflict queries use UTC calendar-day boundaries as a stand-in for the PH calendar day. This only holds because 9AM–6PM PH never crosses UTC midnight. **If working hours are ever extended into the night, this must be reworked to use explicit PH-day boundaries.**
- Not yet implemented: rate limiting on the booking endpoint (spec calls for it, code doesn't enforce it yet).

## Session 3 — Deployment Protection
- Discovered Vercel Authentication was enabled on the project, blocking all inbound API calls (front-end, tests) with a 302 SSO redirect. Confirmed via direct request testing on both endpoints.
- Decision: kept protection ON (Option B), added Protection Bypass for Automation secret. Real callers must send `x-vercel-protection-bypass: <secret>` header.
- Verification: pending user-run curl test (I cannot hold the secret myself to test it, by design — it's never pasted into chat).
- Clarified scope: I have no live channel to OpenCode or other local agents. This log is the hand-off point if you run OpenCode locally against the same project — it should treat this file as the source of truth for what's already decided/built, not redo it.

## Open items for next session
- Confirm the 5-minute buffer value (or remove it).
- Decide data retention policy beyond "keep indefinitely."
- Decide if/when Master Prompt (retail/FAQ mode) gets activated as v2.
- Blocked dates/holidays list is empty — add as they come up.

---

## PAIOS Compliance

- **SSoT:** This is the canonical decision log. All project decisions trace here.
- **DRY:** Decisions not duplicated in other docs (referenced only).
