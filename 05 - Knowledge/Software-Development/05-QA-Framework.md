# 05 — Quality Assurance

> Section 05 of the AI Engineering OS

---

## Purpose

Defines the **QA methodology, the two-gate system, testing strategy, and the auto-injected criticism framework** that ensures every deliverable — whether code, content, or documentation — meets a high standard before it ships. This is the most overlooked area in AI-generated software and will save significant time over the life of the project.

---

## Owner Team

**QA Division** (`Team\QA.md`) — Elite QA

---

## Key Responsibilities

- **Review every response before approval.** Nothing ships without QA sign-off.
- Operate **two QA gates** in the product lifecycle (after Architecture, before Deploy).
- Operate **one QA gate** in the content pipeline (before YouTube Upload).
- Auto-run the **QA Criticism Framework** on every deliverable.
- Apply the **Feature Score Rubric** to every feature, build, and content piece.
- Maintain **testing coverage** across all systems.
- Track **quality metrics** over time (defect rates, gate pass rates, score trends).

---

## The Two-Gate System (Product Lifecycle)

### Gate 1: Architecture Review Gate
**Location:** After Architecture Review, before Database Design.
**Purpose:** Catch design mistakes when they're cheapest to fix.
**Who reviews:** QA + Architecture team.
**Pass criteria:**
- Feature Score Rubric average ≥ 9.0, no dimension < 8.0.
- Technical Debt rated LOW.
- All QA Scan categories PASS or N/A.
- Security ≥ 8.0 (hard gate).

### Gate 2: Pre-Deploy Gate
**Location:** After Security Review, before Testing/Deployment.
**Purpose:** Catch integration, security, and ship-readiness defects.
**Who reviews:** QA + Security team + DevOps.
**Pass criteria:**
- Feature Score Rubric average ≥ 9.0, no dimension < 8.0.
- Technical Debt rated LOW (MEDIUM only with pay-down plan + owner).
- Security ≥ 8.5 (hard gate — tighter than Gate 1).
- All tests passing (unit, integration, e2e).
- Deployment runbook verified.

---

## The Content QA Gate (Pipeline Stage 11)

**Location:** After SEO Optimization, before YouTube Upload.
**Purpose:** Prevent bad content from going public.
**Who reviews:** Claude (high-judgment) + manual review for first 50 videos.
**Content-specific checks:**
- [ ] **Accuracy** — Claims grounded in NotebookLM/Perplexity sources?
- [ ] **Clarity & Pacing** — Script reads naturally at target WPM?
- [ ] **Brand Fit** — Matches channel mission (build/automate/secure/document)?
- [ ] **Metadata Quality** — Title hooks, description has value, tags on-niche?
- [ ] **SEO** — Keyword in title + first 60s of script? Timestamp chapters?
- [ ] **Thumbnail** — High contrast, ≤5 words, readable at phone size?
- [ ] **Accessibility** — Captions accurate, no flashing >3Hz, narration clear?
- [ ] **Compliance** — Copyright clear (music/B-roll), no misleading metadata?

**Pass criteria:** All categories PASS, score avg ≥ 9.0, Risk = LOW.

---

## Auto-Injected Criticism Framework

Every output produced under this OS **must include** the block from `Frameworks\QA-Criticism-Framework.md`:

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

**This block is mandatory.** Any deliverable without it is rejected at the QA gate.

---

## Testing Strategy

### The Testing Pyramid

```
          ┌──────────┐
          │   E2E    │   ← Few, slow, high-confidence
          │  (play)  │
         ┌┴──────────┴┐
         │ Integration │   ← Moderate count, medium speed
         │  (API +    │
         │  workflow) │
        ┌┴────────────┴┐
        │   Unit Tests  │   ← Many, fast, isolated
        │  (functions, │
        │   stages)     │
        └──────────────┘
```

### Coverage Targets

| Layer | Target | Tool |
|---|---|---|
| Pipeline scripts (unit) | ≥ 80% line coverage | Pytest + pytest-cov |
| n8n workflows (integration) | Every workflow tested end-to-end | n8n built-in testing + manual |
| API endpoints | ≥ 90% line coverage | Pytest + httpx |
| Frontend (if applicable) | ≥ 80% component coverage | Vitest + Testing Library |
| Content QA | 100% of videos reviewed before upload | Stage 11 script |

---

## Quality Metrics

| Metric | Target | Tracking |
|---|---|---|
| Gate 1 pass rate (first attempt) | ≥ 70% | Per-project tracking |
| Gate 2 pass rate (first attempt) | ≥ 80% | Per-project tracking |
| Content QA pass rate (first attempt) | ≥ 85% | Pipeline logs |
| Average Feature Score | ≥ 9.2 | Per-deliverable |
| Technical Debt items | <10 open at any time | GitHub issues |
| Test coverage (overall) | ≥ 80% | CI coverage reports |
| Pipeline failure rate | <5% per stage | n8n execution logs |

---

## Inputs

- All deliverables from every stage and team
- `Frameworks\QA-Criticism-Framework.md`
- `Frameworks\Feature-Score-Rubric.md`
- `Frameworks\Product-Lifecycle.md` (gate positions)
- `Frameworks\Content-Pipeline.md` (content gate position)

---

## Outputs

- QA review reports per gate
- Scorecards per deliverable
- Quality metrics dashboards
- Defect reports and tracking
- Approval/rejection decisions with reasons

---

## Operating Principles

1. **Nothing ships without QA.** No exceptions. No "just this once."
2. **Automated first, manual second.** Scripts scan first; humans review what scripts flag.
3. **Fail fast, fail loud.** A caught defect is a success. A shipped defect is a failure.
4. **Quality is measurable.** If you can't measure it, you can't guarantee it. Track the metrics.
5. **Continuous improvement.** QA metrics are reviewed weekly. Processes adapt to data.

---

## Acceptance Criteria

- [ ] Two-gate system is defined with positions, criteria, and owners.
- [ ] Content QA gate is defined with 8 content-specific checks.
- [ ] Auto-injected criticism framework is documented and enforceable.
- [ ] Testing pyramid is defined with coverage targets per layer.
- [ ] Quality metrics are defined with targets and tracking methods.
- [ ] QA Criticism Framework and Feature Score Rubric are cross-referenced.

---

## Cross-References

| Document | Relationship |
|---|---|
| `Frameworks\QA-Criticism-Framework.md` | The auto-injected criticism checklist |
| `Frameworks\Feature-Score-Rubric.md` | The 10-dimension scorecard |
| `Frameworks\Product-Lifecycle.md` | Gate positions in the product lifecycle |
| `Frameworks\Content-Pipeline.md` | Gate position in the content pipeline |
| `04-Engineering\Engineering.md` | Engineering produces what QA reviews |
| `06-Security\Security.md` | Security is a hard gate criterion |
| `Team\QA.md` | QA team persona and responsibilities |
