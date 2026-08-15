---
tags:
  - paios/projects
  - paios/project/ai-appointment-assistant
related:
  - "Projects-MOC.md"
  - "../README.md"
  - "research/"
---

## Plain-language summary of your vision

- Audience: Online sellers and service providers (for example: remote PC support, online services, local service businesses).
    
- Main job of the AI:
    
    - Answer customer questions.
        
    - Help customers book short remote appointments (5–20 minutes) where you connect via AnyDesk or TeamViewer.
        
    - Notify you through Discord (and later email) whenever a booking is made.
        
- Location/time rules:
    
    - All appointments are based on Philippine time (Asia/Manila, UTC+8), which does not change for daylight saving.time+2
        
    - If a customer is overseas, the AI converts their local time into your Philippine time before confirming the appointment.callsphere+2
        
- Cost rules:
    
    - You want to keep everything as close to free as possible, using free tiers (Claude, Perplexity, Vercel, etc.).
        
    - Claude must keep messages short and focused to save tokens.
        
- Tools you plan to use:
    
    - **Claude** – main "brain" of the system.
        
    - **Perplexity** – for research, facts, and validating ideas.
        
    - **Obsidian** – where you store all documentation, rules, and lessons learned.
        
    - **Vercel** – hosting your web app.
        
    - **ChatGPT/Grok** – optional second brain and UI designer, only if they help.
