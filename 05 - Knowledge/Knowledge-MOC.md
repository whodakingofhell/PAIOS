---
tags:
  - paios/moc
  - paios/knowledge
related:
  - "AI/08-AI-Knowledge.md"
  - "AI/AI-Engineering.md"
  - "AI/MASTER-FRAMEWORK.md"
  - "AI/Claude-Handoff.md"
  - "AI/Claude Master Prompt - Online Seller Support and Retail Assistant.md"
  - "Architecture/03-Architecture.md"
  - "Architecture/Architecture.md"
  - "Architecture/SECURITY_ARCHITECTURE.md"
  - "Business/01-Business.md"
  - "Business/10-Marketing.md"
  - "Business/11-Revenue.md"
  - "Business/cost-map.md"
  - "Business/Tool-Role-Mapping.md"
  - "DevOps/06-Security.md"
  - "DevOps/07-Automation.md"
  - "DevOps/Automation-Engineering.md"
  - "DevOps/DevOps.md"
  - "Product-Design/02-Product.md"
  - "Product-Design/Content-Pipeline.md"
  - "Product-Design/Feature-Score-Rubric.md"
  - "Product-Design/Product-Lifecycle.md"
  - "References/AI-Ops-Vault-Manifest.md"
  - "References/EXPERT_CRITIQUES.md"
  - "References/EXPERT_CRITIQUES_CURRENT_PROJECT.md"
  - "References/MASTER_REFERENCE.md"
  - "References/RECOMMENDATIONS.md"
  - "Software-Development/00-Vision.md"
  - "Software-Development/04-Engineering.md"
  - "Software-Development/05-QA-Framework.md"
  - "Software-Development/09-Documentation.md"
  - "Software-Development/12-Roadmap.md"
  - "Software-Development/Backend.md"
  - "Software-Development/Database.md"
  - "Software-Development/Frontend.md"
  - "Software-Development/QA-Criticism-Framework.md"
  - "Software-Development/QA.md"
  - "Software-Development/Security.md"
---

# Knowledge Map of Content

## Purpose

Route curated technical, research, product, business, and learning knowledge.

## Quick Index

| Category | Files |
|----------|-------|
| **AI** | [[AI/08-AI-Knowledge.md]], [[AI/AI-Engineering.md]], [[AI/MASTER-FRAMEWORK.md]], [[AI/Claude-Handoff.md]], [[AI/Claude Master Prompt - Online Seller Support and Retail Assistant.md]] |
| **Architecture** | [[Architecture/03-Architecture.md]], [[Architecture/Architecture.md]], [[Architecture/SECURITY_ARCHITECTURE.md]] |
| **Business** | [[Business/01-Business.md]], [[Business/10-Marketing.md]], [[Business/11-Revenue.md]], [[Business/cost-map.md]], [[Business/Tool-Role-Mapping.md]] |
| **DevOps** | [[DevOps/06-Security.md]], [[DevOps/07-Automation.md]], [[DevOps/Automation-Engineering.md]], [[DevOps/DevOps.md]] |
| **Product Design** | [[Product-Design/02-Product.md]], [[Product-Design/Content-Pipeline.md]], [[Product-Design/Feature-Score-Rubric.md]], [[Product-Design/Product-Lifecycle.md]] |
| **References** | [[References/MASTER_REFERENCE.md]], [[References/EXPERT_CRITIQUES.md]], [[References/EXPERT_CRITIQUES_CURRENT_PROJECT.md]], [[References/RECOMMENDATIONS.md]], [[References/AI-Ops-Vault-Manifest.md]] |
| **Software Development** | [[Software-Development/00-Vision.md]], [[Software-Development/04-Engineering.md]], [[Software-Development/05-QA-Framework.md]], [[Software-Development/09-Documentation.md]], [[Software-Development/12-Roadmap.md]], [[Software-Development/Backend.md]], [[Software-Development/Database.md]], [[Software-Development/Frontend.md]], [[Software-Development/QA.md]], [[Software-Development/Security.md]], [[Software-Development/QA-Criticism-Framework.md]] |

## Category Cross-References

- **Vision → Roadmap**: [[Software-Development/00-Vision.md]] → [[Product-Design/02-Product.md]] → [[Software-Development/12-Roadmap.md]]
- **Business → Revenue**: [[Business/01-Business.md]] → [[Business/10-Marketing.md]] → [[Business/11-Revenue.md]]
- **Architecture → Engineering**: [[Architecture/03-Architecture.md]] → [[Software-Development/04-Engineering.md]] → [[Architecture/SECURITY_ARCHITECTURE.md]]
- **Security**: [[Software-Development/Security.md]] → [[DevOps/06-Security.md]] → [[Architecture/SECURITY_ARCHITECTURE.md]]
- **QA**: [[Software-Development/05-QA-Framework.md]] → [[Software-Development/QA.md]] → [[Software-Development/QA-Criticism-Framework.md]] → [[Product-Design/Feature-Score-Rubric.md]]
- **AI Ops**: [[AI/08-AI-Knowledge.md]] → [[AI/AI-Engineering.md]] → [[AI/MASTER-FRAMEWORK.md]] → [[AI/Claude-Handoff.md]]
- **DevOps & Automation**: [[DevOps/DevOps.md]] → [[DevOps/07-Automation.md]] → [[DevOps/Automation-Engineering.md]]
- **Product Pipeline**: [[Product-Design/02-Product.md]] → [[Product-Design/Content-Pipeline.md]] → [[Product-Design/Product-Lifecycle.md]] → [[Product-Design/Feature-Score-Rubric.md]]

## Workflow

`Capture → Verify → Connect → Apply → Review`

## Rules

- Prefer primary sources.
- Separate facts, interpretation, and open questions.
- Store durable synthesis, not raw source dumps.
- New content goes through [[../06 - Inbox/Inbox.md]] → processed to relevant Knowledge area.

## Health & Maintenance

```dataview
TABLE tags, related, file.etags as "All Tags"
FROM "05 - Knowledge"
SORT file.name
```

```dataview
TABLE length(related) as "Related Links", file.etags as "Tags"
FROM "05 - Knowledge"
WHERE length(related) = 0 OR length(file.etags) = 0
SORT file.name
```

