---
name: youtube-shorts-research
description: Research stage: DuckDuckGo search + web scraping for fact-based scripts
version: 1.0.0
author: Coach (auto-generated from rushindrasinha/youtube-shorts-pipeline)
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [auto-generated, coach, youtube-shorts, media-content]
    source: https://github.com/rushindrasinha/youtube-shorts-pipeline
---

# Youtube Shorts Research

## When to use

Research stage: DuckDuckGo search + web scraping for fact-based scripts

## Tools

- `research-search`
- `research-scrape`
- `research-verify`

## Workflow

1. Initialize the pipeline component
2. Execute the relevant tool
3. Handle response or error
4. Log result

## Error handling

- Stage failed → retry with --force flag
- Provider error → switch via --provider flag
- Upload failed → check YouTube OAuth, retry private upload
