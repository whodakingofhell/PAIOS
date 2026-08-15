---
title: "Scheduling Rules"
version: "1.0"
status: "Canonical"
date: "2026-07-18"
tags:
  - project
  - rules
  - scheduling
  - paios/projects
  - paios/project/ai-appointment-assistant
owner: "OpenCode"
canonical: true
related:
  - "Vision.md"
  - "Claude-Brain-Prompt.md"
---

# Scheduling Rules

> Non-technical reference. These rules are encoded in the Claude Brain Prompt.

---

## Time Zone

- **Base:** Asia/Manila (Philippines, UTC+8)
- **Daylight saving:** None. Philippines does not observe DST.
- **For overseas customers:** Ask their city → resolve against customer's local date first (prevents off-by-one-day errors) → convert to PH time → show both in confirmation.
- **Known limitation:** Daily-cap and conflict queries use UTC calendar-day boundaries as stand-in for PH calendar day. Only works because 9AM–6PM PH never crosses UTC midnight. If hours extend into night, must rework to explicit PH-day boundaries.

## Working Hours

- **Days:** Monday–Sunday (every day)
- **Hours:** 9:00 AM – 6:00 PM Philippine time
- **Weekends:** Open (Mon–Sun)

## Session Duration

- **Range:** 5–20 minutes
- **Default:** 15 minutes (if customer doesn't specify)
- **Longer sessions:** Reject and offer 15 or 20 min options

## Booking Limits

- **Minimum notice:** 2 hours before current time
- **Maximum per day:** 12 bookings
- **Buffer between sessions:** 5 minutes (auto-calculated)
- **Error handling:** Max 2 retries before human handoff

## Notifications

- **Primary:** Discord webhook (instant)
- **Secondary:** Email (planned for v2)
- **Format:** Human-readable message + structured JSON

## Customer Info Required

| Field | Required | Notes |
|-------|----------|-------|
| Name | Yes | |
| Contact | Yes | Email or phone |
| Service type | Yes | PC support, coaching, etc. |
| Date | Yes | |
| Time | Yes | Customer's local time |
| Timezone | Yes | Auto-detected or asked |
| Duration | No | Default 15 min |
| Notes | No | |

---

## PAIOS Compliance

- **SSoT:** Rules defined here, encoded in Claude-Brain-Prompt.md
- **DRY:** Not duplicated in other docs
