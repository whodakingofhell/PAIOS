---
name: fleetbase-warehouse
description: Warehouse and inventory: stock control, pick/pack workflows, fulfillment
version: 1.0.0
author: Coach (auto-generated from fleetbase/fleetbase)
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [auto-generated, coach, fleetbase, warehouse]
    source: https://github.com/fleetbase/fleetbase
---

# Fleetbase Warehouse

## When to use

Warehouse and inventory: stock control, pick/pack workflows, fulfillment

## Tools

- `fleetbase-inventory-list`
- `fleetbase-fulfillment-track`

## Workflow

1. Initialize Fleetbase client with API key
2. Execute the relevant tool
3. Handle response or error
4. Log result

## Error handling

- API key invalid → check dashboard, regenerate
- Order not found → verify order ID and tenant context
- WebSocket disconnect → reconnect, resume from last event ID
