---
name: reflexive-debugging
description: >
  Prevents speculative code editing. When fixing bugs, write a minimal
  reproduction script first, confirm it fails, make the fix, verify it
  passes, and run regression tests before concluding.
version: 1.0.0
author: PAIOS (based on Shinn et al., Reflexion & SWE-bench)
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [debugging, testing, reflexion, sw-e-bench]
    category: development
---

# Reflexive Debugging

## When to use

Use when tasked with fixing bugs, especially complex or recurring ones.
Prevents speculative code editing by forcing a structured approach.

## Rule

When fixing a bug:
1. **Write a minimal reproduction script** — smallest code that demonstrates the bug
2. **Confirm it fails** — run the script, verify the bug manifests
3. **Make the fix** — apply the smallest possible change
4. **Verify it passes** — run the reproduction script again, confirm fix
5. **Run regression tests** — run existing test suite, confirm no breakage

## Workflow

```
Step 1: Reproduce
  Write minimal script that triggers the bug
  Run it, confirm failure

Step 2: Diagnose
  Read error messages, stack traces
  Identify root cause, not symptoms

Step 3: Fix
  Make smallest change that resolves root cause
  Do not refactor unrelated code

Step 4: Verify
  Run reproduction script — must pass
  Run regression tests — must pass
  Run related tests — must pass

Step 5: Document
  Record what the bug was, how it was fixed
  Update /learn with the solution
```

## Pitfalls

- Skipping reproduction → fixes are speculative, often break other things
- Fixing symptoms instead of root cause → bug returns
- Not running regression tests → hidden breakage
- Large refactors during bug fix → introduces new bugs

## Verification

- Reproduction script passes
- All regression tests pass
- No new test failures
- Bug does not return on repeated runs