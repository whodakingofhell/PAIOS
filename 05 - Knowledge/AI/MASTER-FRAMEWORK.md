---
tags: [paios/knowledge, paios/ai, framework, methodology]
related:
  - "AI/08-AI-Knowledge.md"
  - "AI/AI-Engineering.md"
  - "References/MASTER_REFERENCE.md"
  - "References/RECOMMENDATIONS.md"
  - "References/EXPERT_CRITIQUES.md"
  - "Software-Development/00-Vision.md"
---

# MASTER AI ENGINEERING FRAMEWORK

> **The single stable document. Everything else plugs into it.**
> Do not expand this file with project specifics. Keep it stable. Store project details in the specialized documents.

---

## 0. Purpose

This framework turns an AI assistant into an **elite engineering organization** that designs, builds, ships, documents, and monetizes software — and that simultaneously runs an automated content pipeline. Instead of one ever-growing prompt, this is a **document-based operating system**: the framework stays stable, the specialized docs evolve.

Two outcomes from one system:
1. **Build products** like a virtual elite engineering org (Executive → Architecture → Frontend → Backend → Database → DevOps → AI → Automation → Security → QA).
2. **Build an audience and revenue** via a fully automated YouTube pipeline that turns any intake (files / text / docs / new learnings) into published, monetized videos.

---

## 1. The Operating Principles (non-negotiable)

1. **Document stability.** This file changes rarely. Project specifics live in `Project\`, `AI-ENGINEERING-OS\`, `Team\`, and `Frameworks\`.
2. **Stage gates.** No stage advances until the previous one is a solid **10/10** and has passed the QA gate. Quality compounds; debt does too.
3. **Specialization.** Different AI models handle specialized tasks. Don't overload one context. Route: high-volume/cheap → Gemini; high-judgment/precision → Claude; research/grounding → NotebookLM + Perplexity.
4. **Criticism by default.** Every output auto-includes the **QA Criticism Framework** (`Frameworks\QA-Criticism-Framework.md`). No output ships without it.
5. **Scored outputs.** Every feature/build is scored against the **Feature Score Rubric** (`Frameworks\Feature-Score-Rubric.md`) before approval.
6. **Lowest viable cost.** Prefer free tiers and local tools first (`integrations\cost-map.md`). Upgrade only when a stage's free quota is exhausted.
7. **Reproducibility.** Every pipeline stage is independently runnable (`Pipeline\scripts\0X-name.py --input ... --output ...`). If a stage can't run alone, it isn't done.
8. **Security by default.** Secrets via `.env`, never committed. Least privilege. See `AI-ENGINEERING-OS\06-Security\Security.md`.
9. **Feedback closes the loop.** Analytics feed back into the knowledge base. The pipeline is a cycle, not a line.

---

## 2. The Document Map

```
MASTER-FRAMEWORK.md            ← you are here (stable)
│
├── AI-ENGINEERING-OS\         ← the 13 operating sections (00–12)
│     00-Vision … 12-Roadmap
│
├── Project\                   ← per-project set (20 files), one per active project
│     Vision.md Business.md Product.md Features.md UI.md UX.md
│     Database.md Backend.md Frontend.md APIs.md AI.md Automation.md
│     Security.md Testing.md Deployment.md Revenue.md Marketing.md
│     YouTube.md Roadmap.md Changelog.md
│
├── Team\                      ← role personas (system-prompt-ready)
│     Executive Architecture Frontend Backend Database DevOps
│     AI-Engineering Automation-Engineering Security QA
│
├── Frameworks\                ← reusable operating frameworks
│     QA-Criticism-Framework  Feature-Score-Rubric
│     Product-Lifecycle        Content-Pipeline
│
├── Pipeline\                  ← the YouTube automation engine
│     docker-compose.yml  n8n-workflows\  scripts\  prompts\  intake\
│
└── integrations\              ← per-tool setup + cost map
      cost-map.md  gemini.md  claude.md  notebooklm.md  ...
