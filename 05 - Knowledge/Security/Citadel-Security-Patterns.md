---
title: "Citadel — Reusable Security-Engineering Patterns"
version: "1.1"
status: "Reviewed"
date: "2026-08-05"
tags:
  - paios/knowledge
  - paios/security
  - paios/software-development
related:
  - "../../02 - Projects/Active/Citadel/README.md"
  - "Security-Checklist.md"
  - "Penetration-Testing.md"
  - "../Software-Development/Security.md"
  - "../References/Lessons-Ledger.md"
  - "../Architecture/SECURITY_ARCHITECTURE.md"
---

# Reusable Security-Engineering Patterns (learned from Citadel)

> Proven in the Citadel project (74/74 tests, live 14/14 self-check). These are
> patterns any future project — web app, API, or desktop tool — can reuse.

## 1. Fail-Closed Watchdog

- **Pattern:** a health watchdog flips the whole guard to `DEGRADED` when a
  critical invariant breaks (e.g., the audit store becomes unwritable). In
  DEGRADED, mutating endpoints return `503` instead of continuing silently.
- **Rule:** *never fail open on a security-critical dependency.* If you cannot
  record the security decision, refuse the action.
- **Citadel reference:** `citadel/health.py`.

## 2. Tamper-Evident Audit Chain

- **Pattern:** append-only hash chain. Each entry:
  `entry_hash = SHA-256(parent_hash || payload_hash || seq)`. The tip is
  HMAC-signed with a server-side key. A verify endpoint recomputes and reports
  the chain state.
- **Rule:** *detection beats prevention when both are impossible.* You cannot
  always stop an attacker, but you can make silent modification detectable.
- **Citadel reference:** `citadel/audit.py`.

## 3. Enforce with Code, Advise with a Model

- **Pattern:** enforcement and self-verification are deterministic code; any
  LLM is strictly advisory, read-only, instruction-neutralized. The model can
  never gate a security decision.
- **Rule:** *never let learned behaviour make an access-control decision.*
  Keep the model behind a sanitized advisory-only boundary.
- **Citadel reference:** `citadel/analyst.py` (local deterministic fallback).

## 4. WAF = Inspection at a Single Chokepoint

- **Pattern:** one request pipeline: rate limit → blocklist → WAF → auth →
  CSRF → health gate → authorization. Signature + heuristic rules with
  iterative URL-decoding (catch double-encoding).
- **Rule:** *inspect at the edge, decode iteratively, and know exactly which
  rule fired.*
- **Citadel reference:** `citadel/core.py`, `citadel/inspection.py`.

## 5. MFA with Brute-Force Lockout + Replay Protection

- **Pattern:** TOTP (RFC 6238) with a time window, per-user lockout, per-IP
  rate limit, and replay detection. Loopback/local addresses are **never**
  auto-blocked so an operator can never lock their own machine out.
- **Rule:** *MFA is only strong if an attacker cannot brute-force it and a
  stolen code cannot be reused.*
- **Citadel reference:** `citadel/authn.py`.

## 6. Loopback-Only, Userland, Non-Kernel Security Tooling

- **Pattern:** a security console bound only to `127.0.0.1`, running as a
  normal process with no kernel driver, no process injection, no network
  interception.
- **Rule:** *if your tool must run on the machine it protects, keep it
  userland and invisible to other software — it avoids breaking games,
  anti-cheat, and DRM, and it uninstalls cleanly.*
- **Citadel reference:** `run.py` (binds `127.0.0.1` only).

## 7. Passive, Legal Network Visibility

- **Pattern:** read the OS ARP cache (passive) + a single ICMP ping to the
  local gateway. Never probe neighbours, never scan other networks.
- **Rule:** *scanning/collecting/blocking devices on networks you do not own
  is unlawful; build the legal equivalent instead and document the scope
  limit.*
- **Citadel reference:** `citadel/netmon.py` (never egresses the LAN).

## 8. Deterministic Health Score

- **Pattern:** one 0–100 score = weighted factors (audit integrity, chain
  verification, self-check, 2FA coverage, network posture), each with an
  explainer of exactly what is dragging it down.
- **Rule:** *a number without an explainer is a dashboard lie. Show the
  operator what changed and why.*
- **Citadel reference:** `citadel/health.py`.

## 9. TLS-by-Default (never a plaintext foot-gun)

- **Pattern:** the HTTP layer already supports TLS; `serve()` wires certs
  through. Any non-loopback binding without explicit certs auto-generates a
  self-signed pair (bundled crypto lib), so a "let me expose this" mistake can
  never ship plaintext.
- **Rule:** *secure defaults, not optional extras.* Loopback stays HTTP by
  design; the moment you leave the loop you are HTTPS.
- **Citadel reference:** `run.py::_ensure_tls`, `citadel/web/server.py`.

## 10. HMAC-Signed Webhook Alerting

- **Pattern:** the single event funnel (`EventBus.record`) fans out to a
  notifier that forwards sanitized high-severity/lockout/flagged/chain events
  to a webhook. Body is HMAC-SHA256-signed with a shared secret; delivery runs
  on a daemon thread so it can never block the audit write path.
- **Rule:** *alerting turns a "nice log" into an early warning — but a failing
  subscriber must never break the primary write path.*
- **Citadel reference:** `citadel/alerts.py`.

## 11. Off-Host Chain-Tip Mirror

- **Pattern:** the HMAC-signed audit chain tip is written to a second path on
  every append. Truncating or rewriting the DB tail no longer destroys the
  evidence, because the off-host tip proves what the chain's last entry was.
- **Rule:** *tamper evidence only survives if it is not stored beside the thing
  it protects.* Mirror the tip outside the app directory (or a second machine).
- **Citadel reference:** `citadel/audit.py::_mirror_tip` (`CITADEL_TIP_EXPORT`).

## 12. Offline Breached-Password + Session Idle/Expiry

- **Pattern:** (a) an optional local file of SHA-1 breached-password hashes is
  checked at set-password time (never sent anywhere); (b) sessions carry an
  absolute lifetime plus an idle timeout, and idle sessions are *revoked*, not
  just rejected.
- **Rule:** *weak-but-technically-valid passwords are still weak; a session that
  sits idle is a standing credential. Kill it.*
- **Citadel reference:** `citadel/crypto.py`, `citadel/authn.py`
  (`CITADEL_BREACH_FILE`, `CITADEL_SESSION_TTL`, `CITADEL_SESSION_IDLE_TTL`).

## When to Reach for These

| You are building… | Use |
|---|---|
| Any app handling sensitive actions | Fail-closed watchdog + audit chain + MFA lockout |
| An API or web endpoint | Single-chokepoint WAF + iterative decode + rate limit |
| A local/desktop tool | Loopback-only, userland, passive network visibility |
| Anything with an LLM | Deterministic enforcement + advisory-only model |
| Something you will expose on a network | TLS-by-default + HMAC-signed alerting |
| Anything with an audit trail | Off-host chain-tip mirror |
| Anything with user accounts | Offline breached-password + session idle/expiry |
