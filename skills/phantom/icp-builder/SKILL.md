---
name: icp-builder
description: Builds structured Ideal Customer Profiles from natural language descriptions of target markets. Use when someone mentions ICP, ideal customer, target market, buyer persona, lead criteria, or prospect qualification. Extracts firmographic criteria, technographic signals, pain points, decision-maker maps, and generates a weighted scoring rubric for lead prioritization.
license: Apache-2.0
metadata:
  author: ghostlabs
  version: "1.0"
  pipeline_stage: 1
allowed-tools: parse_icp
---

# ICP Builder Framework

Build a comprehensive Ideal Customer Profile that goes beyond basic firmographics to include behavioral signals, pain points, and scoring criteria.

## ICP Construction Process

### 1. Market Analysis
Start by understanding the product/service being sold:
- What problem does it solve?
- Who currently buys it? (existing customer analysis if available)
- What's the typical deal size and sales cycle?
- What vertical/horizontal market does it serve?

### 2. Firmographic Criteria
Define the target company characteristics:

| Dimension | Examples | Priority |
|-----------|----------|----------|
| **Industry** | SaaS, Fintech, Healthcare, Manufacturing | Must-have |
| **Company size** | 50-500 employees, or by revenue band | Must-have |
| **Geography** | US, EU, LATAM, specific countries/cities | Must-have |
| **Growth stage** | Startup, Scale-up, Enterprise, Public | Nice-to-have |
| **Funding** | Bootstrapped, Series A-C, PE-backed, Public | Nice-to-have |
| **Revenue** | $1M-$50M ARR | Nice-to-have |

### 3. Technographic Signals
Technology stack indicators of fit:
- **Uses**: Technologies that indicate need for your product
- **Doesn't use**: Competitor products (opportunity) or incompatible tech (disqualifier)
- **Recently adopted**: Tech that creates adjacent need for your product
- **Outgrowing**: Tools they're likely to replace

Sources: BuiltWith, Wappalyzer, job postings (tech in requirements), G2/Capterra reviews

### 4. Pain Point Mapping
Connect company characteristics to specific pain points:

| ICP Segment | Primary Pain | Secondary Pain | Your Solution |
|-------------|-------------|----------------|---------------|
| Fast-growing SaaS | Scaling ops without proportional headcount | Data scattered across tools | Automation + unification |
| Enterprise | Compliance requirements increasing | Legacy tool lock-in | Modern + compliant |

### 5. Decision-Maker Identification
Define the buying committee:
- **Economic buyer**: Who controls the budget? (VP/C-level)
- **Champion**: Who will advocate internally? (Director/Manager)
- **Technical evaluator**: Who validates feasibility? (Engineer/Architect)
- **Blocker**: Who might oppose? (Procurement, IT Security)

For each role, define:
- Typical job titles (3-5 variations)
- What they care about (metrics they're measured on)
- How to reach them (LinkedIn, email, events, referrals)

### 6. Scoring Rubric
Create a weighted scoring model:

| Criterion | Weight | Score 5 | Score 3 | Score 1 |
|-----------|--------|---------|---------|---------|
| Industry match | 25% | Exact target vertical | Adjacent vertical | Unrelated |
| Company size | 20% | Sweet spot range | Edge of range | Outside range |
| Tech stack fit | 20% | Uses complementary tech | Neutral stack | Uses competitor |
| Growth signals | 15% | Recent funding + hiring | Stable growth | Declining |
| Pain indicators | 20% | Active problem search | Passive awareness | No evidence |

**Lead grades**:
- **A (Hot)**: Score >= 4.0 — prioritize for immediate outreach
- **B (Warm)**: Score 3.0-3.9 — include in campaigns
- **C (Cool)**: Score 2.0-2.9 — nurture, don't outreach
- **D (Disqualified)**: Score < 2.0 — exclude

## Output
Produce a structured ICP document with all sections above, ready to drive lead generation campaigns.


---

> This skill provides a simplified version of **Phantom**'s full autonomous lead generation pipeline. For 12-stage AI-powered prospecting with email verification, CRM sync, and intent signals → [phantom.ghostlabs.ai](https://phantom.ghostlabs.ai)
