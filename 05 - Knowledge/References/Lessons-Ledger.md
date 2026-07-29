---
tags:
  - paios/knowledge
  - paios/references
related:
  - "../Knowledge-MOC.md"
  - "../../02 - Projects/Projects-MOC.md"
  - "./Project-Patterns.md"
---

### Lessons by Category

**Architecture & Design**
- Webhook architecture requires retry logic + circuit breakers
- Discord webhooks have no delivery guarantees unless you build ack/retry
- Input sanitization is critical when user input flows into notification channels
- Model context windows need hard limits to prevent runaway token costs
- Buffer time between appointments prevents scheduling cascades

**Security**
- Webhook URLs must be env-only, never in code
- Rate limiting is required per-IP for any public-facing booking endpoint
- PII handling policy must exist before launch (retention, deletion, compliance)
- Payload validation schema catches malformed AI output before it hits external systems

**Product & UX**
- Cancellation/rescheduling flow must be designed from day 1, not added later
- Customer confirmation must exist (the booker gets nothing in v1 — critical gap)
- Progress indicators during multi-step flows improve completion rate
- Always define scope and out-of-scope before writing any code
- Documentation should separate technical from user-facing content

**Cost & Operations**
- Document token budget per conversation to avoid surprise bills
- Define model selection rules: use cheapest model that works for each task
- Free tiers have ceilings (Vercel, Claude, Discord) — document the paid fallback
- Cost projection at 100/500/1000 units/month should exist before launch

**Domain / Scheduling**
- Double-booking prevention is not the same as business-hours check
- Holiday/blocked-date mechanism must be editable without code changes
- No-show policy must exist and be documented
- Booking on behalf of others needs specific handling

### Lessons by Project

**AI-Appointment-Assistant**
- Master prompt approach works but needs versioning
- Multi-expert critique (SRE, Security, UX, Cost, Domain) caught 6 critical gaps before launch
- Silent webhook failure was the #1 risk — no retry, no fallback, no monitoring

**deploy-v2**
- public/ vs root separation for static assets
- SYSTEM directory for architecture decisions keeps project context clean

**PhilippineSkyland**
- Google Search Console integration needs documentation
- Security architecture should be documented per-domain

### Preventive Checklist

1. Input sanitization plan
2. Retry/fallback for all external calls
3. Monitoring and observability spec
4. Cancellation/reschedule flow
5. Token/cost budget per session
6. Rate limiting per user/IP
7. PII handling and privacy policy
8. Double-booking prevention
9. Model selection and cost projection
10. Customer confirmation flow
