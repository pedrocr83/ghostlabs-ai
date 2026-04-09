# GhostLabs AI

Open-source AI tools by [GhostLabs AI](https://ghostlabs.ai) — enterprise security, lead generation, strategy testing, and business intelligence.

AI skills and MCP servers for security, lead generation, strategy testing, and business intelligence. Free tools for Claude Code, Codex, Cursor, and any MCP-compatible agent.

## What's Inside

### Skills (16 SKILL.md files)

Skills are knowledge packages that teach AI agents how to perform specialized tasks. They auto-trigger when your agent detects a matching context — no manual invocation needed.

| Product | Skill | What it does |
|---------|-------|-------------|
| **Phantom** | `icp-builder` | Build structured Ideal Customer Profiles from natural language |
| **Phantom** | `email-verifier` | 10-layer email verification methodology (syntax → DNS → SMTP) |
| **Phantom** | `b2b-cold-outreach` | Write personalized B2B outreach emails using AIDA/PAS frameworks |
| **Specter** | `adversarial-strategy-test` | Run structured adversarial testing on any strategy or plan |
| **Specter** | `persona-tester` | Evaluate ideas from multiple stakeholder perspectives |
| **Specter** | `decision-pre-mortem` | Pre-mortem analysis: imagine failure, work backwards |
| **Whisper** | `business-data-analyst` | Analyze business data like an experienced analyst |
| **Whisper** | `erp-query-assistant` | Generate safe, read-only SQL for business databases |
| **Whisper** | `primavera-specialist` | Expert Primavera ERP (PHC) database knowledge |
| **Shroud** | `security-threat-analyst` | Analyze security signals and correlate threats like a SOC analyst |
| **Shroud** | `compliance-auditor` | Assess compliance against SOC 2, GDPR, ISO 27001, HIPAA |
| **Shroud** | `domain-security-scanner` | Comprehensive domain security assessment |
| **Community** | `security-compliance` | Full NIST CSF, SOC 2, CIS Controls framework reference |
| **Community** | `sql-optimization-patterns` | SQL optimization: index hints, join strategies, pagination |
| **Community** | `attack-tree-construction` | Systematic attack tree methodology with goal decomposition |
| **Community** | `data-storytelling` | Convert data findings into compelling narrative |

### MCP Servers (5 servers, 32 tools)

MCP servers give AI agents live access to GhostLabs product APIs. Connect them to Claude Code, Codex, or any MCP-compatible client.

| Server | Tools | What it provides |
|--------|-------|-----------------|
| **ghostlabs-phantom-mcp** | 7 | Lead search, email verification, campaign management, health check |
| **ghostlabs-whisper-mcp** | 6 | Business data queries, document search, report generation, health check |
| **ghostlabs-specter-mcp** | 6 | Adversarial analysis, claim extraction, red-team evaluation, health check |
| **ghostlabs-shroud-mcp** | 8 | Domain reputation, PII scanning, CVE lookup, compliance status, health check |
| **ghostlabs-skills-mcp** | 5 | Semantic skill search, skill loading, resource access, health check |

## Quick Start

### Install Skills (Claude Code)

```bash
# Install all GhostLabs skills
claude skills add pedrocr83/ghostlabs-ai

# Or install a specific product's skills
claude skills add pedrocr83/ghostlabs-ai/skills/specter
```

Skills auto-trigger when your conversation matches their domain — no manual invocation needed.

### Connect MCP Servers

Add to your MCP client configuration (e.g., `mcp_config.json`):

```json
{
  "servers": {
    "ghostlabs-shroud": {
      "command": "python",
      "args": ["mcp-servers/ghostlabs-shroud-mcp/server.py"],
      "env": {
        "SHROUD_API_URL": "https://shroud.ghostlabs.ai/api",
        "SHROUD_API_KEY": "your-api-key"
      }
    }
  }
}
```

Each server connects to its product's API. You need a running GhostLabs instance or API key.

## How Skills + MCPs Work Together

Skills provide **expertise** (methodology, frameworks, best practices). MCPs provide **access** (live data, API calls, real-time results). Together they create a powerful combination:

```
Your AI Agent
    │
    ├── Skill: security-threat-analyst (teaches HOW to analyze threats)
    │
    └── MCP: ghostlabs-shroud (provides LIVE threat data via API)
         │
         └── Result: AI agent analyzes real security signals using expert methodology
```

| Product | Skill gives you | MCP gives you |
|---------|----------------|---------------|
| **Phantom** | ICP building, email verification methodology, outreach copywriting | Live lead search, campaign execution, email verification |
| **Whisper** | Business data analysis, KPI formulas, safe SQL patterns | Live database queries, document search, report generation |
| **Specter** | Adversarial testing methodology, persona frameworks | Pipeline execution, claim extraction, red-team evaluation |
| **Shroud** | Threat correlation methodology, compliance frameworks | Domain reputation, PII scanning, CVE lookup |

## Directory Structure

```
ghostlabs-ai/
├── skills/
│   ├── phantom/
│   │   ├── icp-builder/SKILL.md
│   │   ├── email-verifier/SKILL.md
│   │   └── b2b-cold-outreach/SKILL.md
│   ├── whisper/
│   │   ├── business-data-analyst/SKILL.md
│   │   ├── erp-query-assistant/SKILL.md
│   │   └── primavera-specialist/SKILL.md
│   ├── specter/
│   │   ├── adversarial-strategy-test/SKILL.md
│   │   ├── persona-tester/SKILL.md
│   │   └── decision-pre-mortem/SKILL.md
│   ├── shroud/
│   │   ├── security-threat-analyst/SKILL.md
│   │   ├── compliance-auditor/SKILL.md
│   │   └── domain-security-scanner/SKILL.md
│   └── community/
│       ├── security-compliance/SKILL.md
│       ├── sql-optimization-patterns/SKILL.md
│       ├── attack-tree-construction/SKILL.md
│       └── data-storytelling/SKILL.md
├── mcp-servers/
│   ├── ghostlabs-phantom-mcp/
│   ├── ghostlabs-whisper-mcp/
│   ├── ghostlabs-specter-mcp/
│   ├── ghostlabs-shroud-mcp/
│   └── ghostlabs-skills-mcp/
└── docs/
    └── getting-started.md
```

## GhostLabs Products

| Product | What it does | URL |
|---------|-------------|-----|
| **Phantom** | AI-powered B2B lead generation with 12-stage pipeline | [phantom.ghostlabs.ai](https://phantom.ghostlabs.ai) |
| **Whisper** | Enterprise AI assistant with database + document + web search | [whisper.ghostlabs.ai](https://whisper.ghostlabs.ai) |
| **Specter** | Adversarial strategy testing with multi-agent pipelines | [specter.ghostlabs.ai](https://specter.ghostlabs.ai) |
| **Shroud** | AI-native security & compliance platform | [shroud.ghostlabs.ai](https://shroud.ghostlabs.ai) |
| **Haunt** | Autonomous optimization engine (ASI-Evolve) | [haunt.ghostlabs.ai](https://haunt.ghostlabs.ai) |

## Security

- All community skills are audited for prompt injection, credential harvesting, and unauthorized network access before activation
- MCP servers validate all inputs and return structured errors instead of crashing on unexpected responses
- No PII is collected, stored, or transmitted by any skill or MCP server in this repository
- Scripts run in output-only mode — their code never enters the AI context window

## Contributing

We welcome community skills and improvements. See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

1. Fork this repo
2. Create a skill following the SKILL.md format
3. Place it in the appropriate product directory (or `skills/community/`)
4. Submit a PR

All community skills are security-audited before activation.

## License

Skills: Apache 2.0
MCP Servers: Apache 2.0
