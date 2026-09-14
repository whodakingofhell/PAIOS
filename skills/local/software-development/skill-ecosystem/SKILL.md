---
name: skill-ecosystem
description: Manage, discover, and compose Hermes skills without duplication.
version: 0.1.0
author: Mark Chester Santos (chesr), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [skills, registry, composition, deduplication]
    related_skills: [paios-core, github-sync]
---

# Skill Ecosystem Skill

Govern the PAIOS skill library: install, update, compose, and deduplicate skills.

## When to Use

- Installing a new skill from GitHub or registry
- Updating all skills to latest
- Finding duplicate/overlapping skills

## Quick Reference

```bash
skill-ecosystem list
skill-ecosystem install <org>/<skill>
skill-ecosystem update
skill-ecosystem dedupe
skill-ecosystem compose <workflow-name>
skill-ecosystem audit
```

## Procedure

### 1. Inventory Skills

```bash
ls "$LOCALAPPDATA/hermes/skills"
ls "$HERMES_REPO/skills"
ls "$LOCALAPPDATA/hermes/optional-skills" 2>/dev/null || true
```

### 2. Install Skill

```bash
hermes skills install official/<category>/<skill>
```

### 3. Deduplicate

```bash
for f in $(find skills -name SKILL.md); do
  desc=$(grep '^description:' "$f" | cut -d' ' -f2-)
  echo "$f: $desc"
done | sort -k2 | uniq -D -f1
```

### 4. Compose Workflow

```yaml
name: <workflow-name>
steps:
  - skill: <skill-a>
    invoke: <method>
  - skill: <skill-b>
    invoke: <method>
    params:
      input: "{{step_1.output}}"
```

### 5. Health Audit

```bash
for f in $(find skills -name SKILL.md); do
  test=$(echo "$f" | sed 's|SKILL.md|tests/skills/test_'$(basename $(dirname "$f"))'_skill.py|')
  [ -f "$test" ] || echo "$f: no test file"
done
```

## Pitfalls

- Skill names must be unique across tiers
- Submodule skills need git submodule update

## Verification

- skill-ecosystem list shows skills
- dedupe outputs zero lines = no dupes
- audit exits 0
