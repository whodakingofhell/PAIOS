---
name: fleetbase-orders
description: Order management: create orders, schedule deliveries, track status, proof of delivery
version: 1.0.0
author: Coach (auto-generated from fleetbase/fleetbase)
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [auto-generated, coach, fleetbase, dispatch]
    source: https://github.com/fleetbase/fleetbase
---

# Fleetbase Orders

## When to use

Order management: create orders, schedule deliveries, track status, proof of delivery

## Tools

- `fleetbase-order-create`
- `fleetbase-order-schedule`
- `fleetbase-order-track`
- `fleetbase-order-pod`

## Workflow

1. Initialize Fleetbase client with API key
2. Execute the relevant tool
3. Handle response or error
4. Log result

## Error handling

- API key invalid → check dashboard, regenerate
- Order not found → verify order ID and tenant context
- WebSocket disconnect → reconnect, resume from last event ID
