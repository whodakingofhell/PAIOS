---
name: eve-bridge
description: >
  Direct communication bridge between Hermes and EVE Telegram bot.
  Hermes receives directions from EVE, executes, reports back.
  Permission requests go through EVE to user for approval.
version: 1.0.0
author: PAIOS (Hermes-EVE Alignment)
platforms: [windows]
metadata:
  hermes:
    tags: [telegram, eve, bridge, alignment, communication]
    category: communication
    assigned_to: hermes-admin
---

# EVE Bridge — Hermes ↔ EVE Direct Communication

## When to use

Use when:
- User sends direction via EVE Telegram bot
- Hermes needs to report status to user via EVE
- Permission request needs to go to user via EVE
- Options/recommendations need user decision

## Alignment Rules

### EVE → Hermes (direction)
1. EVE receives user message
2. Forwards direction to Hermes
3. Hermes acknowledges
4. Hermes gathers data, analyzes, executes
5. Hermes reports results to EVE

### Permission Flow (Hermes → EVE → User)
1. Hermes detects action needs permission
2. Sends permission request to EVE with options
3. EVE presents to user
4. User responds via EVE
5. EVE confirms to Hermes → Hermes proceeds or aborts

### Auto-Execute (no permission needed)
- Research queries
- Analysis tasks
- Read-only operations
- Skill creation
- Testing/verification

### Requires Permission
- Database drops
- File deletions
- API key changes
- System reconfiguration
- Dependency installations
- Docker container changes

## Communication Format

### Direction from EVE
```
@hermes [ACTION]: <what to do>
@hermes [PERMISSION]: <what needs approval>
@hermes [OPTION]: <choice needed>
```

### Report from Hermes
```
[Hermes] Status: ✅/⚠️/❌
[Hermes] Action: <what was done>
[Hermes] Result: <outcome>
[Hermes] Next: <recommendation>
```

### Permission Request
```
[Hermes] PERMISSION NEEDED:
  Action: <what>
  Risk: <low/medium/high>
  Options:
    1. <option>
    2. <option>
  Recommend: <which>
```

## Current Pending Items (for user via EVE)
1. API Keys — Update for Strix pentest
2. Fleetbase SDK — npm install
3. Agent Reach Cookies — Twitter/Reddit unlock
4. Brave API Key — Search MCP
5. PostgreSQL URL — Database MCP
6. Strix Model — Confirm LLM provider