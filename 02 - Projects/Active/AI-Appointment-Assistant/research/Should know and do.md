
From your requirements and research on AI scheduling and chatbots for small businesses, here’s the brain you’re building:vellum+4

- Understand your business:
    
    - That you offer short remote support sessions (5–20 minutes).
        
    - That your home time zone is Philippine time (Asia/Manila).
        
- Handle conversations with customers:
    
    - Detect when someone wants to book an appointment, not just ask a question.
        
    - Ask simple, clear questions to get the details (name, service, date/time, contact).
        
    - Suggest valid time options that match your working hours and rules.
        
- Handle time zones correctly:
    
    - If the customer is in the Philippines, treat their time as Asia/Manila.
        
    - If they are overseas, ask for their city/country or time zone, then convert to Asia/Manila and clearly show both times.dialzara+2
        
- Respect appointment length:
    
    - Limit each booking to 5–20 minutes to match real remote-session limits.
        
- Produce clean outputs:
    
    - After the customer confirms, send a short summary plus a small JSON object containing all booking details so your backend can trigger a Discord webhook or email.
        
- Stay efficient:
    
    - Keep messages short, ask one question at a time, and avoid long explanations unless the user asks for more detail.