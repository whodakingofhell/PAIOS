# 🧠 Hermes Agent Skills

> 310+ reusable AI agent skills for [Hermes Agent](https://github.com/NousResearch/hermes) — covering coding, marketing, design, finance, MLOps, game development, and much more.

[![Skills](https://img.shields.io/badge/skills-310%2B-blue)](https://github.com/itgoyo/hermes-skills)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Hermes](https://img.shields.io/badge/powered%20by-Hermes%20Agent-purple)](https://github.com/NousResearch/hermes)

---

## 📖 What are Skills?

Skills are **procedural memory** for Hermes Agent — reusable step-by-step guides, proven workflows, and domain expertise that the agent loads on demand. Each skill is a `SKILL.md` file containing:

- Trigger conditions (when to use this skill)
- Numbered steps with exact commands
- Pitfalls and edge cases
- Verification steps

Skills prevent the agent from reinventing the wheel — instead of figuring out how to do something from scratch, it loads the relevant skill and follows the established workflow.

---

## 🚀 Quick Start

### 1. Install Hermes Agent

```bash
pip install hermes-agent
# or follow https://github.com/NousResearch/hermes
```

### 2. Clone this repo into your skills directory

```bash
# Backup existing skills (if any)
cp -r ~/.hermes/skills ~/.hermes/skills.bak

# Clone directly into the skills directory
git clone https://github.com/itgoyo/hermes-skills.git ~/.hermes/skills
```

### 3. Verify skills are loaded

```bash
hermes skills list
# or ask the agent: "show me available skills"
```

### 4. Use a skill

Simply ask Hermes to do something — it will automatically detect and load the relevant skill:

```
"Help me review this GitHub PR"          → loads github-code-review
"Create a Manim animation"               → loads manim-video
"Set up a fine-tuning run with Axolotl"  → loads axolotl
"Write a Xiaohongshu post"               → loads marketing-xiaohongshu-operator
```

---

## 📦 Skills Directory (310+ skills)

### 🎓 Academic (6)
| Skill | Description |
|-------|-------------|
| `academic-anthropologist` | Cultural systems, rituals, kinship, ethnographic methods |
| `academic-geographer` | Physical/human geography, climate systems, cartography |
| `academic-historian` | Historical analysis, periodization, material culture |
| `academic-narratologist` | Narrative theory, story structure, character arcs |
| `academic-psychologist` | Human behavior, personality theory, motivation |
| `academic-study-planner` | Study planning for Chinese exams (考研/考公/CPA/司法) |

### 🍎 Apple / macOS (4)
| Skill | Description |
|-------|-------------|
| `apple-notes` | Manage Apple Notes via memo CLI |
| `apple-reminders` | Manage Reminders via remindctl |
| `findmy` | Track devices/AirTags via FindMy.app |
| `imessage` | Send/receive iMessages via imsg CLI |

### 🤖 Autonomous AI Agents (5)
| Skill | Description |
|-------|-------------|
| `agent-browser` | Browser automation CLI for AI agents |
| `claude-code` | Delegate tasks to Claude Code |
| `codex` | Delegate tasks to OpenAI Codex CLI |
| `hermes-agent` | Complete Hermes Agent usage guide |
| `opencode` | Delegate tasks to OpenCode CLI |

### 🎨 Creative (9)
| Skill | Description |
|-------|-------------|
| `architecture-diagram` | Professional dark-themed system architecture diagrams |
| `ascii-art` | ASCII art with pyfiglet (571 fonts) and cowsay |
| `ascii-video` | ASCII art video production pipeline |
| `excalidraw` | Hand-drawn style diagrams via Excalidraw JSON |
| `manim-video` | Mathematical animation production pipeline |
| `p5js` | Interactive and generative visual art |
| `popular-web-designs` | 54 production-quality design systems |
| `songwriting-and-ai-music` | Songwriting craft and AI music generation (Suno) |
| `gsap` | GSAP animation reference for HyperFrames |

### 📐 Design (9)
| Skill | Description |
|-------|-------------|
| `design-brand-guardian` | Brand identity development and strategic positioning |
| `design-image-prompt-engineer` | AI image generation prompt engineering |
| `design-inclusive-visuals-specialist` | Eliminate bias in AI-generated imagery |
| `design-ui-designer` | Visual design systems and component libraries |
| `design-ux-architect` | CSS systems, layout frameworks, implementation guides |
| `design-ux-researcher` | User behavior analysis and usability testing |
| `design-visual-storyteller` | Visual communication and multimedia content |
| `design-whimsy-injector` | Inject personality and surprise into brand experiences |
| `huashu-design` | High-fidelity HTML prototypes, slides, animations |

### ⚙️ Engineering (34)
| Skill | Description |
|-------|-------------|
| `android-screenshot-share` | Android screenshot sharing workflow |
| `engineering-ai-engineer` | ML model development and deployment |
| `engineering-backend-architect` | Scalable backend systems and APIs |
| `engineering-code-reviewer` | Constructive code reviews focused on correctness |
| `engineering-devops-automator` | CI/CD pipelines and cloud automation |
| `engineering-dingtalk-integration-developer` | DingTalk open platform integration |
| `engineering-embedded-firmware-engineer` | ESP32/RTOS/Arduino firmware development |
| `engineering-feishu-integration-developer` | Feishu/Lark platform integration |
| `engineering-frontend-developer` | React/Vue/Angular and modern web |
| `engineering-git-workflow-master` | Git branching strategies and workflows |
| `engineering-mobile-app-builder` | iOS/Android native and cross-platform |
| `engineering-security-engineer` | AppSec, threat modeling, vulnerability assessment |
| `engineering-senior-developer` | Laravel/Livewire/FluxUI full-stack |
| `engineering-solidity-smart-contract-engineer` | EVM smart contracts and DeFi |
| `engineering-wechat-mini-program-developer` | WeChat Mini Program full-stack |
| *(and 19 more...)* | |

### 💰 Finance (8)
`finance-bookkeeper-controller` / `finance-financial-analyst` / `finance-financial-forecaster` / `finance-fpa-analyst` / `finance-fraud-detector` / `finance-investment-researcher` / `finance-invoice-manager` / `finance-tax-strategist`

### 🎮 Game Development (16)
| Category | Skills |
|----------|--------|
| General | `game-designer` / `game-audio-engineer` / `level-designer` / `narrative-designer` / `technical-artist` |
| Godot | `godot-gameplay-scripter` / `godot-multiplayer-engineer` / `godot-shader-developer` |
| Unity | `unity-architect` / `unity-editor-tool-developer` / `unity-multiplayer-engineer` / `unity-shader-graph-artist` |
| Unreal | `unreal-multiplayer-architect` / `unreal-systems-engineer` / `unreal-technical-artist` / `unreal-world-builder` |
| Roblox | `roblox-avatar-creator` / `roblox-experience-designer` / `roblox-systems-scripter` |

### 🐙 GitHub (7)
`github-auth` / `github-code-review` / `github-issues` / `github-pr-workflow` / `github-repo-management` / `github-repo-mining` / `codebase-inspection`

### 👥 HR (2)
`hr-performance-reviewer` / `hr-recruiter`

### ⚖️ Legal (2)
`legal-contract-reviewer` / `legal-policy-writer`

### 📣 Marketing (35)
Covers all major Chinese and global platforms:

| Platform | Skill |
|----------|-------|
| 抖音 | `marketing-douyin-strategist` |
| 小红书 | `marketing-xiaohongshu-operator` / `marketing-xiaohongshu-specialist` |
| 微信 | `marketing-wechat-operator` / `marketing-wechat-official-account` / `marketing-weixin-channels-strategist` |
| 微博 | `marketing-weibo-strategist` |
| B站 | `marketing-bilibili-strategist` |
| 快手 | `marketing-kuaishou-strategist` |
| 知乎 | `marketing-zhihu-strategist` |
| TikTok | `marketing-tiktok-strategist` |
| LinkedIn | `marketing-linkedin-content-creator` |
| Instagram | `marketing-instagram-curator` |
| Twitter/X | `marketing-twitter-engager` |
| Reddit | `marketing-reddit-community-builder` |
| 电商 | `marketing-china-ecommerce-operator` / `marketing-cross-border-ecommerce` |
| 直播 | `marketing-livestream-commerce-coach` |
| SEO | `marketing-seo-specialist` / `marketing-baidu-seo-specialist` |
| *(and more...)* | |

### 🧬 MLOps (20)
| Category | Skills |
|----------|--------|
| Inference | `vllm` / `llama-cpp` / `gguf` / `outlines` / `guidance` |
| Training | `axolotl` / `unsloth` / `peft` / `trl-fine-tuning` / `grpo-rl-training` / `pytorch-fsdp` |
| Models | `whisper` / `stable-diffusion` / `clip` / `segment-anything` / `audiocraft` |
| Evaluation | `lm-evaluation-harness` / `weights-and-biases` |
| Hub | `huggingface-hub` |
| Cloud | `modal` |
| Research | `dspy` |

### 💡 Productivity (6)
`google-workspace` / `linear` / `nano-pdf` / `notion` / `ocr-and-documents` / `powerpoint`

### 🏗️ Project Management (6)
`project-management-experiment-tracker` / `project-management-jira-workflow-steward` / `project-management-project-shepherd` / `project-management-studio-operations` / `project-management-studio-producer` / `project-manager-senior`

### 🔬 Research (6)
`arxiv` / `blogwatcher` / `llm-wiki` / `ml-paper-writing` / `polymarket` / `youtube-content`

### 💼 Sales (8)
`sales-account-strategist` / `sales-coach` / `sales-deal-strategist` / `sales-discovery-coach` / `sales-engineer` / `sales-outbound-strategist` / `sales-pipeline-analyst` / `sales-proposal-strategist`

### 🛠️ Software Development (7)
| Skill | Description |
|-------|-------------|
| `code-review` | Pre-commit verification pipeline |
| `karpathy-guidelines` | Reduce common LLM coding mistakes |
| `plan` | Plan mode — inspect context, write markdown plans |
| `subagent-driven-development` | Multi-agent implementation workflow |
| `systematic-debugging` | Structured debugging for bugs and failures |
| `test-driven-development` | TDD workflow before any feature/bugfix |
| `writing-plans` | Multi-step implementation planning |

### 🧪 Testing (9)
`testing-accessibility-auditor` / `testing-api-tester` / `testing-embedded-qa-engineer` / `testing-evidence-collector` / `testing-performance-benchmarker` / `testing-reality-checker` / `testing-test-results-analyzer` / `testing-tool-evaluator` / `testing-workflow-optimizer`

### 🏠 Smart Home (1)
`openhue` — Control Philips Hue lights via OpenHue

### 🌐 Social Media (2)
`xitter` — X/Twitter CLI client
`binance-square` — Scrape Binance Square trending topics

### 🎯 Specialized (45)
The largest category — domain-specific expert agents including:
`prompt-engineer` / `blockchain-security-auditor` / `compliance-auditor` / `government-digital-presales-consultant` / `gaokao-college-advisor` / `study-abroad-advisor` / `language-translator` / `technical-translator-agent` / `specialized-mcp-builder` / *(and 36 more)*

---

## 📁 Repository Structure

```
skills/
├── academic/
│   ├── academic-anthropologist/
│   │   └── SKILL.md
│   └── ...
├── engineering/
│   ├── engineering-backend-architect/
│   │   └── SKILL.md
│   └── ...
├── marketing/
│   └── ...
└── README.md  ← you are here
```

Each skill directory contains:
- `SKILL.md` — Main skill file (YAML frontmatter + markdown body)
- `references/` — Optional reference documents
- `templates/` — Optional reusable templates
- `scripts/` — Optional helper scripts

---

## 🔧 How to Add Your Own Skills

```bash
# Create a new skill
hermes skill create my-skill-name

# Or manually create the directory and SKILL.md
mkdir -p ~/.hermes/skills/my-category/my-skill
cat > ~/.hermes/skills/my-category/my-skill/SKILL.md << 'EOF'
---
name: my-skill
description: What this skill does
triggers:
  - when to use this skill
---

## Steps

1. First step
2. Second step
3. Verify with: `some command`
EOF
```

---

## 🤝 Contributing

1. Fork this repo
2. Add or improve a skill in the appropriate category directory
3. Make sure your `SKILL.md` includes:
   - Clear trigger conditions
   - Numbered steps with exact commands
   - A pitfalls/gotchas section
   - Verification steps
4. Submit a PR!

---

## 📄 License

MIT License — free to use, share, and modify.

---

## 🔗 Links

- [Hermes Agent](https://github.com/NousResearch/hermes) — The AI agent framework these skills are built for
- [Nous Research](https://nousresearch.com) — The team behind Hermes
- [itgoyo's GitHub](https://github.com/itgoyo) — More projects

---

*Generated and maintained with ❤️ by [Hermes Agent](https://github.com/NousResearch/hermes)*
