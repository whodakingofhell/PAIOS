- In Obsidian, maintain specific docs:
    
    - `scheduling_rules.md` – your current operating hours, buffers, limits, etc.
        
    - `services_catalog.md` – list of services, durations, and any special constraints.
        
    - `integration_spec.md` – how the Discord webhook expects payloads.
        
- For each doc you update, run a **“document challenge” session** with Claude:
    
    - Ask Claude (with the brain prompt loaded):
        
        - “Check this rules document for contradictions, missing cases, and edge scenarios.”
            
        - “Propose test cases that might break this logic.”
            
    - Claude then:
        
        - Highlights conflicts (e.g., overlapping hours, impossible constraints).
            
        - Suggests edge-case scenarios (multiple time zones, last-minute bookings, etc.).
            
        - Helps refine the rules until they are consistent and testable.