```

**Convention:** `Folder\file.md` paths are referenced everywhere. Keep them stable so cross-references don't break.

---

## 3. The Elite Team (who does what)

| Team | Lead file | Role |
|---|---|---|
| Executive | `Team\Executive.md` | CEO, CTO, CIO, Product Director, Technical Program Manager |
| Architecture | `Team\Architecture.md` | Enterprise, Solution, System, Cloud, Integration Architects |
| Frontend | `Team\Frontend.md` | Senior Frontend Engineer (UI/UX/A11y/Perf) |
| Backend | `Team\Backend.md` | Senior Backend Engineer (APIs, Auth, Logic, Queues) |
| Database | `Team\Database.md` | Senior Database Architect (ERD, indexing, migrations) |
| DevOps | `Team\DevOps.md` | Elite DevOps Engineer (CI/CD, Docker, K8s, GH Actions) |
| AI Engineering | `Team\AI-Engineering.md` | Prompt, LLM, Workflow, RAG, Automation, Knowledge Engineers |
| Automation | `Team\Automation-Engineering.md` | n8n, GitHub, Discord, YouTube, Drive, Notion, Email, CRM |
| Security | `Team\Security.md` | Cybersecurity Eng, SOC Analyst, Threat Hunter, Pen Tester, Compliance |
| QA | `Team\QA.md` | Elite QA Division (gates every stage) |

---

## 4. The Two Lifecycles

### 4.1 Product Lifecycle — `Frameworks\Product-Lifecycle.md`
```
Business Idea → Requirements → Product Spec → Architecture Review
→ Elite QA Review #1 → Database Design → Backend → Frontend
→ Automation Integration → Security Review → Elite QA Review #2
→ Testing → Documentation → Deployment → Monitoring
→ User Feedback → Continuous Improvement
```
**Two QA gates** (Review #1 after architecture, Review #2 before testing) catch defects early when they're cheap.

### 4.2 Content Pipeline — `Frameworks\Content-Pipeline.md`
```
Knowledge Base → Claude (Content Planning) → Script Generation
→ NotebookLM (Research/Voice) → Storyboard → Higgsfield (Animation)
→ Voice Generation → Video Editing → Thumbnail Generation
→ Metadata Generation → SEO Optimization → QA Review
→ YouTube Upload → Analytics Collection → Feedback into Knowledge Base
```
**One QA gate** (between SEO and Upload) prevents bad content from going public.

---

## 5. The Criticism Engine (always on)

Every output produced under this framework **must include** the auto-injected block from `Frameworks\QA-Criticism-Framework.md`:

```
MISSING REQUIREMENTS:
- What has not been considered?
- What assumptions were made?
- What edge cases are unhandled?

QA SCAN (auto-run):
[ ] Missing Features   [ ] Broken Logic       [ ] Conflicts
[ ] Security Risks     [ ] Performance Problems [ ] Duplicate Features
[ ] Poor UX            [ ] Business Risks      [ ] Technical Debt
[ ] Scalability Issues [ ] Future Expansion Risks
[ ] API Design Problems [ ] Naming Problems   [ ] Documentation Gaps
[ ] Monetization Risks [ ] Automation Opportunities
[ ] Accessibility Issues [ ] Testing Coverage
[ ] Maintainability    [ ] Code Smells        [ ] Architecture Smells

SCORECARD: (see Feature-Score-Rubric.md)
```

---

## 6. How to Use This Framework

**For a new software build:**
1. Copy `Project\` into a new project folder (e.g. `Projects\myapp\`).
2. Fill `Vision.md → Business.md → Product.md` first.
3. Route each subsequent doc to the matching Team persona + auto-inject the Criticism Framework.
4. Pass the two QA gates (lifecycle #1 and #2). Each gate uses the Feature Score Rubric. Approval threshold: average ≥ 9.0 and no single dimension < 8.0.

**For content:**
1. Drop intake into `Pipeline\intake\`.
2. Run `Pipeline\scripts\00-intake.py` → `13-analytics-feedback.py` in order (or trigger the n8n master workflow).
3. The QA gate (script 11) must pass before upload (script 12).

---

## 7. Cost Discipline (enforced)

- Default stack is **$0/mo** (`integrations\cost-map.md`).
- Any paid upgrade must be justified by: (a) a free-tier quota hit AND (b) a measurable revenue/efficiency gain.
- No paid API is called during build. Keys are `.env`-driven and supplied by the operator at runtime.

---

## 8. Stability & Evolution

- **Editable often:** `Project\`, `Pipeline\prompts\`, `AI-ENGINEERING-OS\*` content, `integrations\*`.
- **Editable rarely (changes ripple):** this file, `Frameworks\Feature-Score-Rubric.md` dimensions, `Team\*` role definitions.
- **Change log:** every structural change is recorded in `Project\Changelog.md` (per project) and versioned via Git on GitHub.

---

*Framework version: 1.0 — see `Project\Changelog.md` for changes.*
