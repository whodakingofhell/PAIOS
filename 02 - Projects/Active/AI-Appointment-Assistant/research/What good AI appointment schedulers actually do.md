---
tags:
  - paios/projects
  - paios/project/ai-appointment-assistant
related:
  - "Projects-MOC.md"
  - "../README.md"
  - "research/"
---

Modern AI scheduling tools for small service businesses tend to share these characteristics: 


You're aiming for Claude to become a 10/10 "brain" for appointment scheduling first, using Discord webhooks (and maybe email) as the notification channel, with very strong validation and documentation around every decision. That's a good focus because appointment bots are a proven, high‑value use case for service businesses and online sellers.vellum+2

Below is a focused plan just for the **appointment-scheduling brain** plus a Claude "brain prompt" (not yet the final master prompt) that you can evolve as you add more features.

---

## 1. What good AI appointment schedulers actually do

Modern AI scheduling tools for small service businesses tend to share these characteristics:vellum+2

- Collect key booking info up front (service type, preferred time, timezone, contact details).
    
- Check availability rules and avoid conflicts, often across multiple staff or locations.zoho+1
    
- Enforce business constraints like buffer times, max bookings per day, and lead time rules.jotform+1
    
- Send confirmations and reminders over the user's preferred channel (email, SMS, chat, etc.).jotform+1
    
- Allow human override and maintain transparency to avoid over-automation issues.clutch+1
    

You can adapt these "best practices" 

- Required fields for a valid appointment.
    
- Business rules (time ranges, notice periods, slot length, caps per day).
    
- Output format for your Discord webhook/email integration.
