# Philippine Skyland MGT and DEVT OPC — Architecture

> Architecture document for the PPSMDO real estate broker platform

---

## System Overview

Enterprise-grade real estate platform built with Next.js App Router, Prisma ORM, PostgreSQL (Neon cloud), deployed on Vercel Edge Network.

---

## Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| Framework | Next.js (App Router) | 16.x |
| Language | TypeScript | 5.x |
| UI | React | 18.x |
| Styling | Tailwind CSS | 3.x |
| ORM | Prisma | 5.22 |
| Database | PostgreSQL (Neon) | 16.x |
| Auth | NextAuth.js | 4.24.15 |
| Deployment | Vercel (Serverless) | — |
| Password Hashing | bcrypt | 12 rounds |
| Validation | Zod | 3.x |

---

## Database Schema (13 Models)

```
User (1) ──── (1) BrokerProfile
User (1) ──── (1) AppraiserProfile
User (1) ──── (1) ClientProfile
User (1) ──── (Many) Property
User (1) ──── (Many) Transaction
User (1) ──── (Many) Appraisal
User (1) ──── (Many) Review
User (1) ──── (Many) Inquiry
User (1) ──── (Many) ContactSubmission
User (1) ──── (Many) Session
User (1) ──── (Many) AuditLog
```

### Key Models

- **User**: Core auth model with role (BROKER, APPRAISER, CLIENT, ADMIN), email, hashed password, email verification, account lockout
- **PasswordResetToken**: Secure token-based password reset with 1-hour expiry
- **BrokerProfile**: License info, brokerage name, slug for public profile
- **AppraiserProfile**: License info, specialties, service areas
- **ClientProfile**: Budget range, preferred locations, property preferences
- **Property**: Title, type (13 categories), price, location, images (JSON), status, broker relation
- **Transaction**: Buyer/seller, property, commission, status tracking
- **Appraisal**: Property, appraiser, valuation, status
- **Review**: Client review of broker/appraiser
- **Inquiry**: Property inquiries with contact info
- **ContactSubmission**: General contact form submissions

---

## API Routes (14 Endpoints)

| Route | Methods | Purpose | Rate Limit |
|-------|---------|---------|------------|
| `/api/auth/[...nextauth]` | GET, POST | NextAuth handlers | Skip (auth route) |
| `/api/auth/register` | POST | User registration | 3/hr |
| `/api/auth/verify-email` | GET | Email verification | Skip |
| `/api/auth/forgot-password` | POST | Request password reset | 3/hr |
| `/api/auth/reset-password` | POST | Reset password with token | 3/hr |
| `/api/auth/change-password` | POST | Change user password | 10/15min (authLimiter) |
| `/api/properties` | GET, POST | List/create properties | 60/min |
| `/api/properties/[id]` | POST, DELETE | Upload/delete property images | 60/min |
| `/api/transactions` | GET, POST | List/create transactions | 60/min |
| `/api/appraisals` | GET, POST | List/create appraisals | 60/min |
| `/api/reviews` | GET, POST | List/create reviews | 60/min |
| `/api/contact` | POST | Contact form submission | 5/hr |
| `/api/health` | GET | Health check | 60/min |

---

## Property Categories (13 Types)

| Category | Label | Color |
|----------|-------|-------|
| LOT_ONLY | Lot Only | #22c55e |
| HOUSE_AND_LOT | House and Lot | #0ea5e9 |
| FARM_LOT | Farm Lot | #84cc16 |
| COMMERCIAL | Commercial | #8b5cf6 |
| BEACHFRONT | Beachfront | #06b6d4 |
| CONDOMINIUM | Condominium | #ec4899 |
| TOWNHOUSE | Townhouse | #f59e0b |
| MIXED_USE | Mixed Use | #6366f1 |
| INDUSTRIAL | Industrial | #f97316 |
| LAND | Land | #10b981 |
| RESIDENTIAL | Residential | #3b82f6 |
| CONDO | Condo | #ec4899 |
| APARTMENT | Apartment | #a855f7 |

---

## Search Filters

