# Philippine Skyland — Security Assessment

> Security posture and compliance report for PPSMDO platform

---

## Security Layers Implemented

### Layer 1: Content Security Policy (CSP)
- **Header**: `Content-Security-Policy`
- **Policy**: `default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; connect-src 'self' https://neon.tech; font-src 'self' data:; frame-ancestors 'none'; base-uri 'self'; form-action 'self'`
- **Protects**: XSS, code injection, data exfiltration
- **Status**: PASS — deployed via vercel.json

### Layer 2: HTTP Strict Transport Security (HSTS)
- **Header**: `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`
- **Protects**: Protocol downgrade attacks, SSL stripping
- **Status**: PASS — 2-year max-age with preload directive

### Layer 3: Clickjacking Protection
- **Header**: `X-Frame-Options: DENY`
- **Also**: CSP `frame-ancestors 'none'`
- **Protects**: Clickjacking attacks
- **Status**: PASS

### Layer 4: MIME Type Protection
- **Header**: `X-Content-Type-Options: nosniff`
- **Protects**: MIME-type sniffing attacks
- **Status**: PASS

### Layer 5: Rate Limiting
- **Implementation**: In-memory sliding window per IP + path
- **Configurations**:
  | Name | Window | Max Requests | Purpose |
  |------|--------|-------------|---------|
  | authLimiter | 15 min | 10 | Brute-force login + password change prevention |
  | apiLimiter | 1 min | 60 | API abuse prevention |
  | contactLimiter | 1 hr | 5 | Spam prevention |
  | registerLimiter | 1 hr | 3 | Mass account creation prevention |
- **Response**: HTTP 429 with Retry-After, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset headers
- **Cleanup**: Stale entries purged every 10 minutes
- **Status**: PASS

### Layer 6: Password Hashing
- **Algorithm**: bcrypt
- **Rounds**: 12
- **Protects**: Password leakage in database breach
- **Status**: PASS

### Layer 7: JWT Session Management
- **Expiry**: 7 days
- **Cookie prefix**: `__Secure-` (production)
- **Flags**: httpOnly, secure, sameSite: lax, path: /
- **Inactivity Timeout**: 30 minutes with 60-second warning
- **Tab Close Detection**: `beforeunload` event prompt
- **Protects**: Session hijacking, CSRF, abandoned sessions
- **Status**: PASS

