---
title: "Supabase Connection Guide"
version: "1.0"
status: "Canonical"
date: "2026-07-18"
tags: [project, supabase, setup, integration]
owner: "OpenCode"
canonical: true
---

# Supabase Connection Guide

> Connect to the Supabase project for the AI Appointment Assistant.

---

## Project Details

| Field | Value |
|-------|-------|
| Dashboard | https://supabase.com/dashboard/project/lohbjubyaizaxqtikgto |
| Project URL | `https://lohbjubyaizaxqtikgto.supabase.co` |
| Region | (check dashboard) |
| Plan | Free tier |

---

## Setup Steps

### 1. Get API Keys

1. Go to https://supabase.com/dashboard/project/lohbjubyaizaxqtikgto/settings/api
2. Copy the **anon/public** key
3. Copy the **service_role** key (keep secret!)

### 2. Run the Schema

1. Go to https://supabase.com/dashboard/project/lohbjubyaizaxqtikgto/sql/new
2. Paste the contents of `supabase-schema.sql`
3. Click **Run**

### 3. Set Environment Variables

```bash
# In Vercel dashboard or .env.local
SUPABASE_URL=https://lohbjubyaizaxqtikgto.supabase.co
SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_KEY=your-service-role-key
DISCORD_WEBHOOK_URL=your-webhook-url
```

### 4. Deploy to Vercel

```bash
cd appointment-backend
vercel --prod
```

### 5. Test the Connection

```bash
# Create a booking
curl -X POST https://appointment-backend.vercel.app/api/bookings \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","contact":"test@example.com","service":"PC Support","date":"2026-07-20","time":"15:00","timezone":"Asia/Manila","duration":15}'

# List bookings
curl https://appointment-backend.vercel.app/api/bookings?date=2026-07-20
```

---

## Row Level Security (RLS)

For production, enable RLS in Supabase:

```sql
ALTER TABLE appointments ENABLE ROW LEVEL SECURITY;

-- Allow anon insert (for booking form)
CREATE POLICY "Allow insert for anon" ON appointments
  FOR INSERT WITH CHECK (true);

-- Allow anon select (for listing)
CREATE POLICY "Allow select for anon" ON appointments
  FOR SELECT USING (true);

-- Restrict update/delete to service key only
CREATE POLICY "Service key only for update" ON appointments
  FOR UPDATE USING (false);

CREATE POLICY "Service key only for delete" ON appointments
  FOR DELETE USING (false);
```

---

## PAIOS Compliance

- **SSoT:** This guide is the canonical connection reference
- **DRY:** Connection details not duplicated elsewhere