| Filter | Type | Options |
|--------|------|---------|
| Property Type | Select | 13 categories |
| Budget Range | Select | 7 brackets (Under ₱1M → Over ₱50M) |
| Lot Size | Select | 5 ranges (Under 200sqm → Over 5,000sqm) |
| Bedrooms | Select | Any, 1+, 2+, 3+, 4+, 5+ |
| Bathrooms | Select | Any, 1+, 2+, 3+, 4+ |
| City | Text | Free text search |
| Province | Text | Free text search |
| Query | Text | Title, description, address, city |

---

## Authentication Flow

1. User submits credentials to `/api/auth/callback/credentials`
2. NextAuth validates email + bcrypt password hash
3. JWT token generated with 7-day expiry
4. Session cookie set with `__Secure-` prefix (production)
5. `getServerSession()` checks JWT on every request
6. Role-based access enforced in API routes and pages
7. Session timeout: 30-min inactivity with 60-sec warning countdown

---

## Security Architecture (11 Layers)

| # | Layer | Implementation |
|---|-------|---------------|
| 1 | CSP | vercel.json Content-Security-Policy header |
| 2 | HSTS | 2-year max-age + includeSubDomains + preload |
| 3 | Clickjacking | X-Frame-Options: DENY |
| 4 | MIME sniffing | X-Content-Type-Options: nosniff |
| 5 | Rate limiting | Sliding window per IP + path, authLimiter for login/password change |
| 6 | Password hashing | bcrypt 12 rounds |
| 7 | JWT sessions | 7-day expiry, __Secure- prefix, httpOnly |
| 8 | RBAC | Role checks on all protected routes |
| 9 | Input validation | Zod schemas on all endpoints |
| 10 | CORS + UA filter | User-Agent validation on API routes |
| 11 | DB Audit Trail | Security events stored in PostgreSQL AuditLog table |

Additional: Permissions-Policy, Referrer-Policy, COOP, CORP, COEP headers.

---

## Rate Limiting Config

```typescript
authLimiter:    { windowMs: 15min, max: 10 }   // login + password change
apiLimiter:     { windowMs: 1min,  max: 60 }   // general API
contactLimiter: { windowMs: 1hr,   max: 5  }   // contact form
registerLimiter:{ windowMs: 1hr,   max: 3  }   // registration
```

---

## New Features (Latest Update)

### Change Password
- API: `POST /api/auth/change-password` with currentPassword + newPassword
- Validation: Same rules as registration (8+ chars, uppercase, lowercase, number, special char)
- UI: Dedicated section in Edit Profile page
- Security: Requires current password verification

### Session Timeout
- 30-minute inactivity timer with 60-second warning countdown
- Warning modal with "Stay Logged In" and "Log Out Now" options
- Resets on any mouse/keyboard/touch/scroll activity
- Tab close detection with browser `beforeunload` event
- Redirects to `/auth/login?reason=timeout` on expiry

### Property Image Upload
- API: `POST /api/properties/[id]` (upload), `DELETE /api/properties/[id]?index=N` (remove)
- Access: Property owner (broker) + ADMIN only
- Limits: 20 images max, 5MB per image, JPEG/PNG/WebP only
- UI: Add/Remove buttons on property detail page (visible to authorized users only)

### AI Chatbot
- Floating chat widget (bottom-right corner)
- FAQ-based responses for common questions
- Topics: properties, contact, registration, login, filters, dashboard, profile, privacy, terms, dark mode
- Typing animation with bounce dots
- Mobile-responsive (380px width, max viewport)

### July 23, 2026 Security Audit
- **Profile page fixed**: Now fetches from database instead of hardcoded mock data
- **Reviews POST**: Now requires authentication
- **Property POST**: Now validates input via Zod schemas
- **Change password**: Now uses authLimiter (10/15min) for brute-force protection
- **Transaction response**: Strips internal user fields (isVerified, isActive, timestamps)
- **Health endpoint**: Returns only status (no timestamp)
- **Rate limiter**: IP validation improved (checks forwarded-for chain validity)

### World-Class Upgrade (July 23, 2026)
- **Email Verification**: Mandatory email verification before account activation
  - API: `GET /api/auth/verify-email?token=<token>` — verifies email, redirects to login
  - Registration sends verification email with unique token
  - Login checks `isEmailVerified` before allowing authentication
