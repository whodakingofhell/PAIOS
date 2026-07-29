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
- SAST/DAST scanning must be in CI pipeline, not ad-hoc
- Dependency scanning catches vulnerable libraries before they ship
- Secrets scanning prevents credential leaks in commits
- OWASP Top 10 should be reviewed at every project phase boundary

**Product & UX**
- Cancellation/rescheduling flow must be designed from day 1, not added later
- Customer confirmation must exist (the booker gets nothing in v1 — critical gap)
- Progress indicators during multi-step flows improve completion rate
- Always define scope and out-of-scope before writing any code
- Documentation should separate technical from user-facing content
- Usability testing with 5 users catches 80% of UX issues before launch
- Design tokens prevent visual drift as the product scales

**Testing & Quality**
- Unit tests alone are not enough — integration and E2E catch different bug classes
- Testing pyramid prevents slow, brittle test suites
- Security testing (pentest + scan) must happen before every launch, not once
- Performance baselines should exist before optimization attempts
- Accessibility testing is not optional — WCAG 2.1 AA is the minimum legal standard

**Cost & Operations**
- Document token budget per conversation to avoid surprise bills
- Define model selection rules: use cheapest model that works for each task
- Free tiers have ceilings (Vercel, Claude, Discord) — document the paid fallback
- Cost projection at 100/500/1000 units/month should exist before launch
- Monitoring without alerting is just pretty graphs — define P0/P1/P2 alert rules

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

1. Project-Phases.md lifecycle reviewed and current phase identified
2. Security checklist reviewed (OWASP, SAST/DAST, dependency scan)
3. Penetration test scheduled or completed
4. Input sanitization plan documented
5. Retry/fallback for all external calls
6. Monitoring + alerting configured (logs, metrics, traces)
7. Cancellation/reschedule flow designed
8. API design reviewed (versioning, auth, pagination, errors)
9. Token/cost budget per session estimated
10. Rate limiting per user/IP
11. PII handling and privacy policy documented
12. CI/CD pipeline with test + security gates
13. Performance baseline established (load test)
14. Accessibility audit completed (WCAG 2.1 AA)
15. UX usability testing completed (min 5 users)
16. Double-booking prevention
17. Model selection and cost projection
18. Customer confirmation flow
