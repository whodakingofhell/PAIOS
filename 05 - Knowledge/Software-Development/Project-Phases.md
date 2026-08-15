---
tags:
  - paios/knowledge
  - paios/software-development
  - paios/process
related:
  - "00-Vision.md"
  - "12-Roadmap.md"
  - "../Product-Design/02-Product.md"
  - "Testing-Lifecycle.md"
  - "../DevOps/CI-CD-Pipeline.md"
  - "../DevOps/Monitoring-Observability.md"
---

# Project Phases

## Phase 0: Discovery & Inception
- Stakeholder interviews, problem definition, success criteria
- Target users, personas, user stories (epic level)
- Technical feasibility assessment
- Constraints: budget, timeline, compliance, platform
- Output: Vision doc, Business case

## Phase 1: Product Definition
- Feature prioritization (MoSCoW: Must have / Should have / Could have / Won't have)
- User flow diagrams, wireframes (low-fi)
- Technical stack selection (language, framework, database, hosting)
- API contract design (sync with backend team)
- Output: Product Requirements Doc, Architecture Decision Record

## Phase 2: Design
- UI design (hi-fi mockups, prototype)
- Design system / component library selection or creation
- UX review (usability testing of prototype)
- Accessibility audit (WCAG 2.1 AA minimum)
- Output: Figma/Sketch files, Design System spec

## Phase 3: Development
- Sprint planning, task breakdown
- Database schema design and migrations
- API implementation (REST/GraphQL)
- Frontend implementation (responsive, cross-browser)
- Authentication & authorization
- CI/CD pipeline setup (build → lint → test → deploy)
- Environment strategy (dev / staging / production)
- Output: Working software in staging

## Phase 4: Testing
- Developer testing (unit tests, integration tests)
- QA testing (functional, regression, E2E)
- Security testing (SAST, DAST, dependency scan, penetration testing)
- Performance testing (load, stress, profile)
- UAT (User Acceptance Testing with stakeholders)
- Accessibility testing (screen reader, keyboard navigation)
- Output: Test reports, sign-off

## Phase 5: Launch
- Pre-launch checklist (DNS, SSL, backups, monitoring)
- Staged rollout (canary or feature flags)
- Documentation handoff (technical + user)
- Monitoring dashboards and alert rules
- Rollback plan
- Output: Live application

## Phase 6: Maintenance & Iteration
- Bug triage and patch cycle
- Performance monitoring and optimization
- Security updates and vulnerability patching
- Feature requests → backlog → next iteration
- Regular retrospectives → lessons learned → Knowledge base
- Output: Continuous improvement loop

## Cross-cutting concerns (apply in every phase)
- Security: threat modeling in Phase 1, pentest in Phase 4, patch in Phase 6
- Accessibility: design in Phase 2, test in Phase 4, maintain in Phase 6
- Performance: benchmark in Phase 3, load test in Phase 4, monitor in Phase 6
- Documentation: technical in Phase 3, user in Phase 4, handoff in Phase 5
- Privacy: PII mapping in Phase 0, compliance review in Phase 4
