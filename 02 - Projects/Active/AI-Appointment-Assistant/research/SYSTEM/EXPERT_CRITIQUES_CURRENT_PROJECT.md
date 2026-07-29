# EXPERT CRITIQUES: AI Appointment Assistant

Generated: 2026-07-18

---

## 1. SRE / RELIABILITY ENGINEER

**Critical Issues Found:**

1. **SILENT WEBHOOK FAILURE** - No retry mechanism if Discord webhook fails. Booking confirmed in Claude but seller never notified. Customer thinks it's booked, seller doesn't know. This is a P0 incident waiting to happen.

2. **NO CIRCUIT BREAKER** - If Claude API goes down, the entire chat interface becomes non-functional with no graceful degradation (e.g., "Sorry, our system is temporarily unavailable, please try again in 5 minutes" or a fallback contact form).

3. **NO MONITORING** - No documented metrics: How many bookings succeeded? How many failed? What's the p95 response time? Without observability, you're flying blind.

4. **NO ROLLBACK** - If Claude starts producing malformed JSON payloads, there's no validation layer to catch it before it hits the webhook. A bad day from Claude means corrupted notifications.

**Recommendations:**
- Add webhook retry logic (3 attempts with exponential backoff)
- Add payload validation schema before sending to Discord
- Add a simple health check endpoint
- Log every booking attempt (success/failure) to a file or database

---

## 2. SECURITY ENGINEER

**Critical Issues Found:**

1. **NO INPUT SANITIZATION** - Customer names and notes are passed directly into Discord messages. A malicious customer could inject Discord markdown, mentions (@everyone), or even webhook payload manipulation.

2. **NO RATE LIMITING** - Anyone could spam the booking system, creating dozens of fake appointments or causing token overuse on Claude API.

3. **DISCORD WEBHOOK URL EXPOSURE** - If the webhook URL is stored in client-side code or committed to a repo, anyone can spam your Discord channel.

4. **NO PII HANDLING POLICY** - Customer names, emails, and Discord handles are PII. No documentation on retention, deletion, or GDPR/privacy compliance.

**Recommendations:**
- Sanitize all user inputs before Discord output (strip markdown, limit length)
- Add rate limiting per IP/user (e.g., max 3 booking attempts per hour)
- Store webhook URL in environment variables only, never in code
- Add a privacy note: what data is collected, how long it's stored, how to request deletion

---

## 3. UX DESIGNER

**Critical Issues Found:**

1. **NO CANCELLATION/RESCHEDULING FLOW** - Once booked, there's no way to cancel or change the appointment. This is a fundamental UX gap.

2. **NO BOOKING CONFIRMATION TO CUSTOMER** - Seller gets Discord notification, but customer gets nothing. They don't know if their booking was actually saved.

3. **NO VISUAL FEEDBACK DURING CONVERSATION** - No typing indicators, no progress bar ("Step 2 of 4: Pick a time"), no sense of forward momentum.

4. **"WEBHOOK" AND "JSON" APPEAR IN DOCUMENTATION** - The master prompt correctly avoids technical jargon for users, but the architecture docs mix technical and user-facing language.

**Recommendations:**
- Add cancel/reschedule flow (keyphrase: "cancel my booking" or "change my appointment")
- Send a confirmation message back to the customer (email or same chat)
- Add a progress indicator: "Got your name. Now, what service do you need?"
- Keep technical docs separate from user-facing docs

---

## 4. COST / FINOPS ANALYST

**Critical Issues Found:**

1. **NO TOKEN BUDGET** - Each booking conversation could take 3-10 turns. At ~500 tokens per turn, that's 1,500-5,000 tokens per booking. At $0.003/1K tokens (Claude Sonnet), that's $0.004-$0.015 per booking. Cheap now, but no cap exists.

2. **NO CONVERSATION LENGTH LIMIT** - A confused customer could go 20+ turns, burning tokens with no booking. There should be a max-turn limit or a "let me connect you to a human" fallback.

3. **FREE TIER DEPENDENCY** - Vercel, Claude, Discord all have free tiers. But if you hit Vercel's serverless limit or Claude's rate limit, the system breaks with no paid fallback path documented.

4. **CLAUDE MODEL SELECTION NOT DOCUMENTED** - Using Claude Haiku vs. Sonnet vs. Opus changes cost by 10-100x. No guidance on which model for which task.

**Recommendations:**
- Document token budget per conversation (target: <3000 tokens per booking)
- Add max 15 turn limit per conversation
- Document model selection: Haiku for simple booking, Sonnet only for complex multi-timezone
- Create a cost projection at 100/500/1000 bookings per month

---

## 5. DOMAIN EXPERT (Scheduling / Small Business)

**Critical Issues Found:**

1. **NO CANCELLATION POLICY** - What happens if customer no-shows? Can they cancel 5 minutes before? Is there a penalty? Not documented.

2. **NO DOUBLE-BOOKING PREVENTION** - The system checks business hours but doesn't check if a slot is already taken. Two customers could book the same 3:00 PM slot.

3. **NO BUFFER TIME BETWEEN APPOINTMENTS** - Mentioned in `Claude Appointment Brain – v1.md` but never defined. What's the buffer? 5 minutes? 15 minutes?

4. **NO HOLIDAY/BLOCKED DATE HANDLING** - "Blocked dates or holidays" is mentioned as a rule but there's no mechanism to define or update them.

5. **NO SHOW HANDLING** - If customer doesn't show up, what happens? Is the slot freed? Is the seller notified?

6. **NO BOOKING FOR SOMEONE ELSE** - Not addressed. Can a parent book for a child? Can an assistant book for a boss?

**Recommendations:**
- Add cancellation policy: "Cancel up to 2 hours before, no penalty"
- Add double-booking prevention: check slot availability before confirming
- Define buffer time: "10 minutes between appointments"
- Add a `blocked_dates.md` file that Claude reads
- Add no-show handling: "If no contact within 10 minutes of start, slot is freed"
- Add policy for booking on behalf of others

---

## CROSS-EXPERT ALIGNMENT

All 5 experts agree on these critical gaps:

| Gap | Experts Who Flagged It |
|-----|----------------------|
| No retry/fallback for notifications | SRE + Domain |
| No input validation/sanitization | Security + Domain |
| No cancellation/rescheduling flow | UX + Domain |
| No double-booking prevention | SRE + Domain |
| No token budget or conversation limits | Cost + SRE |
| No monitoring or observability | SRE + Cost |

These 6 issues should be fixed before any public launch.
