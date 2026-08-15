---
tags:
  - paios/knowledge
  - paios/security
  - paios/testing
related:
  - "Security-Checklist.md"
  - "../DevOps/06-Security.md"
  - "../Software-Development/Testing-Lifecycle.md"
  - "../Architecture/SECURITY_ARCHITECTURE.md"
  - "../Software-Development/Security.md"
---

# Penetration Testing

## When to Pentest
- Before any public launch (Phase 4 in Project-Phases)
- After major architecture changes
- Annually for active applications
- After a security incident

## Pentest Methodology (PTES-aligned)

### 1. Reconnaissance (passive + active)
- Subdomain enumeration (Sublist3r, Amass)
- Technology fingerprinting (Wappalyzer, WhatWeb)
- Endpoint discovery (crawler, Wayback Machine)
- Open ports and services (Nmap)

### 2. Threat Modeling
- Identify assets, threat actors, attack vectors
- STRIDE per component (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation)
- Data flow diagrams with trust boundaries

### 3. Vulnerability Analysis
- Automated scanning (OWASP ZAP, Nessus, Nikto)
- Manual verification (false positive elimination)
- Dependency vulnerability check (npm audit, pip audit, Dependabot)

### 4. Exploitation (ethical, controlled)
- Web: SQL injection, XSS, CSRF, SSRF, IDOR, file upload abuse
- API: broken auth, mass assignment, rate limit bypass, injection
- Auth: JWT weaknesses, session fixation, OAuth misconfiguration
- Network: exposed services, default creds, unencrypted traffic

### 5. Post-Exploitation
- What access was gained
- What data could be extracted
- Pivot potential (can we reach other systems?)

### 6. Reporting
- Executive summary (non-technical, business risk)
- Technical findings (vulnerability, impact, reproduction steps, CVSS score)
- Remediation guidance per finding (immediate fix + long-term solution)
- Screenshots/PoC videos as evidence

## Tools Reference
| Tool | Purpose |
|------|---------|
| Burp Suite / OWASP ZAP | Web app proxy + scanner |
| Nmap | Network discovery |
| Nuclei | Template-based scanning |
| SQLmap | SQL injection automation |
| John / Hashcat | Password cracking |
| Metasploit | Exploitation framework |
| Semgrep / CodeQL | SAST (source code) |
| Dependabot / Snyk | Dependency scanning |

## Common Web Vulns (OWASP Top 10 prioritized)
1. Broken Access Control (IDOR, privilege escalation)
2. Cryptographic Failures (no HTTPS, weak hashing)
3. Injection (SQL, NoSQL, OS command)
4. Insecure Design (missing threat modeling)
5. Security Misconfiguration (default creds, verbose errors)
6. Vulnerable Components (outdated libraries)
7. Auth Failures (weak passwords, no MFA)
8. Data Integrity Failures (no CSRF, unsigned JWTs)
9. Logging & Monitoring Failures (no audit trail)
10. SSRF (server-side request forgery)
