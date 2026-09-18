---
name: strix-security-audit
description: >
  Security Head uses Strix to run autonomous vulnerability scans
  against PAIOS. Finds exploits, validates PoCs, applies permanent
  fixes. Covers OWASP Top 10, injection, XSS, SSRF, auth bypass,
  IDOR, business logic flaws.
version: 1.0.1
author: PAIOS Security Head (based on usestrix/strix)
platforms: [windows]
metadata:
  hermes:
    tags: [security, pentest, strix, vulnerability, owasp, paios]
    category: security
    assigned_to: security-head
---

# Strix Security Audit — PAIOS Fleet

## When to use

Security Head initiates when:
- New code or integration is added
- Periodic vulnerability sweep needed
- User requests security audit
- After dependency updates

## Audit Workflow

### Phase 1: Pre-flight Checks
1. Verify Docker running: `docker ps` (install via winget: `winget install Docker.DockerDesktop`)
2. Verify valid LLM API key — Strix requires a working key. Test with: `strix --target . -m quick --max-budget 1`
3. Set env vars:
   ```bash
   export STRIX_LLM="openai/gpt-5.4"      # recommended; or deepseek/v4-flash, gemini/gemini-3.6-flash
   export LLM_API_KEY="<valid-key>"       # must be active — expired keys cause silent failures
   ```

### Phase 2: Static Analysis (white-box, no Docker needed)
```bash
strix --target ~/paios -m quick --max-budget 10
```

### Phase 3: Dynamic Analysis (Docker required)
```bash
strix --target ~/paios -m deep --max-budget 30   # first run pulls sandbox image (~2min)
```

### Phase 4: Validate & Fix
1. Review each finding with severity
2. Apply permanent fixes
3. Re-run Strix to verify
4. Document remediation in `audit/security-audit-<date>.md`

## PAIOS Attack Surface

| Asset | Risk | Status |
|---|---|---|
| `~/.hermes/.env` | API keys | ✅ Gitignored |
| `skills/local/` | Skill injection | ⚠️ Needs review |
| `integrations/` | Third-party code | ⚠️ Needs review |
| `config/` | Config leaks | ✅ Clean |
| Fleet Telemetry | Data exposure | ✅ Local only |

## Findings & Fixes (applied 2026-09-18)

### Critical: Dependabot Vulnerabilities
- 2 critical, 17 high, 10 moderate in PAIOS deps
- **Fix:** `npm audit fix` or update dependencies

### Medium: Unpinned openai version
- `openai==3.14.1` installed by Composio
- **Fix:** Pin to `openai==2.24.0` in Hermes venv

### Low: API keys expired
- All LLM keys (OpenAI, DeepSeek, Gemini) returned 401
- **Fix:** Update keys in `~/.hermes/.env` and re-verify

## Verification

After each fix:
```bash
strix --target ~/paios -m quick
```
Exit code 0 = clean, 2 = vulnerabilities remain

## Pitfalls

- **API keys expire silently** — test with a quick scan before deep scan; a 401 from the LLM means the key is dead, not the tool
- **Docker not installed** — Strix local scans require Docker; install via `winget install Docker.DockerDesktop` then start Docker Desktop
- **Model quality matters** — `google/gemini-2.5-flash` is not recommended; use `openai/gpt-5.4`, `deepseek/v4-flash`, or `gemini/gemini-3.6-flash`
- **Strix runs interactively by default** — always use `-n` flag for headless/non-interactive mode