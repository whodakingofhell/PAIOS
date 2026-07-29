# 06 — Security

> Section 06 of the AI Engineering OS

---

## Purpose

Establishes the **security posture, threat model, compliance requirements, and incident response plan** for all systems. Ensures every component — from pipeline scripts to n8n workflows to YouTube uploads — is built with security by default.

---

## Owner Team

**Security Team** (`Team\Security.md`) — Cybersecurity Engineer, SOC Analyst, Threat Hunter, Pen Tester, Compliance Officer

---

## Key Responsibilities

- Define and enforce the **threat model** for all systems.
- Ensure **OWASP Top 10** compliance for any web-facing component.
- Manage **secrets lifecycle** — creation, rotation, storage, revocation.
- Design **authentication and authorization** patterns.
- Enforce **encryption standards** (at rest and in transit).
- Maintain **audit trails** for all sensitive operations.
- Operate **incident response** procedures.
- Conduct periodic **security reviews** at both QA gates.

---

## Threat Model

### Assets

| Asset | Data Class | Threat |
|---|---|---|
| YouTube channel access | High (revenue-generating) | Account takeover, credential theft |
| API keys (Gemini, Claude, ElevenLabs, YouTube) | High (service access) | Key leakage, unauthorized usage, quota abuse |
| Content pipeline | Medium (intellectual property) | Data tampering, pipeline injection |
| Obsidian knowledge base | Medium (competitive intel) | Unauthorized access, data loss |
| n8n orchestration | High (controls all automation) | Workflow tampering, secret extraction |
| GitHub repositories | Medium (source code + secrets) | Secret scanning gaps, dependency attacks |
| Viewer analytics data | Low (aggregated, non-PII) | Data leakage |

### Threat Categories

| Category | Example | Mitigation |
|---|---|---|
| **Credential theft** | Phishing, key logging | Hardware key (YubiKey) for YouTube/GitHub; secrets in `.env` only |
| **Secret leakage** | Keys in code/logs/commits | Pre-commit hooks (detect-secrets); git-secrets; never log keys |
| **API abuse** | Unauthorized usage of paid tiers | Rate limiting; quota monitoring in n8n; alerts on threshold |
| **Supply chain** | Malicious dependencies | Dependabot alerts; lock files; pin versions |
| **Pipeline injection** | Malicious intake files | Sandboxed processing; file type validation; no code execution from intake |
| **Data loss** | Disk failure, accidental deletion | Git versioning + Obsidian backups; structured backups of pipeline state |
| **Insider threat** | Unauthorized internal access | Least privilege; role-based access; audit trails |

---

## OWASP Top 10 Compliance

For any web-facing component (Vercel-hosted pages, APIs):

| # | OWASP Category | Our Mitigation |
|---|---|---|
| A01 | Broken Access Control | Auth required on all non-public endpoints; RBAC |
| A02 | Cryptographic Failures | TLS 1.3 everywhere; AES-256 for secrets; never store plaintext |
| A03 | Injection | Parameterized queries; input validation; no eval/exec |
| A04 | Insecure Design | Threat modeling; security at architecture stage; secure defaults |
| A05 | Security Misconfiguration | No default credentials; harden Docker; disable unused ports |
| A06 | Vulnerable Components | Dependabot; lock files; no unpinned dependencies |
| A07 | Auth Failures | MFA on all accounts; strong password policy; session management |
| A08 | Software/Data Integrity | Signed commits; pin Docker images; verify checksums |
| A09 | Logging/Monitoring Failures | Audit logs on all sensitive ops; Slack alerts on anomalies |
| A10 | SSRF | No user-supplied URLs to internal services; allow-list approach |

---

## Secrets Management

### Rules (non-negotiable)

