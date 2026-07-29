
For the first version (just appointments, no full CRM yet), a lean setup:

- **Front-end (Vercel app)**
    
    - Chat interface where users talk to Claude.
        
    - It passes structured context to Claude:
        
        - `user_id`, `platform` (Discord/web/other), `time_zone`, etc.
          
          **Claude (brain)**

- Handles the conversation, collects appointment details, and validates them against your rules.
    
- When a booking is confirmed, Claude outputs a **standard JSON payload** that your backend uses for webhooks.

**Backend (simple serverless on Vercel)**

- Receives Claude’s final booking payload.
    
- Sends a Discord webhook message to your chosen channel.
    
- Optionally: sends an email notification.
