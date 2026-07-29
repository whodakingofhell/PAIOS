---
title: "Deployment Guide — AI Appointment Assistant"
version: "1.0"
status: "Canonical"
date: "2026-07-18"
tags: [project, deployment, guide, readme]
owner: "OpenCode"
canonical: true
---

# AI Appointment Assistant — Deployment Guide

## Quick Start

### 1. Prerequisites

- Node.js 18+
- Vercel CLI (`npm i -g vercel`)
- Supabase CLI (`npm i -g supabase`)
- Supabase project (free tier)
- Vercel account (free tier)

### 2. Clone & Install

```bash
cd appointment-backend
npm install
```

### 3. Environment Variables

Set these in Vercel dashboard (Settings → Environment Variables):

| Variable | Value | Notes |
|----------|-------|-------|
| `SUPABASE_URL` | `https://lohbjubyaizaxqtikgto.supabase.co` | From Supabase dashboard |
| `SUPABASE_ANON_KEY` | `sb_publishable_...` | From Supabase → Settings → API |
| `SUPABASE_SERVICE_ROLE_KEY` | `sb_secret_...` | From Supabase → Settings → API |
| `DISCORD_WEBHOOK_URL` | `https://discord.com/api/webhooks/...` | From Discord → Server Settings → Integrations |
| `APP_API_KEY` | (optional) | For additional API authentication |

### 4. Database Setup

1. Go to Supabase SQL Editor
2. Run `supabase-schema.sql` (creates appointments table)
3. Run `rls-migration.sql` (enables RLS + audit logging)

### 5. Deploy

```bash
vercel --prod
```

### 6. Test

```bash
# Health check
curl https://appointment-backend-one.vercel.app/api/health

# Create booking
curl -X POST https://appointment-backend-one.vercel.app/api/book-appointment \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","contact":"test@test.com","service":"PC Support","date":"2026-07-25","time":"10:00","duration":15}'

# List bookings
curl https://appointment-backend-one.vercel.app/api/list-appointments
```

---

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/book-appointment` | Create a new booking |
| GET | `/api/list-appointments` | List confirmed bookings |
| GET | `/api/health` | Health check |

### POST /api/book-appointment

**Body:**
```json
{
  "name": "Juan Dela Cruz",
  "contact": "juan@email.com",
  "phone": "+639171234567",
  "service": "PC Support",
  "date": "2026-07-25",
  "time": "10:00",
  "timezone": "Asia/Manila",
  "duration": 15,
  "notes": "Laptop screen issue"
}
```

**Response (201):**
```json
{
  "success": true,
  "booking": { ... },
  "reference": "B5F01F00",
  "message": "Booked! Ref: B5F01F00. PC Support on 2026-07-25 at 10:00 (PH Time). 15 min."
}
```

### GET /api/list-appointments

**Query params:** `date=2026-07-25` (optional)

---

## Security

### Production Security Controls

- **Rate limiting:** 5 bookings per IP per hour (prevents abuse / DoS)
- **Input sanitization:** HTML tags stripped, fields limited to 500 chars (prevents XSS)
- **CORS:** Restricted to app domain only (prevents unauthorized cross-origin requests)
- **Supabase RLS:** Enabled — anon can insert + read only; service-role for admin operations
- **Audit logging:** All booking attempts logged with timestamp, IP, and action type
- **Secrets:** All environment variables managed via Vercel dashboard (never in code or commits)

### Deployment Security Checklist

Before any production deployment:

- [ ] `.env` is not in version control: `git diff --cached --name-only | grep .env`
- [ ] No API keys in codebase: `git secrets --scan` or manual grep for `supabase_key|service_role|webhook`
- [ ] Supabase RLS policies applied and tested: run `rls-migration.sql`
- [ ] Vercel environment variables are set (not default/stub values)
- [ ] Discord webhook URL is valid and scoped to the correct channel
- [ ] API accepts requests over HTTPS only
- [ ] Rate limiting is active (verify: 6 rapid requests in 1 second should return 429)
- [ ] Controlled Folder Access whitelisted this project's directory (dev machines)

### Supabase RLS Policy Verification

```sql
-- Verify that anon cannot delete or update
SELECT * FROM pg_policies WHERE tablename = 'appointments';
-- Expected: policies for INSERT and SELECT only (no UPDATE/DELETE for anon)
```

### Developer Workstation Requirements

See `AI-Ops-Vault/01-Canonical/OS-Sections/06-Security.md` for full workstation hardening guide.
Key requirements:
- Windows Defender active + tamper-protected
- Windows Firewall enabled
- BitLocker encryption enabled
- Microsoft Account + PIN login
- Controlled Folder Access enabled (whitelist this project)
- Database ports not exposed to 0.0.0.0

---

## Architecture

```
Browser → Vercel CDN → Serverless Function → Supabase
                                        ↘ Discord Webhook
```

---

## PAIOS Compliance

- **SSoT:** This guide is the canonical deployment reference
- **DRY:** Not duplicated elsewhere
