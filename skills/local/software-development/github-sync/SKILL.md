---
name: github-sync
description: Sync Hermes projects, skills, vaults to GitHub repos.
version: 0.1.0
author: Mark Chester Santos (chesr), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [github, sync, backup, ci-cd]
    related_skills: [paios-core, skill-ecosystem]
---

# GitHub Sync Skill

Automates bidirectional sync between Hermes local state and GitHub repositories.

## When to Use

- Periodic backup of Hermes workspace to GitHub
- Restoring workspace on a fresh machine

## Quick Reference

```bash
github-sync push
github-sync pull
github-sync sync
github-sync plan
```

## Procedure

### 1. Prepare Repo

```bash
cd "$PAIOS_ROOT"
cat > .gitignore <<'EOF'
state.db*
*.log
cache/
node_modules/
.env
EOF
```

### 2. Define Sync Map

```yaml
# .github-sync.yaml
source_root: "$LOCALAPPDATA/hermes"
target_root: "$PAIOS_ROOT"
mappings:
  - src: "skills"; dst: "skills/local"
  - src: "vaults"; dst: "vaults"
  - src: "projects.db"; dst: "projects/projects.db"
  - src: "config.yaml"; dst: "config/hermes.yaml"
```

### 3. Push

```bash
rsync -av "$SOURCE/skills/" "$TARGET/skills/local/"
cd "$TARGET" && git add -A && git commit -m "sync" && git push
```

### 4. Pull

```bash
cd "$TARGET" && git pull --rebase
rsync -av "$TARGET/skills/local/" "$SOURCE/skills/"
```

## Pitfalls

- Never commit .env or state.db*
- Use Git LFS for large files

## Verification

- git diff --stat shows expected paths
- Round-trip diff empty