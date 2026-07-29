# 07 — Automation

> Section 07 of the AI Engineering OS

---

## Purpose

Defines the **automation philosophy, n8n orchestration strategy, workflow inventory, trigger patterns, error handling, and monitoring** for all automated processes. n8n (self-hosted Docker) is the central automation hub.

---

## Owner Team

**Automation Engineering** (`Team\Automation-Engineering.md`)

---

## Key Responsibilities

- Design, build, and maintain **n8n workflows** for all automated processes.
- Define **trigger patterns** (file watch, cron, webhook, manual).
- Implement **error handling and retry logic** for reliable automation.
- Monitor **workflow execution** and alert on failures.
- Maintain the **workflow inventory** (what exists, what it does, who owns it).
- Integrate all tools through n8n as the **central hub**.
- Automate the **content pipeline** end-to-end (14 stages, `Frameworks\Content-Pipeline.md`).

---

## Automation Philosophy

1. **If it repeats, automate it.** Manual work is a bug.
2. **n8n is the hub.** All tools connect through n8n. No standalone cron jobs outside n8n.
3. **Every automation has a manual fallback.** If n8n is down, a human can run the pipeline scripts directly.
4. **Fail-forward, not fail-silent.** Failures alert (Slack), log details, and allow retry. Never swallow errors.
5. **Cost-aware automation.** Every workflow has an estimated cost per execution. Free-tier usage is monitored.

---

## n8n Architecture

### Self-Hosted Docker Setup

```
┌──────────────────────────────────────┐
│           Docker Compose             │
│                                      │
│  ┌──────────┐  ┌──────────────┐     │
│  │   n8n    │  │   Postgres   │     │
│  │ :5678    │  │   :5432      │     │
│  │          │──│  (workflow   │     │
│  │          │  │   storage)   │     │
│  └──────────┘  └──────────────┘     │
│                                      │
│  Volumes:                            │
│  - n8n_data (workflow persistence)   │
│  - pipeline_data (intake/output)     │
│  - .env (secrets, mounted read-only) │
└──────────────────────────────────────┘
```

### Workflow Naming Convention

```
[domain]—[action]—[detail]

Examples:
  content—pipeline—master          (14-stage content pipeline)
  content—intake—watcher           (file watch trigger)
  content—publish—youtube          (upload + notify)
  devops—deploy—vercel             (auto-deploy on merge)
  monitoring—alert—slack           (failure notifications)
  analytics—collect—youtube       (daily analytics pull)
  analytics—feedback—knowledgebase (analytics → Obsidian)
```

---

## Workflow Inventory

### Core Workflows

| # | Workflow | Trigger | Stages | Owner |
|---|---|---|---|---|
| 1 | **YouTube Content Pipeline** (master) | Manual / cron (2x/day) | Stages 0→13 | Automation |
| 2 | **Intake Watcher** | File system watch on `Pipeline\intake\raw\` | Stage 0 only | Automation |
| 3 | **QA Gate Review** | Triggered by stage 10 completion | Stage 11 only | QA |
| 4 | **YouTube Upload + Notify** | Triggered by stage 11 pass | Stage 12 + Slack alert | Automation |
| 5 | **Analytics → Knowledge Base** | Cron (daily at midnight) | Stage 13 only | AI Engineering |
| 6 | **Deploy to Vercel** | GitHub webhook on main merge | Docker rebuild + deploy | DevOps |
| 7 | **Failure Alert** | n8n error trigger | Slack notification | DevOps |

---

## Trigger Patterns

| Pattern | Use Case | Configuration |
|---|---|---|
| **File Watch** | New intake files dropped in `raw\` or `text\` | n8n local file trigger (or OS-level watcher) |
| **Cron Schedule** | Daily analytics, periodic health checks | n8n cron node (expression) |
| **Webhook** | GitHub push/merge events | n8n webhook node + GitHub webhook config |
| **Manual** | On-demand pipeline execution | n8n manual trigger (start button) |
| **Chain** | Stage N completion triggers Stage N+1 | n8n success output → next workflow trigger |

---

## Error Handling & Retry

### Per-Node Error Handling

1. **Timeout:** Every API node has a configurable timeout (default: 30s, LLM calls: 120s).
2. **Retry:** On transient failure (429, 5xx), retry with exponential backoff (1s, 2s, 4s, 8s — max 3 retries).
3. **Circuit breaker:** If a node fails 5 consecutive times, pause the workflow and alert Slack.
4. **Dead letter queue:** Failed stage outputs go to `Pipeline\intake\processed\errors\` with error detail JSON.

### Per-Workflow Error Handling

1. **Logging:** Every workflow execution writes `status`, `duration`, `error` to n8n execution log.
2. **Alerting:** On failure → Slack message with workflow name, stage, error, and retry link.
3. **Manual recovery:** Failed workflows can be resumed from the failed node (no re-run from start).

---

## Monitoring

### Metrics to Track

| Metric | Source | Alert Threshold |
|---|---|---|
| Workflow execution count | n8n stats | N/A (track volume) |
| Workflow failure rate | n8n execution logs | >5% in any 24h window |
| Pipeline end-to-end duration | n8n execution timestamps | >45 min |
| LLM API call count | n8n node execution logs | >80% of free-tier quota |
| Disk space (pipeline data) | OS-level | <10GB free |
| Docker container health | Docker health check | Container down >5 min |

### Dashboard

n8n's built-in execution log + custom Slack alerts. For Phase 2+, add Grafana + Prometheus (optional upgrade).

---

## Inputs

- Architecture decisions (`03-Architecture\Architecture.md`)
- Content pipeline specification (`Frameworks\Content-Pipeline.md`)
- Tool configurations (`integrations\*`)
- Security constraints (`06-Security\Security.md`)

---

## Outputs

- This automation document (source of truth for all automation decisions)
- n8n workflow JSON files (`Pipeline\n8n-workflows\`)
- Pipeline stage scripts (`Pipeline\scripts\`)
- Monitoring and alerting configuration
- Workflow inventory (this doc)

---

## Operating Principles

1. **n8n is the single hub.** No standalone cron, no ad-hoc scripts run outside n8n (except manual fallback).
2. **Every automation has a test.** n8n workflows are tested with sample data before production use.
3. **Cost per execution is known.** Each workflow documents its API call cost and frequency.
4. **Alert on failure, not on success.** Slack alerts are for problems. Success is assumed.
5. **Version workflows.** Workflow JSON files are in Git. Changes are reviewed like code.

---

## Acceptance Criteria

- [ ] n8n Docker architecture is defined with volumes and env mounting.
- [ ] Workflow naming convention is established and followed.
- [ ] Workflow inventory lists all 7+ core workflows with triggers and owners.
- [ ] Error handling pattern is defined (retry, circuit breaker, dead letter).
- [ ] Monitoring metrics are specified with alert thresholds.
- [ ] Content pipeline stages map to workflows.

---

## Cross-References

| Document | Relationship |
|---|---|
| `03-Architecture\Architecture.md` | Automation implements the integration architecture |
| `04-Engineering\Engineering.md` | Automation follows engineering standards |
| `06-Security\Security.md` | Automation follows security rules (secrets, audit) |
| `08-AI-Knowledge\AI-Knowledge.md` | Automation feeds the knowledge base |
| `Frameworks\Content-Pipeline.md` | The 14-stage pipeline that automation orchestrates |
| `Pipeline\n8n-workflows\` | The actual workflow JSON files |
| `Pipeline\scripts\` | The standalone fallback scripts |
