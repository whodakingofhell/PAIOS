---
tags:
  - paios/knowledge
  - paios/devops
  - paios/testing
related:
  - "Monitoring-Observability.md"
  - "CI-CD-Pipeline.md"
  - "../Software-Development/Testing-Lifecycle.md"
  - "../Software-Development/04-Engineering.md"
---

# Performance Testing

## Types

### Load Testing
- Simulate expected concurrent users (e.g., 500 users over 10 min)
- Measure: response time p50/p95/p99, error rate, throughput (req/s)
- Goal: verify performance meets SLA under normal load

### Stress Testing
- Increase load until system breaks (e.g., 500 → 1000 → 2000 users)
- Find the breaking point: at what concurrency do errors spike?
- Goal: understand capacity ceiling and failure mode

### Endurance Testing
- Sustained load over hours or days
- Detect memory leaks, DB connection pool exhaustion, disk fill
- Goal: verify long-term stability

### Spike Testing
- Sudden traffic surge (e.g., 50 users → 500 users in 10 seconds)
- Test auto-scaling response and recovery time
- Goal: handle viral/event-driven traffic patterns

## Key Metrics
| Metric | Target | What it tells you |
|--------|--------|-------------------|
| p50 latency | <200ms | Typical user experience |
| p95 latency | <500ms | Slow tail (1 in 20 users) |
| p99 latency | <1s | Worst-case acceptable |
| Error rate | <0.1% | System reliability |
| Throughput | varies | Capacity in req/s |
| CPU % | <70% | Compute headroom |
| Memory % | <80% | Leak detection |
| DB connections | <80% pool | Connection starvation |

## Tools
- **k6** — scriptable, CLI-based, CI-friendly (recommended)
- **Locust** — Python-based, distributed
- **Artillery** — Node.js-based
- **JMeter** — GUI + CLI (legacy but comprehensive)

## Process
1. Define test scenarios (most common user journeys — e.g., login, search, checkout)
2. Set baseline (test performance BEFORE any optimization)
3. Run tests against staging environment (mirrors production)
4. Record results and identify bottlenecks
5. Optimize (DB queries → caching → code → infra) in that order
6. Re-run to verify improvement
7. Document results in project memory

## Common Bottlenecks (in order of likelihood)
1. N+1 database queries (ORM misuse)
2. Missing database indexes
3. Not caching repeatable computations
4. Synchronous calls to slow external services
5. Large payloads (unpaginated API responses, unoptimized images)
6. Blocking the event loop (Node.js) or thread pool (other runtimes)
7. Memory leaks under sustained load
