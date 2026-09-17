---
name: fleetbase-webhooks
description: Real-time event handling: WebSocket subscriptions for order/driver events
version: 1.0.0
author: Coach (auto-generated from fleetbase/fleetbase)
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [auto-generated, coach, fleetbase, integration]
    source: https://github.com/fleetbase/fleetbase
---

# Fleetbase Webhooks

## When to use

Real-time event handling: WebSocket subscriptions for order/driver events

## Tools

- `fleetbase-webhook-subscribe`
- `fleetbase-webhook-handle`

## Workflow

1. Initialize Fleetbase client with API key
2. Execute the relevant tool
3. Handle response or error
4. Log result

## Error handling

- API key invalid → check dashboard, regenerate
- Order not found → verify order ID and tenant context
- WebSocket disconnect → reconnect, resume from last event ID
