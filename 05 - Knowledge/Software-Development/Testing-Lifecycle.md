---
tags:
  - paios/knowledge
  - paios/software-development
  - paios/testing
related:
  - "05-QA-Framework.md"
  - "QA.md"
  - "QA-Criticism-Framework.md"
  - "Project-Phases.md"
  - "../Security/Penetration-Testing.md"
  - "../DevOps/Performance-Testing.md"
---

# Testing Lifecycle

## Testing Pyramid (in order of speed/scope)
- **Unit tests** — test individual functions/classes. Fast, deterministic. Target: >80% coverage
- **Integration tests** — test modules interact (DB, API, filesystem). Slower. Target: critical paths
- **E2E tests** — test user flows from UI to DB. Slowest. Target: happy path + top 5 edge cases
- **Manual QA** — exploratory testing, usability, visual regression

## Developer Testing
- Write unit tests alongside code (TDD or test-after)
- Run lint + type check + unit tests before every commit (pre-commit hook or CI gate)
- Integration tests in CI on every push
- Mutation testing for high-risk modules

## QA Testing
- Functional testing: does it do what it should?
- Regression testing: did we break anything?
- Smoke testing: does the build pass basic sanity?
- Exploratory testing: unstructured finding of edge cases
- UAT: stakeholders validate against acceptance criteria

## Security Testing
- SAST (Static Analysis) — scan source code for vulns (e.g., Semgrep, CodeQL)
- DAST (Dynamic Analysis) — scan running app (e.g., OWASP ZAP)
- Dependency scanning — check third-party libraries (e.g., Dependabot, Snyk)
- Penetration testing — manual ethical hacking (see Penetration-Testing.md)
- Secrets scanning — prevent credentials in code

## Performance Testing
- Load testing: expected concurrent users
- Stress testing: breaking point
- Endurance testing: memory leaks over time
- Spike testing: sudden traffic surge
- Profiling: CPU, memory, DB query performance

## Test Artifacts
- Test plan doc
- Test case inventory (linked to requirements)
- Bug reports (severity, reproduction steps, expected vs actual)
- Test summary report (pass/fail metrics, coverage gaps, risks)

## Automation Recommendations
- Unit + Integration: pytest (Python), Jest (JS/TS), JUnit (Java)
- E2E: Playwright or Cypress
- API: Postman/Newman collections or Rest Assured
- Security: OWASP ZAP in CI pipeline
- Performance: k6 or Locust
