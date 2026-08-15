---
tags:
  - paios/knowledge
  - paios/devops
  - paios/automation
related:
  - "07-Automation.md"
  - "DevOps.md"
  - "Automation-Engineering.md"
  - "Performance-Testing.md"
  - "../Software-Development/Project-Phases.md"
  - "Monitoring-Observability.md"
---

# CI/CD Pipeline

## Pipeline Stages (standard)
1. **Lint** — code formatting, style checks, import sorting
2. **Type check** — TypeScript strict mode, mypy, etc.
3. **Unit tests** — fast, isolated, parallelized
4. **Build** — compile, bundle, Docker image build
5. **SAST** — static security analysis (Semgrep, CodeQL)
6. **Integration tests** — API tests with test DB
7. **Dependency scan** — check for known vulns (npm audit, pip audit, Snyk)
8. **Deploy to staging** — automatic on main branch
9. **E2E tests** — Playwright/Cypress against staging
10. **DAST** — OWASP ZAP scan on staging
11. **Deploy to production** — manual approval gate
12. **Smoke tests** — health check + critical path assertions on production

## Environment Strategy
- **Development** — local machine. Developer runs lint + unit tests before commit
- **Staging** — deploys from main branch. Full pipeline runs. Mirrors production config
- **Production** — deploys from Git tag or release branch. Manual approval required

## CI Tools
| Tool | Purpose |
|------|---------|
| GitHub Actions | CI/CD runner (preferred for GitHub repos) |
| GitLab CI | Alternative with built-in registry |
| Docker | Build and deploy containers |
| Docker Compose | Local and CI service orchestration |
| SonarQube | Code quality gate |
| Codecov | Coverage reporting |

## Pipeline Rules
- Fail fast: lint → type → unit (fail here before spending build minutes)
- Cache dependencies across runs (npm cache, pip cache)
- Parallelize when possible (lint + type + unit in parallel)
- Secrets: use environment variables / secrets manager, never in code
- Artifacts: store builds, test reports, coverage reports

## Git Workflow (Trunk-Based)
- Short-lived feature branches (1-2 days max)
- Main branch is always deployable
- Feature flags for in-progress work
- No long-running release branches
