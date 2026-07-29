---
tags:
  - paios/knowledge
  - paios/security
related:
  - "Penetration-Testing.md"
  - "../DevOps/06-Security.md"
  - "../Software-Development/Security.md"
  - "../Architecture/SECURITY_ARCHITECTURE.md"
  - "../Software-Development/Project-Phases.md"
---

# Security Checklist

## Pre-Development (Phase 0-1)
- [ ] Threat model documented (data flows, trust boundaries)
- [ ] PII inventory: what data is collected, stored, processed
- [ ] Compliance requirements identified (GDPR, CCPA, SOC2, etc.)
- [ ] Third-party security review (vendor risk assessment)
- [ ] Security requirements in user stories

## Development (Phase 3)
- [ ] Input validation on ALL user inputs (server-side)
- [ ] Output encoding (prevent XSS)
- [ ] Parameterized queries (prevent SQL injection)
- [ ] Authentication: bcrypt/argon2 for passwords, MFA where applicable
- [ ] Authorization checks on every endpoint (not just frontend)
- [ ] JWT: short expiry, secure storage (httpOnly cookie), rotation
- [ ] File upload: validate type, size, scan, store outside webroot
- [ ] Rate limiting per endpoint (auth endpoints get stricter limits)
- [ ] CORS whitelist (not wildcard in production)
- [ ] HTTPS enforced (HSTS header, redirect HTTP→HTTPS)
- [ ] Security headers: Content-Security-Policy, X-Frame-Options, X-Content-Type-Options
- [ ] Dependency scanning in CI (fail build on critical vulns)
- [ ] SAST scanning in CI
- [ ] Secrets: environment variables only, never in code/repos
- [ ] Error handling: no stack traces in production responses
- [ ] Logging: auth events, data access, admin actions (immutable logs)

## Pre-Launch (Phase 4-5)
- [ ] Penetration test completed (see Penetration-Testing.md)
- [ ] DAST scan passed (OWASP ZAP)
- [ ] All critical/high findings remediated
- [ ] Vulnerability disclosure policy published
- [ ] Incident response plan documented
- [ ] Backups configured and tested (encrypted, off-site)
- [ ] SSL/TLS configuration verified (SSL Labs A+)
- [ ] DDoS protection (WAF, CDN, rate limiting)
- [ ] Monitoring + alerting for security events

## Maintenance (Phase 6)
- [ ] Regular dependency updates (automated PRs)
- [ ] Quarterly vulnerability scan
- [ ] Annual penetration test
- [ ] Log review (weekly)
- [ ] Access review (quarterly — revoke unused accounts)
- [ ] Incident response drills (annual)
