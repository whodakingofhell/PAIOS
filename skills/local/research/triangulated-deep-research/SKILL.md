---
name: triangulated-deep-research
description: >
  When researching technical topics, competitors, or academic subjects, the
  agent does not rely on a single search query. It generates multi-angle
  queries, compares at least three independent sources, flags conflicting
  data, traces source citations, and constructs a structured synthesis report.
version: 1.0.0
author: PAIOS (based on Stanford's Co-STORM architecture)
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [research, triangulation, deep-research, co-storm, synthesis]
    category: research
---

# Triangulated Deep Research

## When to use

Use when researching technical topics, competitors, or academic subjects.
Prevents single-source bias by comparing multiple independent sources.

## Rule

When researching:
1. **Generate multi-angle queries** — don't rely on one search
2. **Compare at least 3 independent sources** — cross-reference
3. **Flag conflicting data** — note disagreements between sources
4. **Trace source citations** — follow the evidence chain
5. **Construct structured synthesis report** — combine into coherent answer

## Workflow

```
Step 1: Multi-Angle Queries
  Generate 3+ queries from different angles
  Example: "X feature" vs "X alternative" vs "X comparison"

Step 2: Source Collection
  Collect from 3+ independent sources
  Don't rely on single source

Step 3: Cross-Reference
  Compare findings across sources
  Flag conflicts and disagreements

Step 4: Trace Citations
  Follow evidence chain to original sources
  Verify claims against primary sources

Step 5: Synthesize
  Construct structured report
  Note confidence level per claim
  Flag unresolved conflicts
```

## Report Template

```markdown
# Research Report: <topic>

## Sources
1. <source 1> — <confidence>
2. <source 2> — <confidence>
3. <source 3> — <confidence>

## Findings
- <finding 1> (confidence: high/medium/low)
- <finding 2> (confidence: high/medium/low)

## Conflicts
- <conflict 1> — <resolution>

## Citations
- <primary source 1>
- <primary source 2>

## Confidence
Overall: <high/medium/low>
```

## Pitfalls

- Single source → biased conclusions
- No cross-referencing → missed conflicts
- Not tracing citations → unverified claims
- Ignoring conflicts → wrong conclusions