- **Password Reset**: Secure token-based password reset with 1-hour expiry
  - API: `POST /api/auth/forgot-password` — generates reset token, sends email
  - API: `POST /api/auth/reset-password` — validates token, resets password
  - UI: `/auth/forgot-password` and `/auth/reset-password` pages
  - Single-use tokens with expiry and `isUsed` flag
- **Account Lockout**: Automatic 15-minute lockout after 5 failed login attempts
  - Tracks `failedLoginAttempts` and `lockedUntil` on User model
  - Login returns specific error messages for locked accounts
  - Auto-unlocks after cooldown period
- **DB Audit Logging**: Security events stored permanently in PostgreSQL AuditLog table
  - `logAuditAction()` writes to both console and database
  - `logSecurityEvent()` captures security events with hashed IPs
  - AuditLog model tracks userId, action, resource, resourceId, details, ipAddress, userAgent
- **Forgot Password UI**: Professional forgot password page with email input
- **Reset Password UI**: Password reset form with real-time validation feedback
- **Login Page Updates**: Shows verification/lockout status messages from URL params

---

## Project Structure

```
NALBAP-App/
├── src/
│   ├── app/              # Next.js App Router pages
│   │   ├── api/          # API routes (10 endpoints)
│   │   │   ├── auth/
│   │   │   │   ├── [...nextauth]/
│   │   │   │   ├── register/
│   │   │   │   └── change-password/
│   │   │   ├── properties/
│   │   │   │   ├── route.ts
│   │   │   │   └── [id]/route.ts
│   │   │   ├── transactions/
│   │   │   ├── appraisals/
│   │   │   ├── reviews/
│   │   │   ├── contact/
│   │   │   └── health/
│   │   ├── auth/         # Login, register, error pages
│   │   ├── dashboard/    # Dashboard (5 sub-pages)
│   │   │   ├── properties/
│   │   │   ├── transactions/
│   │   │   ├── profile/     # Edit profile + change password
│   │   │   └── inquiries/
│   │   ├── properties/   # Property listing + detail
│   │   ├── profile/      # Public broker profiles
│   │   ├── faq/
│   │   ├── privacy/
│   │   └── terms/
│   ├── components/
│   │   ├── Navbar.tsx
│   │   ├── ThemeToggle.tsx
│   │   ├── Providers.tsx
│   │   ├── ContactButtons.tsx
│   │   ├── ContactForm.tsx
│   │   ├── SessionTimeout.tsx    # NEW: 30-min inactivity timer
│   │   └── Chatbot.tsx           # NEW: AI FAQ chatbot
│   ├── lib/
│   │   ├── auth.ts        # NextAuth config
│   │   ├── prisma.ts      # Prisma singleton
│   │   ├── rate-limit.ts  # Rate limiter
│   │   ├── validation.ts  # Zod schemas
│   │   ├── logger.ts      # Secure logger
│   │   └── email.ts       # Email utilities
│   ├── styles/
│   │   └── globals.css    # Tailwind + component classes
│   └── middleware.ts      # Request validation + static file exclusions
├── prisma/
│   ├── schema.prisma      # Database schema (10 models)
│   ├── seed-production.js # Production seed (Nelson + 6 properties)
│   ├── seed-test-accounts.js
│   └── fix-property-types.js
├── public/
│   ├── robots.txt
│   ├── sitemap.xml
│   └── manifest.webmanifest
├── vercel.json            # Security headers
├── .npmrc                 # legacy-peer-deps
├── tailwind.config.js
└── package.json           # Dependencies + scripts
```

---

## Deployment

- **Platform**: Vercel (iad1 region)
- **Database**: Neon PostgreSQL (ap-southeast-1)
- **CI/CD**: `vercel --prod --yes` (direct CLI deploy)
- **GitHub**: https://github.com/whodakingofhell/MarkChesterSantosRealEstateProj
- **Environment**: Vercel Dashboard → Settings → Environment Variables
- **Live URL**: https://philippine-skyland.vercel.app
- **Build Command**: `prisma generate && next build`
- **Post-install**: `prisma generate`
