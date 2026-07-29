---
tags:
  - paios/system
  - paios/config
related:
  - "../Automations/AUTOMATION-REGISTRY.md"
  - "../../AGENTS.md"
---

# Obsidian Setup Guide

## Already Enabled (Core Plugins)

These are already active and useful for PAIOS:

| Plugin | What it does for you |
|--------|---------------------|
| **Backlinks** | Shows all files linking to the current note (uses YAML `related` field) |
| **Graph View** | Visual map of all connections between files |
| **Tag Pane** | Lists all `paios/*` tags for filtering by area |
| **Properties** | Displays YAML frontmatter in a table view |
| **Outgoing Links** | Shows links FROM the current file |
| **Templates** | Insert template files from `08 - Templates/` |

## Recommended Community Plugins

Install these from **Settings → Community Plugins → Browse**:

### 1. Dataview (Essential)
Live-updating database queries over your vault.

**Why for PAIOS:** Auto-generates tables of all knowledge files by tag, shows unlinked files, creates dynamic indexes.

**How to install:**
1. Settings → Community plugins → Turn off Restricted Mode → Browse
2. Search "Dataview" → Install → Enable
3. No further config needed

**Example query to run anywhere:**
```
\`\`\`dataview
TABLE tags, file.outlinks AS "Related"
FROM "05 - Knowledge"
SORT file.name
\`\`\`
```

### 2. Quiet Outline (Recommended)
Better outline/table of contents panel.

### 3. Obsidian Git (For power users)
Auto-commit and sync to GitHub from within Obsidian.

---

## How the Connections Work

Now that every knowledge file has `tags` and `related` in YAML frontmatter:

1. **Backlinks panel** will show related files when you're viewing any note
2. **Graph View** (global or local) visualizes the connections as nodes
3. **Tag Pane** groups files by `paios/ai`, `paios/security`, etc.
4. **Properties** shows the structured data at the top of each file
5. **With Dataview**: you can write `TABLE related FROM "05 - Knowledge"` for a live index

## Tagging Convention

Tags used across PAIOS knowledge files:

| Tag | Area |
|-----|------|
| `paios/knowledge` | All knowledge files |
| `paios/ai` | AI-related knowledge |
| `paios/architecture` | Architecture docs |
| `paios/business` | Business operations |
| `paios/devops` | DevOps & automation |
| `paios/product-design` | Product design |
| `paios/references` | Reference materials |
| `paios/software-development` | Software engineering |
| `paios/security` | Security docs |
| `paios/qa` | Quality assurance |
| `paios/moc` | Maps of Content |
