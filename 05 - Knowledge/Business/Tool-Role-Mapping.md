# Tool-to-Role Mapping

> Which AI tool handles which team role. Updated 2026-07-18.

---

## The Mapping

| # | Team Role | Primary Tool | Secondary Tool | Why |
|---|-----------|-------------|----------------|-----|
| 1 | **Executive** | ChatGPT | Perplexity | Strategic reasoning + real-time grounding |
| 2 | **Architecture** | Claude | OpenCode | High-judgment design + implementation |
| 3 | **Frontend** | AntiGravity IDE + Copilot | Gemini | IDE + inline completion + framework plugins |
| 4 | **Backend** | ZCode/Z.ai | Codex | GLM-5.2 large context + automation |
| 5 | **Database** | Claude | Codex | Schema design + migration scripts |
| 6 | **DevOps** | Codex | Vercel + nGrok | Ops coordination + deploy + tunneling |
| 7 | **AI Engineering** | Claude + NotebookLM | Gemini | Prompt/RAG design + research grounding |
| 8 | **Automation** | n8n | Codex | Workflow orchestration + browser automation |
| 9 | **Security** | Claude | OpenCode | Threat modeling + security code review |
| 10 | **QA** | Codex | Claude | E2E testing + Criticism Framework |

---

## Tool Inventory

| Tool | Config Location | Models Available |
|------|----------------|-----------------|
| OpenCode | `.opencode/` | big-pickle, deepseek-v4-flash-free, 200+ via Vercel |
| Claude | `.claude/` | Claude (via API) |
| Codex | `.codex/` | GPT-5.x series, plugins: Slack, Chrome, Notion, docs |
| Copilot | `.copilot/` | GitHub Copilot |
| Gemini | `.gemini/` | Gemini, plugins: Android, Chrome DevTools, Firebase |
| ZCode/Z.ai | `.zcode/` | GLM-5.2/5-Turbo, 1M context |
| AntiGravity IDE | `.antigravity-ide/` | VS Code fork, Go/Python/Ruby/C++ extensions |
| Perplexity | (web) | Sonar models |
| Obsidian | (local) | Knowledge base |
| NotebookLM | (web) | Research + audio |
| Slack | (web) | Notifications |
| Vercel | (web) | Hosting |
| nGrok | (local) | Tunneling |

---

## Gaps to Fill

| Gap | Role | Recommendation |
|-----|------|---------------|
| No DB GUI | Database | Install DBeaver or use Supabase |
| No container tooling | DevOps | Install Docker Desktop |
| No security scanner | Security | Add Snyk CLI or Semgrep |
| No testing framework | QA | Install Playwright for E2E |
| No vector DB | AI Engineering | Add ChromaDB (local, free) |
| No monitoring | DevOps | Add Sentry for error tracking |
