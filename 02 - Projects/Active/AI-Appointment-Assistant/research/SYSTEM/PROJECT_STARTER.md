# PERMANENT PROJECT STARTER SYSTEM

Use this template at the START of every new project. Copy, fill in, and save.

---

## STEP 0: ENVIRONMENT SETUP (Run Every Time)

```
Platform: win32
Shell: powershell
Workspace: C:\Users\My PC\OneDrive\Desktop\AI PROJECTS\Artificial Inteligence\AI\
```

### System Defaults
- **Timezone:** Asia/Manila (UTC+8, no DST)
- **Cost Target:** Free tiers only until revenue justifies paid
- **AI Brain:** Claude (primary), Perplexity (research), ChatGPT/Grok (secondary)
- **Documentation:** Obsidian-compatible Markdown
- **Hosting:** Vercel (serverless)
- **Notifications:** Discord webhooks (primary), email (secondary)

---

## STEP 1: DEFINE PROJECT (5 minutes)

Fill this out for every new project:

```yaml
project_name: ""
one_liner: ""
target_user: ""
core_pain_point: ""
solution_summary: ""
mvp_scope: ""
success_metric: ""
```

## STEP 2: DOCUMENT STRUCTURE (Create These Files)

Every project must have these Obsidian-compatible docs:

```
[Project Name]/
  vision.md              - What we're building and why
  product_brief.md       - Full product specification
  business_rules.md      - Hard constraints and logic
  master_prompt.md       - The AI brain prompt
  pipeline.md            - Step-by-step implementation plan
  token_efficiency.md    - Rules for keeping costs low
  timezone_rules.md      - If timezone conversion is needed
  tests.md               - Example conversations/scenarios
  lessons_learned.md     - What broke and how we fixed it
  architecture.md        - High-level system diagram
  expert_critiques.md    - World-expert feedback (see STEP 4)
```

## STEP 3: BUILD SEQUENCE (Order of Operations)

1. Write `vision.md` first (non-technical, plain language)
2. Write `business_rules.md` (hard constraints)
3. Build `master_prompt.md` (encode rules into AI instructions)
4. Create `tests.md` (5-10 scenarios, local + edge cases)
5. Run tests, update `lessons_learned.md`
6. Design `architecture.md` (components and data flow)
7. Set up notifications/integrations
8. Deploy MVP, iterate

## STEP 4: EXPERT CRITIQUE FRAMEWORK (Apply Before Every Launch)

Before declaring any deliverable "done," run it through these 5 expert lenses:

| Expert Role | What They Check | Red Flags |
|-------------|----------------|-----------|
| **SRE/Reliability Engineer** | Failure modes, retry logic, monitoring, fallbacks | Silent failures, no alerting, single points of failure |
| **Security Engineer** | Input validation, injection attacks, data privacy, secrets management | Exposed API keys, no rate limiting, PII logging |
| **UX Designer** | Friction points, jargon, accessibility, mobile experience | Technical language to users, too many steps, no error recovery |
| **Cost/FinOps Analyst** | Token usage, API call costs, free tier limits, scaling costs | Unbounded loops, no token budget, expensive fallback paths |
| **Domain Expert** | Business rule completeness, edge cases, legal/compliance | Missing holiday handling, no cancellation policy, no-show rules |

### How to Run Expert Critiques

For each deliverable:
1. Load the relevant document
2. Ask Claude to role-play as each expert (one at a time)
3. Expert must find at least 3 issues
4. Issues are logged in `expert_critiques.md`
5. Fix all critical issues before proceeding
6. Re-run experts after fixes to verify

## STEP 5: QUALITY GATES (Checklist Before Launch)

- [ ] All 5 expert roles have reviewed and logged feedback
- [ ] All critical issues from critiques are resolved
- [ ] At least 10 test scenarios pass (local + overseas + edge cases)
- [ ] Token usage is documented and within budget
- [ ] Failure mode for every integration is documented
- [ ] Rollback plan exists if AI behavior is wrong
- [ ] No secrets or API keys in any committed file
- [ ] Discord/email notifications are tested end-to-end
- [ ] Documentation is complete and non-technical friendly
