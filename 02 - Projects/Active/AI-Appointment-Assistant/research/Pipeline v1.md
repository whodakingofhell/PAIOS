## Step 1 – Define the business rules (non-technical)

Goal: Write down your rules in simple language so even non-technical people can understand.

What to capture:

- Working days and hours (Philippine time).
    
- Allowed appointment length (5–20 minutes).
    
- How much advance notice you need (e.g., at least 2 hours before).
    
- Maximum number of appointments per day.
    
- How you want to be notified (Discord channel, email).
    

Where to store:

- Put these in Obsidian (for example: a note called `scheduling_rules.md`).
    
- Use simple bullet points so they’re easy to read.
    

Why this matters:

- Research on appointment systems for small businesses shows that clear rules and user-friendly design are crucial for reliability and usability.ijcope+2
    

## Step 2 – Build and test the “appointment brain” in Claude

Goal: Give Claude a clear, human-readable set of instructions (the “brain prompt”) for handling appointments.

What to include in the prompt:

- Your business rules (from Step 1).
    
- Required booking details: name, contact, service, date, time, time zone, duration.
    
- Time zone logic:
    
    - Always convert to Asia/Manila and show both local time and Philippine time when needed.linkedin+2
        
- Token efficiency:
    
    - Short questions, short confirmations, no long essays by default.ieeexplore.ieee+1
        

How to test:

- Create a list of example conversations in Obsidian (e.g. `tests_appointment_brain.md`):
    
    - “I’m from Manila, can I book today at 3 PM?”
        
    - “I’m in London. Can I book at 10 AM my time?”
        
    - “Can I book a 1-hour session?” (Expected: Claude explains 5–20 minute limit and offers options.)
        
- Run these scenarios with Claude and see if it behaves correctly.
    
- If something fails or is confusing, update your rules or prompt.
    

Why this matters:

- Studies on AI appointment systems show the best results come from iterative design with user feedback and testing.ieeexplore.ieee+2
    

## Step 3 – Set up your notifications (Discord webhook and email)

Goal: Make sure that once Claude confirms an appointment, you get notified immediately.

What you need:

- A small backend (for example, serverless functions on Vercel).
    
- A Discord webhook URL.
    

Flow:

- Claude creates a compact booking object and a short human summary.
    
- Your backend receives that object.
    
- The backend sends a Discord message like:
    
    - “New appointment: [Name], [Service], [PH time], [Duration], [Contact].”
        
- Later you can add email notifications too.
    

Why this matters:

- Modern scheduling tools emphasize “instant notifications and confirmations” as a key feature for small businesses.adminify+2
    

## Step 4 – Document everything in Obsidian

Goal: Treat your project like a real product with a clear knowledge base.

Suggested notes:

- `vision.md` – plain-language description of what the assistant does and who it helps.
    
- `scheduling_rules.md` – all your business rules (time, duration, limits).
    
- `appointment_brain_prompt.md` – the prompt you give to Claude.
    
- `integration_spec_discord.md` – how the JSON output maps to Discord.
    
- `lessons_learned.md` – what went wrong and how you fixed it.
    

Use Claude as a “critic”:

- After you update any document, ask Claude to:
    
    - Check for contradictions or missing details.
        
    - Suggest edge cases you haven’t covered.## Step 5 – Design a simple, friendly interface

Goal: Make the system understandable and usable for non-technical users.

With Grok (or any design tool), focus on:

- A simple chat box that says:
    
    - “Tell us what appointment you’d like to book.”
        
- One thing per screen / step:
    
    - Step-by-step questions for non-technical users.
        
- Clear labels:
    
    - “Your time” vs. “Philippines time”.
        
- No technical jargon (“webhook”, “token”, etc.).
    

This kind of simple, outcome-focused interface has been shown to help non-technical users adopt AI tools more easily.iacis+2

## Step 6 – Iterate and expand

Once appointment scheduling is stable:

- Add features like:
    
    - FAQs and support questions.
        
    - Product/service recommendations.
        
    - Summaries for you (recurring issues, common times, etc.).
        
- Keep the same pattern:
    
    - Define rules → update Claude brain → test → document → deploy.