### Layer 8: Role-Based Access Control (RBAC)
- **Roles**: BROKER, APPRAISER, CLIENT, ADMIN
- **Enforcement**: Middleware + API route checks
- **Protected routes**: /dashboard/*, /api/transactions, /api/appraisals, /api/properties (POST)
- **Image Upload**: Broker owner + ADMIN only
- **Status**: PASS

### Layer 9: Input Validation
- **Library**: Zod
- **Coverage**: All API endpoints validate request body
- **Schema types**: String, email, enum, number, URL
- **Password Validation**: 8+ chars, uppercase, lowercase, number, special char
- **Property creation**: Zod propertySchema validates all fields including type enum, price bounds, and location requirements
- **Status**: PASS

### Layer 10: CORS + User-Agent Filtering
- **CORS**: Origin validation on API routes
- **User-Agent**: Blocked if missing or < 5 characters
- **Exclusion**: /api/auth/* routes skip UA check
- **Status**: PASS

### Layer 11: DB Audit Trail
- **Implementation**: PostgreSQL AuditLog table
- **Fields**: userId, action, resource, resourceId, details, ipAddress, userAgent, createdAt
- **Coverage**: All security events, authentication attempts, data modifications
- **PII Protection**: IP addresses hashed before logging, sensitive fields redacted
- **Status**: PASS

---

## Additional Security Headers

| Header | Value | Purpose |
|--------|-------|---------|
| Permissions-Policy | camera=(), microphone=(), geolocation=(), payment=() | Feature abuse prevention |
| Referrer-Policy | strict-origin-when-cross-origin | Information leakage prevention |
| Cross-Origin-Opener-Policy | same-origin | Spectre attack prevention |
| Cross-Origin-Resource-Policy | same-origin | Cross-origin resource theft |
| Cross-Origin-Embedder-Policy | credentialless | Side-channel attack prevention |
| X-Request-Id | UUID per request | Request tracing |

---

## Secrets Management

| Secret | Storage | In Code | In .gitignore |
|--------|---------|---------|---------------|
| DATABASE_URL | Vercel Dashboard | NO | YES (.env) |
| NEXTAUTH_SECRET | Vercel Dashboard | NO | YES (.env) |
| JWT_SECRET | Vercel Dashboard | NO | YES (.env) |
| HMAC_SECRET | Vercel Dashboard | NO | YES (.env) |
| SMTP_USER | Vercel Dashboard | NO | YES (.env) |
| SMTP_FROM | Vercel Dashboard | NO | YES (.env) |

**.env.example**: Contains placeholder values with generation instructions only.

---

## OWASP Top 10 Compliance

| Risk | Status | Mitigation |
|------|--------|-----------|
| A01 Broken Access Control | PASS | RBAC + middleware + API checks + image upload restrictions + reviews now require authentication |
| A02 Cryptographic Failures | PASS | bcrypt 12, HTTPS, __Secure- cookies |
| A03 Injection | PASS | Zod validation + parameterized queries (Prisma) |
| A04 Insecure Design | PASS | Security-by-default architecture |
| A05 Security Misconfiguration | PASS | vercel.json headers, no debug in prod |
| A06 Vulnerable Components | PASS | npm audit, overrides for postcss/sharp/nodemailer |
| A07 Auth Failures | PASS | Rate limiting + bcrypt + JWT + session timeout |
| A08 Data Integrity | PASS | Prisma ORM + input validation |
| A09 Logging Failures | PASS | Request logging + PII redaction |
| A10 SSRF | PASS | CORS + User-Agent filtering |

---

## New Security Features

### Session Timeout (30-min inactivity)
- Inactivity timer resets on: mousedown, mousemove, keypress, scroll, touchstart, click
- Warning modal at 29 minutes with countdown
- Auto-logout at 30 minutes, redirects to /auth/login?reason=timeout
- Tab close detection via `beforeunload` event

### Change Password
- Requires current password verification
- Same strength rules as registration (8+ chars, mixed case, number, special char)
- New password must differ from current
- Rate limited via apiLimiter (60/min)

### July 2026 Security Audit Hardening
- **Reviews POST**: Authentication required (was unauthenticated, allowing fake review injection)
- **Property POST**: Full Zod validation (was using raw body, allowing unvalidated data)
- **Password change**: Rate limit tightened to authLimiter (10/15min, was apiLimiter 60/min)
- **Transaction response**: Internal fields stripped (isVerified, isActive, createdAt, updatedAt)
- **Health endpoint**: Timestamp removed to prevent server time reconnaissance
- **Profile page**: Now fetches from database instead of hardcoded mock data
- **Rate limiter**: Improved IP validation for forwarded-for header chain

### World-Class Security Features (July 23, 2026)

#### Email Verification
- **Mandatory**: All new accounts must verify email before login
- **Token**: Unique verification token stored in database
- **Flow**: Register → Send verification email → Click link → `/api/auth/verify-email` → Account activated
- **Protection**: Prevents fake account creation and ensures valid email addresses

#### Password Reset
- **Secure Tokens**: Cryptographically random tokens with 1-hour expiry
- **Single-Use**: Tokens marked as `isUsed` after successful reset
- **Rate Limited**: 3 requests per hour per email
- **Strength Rules**: Same as registration (8+ chars, uppercase, lowercase, number, special char)
- **Flow**: Forgot Password → Enter email → Receive reset link → Set new password → Login

#### Account Lockout
- **Threshold**: 5 failed login attempts
- **Duration**: 15-minute automatic lockout
- **Tracking**: `failedLoginAttempts` and `lockedUntil` fields on User model
- **Auto-Reset**: Failed attempts cleared on successful login
- **User Feedback**: Specific error messages for locked accounts

#### DB Audit Logging
- **Storage**: PostgreSQL AuditLog table (permanent)
- **Events**: Login attempts, registration, password changes, data modifications
- **Fields**: userId, action, resource, resourceId, details (JSON), ipAddress, userAgent
- **PII Protection**: IP addresses hashed, sensitive fields redacted
- **Fail-Safe**: Console logging continues even if DB write fails

### Property Image Upload (Owner + Admin Only)
- Role check: broker owner (broker.userId === session.user.id) + ADMIN
- File validation: JPEG/PNG/WebP only, 5MB max, 20 images max
- Base64 data URLs stored in property.images JSON field
- Separate POST (upload) and DELETE (remove by index) endpoints

---

## Test Results Summary

| Test | Result | Details |
|------|--------|---------|
| CSP headers | PASS | 10 headers present via vercel.json |
| HSTS | PASS | 2-year max-age with preload |
| Rate limiting | PASS | 429 returned after threshold |
| Auth persistence | PASS | JWT 7-day expiry, Secure cookie |
| RBAC enforcement | PASS | Role checks on all protected routes |
| Input validation | PASS | Zod schemas on all endpoints |
| Password hashing | PASS | bcrypt 12 rounds |
| Secrets exposure | PASS | No hardcoded secrets in source |
| XSS protection | PASS | CSP + React auto-escaping |
| Clickjacking | PASS | X-Frame-Options: DENY |
| CSRF | PASS | SameSite cookies + JWT |
| SSRF | PASS | CORS + origin validation |
| Session timeout | PASS | 30-min inactivity, 60-sec warning |
| Password change | PASS | Current password verified, Zod validation |
| Image upload auth | PASS | Owner + admin check enforced |
| Image upload validation | PASS | File type, size, count limits |
| Chatbot safety | PASS | No external API calls, FAQ-only responses |
| Reviews POST auth | PASS | Authentication required before submission |
| Property POST validation | PASS | Zod schema validates all input |
| Change password rate limit | PASS | Uses authLimiter 10/15min |

**Overall Verdict**: PRODUCTION-READY
