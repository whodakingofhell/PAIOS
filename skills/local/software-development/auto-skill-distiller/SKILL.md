---
name: auto-skill-distiller
description: >
  When Hermes successfully solves a multi-step challenge after several
  iterations, it automatically distills the solution into a new SKILL.md
  under ~/.hermes/skills/ using Hermes's built-in /learn workflow.
version: 1.0.0
author: PAIOS (based on Wang et al., Voyager)
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [self-evolution, skill-distillation, voyager, learn, procedural-memory]
    category: self-improvement
---

# Self-Evolving Skill Extraction (auto-skill-distiller)

## When to use

Use when Hermes successfully solves a multi-step challenge after several
iterations. Automatically distills the solution into a reusable skill.

## Rule

After solving a complex challenge:
1. **Distill the solution** into a new SKILL.md file
2. **Use Hermes's /learn workflow** — built-in skill extraction
3. **Store under ~/.hermes/skills/** — discoverable by all agents
4. **Tag with category and triggers** — when to use this skill

## Workflow

```
Step 1: Solve Challenge
  Complete the multi-step task
  Document each step taken

Step 2: Distill
  Extract the pattern from the solution
  Write SKILL.md with:
    - Trigger conditions
    - Step-by-step procedure
    - Pitfalls and edge cases
    - Verification steps

Step 3: Store
  Save to ~/.hermes/skills/<category>/<skill-name>/SKILL.md
  Make discoverable by all agents

Step 4: Verify
  Test the skill on a similar challenge
  Confirm it works reliably
```

## Skill Template

```markdown
---
name: <skill-name>
description: >
  <when to use this skill>
version: 1.0.0
author: PAIOS (auto-distilled)
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [<category>, <triggers>]
    category: <category>
---

# <Skill Name>

## When to use

<trigger conditions>

## Steps

1. <step 1>
2. <step 2>
3. <step 3>

## Pitfalls

<common mistakes>

## Verification

<how to verify success>
```

## Pitfalls

- Not distilling → knowledge lost
- Too vague → skill not usable
- No verification → skill untested
- Not storing → skill not discoverable