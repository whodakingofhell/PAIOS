---
tags:
  - paios/knowledge
  - paios/references
related:
  - "./Lessons-Ledger.md"
  - "../../02 - Projects/Projects-MOC.md"
---

### Webhook Notification Pattern (from AI-Appointment-Assistant)
- Stack: Claude → Webhook → Discord
- Issues found: no retry, no circuit breaker, no payload validation
- Recommended architecture: webhook → validation layer → retry queue (3 attempts, exponential backoff) → Discord
- Use case: Any AI → external notification system

### Booking/Scheduling Pattern (from AI-Appointment-Assistant)
- Stack: Chat → Business hours check → Slot availability → Confirmation → Notification
- Critical components: timezone handling, buffer time, double-booking prevention, holiday calendar
- Use case: Any appointment booking system

### Project Scaffold Pattern (standard PAIOS pattern)
- Structure: PROJECT-CONTEXT.md + DECISIONS.md + memory.md + handoff.md + <domain files>
- Lifecycle: Incubating → Active → Completed/Archive
- Use case: Every new PAIOS project

### Multi-Expert Review Pattern (from SYSTEM framework)
- Method: 5 experts (SRE, Security, UX, Cost, Domain) review independently, then cross-reference
- Output: aligned list of critical gaps before launch
- Use case: Any project before public launch, architecture decision review

### Static Site Deployment Pattern (from deploy-v2)
- Stack: Next.js → Vercel
- Key: public/ for static assets, root for app config, SYSTEM/ for architecture docs
- Use case: Any Next.js web application
