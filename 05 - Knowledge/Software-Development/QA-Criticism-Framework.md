---
tags: [paios/knowledge, paios/software-development, paios/qa, criticism, review]
related:
  - "Software-Development/QA.md"
  - "Software-Development/05-QA-Framework.md"
  - "Product-Design/Feature-Score-Rubric.md"
---

# QA Criticism Framework

> **Auto-injected into every generation under this OS.**
> This block is mandatory. Any output produced without it is rejected at the QA gate.

---

## How to use

1. Before finalizing **any** deliverable (doc, feature, prompt, video script, design), run the full scan below.
2. Output the result as a structured block at the end of the deliverable.
3. Anything that fails a category must either be (a) fixed, or (b) explicitly accepted as a known limitation with a documented reason + owner + follow-up ticket.

---

## Mandatory Block (copy/paste at end of every output)

```markdown
---

## AI CRITICISM FRAMEWORK — AUTO-INJECTED

### MISSING REQUIREMENTS
- What has not been considered?
- What assumptions were made?
- What edge cases are unhandled?
- What non-functional requirements (scale, latency, accessibility, i18n, cost) are missing?

### QA SCAN
| Category | Status | Notes |
|---|---|---|
| Missing Features | PASS / FAIL / N/A | |
| Broken Logic | PASS / FAIL / N/A | |
| Conflicts | PASS / FAIL / N/A | |
| Security Risks | PASS / FAIL / N/A | |
| Performance Problems | PASS / FAIL / N/A | |
| Duplicate Features | PASS / FAIL / N/A | |
| Poor UX | PASS / FAIL / N/A | |
| Business Risks | PASS / FAIL / N/A | |
| Technical Debt | PASS / FAIL / N/A | |
| Scalability Issues | PASS / FAIL / N/A | |
| Future Expansion Risks | PASS / FAIL / N/A | |
| API Design Problems | PASS / FAIL / N/A | |
| Naming Problems | PASS / FAIL / N/A | |
| Documentation Gaps | PASS / FAIL / N/A | |
| Monetization Risks | PASS / FAIL / N/A | |
| Automation Opportunities | PASS / FAIL / N/A | |
| Accessibility Issues | PASS / FAIL / N/A | |
| Testing Coverage | PASS / FAIL / N/A | |
| Maintainability | PASS / FAIL / N/A | |
| Code Smells | PASS / FAIL / N/A | |
| Architecture Smells | PASS / FAIL / N/A | |

### SCORECARD (see Feature-Score-Rubric.md)
| Dimension | Score | |
|---|---|---|
| Architecture | __ / 10 | |
| Security | __ / 10 | |
| Performance | __ / 10 | |
| Maintainability | __ / 10 | |
| Scalability | __ / 10 | |
| Accessibility | __ / 10 | |
| Documentation | __ / 10 | |
| Business Value | __ / 10 | |
| Automation Potential | __ / 10 | |
| Revenue Impact | __ / 10 | |
| **Average** | **__ / 10** | |

### DECISION
- Technical Debt: LOW / MEDIUM / HIGH
- Recommendation: APPROVE / REVISE / REJECT
- Risk Level: LOW / MEDIUM / HIGH / CRITICAL
- Priority: P0 / P1 / P2 / P3
- Approval Status: APPROVED / PENDING / BLOCKED
- Future Improvements:
- Estimated Dev Time:
- Dependencies:
```

---

## Category definitions (what "FAIL" means)

- **Missing Features** — promised/expected capability is absent or stubbed.
- **Broken Logic** — code path that produces wrong output, crashes, or dead-ends.
- **Conflicts** — contradicts another doc, decision, or existing feature.
- **Security Risks** — authz/authn gaps, secret leakage, injection, OWASP Top 10.
- **Performance Problems** — N+1, sync I/O on hot path, unbounded loops, large payloads.
- **Duplicate Features** — same capability exists elsewhere (DRY violation).
- **Poor UX** — confusing flow, missing feedback, no error states, low contrast.
- **Business Risks** — undermines revenue, legal exposure, brand harm.
- **Technical Debt** — shortcuts taken that will cost future time.
- **Scalability Issues** — works at 1 user, breaks at 1k/10k.
- **Future Expansion Risks** — decisions that block tomorrow's roadmap.
- **API Design Problems** — inconsistent naming, wrong verbs, leaky internals, no versioning.
- **Naming Problems** — misleading, inconsistent, or ambiguous names.
- **Documentation Gaps** — code/feature without explanation or examples.
- **Monetization Risks** — pricing model friction, free-tier abuse path.
- **Automation Opportunities** — manual steps that should be scripted/n8n'd.
- **Accessibility Issues** — WCAG 2.1 AA violations (keyboard, ARIA, contrast, alt text).
- **Testing Coverage** — untested critical paths, no edge cases.
- **Maintainability** — unclear code, no separation of concerns, magic numbers.
- **Code Smells** — long methods, god classes, deep nesting, primitive obsession.
- **Architecture Smells** — circular deps, tight coupling, wrong-layer logic, no clear boundaries.

---

## Pass criteria for the QA Gate

A deliverable **passes the QA gate** when:
1. Every QA Scan category is PASS or N/A (FAILs must have an accepted-and-documented exception).
2. Scorecard average ≥ **9.0** and no single dimension < **8.0**.
3. Technical Debt rated **LOW**.
4. Recommendation = **APPROVE**, Approval Status = **APPROVED**.

Anything else is held for revision.
