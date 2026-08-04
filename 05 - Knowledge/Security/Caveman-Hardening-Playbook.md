---
title: "Caveman Hardening Playbook"
version: "1.0"
status: "Reviewed"
date: "2026-08-05"
tags:
  - paios/knowledge
  - paios/security
  - paios/software-development
  - paios/playbook
related:
  - "Citadel-Security-Patterns.md"
  - "Security-Checklist.md"
  - "../Software-Development/Security.md"
  - "Penetration-Testing.md"
  - "../../02 - Projects/Active/Citadel/README.md"
---

# Caveman Hardening Playbook

> Terse, proven, copy-pasteable. Benchmark basis: **OWASP CheatSheetSeries**
> (32k★), **OWASP/WSTG**, **NIST CSF**, **CIS 18**. Each step is a *control*
> you can ship in under an hour with stdlib + one crypto lib. All proven in
> the Citadel project (74 tests).

## 0. Rules that cost nothing

1. **Secure defaults, not optional extras.** Loopback = plaintext OK; leave
   loopback = auto-TLS or refuse.
2. **Fail closed.** Can't record the security decision? Refuse the action.
3. **Never send a password anywhere.** Offline checks only.
4. **A failing fan-out must never break the write path.** Deliver on a thread.
5. **A number without an explainer is a dashboard lie.**

## 1. TLS-by-default (≤ 30 min)

- HTTP layer already supports TLS? Wire `tls_cert`/`tls_key` through `serve()`.
- Any non-loopback bind with no certs → auto-generate self-signed via the
  bundled crypto lib (`cryptography.x509`, 2048-bit RSA, 10-yr validity).
- Guard: `if not loopback and no certs: generate(); scheme = https`.
- Result: "let me expose this" can never ship plaintext.
- Citadel: `run.py::_ensure_tls`, `citadel/web/server.py`.

## 2. Tamper-evident chain + off-host tip (≤ 30 min)

- Append-only hash chain: `entry = SHA256(parent || payload_hash || seq)`.
- HMAC-sign the tip with a server key; write it to a *second path outside the
  app dir* on every append.
- Verify endpoint recomputes the chain and compares tip.
- Rule: *evidence only survives if it is not stored beside the thing it
  protects.*
- Citadel: `citadel/audit.py::_mirror_tip` (`CITADEL_TIP_EXPORT`).

## 3. HMAC-signed alerting (≤ 20 min)

- Single event funnel → subscriber filters (severity high/critical OR action
  in `blocked_ip,rate_limited,degraded,chain_failed,flagged`).
- POST sanitized JSON to webhook; `X-Signature = HMAC-SHA256(body, secret)`.
- Daemon thread delivery so the audit path never blocks.
- Citadel: `citadel/alerts.py` (`CITADEL_ALERT_WEBHOOK`, `CITADEL_ALERT_HMAC`).

## 4. Password policy that means it (≤ 15 min)

- scrypt (memory-hard), constant-time compare, never log.
- Length ≥ 12, ≥ 3 of 4 char classes, reject common list.
- Optional offline SHA-1 breach file (`HaveIBeenPwned` format): reject any
  password whose hash is in it. Nothing leaves the machine.
- Citadel: `citadel/crypto.py`, `citadel/authn.py` (`CITADEL_BREACH_FILE`).

## 5. Sessions that die (≤ 15 min)

- Absolute lifetime (revoke at `expires_at`) **and** idle timeout (revoke when
  `last_activity` older than N). Revoke — don't just reject.
- Store only SHA-256 of the token; CSRF token separate.
- Citadel: `citadel/authn.py` (`CITADEL_SESSION_TTL`, `CITADEL_SESSION_IDLE_TTL`).

## 6. MFA that survives brute force (≤ 30 min)

- TOTP (RFC 6238) + replay counter persisted per user (reject equal/older step).
- Per-user lockout + per-IP sliding rate limit.
- **Never auto-block loopback** — a security console must not lock its own
  machine out.
- Citadel: `citadel/authn.py`.

## 7. Post-ship checklist (≤ 10 min)

- `bandit` + `semgrep` SAST on your package.
- `gitleaks`/`trufflehog` secret scan before first push.
- Rerun your full suite after every control; log the count.
- Document the controls in a `SECURITY_ANALYSIS.md` with a roadmap table.
