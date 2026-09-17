---
name: fleetbase-logistics
description: |
  Fleetbase integration skill. Fleetbase is an open-source modular logistics
  and supply chain operating system (LSOS). Covers dispatch, fleet management,
  live tracking, commerce, warehousing, and finance via REST API, webhooks,
  and WebSocket events.
version: 1.0.0
author: Coach (auto-generated from fleetbase/fleetbase)
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [fleetbase, logistics, supply-chain, dispatch, tracking]
    source: https://github.com/fleetbase/fleetbase
    category: logistics
---

# Fleetbase — Logistics & Supply Chain OS

## When to use

Use when your agent needs logistics, fleet, dispatch, tracking, or supply
chain capabilities. Fleetbase is the OS layer — your agent talks to its
API and Fleetbase handles the rest.

## Key modules

| Module | What it does |
|--------|--------------|
| Fleet-Ops | Dispatch drivers, track vehicles, optimize routes |
| Customer Portal | Self-service orders, quotes, invoices, support tickets |
| Storefront App | iOS/Android shop/marketplace |
| Navigator App | Driver app with dispatch, navigation, POD |
| Pallet | Warehouse & inventory (launching) |
| Ledger | Accounting, invoicing, driver wallets, P&L |

## API endpoints (core)

```bash
# Service quotes
GET /v1/service-quotes?pickup=...&dropoff=...

# Create order (ad hoc)
POST /v1/orders

# Schedule order
PATCH /v1/orders/:id/schedule {"scheduled_at": "..."}

# Proof of delivery
GET /v1/orders/:id/proofs

# Real-time driver tracking (WebSocket)
# Subscribe to driver location updates via SocketCluster
```

## SDK (JavaScript)

```javascript
import Fleetbase from '@fleetbase/sdk';
const fleetbase = new Fleetbase('<API_KEY>');
const quotes = await fleetbase.serviceQuotes.query({
  pickup: '10020 2nd Ave S, Seattle, WA',
  dropoff: '101 W Olympic Pl, Seattle, WA',
  currency: 'USD',
});
```

## CLI

```bash
npm install -g @fleetbase/cli
flb install-fleetbase
```

## Integration with PAIOS agents

- **Citadel**: Security audit for Fleetbase deployments
- **AI-Ops-Vault**: Store Fleetbase API keys securely
- **hermes-orchestrator**: Coordinate multi-agent logistics workflows
- **evelyn-brain**: Log fleet events to memory
- **composio**: Connect Fleetbase tools to other agents

## Setup

1. Get API key from Fleetbase dashboard
2. Add `FLEETBASE_API_KEY` to `.env`
3. Install SDK: `npm install @fleetbase/sdk`
4. Configure webhooks for real-time events

## Error handling

- API key invalid → check dashboard, regenerate
- WebSocket disconnect → reconnect, resume from last event ID
- Order not found → verify order ID and tenant context