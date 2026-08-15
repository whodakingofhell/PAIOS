---
tags:
  - paios/knowledge
  - paios/devops
  - paios/monitoring
related:
  - "CI-CD-Pipeline.md"
  - "Performance-Testing.md"
  - "DevOps.md"
  - "../Software-Development/Project-Phases.md"
  - "../Architecture/03-Architecture.md"
---

# Monitoring & Observability

## Three Pillars

### 1. Logs (what happened)
- Structured logs (JSON format): timestamp, level, service, request_id, message, context
- Levels: DEBUG, INFO, WARN, ERROR, FATAL
- Centralized: ship to Loki, Elasticsearch, or CloudWatch
- Retention: 30 days hot, 1 year cold archive
- Never log: passwords, tokens, PII (mask or omit)

### 2. Metrics (how many, how fast, how often)
- RED method: Rate (requests/sec), Errors (error rate %), Duration (latency p50/p95/p99)
- USE method: Utilization (CPU/mem/disk %), Saturation (queue depth), Errors
- Business metrics: signups, bookings, revenue, active users
- Tools: Prometheus + Grafana (self-hosted), Datadog (SaaS), CloudWatch (AWS)

### 3. Traces (what happened where)
- Distributed tracing across services (OpenTelemetry standard)
- Each request gets a trace_id propagated across all services
- Spans per operation: DB query, external API call, function execution
- Tools: Jaeger, Tempo, Datadog APM

## Alerting
- Alert on: error rate spike, latency p99 breach, service down, certificate expiry
- Avoid alert fatigue: no alerts for single errors, only sustained problems
- Severity levels:
  - P0: service down, data loss — alert immediately (call/chat)
  - P1: major feature broken — alert within 15 min
  - P2: minor issue — alert within 4 hours
  - P3: cosmetic — fix in next sprint
- Runbook: each alert must link to a runbook with diagnosis + remediation steps

## Dashboards
- **Service Overview**: request rate, error rate, latency, CPU/mem, DB connections
- **Business**: active users, conversion funnel, revenue, API usage by endpoint
- **Infrastructure**: host health, disk space, network I/O, deploy events
- **Security**: auth failures, rate limit hits, WAF blocks, dependency vuln count

## Health Checks
- /health endpoint: returns 200 + DB connection status, cache status, external dependency status
- /ready endpoint: is this instance ready to serve traffic? (for load balancer)
- External monitoring: Pingdom, UptimeRobot, or StatusCake (checks from outside)

## On-Call Practices
- Define escalation path: primary → secondary → manager
- Post-incident review: timeline, root cause, action items (blameless)
- Regular incident drills (simulate failure scenarios)
