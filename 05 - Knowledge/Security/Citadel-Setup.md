# Citadel Security Setup

> Zero-trust security guard for your personal network. Last updated: 2026-08-15

## Current Status

- **Running:** Yes (PID 1740)
- **Port:** 8443
- **Health:** `http://127.0.0.1:8443/healthz` → `{"status": "ok"}`
- **Web UI:** `https://127.0.0.1:8443` (requires auth)

## Quick Commands

Ask Jarvis:
- *"How's my security status?"* → Health score + threats
- *"Any security alerts?"* → Threat board
- *"What devices are on my network?"* → Network scan
- *"Run a self-test"* → Self-attack simulation
- *"Verify audit chain"* → Log tampering check

## Credentials

**Stored in Hermes secrets** (never in chat):
```powershell
hermes secrets set citadel_username admin
hermes secrets set citadel_password YOUR_PASSWORD
```

## Integration with Hermes

- **Skill:** `citadel` (enabled)
- **Access:** Read-only from Hermes
- **Alerts:** Can be routed to Telegram

## Self-Hosted Setup

```powershell
cd "C:\Users\My PC\OneDrive\Desktop\AI PROJECTS\citadel"
python run.py --port 8443
```

## References

- **GitHub:** `whodakingofhell/citadel` (private repo)
- **Local:** `C:\Users\My PC\OneDrive\Desktop\AI PROJECTS\citadel\`
