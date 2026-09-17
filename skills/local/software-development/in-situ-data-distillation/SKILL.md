---
name: in-situ-data-distillation
description: >
  Instead of dumping huge API responses, SQL dumps, or terminal logs into
  the context window (wasting tokens and diluting reasoning), the agent
  writes a short bash/python one-liner to filter, count, or aggregate the
  data directly on the filesystem and returns only the necessary signal.
version: 1.0.0
author: PAIOS
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [efficiency, context, token-optimization, data-distillation]
    category: efficiency
---

# In-Situ Data Distillation

## When to use

Use when dealing with large API responses, SQL dumps, or terminal logs.
Prevents wasting tokens and diluting reasoning by filtering data on the filesystem.

## Rule

Instead of dumping large data into context:
1. **Write a bash/python one-liner** to filter, count, or aggregate on the filesystem
2. **Return only the necessary signal** — small, focused result
3. **Keep context lean** — only relevant data in the conversation

## Workflow

```
Step 1: Identify large data source
  API response? SQL dump? Terminal log?

Step 2: Write distillation command
  bash: grep, awk, sed, cut, sort, uniq
  python: pandas, json filtering, csv processing

Step 3: Extract signal
  Count, filter, aggregate, summarize
  Return only what's needed

Step 4: Use signal in context
  Small result → clear reasoning → good decisions
```

## Examples

```bash
# Instead of dumping full API response:
curl -s "https://api.example.com/data" | python -c "import sys,json; d=json.load(sys.stdin); print(len(d), 'items')"

# Instead of full SQL dump:
sqlite3 db.sqlite "SELECT COUNT(*), status FROM orders GROUP BY status"

# Instead of full log file:
grep -c "ERROR" app.log && grep "ERROR" app.log | head -10
```

## Pitfalls

- Dumping full data into context → token waste, diluted reasoning
- Not filtering → noise overwhelms signal
- Over-distilling → loses important details
- Not verifying distillation → wrong conclusions