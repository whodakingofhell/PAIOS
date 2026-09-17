---
name: fleetbase-service-quotes
description: Service quotes and pricing: estimate delivery costs, compare service types
version: 1.0.0
author: Coach (auto-generated from fleetbase/fleetbase)
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [auto-generated, coach, fleetbase, finance]
    source: https://github.com/fleetbase/fleetbase
---

# Fleetbase Service Quotes

## When to use

Service quotes and pricing: estimate delivery costs, compare service types

## Tools

- `fleetbase-quote-estimate`
- `fleetbase-quote-compare`

## Workflow

1. Initialize Fleetbase client with API key
2. Execute the relevant tool
3. Handle response or error
4. Log result

## Error handling

- API key invalid → check dashboard, regenerate
- Order not found → verify order ID and tenant context
- WebSocket disconnect → reconnect, resume from last event ID
