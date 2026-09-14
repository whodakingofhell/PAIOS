---
name: web-content
description: Fetch and extract structured web content with caching.
version: 0.1.0
author: Mark Chester Santos (chesr), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [web, fetch, extract, cache]
    related_skills: [paios-core, github-sync]
---

# Web Content Skill

Fetch pages/APIs and extract clean content; cache to avoid repeat hits.

## When to Use

- Reading articles, docs, blogs, PDFs
- Calling REST/JSON APIs
- Caching to avoid rate limits
- Converting HTML/PDF to text

Don't use for: interactive browser sessions (use browser_exec).

## Quick Reference

```bash
web-content fetch <url> [--format json|markdown|text]
web-content cache-list
web-content cache-rm <hash>
```

## Procedure

### 1. Fetch

```bash
# Hermes built-in extract (auto PDF/docx)
web_extract(urls=["$URL"], char_limit=30000)

# Raw JSON API
curl -sL "$URL" | jq .

# Browser-rendered page
browser_exec("document.title + '\n' + document.querySelector('main')?.innerText || ''")
```

### 2. Cache

```bash
HASH=$(echo -n "$URL" | sha256sum | cut -d' ' -f1)
mkdir -p "$PAIOS_ROOT/cache/web"
echo "$CONTENT" > "$PAIOS_ROOT/cache/web/$HASH.txt"
```

### 3. List / Clean Cache

```bash
find "$PAIOS_ROOT/cache/web" -type f -printf "%T+ %f\n" | sort -r
rm "$PAIOS_ROOT/cache/web/<hash>.txt"
```

## Pitfalls

- Blocked/non-browser origins: use browser_exec or browser_navigate
- JS-heavy sites: browser_exec reads rendered DOM
- Scanned PDFs need OCR (not yet wired here)
- Rate limits: cache first, request second

## Verification

- fetch returns content > 0 bytes
- cache file exists at predicted hash path
- JSON parses with jq
