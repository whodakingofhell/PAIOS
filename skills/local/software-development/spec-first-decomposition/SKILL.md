---
name: spec-first-decomposition
description: >
  For complex, ambiguous projects. Enforces a phase where the agent drafts
  clear interface contracts, data schemas, and milestones before writing
  production code.
version: 1.0.0
author: PAIOS
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [specification, decomposition, contracts, schemas, milestones]
    category: development
---

# Spec-First Decomposition

## When to use

Use for complex, ambiguous projects before writing any production code.
Enforces a specification phase that prevents scope creep and rework.

## Rule

For complex projects:
1. **Draft interface contracts** — what does each component expose?
2. **Define data schemas** — what data flows between components?
3. **Set milestones** — what are the delivery checkpoints?
4. **Only then write code** — production code follows the spec

## Workflow

```
Phase 1: Specification
  Draft interface contracts for each component
  Define data schemas (input/output formats)
  Set milestones with deliverables
  Review spec with stakeholders

Phase 2: Implementation
  Write code following the spec
  Each component matches its contract
  Data flows match the schemas

Phase 3: Validation
  Verify each contract is fulfilled
  Validate data schemas
  Confirm milestones met
```

## Contract Template

```
Component: <name>
Interface:
  - Input: <type, format>
  - Output: <type, format>
  - Errors: <error types>
Dependencies:
  - <other components>
Contract:
  - <obligations>
  - <guarantees>
```

## Pitfalls

- Skipping spec → rework, scope creep
- Vague contracts → integration failures
- No milestones → no progress tracking
- Changing spec mid-implementation → confusion