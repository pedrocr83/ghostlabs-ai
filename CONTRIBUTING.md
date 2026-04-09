# Contributing to GhostLabs AI

We welcome contributions of new skills and improvements to existing ones.

## Contributing a Skill

1. Fork this repo
2. Create your skill directory under the appropriate product folder (or `skills/community/`)
3. Follow the SKILL.md format:

```yaml
---
name: your-skill-name
description: Clear description with trigger contexts (max 1024 chars)
license: Apache-2.0
metadata:
  author: your-name
  version: "1.0"
allowed-tools: []
---

# Your Skill Title

Instructions here...
```

4. Keep SKILL.md under 500 lines (~5000 tokens)
5. Move detailed references to `references/` or `REFERENCE.md`
6. Add executable scripts to `scripts/` (they run via bash, output only — code never enters context)
7. Submit a PR

## Security

All community skills are security-audited before activation. The audit checks for:
- Prompt injection patterns ("ignore previous instructions", etc.)
- Credential/environment variable harvesting
- Outbound network calls in scripts
- Excessive permission requests

Skills with critical issues are rejected. Skills with warnings are flagged for review.

## Quality Guidelines

- One clear purpose per skill
- Front-load the description with what the skill does
- Include specific trigger contexts in the description
- Provide concrete examples with expected inputs/outputs
- Challenge every line: "Does the AI need this, or does it already know this?"

## Contributing an MCP Server

MCP server contributions are reviewed more carefully due to security implications. Please open an issue first to discuss the proposed server before submitting a PR.

## License

By contributing, you agree that your contributions will be licensed under the Apache 2.0 License.
