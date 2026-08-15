---
tags: [paios/knowledge, paios/product-design, lifecycle, product-management]
related:
  - "Product-Design/02-Product.md"
  - "Product-Design/Content-Pipeline.md"
  - "Product-Design/Feature-Score-Rubric.md"
  - "Business/01-Business.md"
---

# Product Lifecycle

> The flow every software build follows under this OS. **Two QA gates** catch defects when they're cheapest.

```
Business Idea
      │
      ▼
Requirements Analysis
      │
      ▼
Product Specification
      │
      ▼
Architecture Review          ── Team\Architecture.md
      │
      ▼
╔════════════════════════╗
║  Elite QA Review #1   ║   ◀── GATE 1 (catch design defects early)
╚════════════════════════╝
      │
      ▼
Database Design              ── Team\Database.md
      │
      ▼
Backend Development          ── Team\Backend.md
      │
      ▼
Frontend Development         ── Team\Frontend.md
      │
      ▼
Automation Integration       ── Team\Automation-Engineering.md
      │
      ▼
Security Review              ── Team\Security.md
      │
      ▼
╔════════════════════════╗
║  Elite QA Review #2   ║   ◀── GATE 2 (catch ship defects before deploy)
╚════════════════════════╝
      │
      ▼
Testing                      ── Team\QA.md
      │
      ▼
Documentation                ── AI-ENGINEERING-OS\09-Documentation
      │
      ▼
Deployment                   ── Team\DevOps.md
      │
      ▼
Monitoring                   ── Team\DevOps.md
      │
      ▼
User Feedback                ── 10-Marketing + 11-Revenue
      │
      ▼
Continuous Improvement       ── loops back to Requirements Analysis
```

---

## Stage detail

| Stage | Owner (Team) | Key docs | Exit criteria |
|---|---|---|---|
| Business Idea | Executive | `Project\Vision.md`, `Business.md` | Problem, audience, value prop, monetization stated |
| Requirements Analysis | Product Director | `Project\Features.md` | Functional + non-functional requirements, prioritized |
| Product Specification | Product Director | `Project\Product.md`, `UI.md`, `UX.md` | User stories, flows, acceptance criteria |
| Architecture Review | Architecture team | `Project\APIs.md`, `03-Architecture` | Components, data flow, tech choices justified |
| **QA Review #1 (GATE)** | QA | `Frameworks\QA-Criticism-Framework.md` | Score avg ≥ 9.0, no dim < 8.0, debt LOW |
| Database Design | Database team | `Project\Database.md` | ERD, indexes, migrations drafted |
| Backend Development | Backend team | `Project\Backend.md`, `APIs.md` | APIs implemented + unit tested |
| Frontend Development | Frontend team | `Project\Frontend.md`, `UI.md` | UI meets stories + a11y AA |
| Automation Integration | Automation team | `Project\Automation.md`, `AI.md` | n8n/CI workflows in place |
| Security Review | Security team | `Project\Security.md`, `06-Security` | OWASP covered, secrets externalized |
| **QA Review #2 (GATE)** | QA | Rubric + Framework | Score avg ≥ 9.0, no Security < 8.0 |
| Testing | QA | `Project\Testing.md` | Unit/integration/e2e green; coverage target met |
| Documentation | All | `Project\Changelog.md`, `09-Documentation` | README, ADRs, API ref, runbook current |
| Deployment | DevOps | `Project\Deployment.md` | Blue/green or canary; rollback verified |
| Monitoring | DevOps | `04-Engineering` | Logs, metrics, alerts, dashboards live |
| User Feedback | Marketing + Revenue | `10-Marketing`, `11-Revenue` | Feedback channels captured into KB |
| Continuous Improvement | Executive + Product | loops to Requirements | Roadmap updated; cycle repeats |

---

## The two gates — why they exist

- **Gate #1 (after Architecture):** The cheapest place to fix design mistakes. A bad schema or wrong boundary found here costs hours; the same defect found in Testing costs days.
- **Gate #2 (before Testing/Deploy):** Catches integration/security defects before they reach users. Security < 8.0 is a hard block.

**Both gates use** `Frameworks\QA-Criticism-Framework.md` + `Frameworks\Feature-Score-Rubric.md`. No exceptions without a documented, owner-approved waiver.
