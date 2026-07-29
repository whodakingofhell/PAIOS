---
tags: [paios/knowledge, paios/product-design, scoring, rubric, prioritization]
related:
  - "Product-Design/02-Product.md"
  - "Product-Design/Content-Pipeline.md"
  - "Product-Design/Product-Lifecycle.md"
  - "Software-Development/05-QA-Framework.md"
  - "Software-Development/QA-Criticism-Framework.md"
---

# Feature Score Rubric

> **The scorecard every feature/build is measured against before approval.**
> Auto-attached to the QA Criticism Framework block. See `QA-Criticism-Framework.md`.

---

## The 10 scored dimensions

| # | Dimension | What 10/10 looks like |
|---|---|---|
| 1 | **Architecture** | Clear layers, separation of concerns, documented boundaries, right patterns for the problem, no architecture smells. |
| 2 | **Security** | OWASP Top 10 covered, authn/authz correct, secrets externalized, least privilege, input validated, audit trail. |
| 3 | **Performance** | Hot paths profiled, no N+1, bounded payloads, async where it matters, latency/throughput targets met. |
| 4 | **Maintainability** | Readable, consistent style, meaningful names, low cyclomatic complexity, easy to change with confidence. |
| 5 | **Scalability** | Stateless where possible, horizontally scalable, no single-machine bottlenecks, queue-based for spikes. |
| 6 | **Accessibility** | WCAG 2.1 AA: keyboard nav, ARIA correct, ≥4.5:1 contrast, alt text, focus management, reduced-motion support. |
| 7 | **Documentation** | README, architecture decision records, API reference, examples, runbook, and changelog all current. |
| 8 | **Business Value** | Directly advances a stated business goal; measurable KPI attached; ROI positive. |
| 9 | **Automation Potential** | Build/test/deploy automated; repetitive ops scripted; n8n-orchestrated where sensible. |
| 10 | **Revenue Impact** | Clear path to revenue or cost savings; pricing/monetization model sound; no abuse path. |

Each dimension scored **0–10** in 0.1 increments.

---

## Scorecard template (paste into every feature review)

```
Feature Score
─────────────────────────────
Architecture         9.4
Security             8.8
Performance          9.2
Maintainability      9.6
Scalability          9.3
Accessibility        8.9
Documentation        9.5
Business Value       9.4
Automation Potential 9.7
Revenue Impact       8.7
─────────────────────────────
Average              9.25
Technical Debt       LOW

Recommendation       APPROVE
Risk Level           LOW
Priority             P1
Future Improvements  ...
Estimated Dev Time   ...
Dependencies         ...
Approval Status      APPROVED
```

---

## Scoring scale

| Score | Meaning |
|---|---|
| 9.0 – 10.0 | Excellent — ship it. |
| 8.0 – 8.9 | Good — ship with documented minor follow-ups. |
| 7.0 – 7.9 | Acceptable — only with owner-approved exceptions; mandatory follow-ups logged. |
| 6.0 – 6.9 | Weak — revise before approval. |
| < 6.0 | Reject — rework required. |

---

## Approval thresholds

- **Average ≥ 9.0** AND **no single dimension < 8.0** → eligible for APPROVE.
- **Technical Debt must be LOW** (MEDIUM allowed only with a documented pay-down plan + owner).
- Any **Security < 8.0** → BLOCKED regardless of average. Security is a hard gate.
- Any **Performance < 7.0 on a hot path** → BLOCKED.

---

## Decision fields (definitions)

- **Recommendation** — APPROVE (meets bar) / REVISE (close, needs work) / REJECT (fundamentally off).
- **Risk Level** — LOW (isolated, reversible) / MEDIUM (cross-cutting, recoverable) / HIGH (customer/data facing) / CRITICAL (legal/financial/safety).
- **Priority** — P0 (now/blocking) / P1 (this sprint) / P2 (this quarter) / P3 (backlog).
- **Approval Status** — APPROVED / PENDING (waiting review) / BLOCKED (failing gate).
- **Future Improvements** — concrete next-iteration items, each with owner + ticket.
- **Estimated Dev Time** — in story points or hours, broken down if > 1 day.
- **Dependencies** — upstream people/teams/services/decisions this depends on.

---

## Worked example

A new REST endpoint that adds user-export:

```
Architecture         9.4   — clean controller→service→repo layering
Security             8.8   — authz correct; add rate-limit follow-up
Performance          9.2   — streaming response, profiled
Maintainability      9.6   — single responsibility, well named
Scalability          9.3   — stateless worker, queue-backed
Accessibility        8.9   — UI surface is keyboard/ARIA compliant
Documentation        9.5   — OpenAPI + examples + runbook
Business Value       9.4   — enables GDPR export (measurable)
Automation Potential 9.7   — fully CI/CD + n8n monitored
Revenue Impact       8.7   — enables Pro-tier retention
─────────────────────────────
Average              9.25   Technical Debt: LOW
Recommendation       APPROVE   Risk: LOW   Priority: P1
Approval Status      APPROVED
```
