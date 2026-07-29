---
tags:
  - paios/projects
  - paios/project/ai-appointment-assistant
related:
  - "Projects-MOC.md"
  - "../README.md"
  - "research/"
---

## 1. Overview

This project is an AI assistant (with Claude as the main "brain") that helps online sellers and service providers automate customer support, starting with appointment scheduling. It is designed for non-technical users, focuses on short remote support sessions (5–20 minutes via AnyDesk/TeamViewer), and keeps all times anchored to Philippine time (Asia/Manila, UTC+8) while handling overseas clients.

The system aims to be low-cost (mostly free tiers) and token-efficient, with short, clear conversations.

## 2. Target Users

- Online service providers (e.g., remote PC support, coaching, consulting).
    
- Small/local businesses offering appointment-based services.
    
- Sellers who use Discord or similar platforms and want automatic notifications when customers book.
Key pain points:

- Manual back-and-forth scheduling.
    
- Time zone confusion with overseas customers.
    
- Short remote sessions that need precise timing.
## 3. Core Value Proposition

The assistant:

- Talks to customers in natural language to book appointments.
    
- Converts customer time to Philippine time (Asia/Manila) before confirming.
    
- Limits sessions to 5–20 minutes to match real remote-support constraints.
    
- Sends instant notifications (Discord, later email) with all necessary details.
    
- Uses short, focused messages to keep AI usage costs very low.
    

Research shows AI appointment tools can drastically reduce scheduling effort and no-shows for small businesses when they handle time zones and rules correctly.

## 4. Key Features

1. **Appointment Scheduling (v1 focus)**
    
    - Collects: name, contact, service, date, time, time zone, duration (5–20 minutes), notes.
        
    - Enforces business rules (working hours, minimum notice, max appointments per day).
        
    - Confirms bookings clearly with a compact summary.
        
2. **Time Zone Handling**
    
    - Home base: Philippine time (Asia/Manila, UTC+8), no daylight saving.time+2
        
    - For overseas users:
        
        - Asks for their city/country or time zone.
            
        - Interprets their requested time locally and converts to Asia/Manila.
            
        - Shows both "your time" and "Philippine time" in the confirmation.callsphere+2
            
3. **Discord (and Email) Notifications**
    
    - After confirmation, the system sends:
        
        - A short human-readable message.
            
        - A small structured JSON object with all booking details.
            
    - Discord receives a clear message (e.g., "New appointment: [Name], [Service], [PH time], [Duration], [Contact]").
        
4. **Token-Efficient Conversations**
    
    - Short questions, one missing field at a time.
        
    - Short confirmations, using bullet lists where helpful.
        
    - No long explanations unless the user asks.
        
    - This aligns with best practices for efficient AI workflows and scalable deployments.ijsat+1
        

---

## 5. System Architecture (High-Level)

- **Claude (main brain)**
    
    - Handles conversations.
        
    - Applies business rules and time zone logic.
        
    - Outputs a structured booking payload plus a short summary.
        
- **Front-End (Vercel app)**
    
    - Chat interface for customers.
        
    - Sends context (user ID, platform, time zone, etc.) to Claude.
        
- **Backend (Serverless on Vercel)**
    
    - Receives Claude's booking payload.
        
    - Sends Discord webhook messages and, later, email notifications.
        
- **Perplexity**
    
    - Used by the owner for research and validation (e.g., best practices in scheduling, customer support).
        
- **Obsidian**
    
    - Knowledge base:
        
        - `vision.md` – product vision.
            
        - `scheduling_rules.md` – business rules.
            
        - `appointment_brain_prompt.md` – Claude's instructions.
            
        - `tests_appointment_brain.md` – example conversations and expected outputs.
            
        - `lessons_learned.md` – issues found and fixes.
            
- **Optional tools**
    
    - ChatGPT – second opinion on prompts or code.
        
    - Grok – UI copy and flow suggestions.
        

---

## 6. Appointment Rules (Initial)

- **Time zone**:
    
    - Base: Asia/Manila (Philippines, UTC+8), no DST.time+2
        
- **Duration**:
    
    - Each appointment: 5–20 minutes.
        
    - If user doesn't specify, default to a configured length (e.g., 15 minutes).
        
- **Availability** (to be defined precisely):
    
    - Working days and hours (e.g., Mon–Fri, 9:00–18:00 PH time).
        
    - Minimum notice (e.g., at least 2 hours before).
        
    - Maximum appointments per day.
        

---

## 7. Implementation Pipeline

1. **Write the Rules (Non-Technical)**
    
    - Document working hours, allowed durations, limits, and notification preferences in simple language in Obsidian.
        
    - Research shows clear requirements and user-friendly design are key for successful e-appointment systems.ijcope+2
        
2. **Build the Claude "Appointment Brain"**
    
    - Encode rules, required fields, time zone logic, and token-efficiency behavior in a system prompt.
        
    - Add an error-handling loop:
        
        - Error → Troubleshoot → Validate → Improve → Retry → Solidify.
            
3. **Create and Run Test Scenarios**
    
    - Example conversations (local and overseas users, invalid times, long duration requests).
        
    - Check if Claude:
        
        - Enforces PH time and rules.
            
        - Keeps messages short.
            
        - Produces correct structured outputs.
            
4. **Integrate Discord Webhooks (and Email Later)**
    
    - Implement a small backend that:
        
        - Accepts Claude's booking payload.
            
        - Posts a formatted message to a Discord channel.
            
5. **Refine UI/UX**
    
    - Ensure the chat interface uses simple language:
        
        - "Your time" vs. "Philippine time".
            
        - No technical terms like "webhook" for users.
            
    - Research on non-technical chatbot users emphasizes simple, predictable interfaces and clear feedback.iacis+2
        
6. **Iterate and Expand**
    
    - Use real conversations and "lessons_learned.md" to:
        
        - Improve rules and prompts.
            
        - Add new capabilities (FAQ support, product recommendations, seller insights).
