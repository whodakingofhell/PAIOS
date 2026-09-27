---
name: iot-claw-integration
description: >
  IoT-Claw smart home integration — conversational device control,
  MQTT/Zigbee/Home Assistant, ESP32 flashing, OpenCV security,
  autonomous claw sandbox, drag-and-drop workflows.
version: 1.0.0
author: PAIOS (scanned & verified by Security Head)
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [iot, smart-home, mqtt, esp32, home-assistant, zigbee, security]
    category: smart-home
    security_clearance: passed
---

# IoT-Claw Integration

## When to use

Use for smart home automation, IoT device control, ESP32 flashing,
MQTT/Zigbee/Home Assistant integration, voice-controlled devices.

## Security Scan Results

| Check | Result |
|---|---|
| Hardcoded secrets | ✅ None |
| Code injection (eval/exec) | ✅ None |
| CORS | ✅ localhost only |
| Telegram bot | ✅ HTML escaping |
| MQTT auth | ✅ Env vars |
| Dependencies | ✅ Standard, up-to-date |

## Integration Points

- MQTT broker (port 1883)
- Home Assistant WebSocket
- Zigbee2MQTT bridge
- Telegram bot (optional)
- OpenCV security cameras
- ESP32 Web Serial flashing

## Setup

```bash
cd backend && python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --port 8000 --reload
```

## Coach Learning Source

Skills Bot should learn from:
- Autonomous agent patterns (self-improving sandbox)
- Edge compilation (visual → MicroPython)
- MQTT pub/sub architecture
- Telegram bot integration patterns