---
tags:
  - paios/system
  - paios/automation
related:
  - "../../06 - Inbox/Inbox.md"
  - "../../06 - Inbox/Imports/claude/"
  - "../../AGENTS.md"
  - "../Config/Obsidian-Setup.md"
  - "AUTOMATION-REGISTRY.md"
---
# Inbox Processing Pipeline

## Flow
Capture → Categorize → File → Cross-reference → Archive

## Step 1: Capture
Anything goes into `06 - Inbox/`. Raw links, quick notes, voice memos, screenshots, AI chat exports. No filtering at capture time.

## Step 2: Categorize (daily or weekly)
Open `06 - Inbox/Inbox.md`. For each item, decide:
- **Project material** → tag with `paios/projects`, move to `02 - Projects/Active/<project>/research/` or create new project
- **Knowledge** → tag with `paios/knowledge`, file into `05 - Knowledge/<category>/`
- **Template** → tag with `paios/templates`, file into `08 - Templates/<area>/`
- **Business** → tag with `paios/business`, file into `01 - Business/<area>/`
- **Daily/Task** → tag with `paios/daily`, file into `07 - Daily/`
- **Reference** → tag with `paios/references`, file into `05 - Knowledge/References/`

## Step 3: File
- Give it a clear filename matching convention: `Category-Subject.md`
- Add YAML frontmatter with `tags:` and `related:` links
- Write a 2-3 sentence summary at the top
- Link to source if applicable (`via:` in frontmatter)

## Step 4: Cross-reference
- Update the relevant MOC to include the new file
- Add `related:` links to 2-3 sibling files
- Ensure `tags:` uses the `paios/*` convention

## Step 5: Archive
- Move raw source (chat exports, screenshots, PDFs) to `09 - Attachments/` or `99 - Archive/`
- Clear processed items from Inbox

## Automation Check
Run this Dataview query weekly to catch uncategorized inbox items:
```dataview
TABLE file.cday AS "Captured"
FROM "06 - Inbox"
SORT file.cday DESC
```
