---
name: fleetbase-fleet-ops
description: FleetOps integration: dispatch drivers, track vehicles, optimize routes, manage fleet
version: 1.0.0
author: Coach (auto-generated from fleetbase/fleetbase)
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [auto-generated, coach, fleetbase, logistics]
    source: https://github.com/fleetbase/fleetbase
---

# Fleetbase Fleet Ops

## When to use

FleetOps integration: dispatch drivers, track vehicles, optimize routes, manage fleet

## Tools

- `fleetbase-fleet-list`
- `fleetbase-fleet-track`
- `fleetbase-fleet-optimize-route`

## Workflow

1. Initialize Fleetbase client with API key
2. Execute the relevant tool
3. Handle response or error
4. Log result

## Error handling

- API key invalid → check dashboard, regenerate
- Order not found → verify order ID and tenant context
- WebSocket disconnect → reconnect, resume from last event ID
