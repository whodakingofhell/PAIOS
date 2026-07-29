---
title: "Supabase Schema — Appointments Table"
version: "1.0"
status: "Canonical"
date: "2026-07-18"
tags: [project, supabase, schema, database]
owner: "OpenCode"
canonical: true
---

# Supabase Schema

> Run this SQL in the Supabase SQL Editor once to create the appointments table.

---

```sql
-- Appointments table — Supabase (Postgres)
-- Run this in the Supabase SQL editor once.

create extension if not exists "pgcrypto";

create table if not exists appointments (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  contact text not null,
  service text not null,
  duration_minutes int not null check (duration_minutes between 5 and 20),
  time_ph timestamptz not null,
  time_user_local timestamptz,
  time_user_zone text,
  notes text,
  status text not null default 'confirmed' check (status in ('confirmed', 'cancelled')),
  created_at timestamptz not null default now()
);

-- Speeds up conflict-check and daily-cap queries
create index if not exists idx_appointments_time_ph on appointments (time_ph) where status = 'confirmed';
create index if not exists idx_appointments_contact on appointments (contact);

-- Prevents exact duplicate double-submits (same contact, same start time, still confirmed)
create unique index if not exists uniq_contact_time_confirmed
  on appointments (contact, time_ph)
  where status = 'confirmed';
```

---

## Fields

| Column | Type | Notes |
|--------|------|-------|
| `id` | UUID | Auto-generated |
| `name` | text | Customer name |
| `contact` | text | Email or phone |
| `service` | text | Service type |
| `duration_minutes` | int | 5–20 range enforced |
| `time_ph` | timestamptz | Philippine time (canonical) |
| `time_user_local` | timestamptz | Customer's local time (optional) |
| `time_user_zone` | text | Customer's timezone (optional) |
| `notes` | text | Optional notes |
| `status` | text | 'confirmed' or 'cancelled' |
| `created_at` | timestamptz | Auto-set |

---

## PAIOS Compliance

- **SSoT:** This is the canonical schema for the appointments table
- **DRY:** Not duplicated elsewhere
