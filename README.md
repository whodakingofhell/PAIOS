# PAIOS — Personal AI Operating System

Unified workspace for Hermes Agent: skills, vaults, projects, workflows, and GitHub-synced knowledge.

## Structure

```
paios/
├── skills/
│   ├── local/      # Hermes bundled + installed skills
│   └── user/       # User-created skills (~/.hermes/skills)
├── vaults/         # Encrypted secrets, API keys, configs
├── projects/       # Hermes projects.db export
├── agents/         # Agent definitions, prompts
├── workflows/      # Multi-skill workflow YAMLs
├── docs/           # Generated docs, architecture
├── config/         # Hermes config.yaml, sync maps
└── cron/           # Scheduled jobs
```

## Sync

```bash
# Push local changes to GitHub
cd ~/paios && git add -A && git commit -m "sync: $(date -u +%Y-%m-%dT%H:%M:%SZ)" && git push

# Pull from GitHub
cd ~/paios && git pull --rebase
```

## Skills

Managed via `skill-ecosystem` skill. See `skills/local/software-development/skill-ecosystem/SKILL.md`.
