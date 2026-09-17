---
name: synthetic-data-generator
description: >
  Leveraging Nous Research's background (OpenHermes, Evol-Instruct), this
  skill guides Hermes in generating high-quality prompt-response synthetic
  datasets, edge-case perturbations, and evaluation benchmarks.
version: 1.0.0
author: PAIOS (based on Nous Research: OpenHermes, Evol-Instruct)
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [synthetic-data, instruction-tuning, evaluation, benchmarks, openhermes, evol-instruct]
    category: research
---

# Synthetic Data & Instruction-Tuning Generator

## When to use

Use when you need to generate training data, test cases, or evaluation
benchmarks. Leverages Nous Research's OpenHermes and Evol-Instruct methodology.

## Workflow

```
Step 1: Define Task
  What task are we generating data for?
  What's the input/output format?

Step 2: Generate Base Examples
  Create prompt-response pairs
  Cover the happy path

Step 3: Evolve (Evol-Instruct)
  Add complexity to simple examples
  Generate edge cases
  Create difficult variants

Step 4: Validate
  Check for consistency
  Verify edge cases are valid
  Remove duplicates

Step 5: Package
  Format as training dataset
  Create evaluation benchmarks
  Document labeling guidelines
```

## Evol-Instruct Process

```
Simple Example → Complexify → Edge Case → Difficult Variant
     ↓              ↓            ↓              ↓
  Base          Harder      Boundary      Stress Test
```

## Dataset Template

```markdown
# Dataset: <name>

## Task
<description>

## Format
- Input: <type>
- Output: <type>

## Examples
1. <input> → <output>
2. <input> → <output>

## Edge Cases
- <edge case 1>
- <edge case 2>

## Benchmarks
- <benchmark 1>
- <benchmark 2>
```

## Pitfalls

- No evolution → only simple examples
- Not validating → bad training data
- No benchmarks → can't measure progress
- Not documenting → unclear labeling