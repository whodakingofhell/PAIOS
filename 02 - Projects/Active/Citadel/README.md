---
title: "Citadel — Self-Monitoring Security Console"
version: "2.0"
status: "Active"
date: "2026-08-02"
tags:
  - project
  - security
  - citadel
  - paios/projects
  - paios/project/citadel
  - paios/security
owner: "OpenCode"
canonical: true
related:
  - "../../../05 - Knowledge/Security/Citadel-Security-Patterns.md"
  - "../../../05 - Knowledge/Security/Security-Checklist.md"
  - "../../../05 - Knowledge/References/Lessons-Ledger.md"
---

# Citadel — Self-Monitoring Security Console

> Status: **Working prototype, tested and hardened.** A self-monitoring zero-trust security control plane built in pure Python 3.14 + `cryptography`. No frameworks, no internet dependency, no kernel-level code.

**One-liner:** Citadel is a web app that watches its own front door — every request is inspected by an OWASP-aligned WAF, authenticated with scrypt + TOTP MFA, authorized through RBAC with just-in-time elevation, and written to a tamper-evident SHA-256 audit chain — then it periodically re-attacks itself with the same payloads it is built to stop, and proves it.

## Quick Facts

| Item | Value |
|---|---|
| Language | Python 3.14 standard library + `cryptography` |
| Interface | Web UI + JSON API, loopback-only `http://127.0.0.1:8443` |
| Deployment | Windows scheduled task `CitadelGuard` via `start-citadel.ps1` |
| Tests | 68/68 unit/integration passing; live self-check 14/14 controls |
| Code | `C:\Users\My PC\OneDrive\Desktop\AI PROJECTS\citadel\` |
| GitHub | `https://github.com/whodakingofhell/Citadel` |
| Docs | `README.md`, `USER_GUIDE.md`, `SECURITY_ANALYSIS.md` (in the repo) |

## What It Does (plain language)

1. **Watches the door** — the WAF blocks the top web attack classes (SQLi, XSS, path traversal, command injection, SSTI, XXE/SSRF, sensitive-file access, scanner UAs, prototype pollution).
2. **Watches the room** — reads the OS ARP cache and shows which devices are on the local network, identifying each device's maker from its MAC address (official IEEE OUI data) and auto-recognising the router so it is never a false alarm.
3. **Keeps a diary that cannot be silently edited** — every sign-in, block, and change is chained in a SHA-256 audit log with an HMAC-signed tip; if someone alters a past entry, the chain verification detects it.
4. **Proves itself** — a 14-check self-attack suite runs hourly and reports the results (fail-closed `DEGRADED` state if the audit store is unwritable).

## Security Model

- **Trust boundary:** the application process is trusted; everything outside it is untrusted.
- **Enforcement is deterministic code**, never learned behavior, never delegated to a model. The optional LLM analyst is strictly read-only advisory output.
- **MFA everywhere:** TOTP (RFC 6238) with brute-force lockout + replay protection, per-IP rate limiting, loopback never self-locks (the operator can never lock this computer out of its own guard).
- **Fail closed:** if the audit store becomes unwritable the guard suspends mutating actions (`503 DEGRADED`) rather than continuing in a broken state.
- **Passive, legal network visibility:** reads the ARP cache only (one ICMP ping to the local gateway). It does not probe neighbours, intercept traffic, or block devices.

## Safety on This Machine

- Userland Python process, loopback-bound only; **no kernel driver** (unlike Riot Vanguard), no process injection, no network interception, no overlay/input capture — it does not conflict with Steam Guard, Valorant/Vanguard, or any anti-cheat/DRM.
- Monitors **only while its scheduled task is running**; it is not an always-on background service and does not survive a reboot on its own.
- Writes only inside its own `data/` directory; nothing destructive.

## Current Status (2026-08-02)

- Live-verified end-to-end: passwordless TOTP login, Self-Check button (14/14), AI advisor (local fallback engine), network refresh showing 9 identified devices, audited resolution of all high-severity findings.
- Guard Health Score: 85/Good (25 audit + 25 integrity + 20 self-check + 15 2FA + 0/15 network until the operator marks their own devices as "mine").
- Known next steps: mark own devices as recognised to reach 100; roadmap in the repo's `SECURITY_ANALYSIS.md` §8.7 (off-host chain-tip export, TLS-by-default, alerting).

## Knowledge Cross-References

- Reusable security-engineering patterns: [[../../../05 - Knowledge/Security/Citadel-Security-Patterns.md]]
- General security checklist: [[../../../05 - Knowledge/Security/Security-Checklist.md]]
- Lessons learned ledger: [[../../../05 - Knowledge/References/Lessons-Ledger.md]]
- Project hub: [[../../Projects-MOC]]
