---
name: paios-core
description: Core PAIOS Personal AI Operating System orchestration.
version: 0.1.0
author: Mark Chester Santos (chesr), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [paios, orchestration, ai-os, automation]
    related_skills: [github-sync, skill-ecosystem]
---

# PAIOS Core Skill

Orchestrates the Personal AI Operating System — a unified layer for agents, skills, vaults, projects, and GitHub-synced knowledge.

## When to Use

- Bootstrapping a new PAIOS workspace
- Coordinating multi-agent workflows across projects
- Syncing skills, vaults, and projects to GitHub
- Managing the PAIOS skill ecosystem

Don't use for: single one-off tasks; use the specific sub-skills instead.

## Prerequisites

- GitHub CLI (`gh`) authenticated
- Git configured with user.name/user.email
- Hermes Agent running
- API keys in `$LOCALAPPDATA/hermes/.env` (OpenRouter, Anthropic, Google, OpenAI, DeepSeek, HF, Kimi, etc.)
- `PAIOS_ROOT` env var pointing to the PAIOS repo root (default: `~/paios`)

## Quick Reference

```bash
# Initialize PAIOS workspace
paios init

# Sync all to GitHub
paios sync

# Install a skill from GitHub
paios skill install <org>/<skill>

# List local skills
paios skill list

# Run a multi-agent workflow
paios workflow run <name>
```

## Procedure

### 1. Initialize Workspace

```bash
mkdir -p "$PAIOS_ROOT"/{projects,skills,vaults,agents,workflows,docs}
cd "$PAIOS_ROOT"
git init
gh repo create paios --private --source=. --push
```

**Completion:** `PAIOS_ROOT` exists with dir structure; GitHub repo created and pushed.

### 2. Sync Skills to GitHub

```bash
# From Hermes skills dir
cp -r "$LOCALAPPDATA/hermes/skills" "$PAIOS_ROOT/skills/local"
cd "$PAIOS_ROOT"
git add skills/local
git commit -m "chore: sync local skills"
git push
```

**Completion:** Local skills mirrored to GitHub under `skills/local/`.

### 3. Sync Vaults/Projects

```bash
# Vaults (encrypted secrets, configs)
cp -r "$LOCALAPPDATA/hermes/vaults" "$PAIOS_ROOT/vaults" 2>/dev/null || true
# Projects (Hermes projects.db export)
cp "$LOCALAPPDATA/hermes/projects.db" "$PAIOS_ROOT/projects/" 2>/dev/null || true
cd "$PAIOS_ROOT" && git add -A && git commit -m "chore: sync vaults/projects" && git push
```

**Completion:** Vaults and projects backed up to GitHub.

### 4. Install Remote Skill

```bash
cd "$PAIOS_ROOT/skills"
git submodule add https://github.com/<org>/<skill>.git "optional/<skill>"
# Or use hermes skills install if published
```

**Completion:** Skill available at `skills/optional/<skill>/SKILL.md`.

## Pitfalls

- GitHub device flow auth must complete before any `gh` command works
- Large vaults/projects.db may exceed GitHub file limits — use Git LFS if needed
- Skill submodules require `git submodule update --init --recursive` on clone
- Windows paths in skills must use forward slashes or `pathlib`

## Verification

- `gh auth status` shows logged in
- `git -C "$PAIOS_ROOT" remote -v` shows origin
- `ls "$PAIOS_ROOT/skills/local"` lists synced skills
- `gh repo view paios --json name,visibility` returns repo info