---
name: adversarial-red-teaming
description: >
  Applied before executing destructive commands, database migrations,
  or major architectural changes. The agent conducts a structured critique:
  identifying three likely failure modes, checking edge conditions, and
  establishing a rollback plan.
version: 1.0.0
author: PAIOS (based on Chain-of-Verification)
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [red-teaming, pre-mortem, safety, rollback, chain-of-verification]
    category: development
---

# Adversarial Red-Teaming & Pre-Mortem

## When to use

Use before executing destructive commands, database migrations, or major
architectural changes. Forces structured critique before action.

## Rule

Before any destructive action:
1. **Identify three likely failure modes** — what could go wrong?
2. **Check edge conditions** — what happens at boundaries?
3. **Establish a rollback plan** — how do you undo if things break?

## Workflow

```
Step 1: Identify Failure Modes
  List 3 things that could go wrong
  Rank by likelihood and impact

Step 2: Check Edge Conditions
  What happens with empty data?
  What happens with max load?
  What happens with invalid input?
  What happens concurrently?

Step 3: Establish Rollback Plan
  Backup current state
  Define rollback steps
  Test rollback procedure

Step 4: Execute
  Proceed only if failure modes are acceptable
  Execute with rollback ready

Step 5: Verify
  Confirm success
  Monitor for failure modes
```

## Failure Mode Template

For each failure mode, document:
- What happens
- How likely (low/medium/high)
- Impact if it occurs
- Prevention strategy
- Detection method
- Rollback procedure

## Pitfalls

- Skipping pre-mortem → surprise failures
- No rollback plan → stuck with broken state
- Ignoring edge cases → production incidents
- Not testing rollback → rollback fails when needed