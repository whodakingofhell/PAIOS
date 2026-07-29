---
tags:
  - paios/knowledge
  - paios/documentation
  - paios/software-development
  - technical-writing
related:
  - "../Knowledge-MOC.md"
  - "../AI/08-AI-Knowledge.md"
  - "Product-Design/Content-Pipeline.md"
  - "Product-Design/02-Product.md"
---

# 09 — Documentation

> Section 09 of the AI Engineering OS

---

## Purpose

Establishes **documentation standards, what gets documented and when, README conventions, API documentation, Architecture Decision Records (ADRs), changelog format, and the documentation-as-code approach**. Ensures all knowledge is captured, searchable, and maintainable.

---

## Owner Team

**All Teams** — Documentation is everyone's responsibility, coordinated by QA

---

## Key Responsibilities

- Define **what gets documented** and at what level of detail.
- Establish **documentation templates** (README, ADR, runbook, changelog).
- Enforce **documentation-as-code** — docs in Git, reviewed like code, versioned with releases.
- Maintain the **changelog** using Keep a Changelog format.
- Ensure **API documentation** is auto-generated or maintained alongside code.
- Track **documentation coverage** — are all systems and decisions documented?

---

## What Gets Documented

| Category | What | When | Template |
|---|---|---|---|
| **Project overview** | Vision, business case, product spec | Project start | `Project\Vision.md`, `Business.md`, `Product.md` |
| **Architecture** | System design, tech choices, data flow | Design phase | `Project\Architecture.md` + ADRs |
| **Code** | Inline comments, README per module | While coding | Standard README template |
| **APIs** | Endpoints, request/response, auth | While building | OpenAPI-style template |
| **Decisions** | Why a choice was made, alternatives considered | At decision time | ADR template |
| **Changes** | What changed, why, who | Every release | Keep a Changelog format |
| **Runbooks** | How to operate, deploy, recover | At deployment | Runbook template |
| **Content pipeline** | Stage configs, prompt versions, quality scores | Per video | Pipeline state JSON + prompts |
| **Learnings** | What worked, what didn't, what to try next | Per sprint/project | Obsidian vault notes |

---

## Documentation Templates

### README Standard

Every repo, module, and project directory has a README with:

```markdown
# [Name]

> One-sentence description

## Quick Start
[3-5 commands to get running]

## Architecture
[System diagram or link]

## Configuration
[Env vars, config files, setup steps]

## Usage
[Common operations with examples]

## Testing
[How to run tests]

## Contributing
[Branch, commit, PR conventions]

## License
[License type]
```

### Architecture Decision Record (ADR)

```markdown
# ADR-[NNN]: [Title]

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR-XXX]

## Context
[Why this decision was needed. What forces are at play.]

## Decision
[What was decided. One clear statement.]

## Consequences
### Positive
[Benefits of this decision]
### Negative
[Trade-offs and costs]
### Risks
[What could go wrong]
```

### Changelog Format (Keep a Changelog)

```markdown
# Changelog

## [Unreleased]

## [X.Y.Z] - YYYY-MM-DD
### Added
- New feature or capability
### Changed
- Changes to existing functionality
### Deprecated
- Features about to be removed
### Removed
- Features removed in this release
### Fixed
- Bug fixes
### Security
- Security-related fixes
```

---

## Documentation-as-Code Principles

1. **Docs in Git.** All documentation lives in the repository alongside code. No separate wiki (except Obsidian vault for knowledge management, which IS Git-backed).
2. **Reviewed like code.** Doc changes go through PR review. Spelling, accuracy, and completeness checked.
3. **Versioned with releases.** Documentation versions match software versions. A reader of v2.1 docs should see v2.1 behavior.
4. **Auto-generated when possible.** API docs from code annotations. Dependency lists from lock files. Pipeline state from script outputs.
5. **Searchable.** All docs are plain text (markdown, YAML, JSON). No PDFs, no images-of-text. Grep-friendly.

---

## Documentation Coverage Checklist

For any system or project, the following must be documented:

- [ ] **README** — What it is, how to run it, how to test it.
- [ ] **Architecture** — How it works, components, data flow.
- [ ] **Configuration** — All env vars, config files, their meanings.
- [ ] **API Reference** — All endpoints, request/response, auth.
- [ ] **Decisions** — ADRs for all significant technical choices.
- [ ] **Runbook** — How to deploy, monitor, recover from failure.
- [ ] **Changelog** — What changed in each release.
- [ ] **Security** — Threat model, secrets, auth (see `06-Security`).

---

## Inputs

- All project and system artifacts
- Architecture decisions (`03-Architecture\Architecture.md`)
- Code and pipeline outputs
- Team decisions and rationale

---

## Outputs

- This documentation standards document
- README files (per repo, module, project)
- ADRs (per significant decision)
- Changelogs (per release)
- Runbooks (per deployed system)
- API documentation (per service)

---

## Operating Principles

1. **Document at the point of decision.** Write the ADR when you make the choice, not weeks later.
2. **A comment in code explains WHY.** The code explains WHAT. Comments explain WHY.
3. **If it's not documented, it doesn't exist.** Undocumented systems are unmaintainable systems.
4. **Keep docs current.** A stale doc is worse than no doc. Update in the same PR as the code change.
5. **One source of truth.** Don't duplicate documentation. Link instead. If you must duplicate, note where the canonical version lives.

---

## Acceptance Criteria

- [ ] Documentation coverage checklist is defined with 8 categories.
- [ ] README template is established and used in all repos.
- [ ] ADR template is defined with status, context, decision, consequences.
- [ ] Changelog format follows Keep a Changelog.
- [ ] Documentation-as-code principles are stated (5 principles).
- [ ] All 13 OS sections and 20 Project templates exist and are substantive.

---

## Cross-References

| Document | Relationship |
|---|---|
| `04-Engineering\Engineering.md` | Engineering produces code that needs docs |
| `08-AI-Knowledge\AI-Knowledge.md` | Knowledge base is a form of documentation |
| `Project\Changelog.md` | Per-project changelog template |
| `Project\Documentation.md` | Per-project documentation spec |

## Applied in PAIOS Projects

**PAIOS Vault (this knowledge base)** — This documentation section is meta: the PAIOS vault itself is the most comprehensive example of the documentation standards defined here. Every file has YAML frontmatter with `tags` and `related` fields for cross-referencing. The `PROJECT-CONTEXT.md` files in each project are READMEs following the standard template. The SYSTEM docs (like `SYSTEM/MASTER_REFERENCE.md`) contain ADRs documenting architectural decisions. The vault is versioned on GitHub, reviewed through PRs, and searchable via Obsidian's built-in grep — meeting every "Documentation-as-Code" principle.

**AI-Appointment-Assistant** — The `PROJECT-CONTEXT.md` for this project was the template that inspired the README standard in this section. The project's `CHANGELOG.md` follows the "Keep a Changelog" format with every release documented. The inline code comments follow the "explain WHY, not WHAT" principle — for example, the webhook handler has a comment explaining *why* SMS replies are idempotent (to prevent double-booking), not *what* the code does.
