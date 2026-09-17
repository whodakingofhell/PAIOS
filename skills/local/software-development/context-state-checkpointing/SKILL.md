---
name: context-state-checkpointing
description: >
  For long-horizon tasks. Prompts the agent to write intermediate summaries
  and active state into a scratchpad file (scratch/status.md), keeping active
  conversational context lean.
version: 1.0.0
author: PAIOS
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [context, checkpointing, scratchpad, long-horizon, state-management]
    category: efficiency
---

# Context State Checkpointing

## When to use

Use for long-horizon tasks that span multiple conversations or sessions.
Keeps active context lean by writing intermediate summaries to a scratchpad.

## Rule

For long tasks:
1. **Write intermediate summaries** to scratchpad file
2. **Track active state** — what's done, what's next
3. **Keep conversational context lean** — only current step in context
4. **Resume from scratchpad** when returning to task

## Workflow

```
Step 1: Create scratchpad
  mkdir -p scratch
  Write scratch/status.md

Step 2: Checkpoint regularly
  After each major step, update scratch/status.md
  Summarize: done, next, blockers

Step 3: Resume from checkpoint
  Read scratch/status.md
  Continue from last checkpoint

Step 4: Clean up
  When task complete, archive scratchpad
```

## Scratchpad Template

```markdown
# Task Status

## Done
- [x] Step 1
- [x] Step 2

## Next
- [ ] Step 3

## Blockers
- None

## Notes
- Key decisions made
- Important context
```

## Pitfalls

- No checkpointing → lost context on resume
- Too much detail → scratchpad becomes noise
- Not updating → stale state
- Not reading on resume → repeats work