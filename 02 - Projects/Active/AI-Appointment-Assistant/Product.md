---
title: "AI Appointment Assistant — Product Spec"
version: "1.0"
status: "Canonical"
date: "2026-07-18"
tags:
  - project
  - product
  - specification
  - features
  - paios/projects
  - paios/project/ai-appointment-assistant
owner: "OpenCode"
canonical: true
related:
  - "Business.md"
  - "README.md"
---

# Product Specification

---

## System Architecture

```
┌─────────────────────────────────────────────────┐
│              CUSTOMER CHAT (Vercel)              │
│         Simple chat UI — no jargon               │
└──────────────────────┬──────────────────────────┘
                       │ message
                       ▼
┌─────────────────────────────────────────────────┐
│           CLAUDE APPOINTMENT BRAIN               │
│  System prompt + business rules + TZ logic       │
│  Token-efficient: short Q, short A               │
│  Output: booking JSON + human summary            │
└──────────────────────┬──────────────────────────┘
                       │ booking payload
                       ▼
┌─────────────────────────────────────────────────┐
│         VERCEL SERVERLESS FUNCTION               │
│  Receives payload → validates → stores           │
└──────┬──────────────────────┬───────────────────┘
       │                      │
       ▼                      ▼
┌──────────────┐    ┌──────────────────┐
│   SUPABASE   │    │ DISCORD WEBHOOK  │
│  (bookings)  │    │  (notification)  │
└──────────────┘    └──────────────────┘
```

---

## Core Features (v1)

### F1: Appointment Scheduling
- Collects: name, contact, service, date, time, timezone, duration (5–20 min), notes
- Enforces business rules (hours, min notice, max/day)
- Confirms with compact summary

### F2: Time Zone Handling
- Base: Asia/Manila (UTC+8), no DST
- For overseas: ask city/country → convert → show both times
- Confirmation shows "Your time: X / Philippine time: Y"

### F3: Discord Notifications
- Human-readable message: "New: [Name], [Service], [PH time], [Duration]"
- Structured JSON payload for automation
- Latency target: <3 seconds

### F4: Token Efficiency
- Ask one missing field at a time
- 2–3 sentence confirmations
- No long explanations unless asked
- Target: <6 turns per booking

---

## Business Rules

| Rule | Value | Notes |
|------|-------|-------|
| Timezone base | Asia/Manila (UTC+8) | No daylight saving |
| Session duration | 5–20 minutes | Default 15 if unspecified |
| Working hours | Mon–Sun, 9:00–18:00 PH | Every day |
| Min notice | 2 hours | Before current time |
| Max bookings/day | 12 | Configurable |
| Buffer | 5 minutes | Between sessions |

---

## Data Model (Supabase)

```sql
CREATE TABLE bookings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  customer_name TEXT NOT NULL,
  customer_email TEXT,
  customer_contact TEXT,
  service_type TEXT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  timezone TEXT DEFAULT 'Asia/Manila',
  duration_minutes INT DEFAULT 15,
  notes TEXT,
  status TEXT DEFAULT 'confirmed',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  discord_notified BOOLEAN DEFAULT FALSE
);
```

---

## Token Efficiency Rules (from AI Projects)

1. **Minimal questions:** One missing field at a time, shortest possible question
2. **Short answers:** 2–3 sentences or compact bullets for confirmations
3. **No restatements:** Only full details at final confirmation
4. **No explanations:** State the rule and move on unless asked

---

## Testing Scenarios

| # | Scenario | Expected Behavior |
|---|----------|-------------------|
| 1 | "I'm from Manila, book today 3 PM" | Confirm: 3:00 PM PH time, 15 min |
| 2 | "I'm in London, book 10 AM my time" | Convert: 10 AM GMT → 6 PM PH time |
| 3 | "Book a 1-hour session" | Reject: max 20 min, offer 15 or 20 |
| 4 | "Book for 2 AM PH time" | Reject: outside working hours |
| 5 | "Book for tomorrow (1 hr notice)" | Reject: min 2 hours notice |
| 6 | "Book 13th booking today" | Reject: max 12/day |

---

## QA Criticism

- [ ] Architecture covers all data flow paths
- [ ] Business rules are complete and testable
- [ ] Token efficiency rules are measurable
- [ ] Data model supports all required fields
- [ ] Security: no secrets in client-side code
- [ ] Scalability: Supabase free tier handles 50k rows

---

## PAIOS Compliance

- **SSoT:** This spec derives from Vision.md and Business.md
- **DRY:** Business rules defined here, referenced by Claude brain prompt
- **Ownership:** Product spec lives in `01-Canonical/Projects/`