1. **All secrets in `.env` files.** Never in code, never in commits, never in logs.
2. **`.env` is gitignored.** Enforced by `.gitignore` + pre-commit hook.
3. **No secret in n8n workflow JSON.** Workflows reference `{{$env.KEY_NAME}}`.
4. **Key rotation schedule.** YouTube OAuth: 90 days. API keys: 180 days. Slack webhooks: 365 days.
5. **Least privilege per key.** Each key has minimum required scopes.
6. **No secrets in Obsidian vault** (it's markdown, searchable — keep keys out).
7. **Post-mortem on any leak.** If a secret is accidentally committed, rotate immediately and document.

### Secrets Inventory Template

| Secret | Service | Scopes | Rotation | Owner |
|---|---|---|---|---|
| `YOUTUBE_CLIENT_SECRET` | YouTube Data API v3 | upload, analytics | 90 days | DevOps |
| `GEMINI_API_KEY` | Google AI | generate, chat | 180 days | AI Eng |
| `CLAUDE_API_KEY` | Anthropic | messages, code | 180 days | AI Eng |
| `ELEVENLABS_API_KEY` | ElevenLabs | tts | 180 days | Automation |
| `SLACK_WEBHOOK_URL` | Slack | post messages | 365 days | DevOps |
| `PERPLEXITY_API_KEY` | Perplexity | search | 180 days | AI Eng |
| `GITHUB_TOKEN` | GitHub | repo, actions | 90 days | DevOps |

---

## Authentication & Authorization

| System | Auth Method | Notes |
|---|---|---|
| YouTube | OAuth 2.0 + MFA | Service account for uploads; personal account for management |
| n8n | Username + password + MFA | Local network only or VPN if remote |
| GitHub | SSH key + MFA | Signed commits (GPG or SSH) |
| Vercel | GitHub SSO | No standalone credentials |
| Obsidian | Local only | No remote auth needed |
| AI APIs | API key in header | Each key scoped to minimum permissions |

---

## Encryption Standards

| Data State | Standard | Where Applied |
|---|---|---|
| In transit | TLS 1.3 | All API calls, web traffic, n8n webhooks |
| At rest | AES-256 | Disk encryption (BitLocker/FileVault); encrypted backups |
| Secrets | AES-256 via env | `.env` files on encrypted disks; never in plaintext logs |

---

## Audit Trail

All sensitive operations are logged:

| Operation | Logged Fields | Retention |
|---|---|---|
| Pipeline stage execution | Stage ID, input hash, output hash, status, duration, timestamp | 90 days |
| YouTube upload | Video ID, title, status, timestamp, API response code | Indefinite |
| API key usage | Key ID (partial), request count, error count, timestamp | 30 days |
| n8n workflow modification | Workflow ID, modifier, change summary, timestamp | Indefinite |
| Git push | Commit SHA, author, branches affected, timestamp | Indefinite |

---

## Incident Response Plan

### Severity Levels

| Level | Definition | Response Time | Escalation |
|---|---|---|---|
| **CRITICAL** | Secret leaked publicly; YouTube channel compromised | Immediate (<15 min) | CTO + full team |
| **HIGH** | Pipeline injecting bad content; API key used unauthorized | <1 hour | Security lead + affected team |
| **MEDIUM** | Dependency vulnerability discovered; quota exhausted | <24 hours | Affected team lead |
| **LOW** | Audit anomaly; backup failed | <1 week | On next sprint |

### Response Steps

1. **Detect** — Alert from monitoring or manual discovery.
2. **Contain** — Rotate secrets, pause pipeline, revoke access.
3. **Assess** — Determine scope and impact.
4. **Remediate** — Fix the root cause, not just the symptom.
5. **Review** — Post-mortem within 48 hours; document in `Project\Security.md`.
6. **Prevent** — Update threat model, add monitoring, adjust process.

---

## Inputs

- Architecture decisions (`03-Architecture\Architecture.md`)
- Tool configurations (`integrations\*`)
- Pipeline specifications (`Frameworks\Content-Pipeline.md`)

---

## Outputs

- This security document (source of truth for all security decisions)
- Threat model with asset inventory
- Secrets inventory with rotation schedule
- Incident response records
- Security review reports (per QA gate)

---

## Operating Principles

1. **Security by default.** Every system starts secure. You don't "add security later."
2. **Least privilege.** Every key, account, and role has the minimum permissions needed.
3. **Assume breach.** Design as if credentials will leak. Detect quickly, respond fast.
4. **Secrets are ephemeral.** Rotate on schedule. Revoke when no longer needed.
5. **Audit everything sensitive.** If it touches money, content, or access, it's logged.

---

## Acceptance Criteria

- [ ] Threat model covers all identified assets with threats and mitigations.
- [ ] OWASP Top 10 mitigations are documented for each category.
- [ ] Secrets management rules are ≤7, clear, and enforceable.
- [ ] Secrets inventory template is defined with rotation schedule.
- [ ] Authentication method is specified for every system.
- [ ] Incident response plan has 4 severity levels with response times.
- [ ] Audit trail specifies what's logged, where, and for how long.

---

## Appendix A: Workstation Security Hardening Guide

> **Applies to every developer workstation in the organization.**
> Based on real-world vulnerability assessment conducted 2026-07-18.

### A.1 Initial Security Audit Checklist

Run this on every new workstation or quarterly:

| Check | Command / Action | Pass Criteria |
|-------|------------------|---------------|
| Antivirus real-time protection | `Get-MpComputerStatus \| Select RealTimeProtectionEnabled` | True |
| Windows Firewall all profiles | `Get-NetFirewallProfile \| Select Name, Enabled` | All True |
| Tamper protection | `Get-MpComputerStatus \| Select IsTamperProtected` | True |
| UAC enabled | `(Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System).EnableLUA` | 1 |
| No unauthorized remote access | Check for AnyDesk, TeamViewer, VNC, LogMeIn running | None unapproved |
| No exposed database ports | `netstat -ano \| findstr ":3306 :5432 :27017"` | Should not show 0.0.0.0 |
| No exposed SMB/RDP | Verify firewall rules for ports 445, 3389 | No inbound allow rules |
| Microsoft account + PIN | Check Settings > Accounts > Sign-in options | PIN required |
| BitLocker encryption | `Get-BitLockerVolume -MountPoint "C:"` | EncryptionPercentage ≥ 100 |
| DNS not hijacked | `Get-DnsClientServerAddress -AddressFamily IPv4` | Should use 1.1.1.1, 8.8.8.8, or org-approved |

### A.2 Firewall Hardening Procedure

If a service must listen on a network port, it should bind to **127.0.0.1** unless remote access is explicitly required.

#### For MySQL / MariaDB:
1. Open `C:\ProgramData\MySQL\MySQL Server 8.0\my.ini`
2. Find the `[mysqld]` section and set/add: `bind-address = 127.0.0.1`
3. Restart service: `Restart-Service MySQL80`
4. If that changes require a production deployment that needs remote MySQL, use an **SSH tunnel** or **VPN** — never expose directly.

#### For any service bound to 0.0.0.0 unnecessarily:
1. Identify: `netstat -ano | findstr "LISTENING"` and match PIDs to processes
2. Block at firewall as last resort: `Disable-NetFirewallRule -Name <RuleName>`
3. Better: reconfigure the service to bind localhost

#### Automated Firewall Audit (PowerShell):
```powershell
# Find all listening ports and their public accessibility
netstat -ano | Select-String "0.0.0.0:" | ForEach-Object {
    if ($_ -match '0\.0\.0\.0:(\d+)') { $port = $matches[1] }
} | Sort-Object -Unique | ForEach-Object {
    Write-Warning "Port $_ is bound to ALL interfaces — investigate"
}
```

### A.3 Account Security

- **Local accounts must have passwords.** Zero exceptions.
- Microsoft accounts (Windows 11) with **PIN + TPM** are acceptable — the PIN is hardware-bound and cannot be cracked offline.
- **Guest account must be disabled.** Verify: `Get-LocalUser Guest | Select Enabled`
- **Built-in Administrator must be disabled.** Verify: `Get-LocalUser Administrator | Select Enabled`
- **Remove unused accounts.** Sandbox/development accounts (CodexSandbox, etc.) should be disabled when not in active use.

### A.4 Application Hardening

| Application | Setting | Why |
|-------------|---------|-----|
| AnyDesk / Remote Access | Disable firewall allow rules; run behind VPN only | Most common ransomware entry vector |
| Browser | Enable "Always use secure connections" (HTTPS-Only Mode) | Prevents downgrade attacks |
| Browser | Disable saved passwords; use a password manager instead | Stored passwords are plaintext-accessible locally |
| MySQL / PostgreSQL | Bind to 127.0.0.1 only | Prevents network-based attacks |
| Node.js / Dev servers | Use `--host 127.0.0.1` explicitly, not `0.0.0.0` | Prevents local network access |
| Docker | Review published ports; never use `--network host` without firewall | Container breakout risk |

### A.5 Controlled Folder Access (Ransomware Protection)

Enable and configure for all workstations:

```powershell
# Enable Controlled Folder Access (requires admin)
Set-MpPreference -EnableControlledFolderAccess Enabled

# Add game & dev directories to allowed apps
Add-MpPreference -ControlledFolderAccessAllowedApplications "C:\Program Files (x86)\Steam\Steam.exe"
Add-MpPreference -ControlledFolderAccessAllowedApplications "C:\Program Files (x86)\Ubisoft\Ubisoft Connect.exe"
# Add any other game launchers or code editors
```

If a legitimate app gets blocked, check: `Settings > Privacy & Security > Windows Security > Virus & threat protection > Ransomware protection > Allow an app through Controlled folder access`

### A.6 Recommended Security Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Antivirus | Microsoft Defender (built-in) | Real-time, cloud-delivered, tamper-proof |
| Firewall | Windows Firewall (built-in) | All 3 profiles enabled by default |
| DNS | Cloudflare 1.1.1.1 / 1.0.0.1 | Encrypted, private, fast |
| Disk encryption | BitLocker (built-in) | AES-256, TPM-bound, zero performance impact |
| Password manager | Bitwarden / 1Password | Encrypted vault, MFA support |
| VPN (optional) | WireGuard / Tailscale | Zero-trust network access |
| Browser security | uBlock Origin + HTTPS-Only Mode | Blocks trackers, forces TLS |

### A.7 Periodic Maintenance (Quarterly)

```powershell
# 1. Update signatures
Update-MpSignature

# 2. Run quick scan
Start-MpScan -ScanType QuickScan

# 3. Check for pending updates
# Use Windows Settings > Windows Update

# 4. Review firewall rules
Get-NetFirewallRule -Direction Inbound -Enabled True | Select DisplayName

# 5. Check installed remote access software
Get-WmiObject Win32_Product | Where-Object Name -match 'AnyDesk|TeamViewer|VNC|LogMeIn'

# 6. Audit listening ports
netstat -ano | Select-String LISTENING

# 7. Verify user accounts
Get-LocalUser | Where-Object Enabled -eq $true | Select Name, PasswordRequired, LastLogon

# 8. Check startup programs
Get-CimInstance Win32_StartupCommand | Select Name, Command
```

### A.8 Incident Response for Individual PC

| Event | Action |
|-------|--------|
| Suspect malware | Run Defender offline scan: `Start-MpScan -ScanType FullScan` |
| Unknown listening port | `Get-Process -Id <PID>` to identify, then `netstat -bano` for the binary |
| Unexpected firewall rule | `Get-NetFirewallRule -Name <RuleName> \| fl` to inspect, delete if unauthorized |
| Account compromised | Immediately change Microsoft password, revoke all sessions, enable MFA |
| Data breach suspicion | Run full antivirus scan, change all passwords, check for unauthorized access

---

## Cross-References

| Document | Relationship |
|---|---|
| `03-Architecture\Architecture.md` | Architecture is designed with security constraints |
| `04-Engineering\Engineering.md` | Engineering implements security standards |
| `05-Quality-Assurance\QA-Framework.md` | Security is a hard gate at both QA gates |
| `07-Automation\Automation.md` | Automation workflows must follow security rules |
| `Project\Security.md` | Per-project security spec |
| `integrations\*` | Per-tool security setup notes |
