---
name: web-content
description: Fetch, extract, and cache structured web content from pages and APIs.
version: 0.1.0
author: Mark Chester Santos (chesr), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [web, fetch, extract, cache, scrape]
    related_skills: [paios-core, skill-ecosystem]
---

# Web Content Skill

Fetch and extract structured content from web pages, APIs, and documents — with caching to avoid repeats.

## When to Use

- Extracting article text, documentation, or blog posts
- Downloading JSON/API responses for processing
- Caching fetches to avoid hitting rate limits
- Converting PDF/HTML to text for analysis

Don't use for: interactive browsing (use browser_exec); real-time scraping against blocked sites.

## Quick Reference

```bash
web-content fetch <url> [--cache] [--format json|text|markdown]
web-content extract <source> [--select css-selector]
web-content cache-list [--older-than <age>]
```

## Procedure

### 1. Fetch URL

```bash
# Use Hermes built-in tools
web_extract(urls=["$URL"], char_limit=30000)
# or raw curl with headers
curl -sL -A "Mozilla/5.0" "$URL" | python -m json.tool  # for JSON APIs
```

**Completion:** Content captured, parsed if JSON.

### 2. Extract Structured Content

```bash
# HTML to markdown via read_file (auto-extracts PDF/docx)
read_file(path="$LOCALFILE")  # PDF, docx, pptx auto-extract

# From browser page (render JS-heavy pages)
browser_exec("""
(() => {
  return document.title + "\n" +
         Array.from(document.querySelectorAll("article, main, .content"))
           .map(el => el.innerText).join("\n\n");
})()
""")
```

**Completion:** Extracted text in target format.

### 3. Cache Management

```bash
# Cache to local file with hash-based name
echo "$URL" | shasum | cut -d' ' -f1  # file hash
mkdir -p "$PAIOS_ROOT/cache/web"
echo "$CONTENT" > "$PAIOS_ROOT/cache/web/$(echo -n "$URL" | shasum | cut -d' ' -f1).txt"

# List cache
find "$PAIOS_ROOT/cache/web" -type f -printf "%T+ %p\n" | sort -r
```

**Completion:** Cached files written with URL-derived names.

### 4. Parse Tables / Lists

```python
# Extract tables from HTML
python -c "
from bs4 import BeautifulSoup
import sys, html
soup = BeautifulSoup(sys.stdin.read(), 'html.parser')
for t in soup.find_all('table'):
    print('---')
    for row in t.find_all('tr'):
        print('| ' + ' | '.join(c.get_text(strip=True) for c in row.find_all(['td','th'])) + ' |')
"
```

**Completion:** Tables extracted to markdown format.

## Pitfalls

- Some sites block non-browser user-agents — use browser_exec for JS-rendered content
- PDf extraction depends on text layer; scanned PDFs need OCR (not yet wired)
- Cache naming collisions: use full URL hash, not truncated
- Rate limits: stagger requests, use cache before fetch
- Large pages: web_extract truncates at char_limit — raise it or use browser_exec for full DOM text

## Verification

- `web-content fetch <url>` returns valid content
- `find "$PAIOS_ROOT/cache/web" | wc -l` increases after fetch
- JSON fetches parse without error
- Table extraction produces markdown table rows")
