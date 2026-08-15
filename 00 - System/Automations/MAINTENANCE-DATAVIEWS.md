---
tags:
  - paios/system
  - paios/maintenance
related:
  - "../05 - Knowledge/Knowledge-MOC.md"
  - "./AUTOMATION-REGISTRY.md"
---

# Maintenance Dataviews

Quick-reference Dataview queries for vault health.

---

## Set A — "Health Checks"

### 1. Missing Frontmatter

```dataview
TABLE file.path FROM "" WHERE file.frontmatter = null
```

### 2. Orphan Files (no related links)

```dataview
TABLE file.path, tags FROM "" WHERE length(related) = 0 AND file.folder != "09 - Attachments/" AND file.folder != "99 - Archive/"
```

### 3. Tag Cloud

```dataview
TABLE length(file.etags) as "Tags Count" FROM "" FLATTEN file.etags GROUP BY file.etags SORT length(file.etags) DESC
```

---

## Set B — Link Health

### Files Missing Related or Tags

```dataview
TABLE file.path AS "File", tags, related
FROM ""
WHERE length(related) = 0 OR length(file.tags) = 0
SORT file.folder ASC
```
