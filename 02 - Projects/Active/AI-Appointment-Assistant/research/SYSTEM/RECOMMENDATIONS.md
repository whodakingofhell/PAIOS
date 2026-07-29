# RECOMMENDATIONS: How to Improve the System

Generated: 2026-07-18
Based on: Full project analysis, scenario modeling, and 5-expert critique

---

## PRIORITY 1: FIX BEFORE LAUNCH (Critical)

### 1. Add Webhook Retry + Fallback
- **What:** If Discord webhook fails, retry 3x with 2s/5s/10s backoff
- **Why:** Silent failures mean missed bookings = lost revenue
- **Effort:** 30 minutes of backend code
- **Impact:** Prevents the #1 catastrophic failure mode

### 2. Add Input Sanitization
- **What:** Strip markdown, limit string lengths, escape special chars before Discord output
- **Why:** Prevents @everyone spam, markdown injection, payload corruption
- **Effort:** 15 minutes
- **Impact:** Security baseline

### 3. Add Double-Booking Prevention
- **What:** Maintain a simple availability state (file or in-memory). Check slot before confirming.
- **Why:** Two customers booking the same slot = disaster
- **Effort:** 1-2 hours (need a simple data store)
- **Impact:** Core business logic gap

### 4. Add Cancellation/Reschedule Flow
- **What:** Detect "cancel" or "change" intent → look up booking → update/release slot → confirm
- **Why:** Every booking system needs this. Without it, you'll manually handle cancellations.
- **Effort:** 2-3 hours
- **Impact:** Critical UX completeness

---

## PRIORITY 2: ADD WITHIN FIRST WEEK (Important)

### 5. Define Token Budget
- **What:** Target <3000 tokens per booking conversation. Add max 15 turn limit.
- **Why:** Prevents runaway costs and degraded experience
- **Effort:** 10 minutes (just add to master prompt)

### 6. Add Customer Confirmation
- **What:** After booking, send a summary back to the customer (in chat or via email)
- **Why:** Customer has no proof of booking. This is table-stakes for any scheduler.
- **Effort:** 30 minutes
- **Impact:** Trust and completeness

### 7. Define Buffer Time + Blocked Dates
- **What:** Set buffer (e.g., 10 min between appointments). Add `blocked_dates.md` that Claude reads.
- **Why:** Without buffer, back-to-back bookings exhaust the seller
- **Effort:** 20 minutes
- **Impact:** Operational sustainability

### 8. Add Model Selection Strategy
- **What:** Use Claude Haiku for simple bookings, Sonnet only for complex multi-timezone or edge cases
- **Why:** 10-100x cost difference between models
- **Effort:** 10 minutes (document in token_efficiency.md)
- **Impact:** Major cost savings at scale

---

## PRIORITY 3: ADD WITHIN FIRST MONTH (Enhancement)

### 9. Add No-Show Handling
- **What:** If customer doesn't connect within 10 minutes of start time, mark slot as freed
- **Why:** Seller's time is wasted if customer doesn't show
- **Effort:** 1 hour
- **Impact:** Reduces lost productivity

### 10. Add Monitoring Dashboard
- **What:** Log every booking attempt (success/fail), token usage, response times
- **Why:** Can't improve what you can't measure
- **Effort:** 2-4 hours
- **Impact:** Data-driven iteration

### 11. Add Booking-on-Behalf Policy
- **What:** Document rules: "Can book for others if customer provides their name and contact"
- **Why:** Common real-world scenario currently unaddressed
- **Effort:** 15 minutes
- **Impact:** Edge case completeness

### 12. Add Reminder System
- **What:** 24-hour and 1-hour reminders via Discord/Email before appointment
- **Why:** Reduces no-shows by 30-50% (industry data)
- **Effort:** 3-4 hours (need a scheduled job)
- **Impact:** Direct revenue protection

---

## SYSTEM-LEVEL RECOMMENDATIONS

### For Your Permanent Starter System

| Area | Recommendation | Why |
|------|---------------|-----|
| **Documentation** | Always create `expert_critiques.md` per project | Prevents shipping known-broken features |
| **Testing** | Always write 10+ test scenarios before first deploy | Catches 80% of issues before users see them |
| **Cost** | Always document token budget per feature | Prevents surprise bills |
| **Security** | Always sanitize user inputs before any external output | Baseline security hygiene |
| **Resilience** | Always add retry logic for external integrations (Discord, email) | External APIs fail. Plan for it. |
| **Monitoring** | Always log success/failure for every automated action | You can't fix what you can't see |
| **UX** | Always add cancel/reschedule before launch | Users will try it. If it's not there, they'll be frustrated. |

### For Future Projects

1. **Start with `PROJECT_STARTER.md`** - Open it at the beginning of every new project
2. **Fill the YAML block** - Forces you to clarify the project before writing code
3. **Follow the 5-step build sequence** - Don't skip steps
4. **Run all 5 experts before launch** - Non-negotiable quality gate
5. **Log everything in `lessons_learned.md`** - Your future self will thank you

---

## COST PROJECTION (Current Project)

| Volume | Tokens/Month | Claude Cost (Haiku) | Claude Cost (Sonnet) | Vercel Cost | Discord Cost |
|--------|-------------|--------------------|--------------------|-------------|-------------|
| 10 bookings/mo | ~30K | $0.09 | $0.45 | Free | Free |
| 100 bookings/mo | ~300K | $0.90 | $4.50 | Free | Free |
| 500 bookings/mo | ~1.5M | $4.50 | $22.50 | $20 | Free |
| 1000 bookings/mo | ~3M | $9.00 | $45.00 | $20 | Free |

**Recommendation:** Start with Haiku, upgrade to Sonnet only if quality is insufficient.
