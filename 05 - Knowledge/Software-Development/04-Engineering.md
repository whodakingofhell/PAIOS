---
tags: [paios/knowledge, paios/software-development, engineering, development]
related:
  - "Architecture/03-Architecture.md"
  - "Software-Development/Backend.md"
  - "Software-Development/Frontend.md"
  - "Software-Development/Database.md"
  - "Software-Development/05-QA-Framework.md"
  - "DevOps/DevOps.md"
---

# 04 — Engineering

> Section 04 of the AI Engineering OS

---

## Purpose

Defines **engineering standards, code quality, version control workflow, branching strategy, PR review process, CI/CD pipeline, and technical debt management**. Ensures all code and automation is production-grade, reviewable, and maintainable.

---

## Owner Team

**DevOps** (`Team\DevOps.md`) + **Backend** (`Team\Backend.md`) + **Frontend** (`Team\Frontend.md`)

---

## Key Responsibilities

- Establish and enforce **code quality standards** across all languages and scripts.
- Own the **Git workflow** — branching, commits, PRs, reviews, merges.
- Manage the **CI/CD pipeline** — automated testing, building, deploying.
- Track and manage **technical debt** — prevent it from compounding.
- Maintain **engineering documentation** inline with code.
- Define **performance and reliability targets** for all systems.

---

## Code Quality Standards

### Universal Rules (all languages)

1. **Meaningful names.** Variables, functions, files describe their purpose. No `x`, `temp`, `data`.
2. **Functions do one thing.** ≤30 lines. If it needs "and", it's two functions.
3. **No magic numbers.** Constants with descriptive names.
4. **Error handling, not error ignoring.** Every failure path is explicit.
5. **Comments explain WHY, not WHAT.** Code says what; comments say why.
6. **Consistent style.** One linter config per language, enforced in CI.
7. **No hard-coded secrets.** Ever. Secrets via `.env` or secrets manager.

### Language-Specific Standards

| Language | Linter | Formatter | Test Framework |
|---|---|---|---|
| Python | Ruff | Black | Pytest |
| JavaScript/TS | ESLint | Prettier | Vitest |
| Markdown | markdownlint | Prettier | N/A (structure check) |
| JSON | jsonlint | Prettier | N/A |
| YAML | yamllint | Prettier | N/A |

---

## Version Control Workflow

### Branching Strategy (GitHub Flow — simplified)

```
main (protected)
  │
  ├── feature/00-intake-processor
  ├── feature/qa-gate-script
  ├── fix/ffmpeg-compatibility
  └── docs/architecture-update
```

**Rules:**
1. `main` is protected. Only merges via PR with ≥1 approval.
2. Feature branches: `feature/description` or `fix/description`.
3. Commit messages: conventional commits (`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`).
4. Every PR must pass CI before merge.
5. Squash-merge to main for clean history.

### Commit Message Format

```
type(scope): description

feat(pipeline): add QA gate stage 11 script
fix(intake): handle binary file edge case in 00-intake.py
docs(os): update 03-Architecture with new ComfyUI integration
refactor(n8n): extract shared retry logic into sub-workflow
chore(deps): bump n8n Docker image to 1.x
```

---

## PR Review Process

### Checklist (every PR must pass)

- [ ] **Code quality:** Linter passes, no warnings.
- [ ] **Tests pass:** All existing + new tests green.
- [ ] **Documentation:** README/API doc updated if behavior changed.
- [ ] **No secrets:** `.env` not modified, no keys in code.
- [ ] **Conventional commit:** Message follows format.
- [ ] **Single concern:** PR does one thing (not a "kitchen sink" PR).
- [ ] **Self-review:** Author has reviewed their own diff before requesting review.
- [ ] **QA Criticism Framework:** Applied to the change (see `Frameworks\QA-Criticism-Framework.md`).

---

## CI/CD Pipeline

### GitHub Actions Workflow

```
On push/PR to main:
  1. Lint (all files)
  2. Type check (if applicable)
  3. Unit tests
  4. Integration tests (pipeline stage tests)
  5. Build (if applicable — Docker images, bundles)
  6. Security scan (secrets detection, dependency audit)
  7. Deploy (Vercel auto-deploy on main merge; Docker rebuild on pipeline changes)
```

### Pipeline Scripts (special CI)

Pipeline scripts (`Pipeline\scripts\0X-*.py`) have their own validation:
- Each script validates its own input schema.
- Each script writes a structured JSON output with `status: success|failed`.
- Failed scripts write to `Pipeline/intake/processed/errors/` with error detail.

---

## Technical Debt Management

### Debt Tracking

| Debt Item | Category | Severity | Owner | Pay-down Plan | Deadline |
|---|---|---|---|---|---|
| [Example] | Code smell | Medium | Backend | Refactor in next sprint | Sprint 3 |

### Debt Rules

1. **No debt without a ticket.** Every shortcut gets a GitHub issue tagged `technical-debt`.
2. **Severity scale:** LOW (cosmetic), MEDIUM (impacts maintainability), HIGH (impacts reliability).
3. **Pay-down budget:** 20% of each sprint dedicated to debt reduction.
4. **Compound interest:** Debt rated HIGH and unresolved for >2 sprints is escalated to CTO.

---

## Performance & Reliability Targets

| System | Target | Measurement |
|---|---|---|
| Pipeline (end-to-end) | <30 min for a 10-min video | n8n execution logs |
| Single script execution | <60 sec per stage | Script output timestamp |
| YouTube upload | <2 min for 1080p, 10 min video | Upload API timing |
| n8n instance | 99.5% uptime | Docker health check |
| Vercel-hosted pages | <1s LCP, <100ms FID | Lighthouse CI |
| API rate limit buffer | Stay under 80% of free tier | Pipeline monitoring |

---

## Inputs

- Architecture decisions (`03-Architecture\Architecture.md`)
- Security requirements (`06-Security\Security.md`)
- QA framework (`05-Quality-Assurance\QA-Framework.md`)
- Pipeline specifications (`Frameworks\Content-Pipeline.md`)

---

## Outputs

- This engineering standards document
- CI/CD pipeline configuration
- Technical debt register
- Engineering runbook (how to develop, test, deploy)

---

## Operating Principles

1. **Automate everything.** If you do it twice, script it. If a script runs twice, put it in CI/CD.
2. **Reviews are non-negotiable.** No code merges without review — even for pipeline scripts.
3. **Fast feedback loops.** CI runs in <5 minutes. Slow CI means people skip it.
4. **Technical debt is a first-class concern.** It gets tickets, owners, and deadlines like features do.
5. **Documentation is code.** README, ADRs, and runbooks are updated in the same PR as the code they describe.

---

## Acceptance Criteria

- [ ] Code quality standards cover all project languages with linter/formatter/test config.
- [ ] Git branching strategy is defined with rules for `main` protection.
- [ ] PR review checklist is complete and enforceable.
- [ ] CI/CD pipeline stages are specified with tool choices.
- [ ] Technical debt tracking format is defined with severity scale and pay-down rules.
- [ ] Performance targets are set for all key systems.

---

## Cross-References

| Document | Relationship |
|---|---|
| `03-Architecture\Architecture.md` | Engineering implements the architecture |
| `05-Quality-Assurance\QA-Framework.md` | QA validates engineering output |
| `06-Security\Security.md` | Security constraints on engineering |
| `07-Automation\Automation.md` | Automation is engineered work |
| `Project\Backend.md`, `Project\Frontend.md` | Per-project engineering specs |
| `Project\Testing.md` | Per-project test strategy |
