---
name: decision-pre-mortem
description: Structured pre-mortem framework for business decisions - imagine the decision failed, work backwards to identify why, and build prevention plans.
license: Apache-2.0
metadata:
  author: ghostlabs
  version: "1.0"
  pipeline_stage: 99
allowed-tools: generate_strategies, solution_critique
---

# Decision Pre-Mortem Framework

Before committing to a decision, imagine it's 12 months later and the decision has failed catastrophically. Work backwards to understand why.

## Why Pre-Mortems Work

- Overcomes optimism bias (teams are 30% more likely to identify risks in pre-mortem vs. prospective analysis)
- Gives permission to voice concerns without being "negative"
- Converts vague worries into specific, addressable scenarios

## Pre-Mortem Process

### Phase 1: Set the Scene
"It is [date + 12 months]. The [decision/project/strategy] has failed. It was a significant failure — not a minor setback, but a genuine failure that cost the organization [time/money/reputation/opportunity]."

### Phase 2: Generate Failure Scenarios
Each participant independently generates reasons WHY it failed:
- **Execution failures**: What went wrong in implementation?
- **Assumption failures**: What did we believe that turned out to be false?
- **External shocks**: What market/competitive/regulatory change blindsided us?
- **People failures**: What team/leadership/culture issues derailed us?
- **Timing failures**: What was too early, too late, or poorly sequenced?

### Phase 3: Categorize and Prioritize
Group failure scenarios by:
- **Probability**: How likely is this failure mode? (1-5)
- **Impact**: How severe if it occurs? (1-5)
- **Detectability**: How early can we spot this going wrong? (1-5, where 1 = easily detected)
- **Risk Score**: Probability x Impact x Detectability

### Phase 4: Build Prevention Plans
For the top 5 risks:
1. **Early warning signal**: What's the first indicator this failure mode is materializing?
2. **Prevention action**: What can we do NOW to reduce probability?
3. **Mitigation plan**: If prevention fails, what's our response?
4. **Kill trigger**: At what point do we abandon this path entirely?
5. **Owner**: Who is accountable for monitoring this risk?

### Phase 5: Decision Gate
After the pre-mortem, one of three outcomes:
- **Proceed**: Risks are manageable, prevention plans are solid
- **Proceed with modifications**: Specific changes needed before proceeding
- **Abort**: Risks are too high or unmitigable — the pre-mortem saved us

## Output Template

| Rank | Failure Scenario | Prob | Impact | Detect | Score | Early Warning | Prevention | Owner |
|------|-----------------|------|--------|--------|-------|---------------|------------|-------|
| 1 | ... | | | | | | | |

**Decision**: Proceed / Modify / Abort
**Key modifications required**: [list]
**Review date**: [when to reassess]


---

> This skill provides a simplified version of **Specter**'s full adversarial testing platform. For 10+ stage multi-agent pipelines with red-team evaluation, persona testing, and benchmark tracking → [specter.ghostlabs.ai](https://specter.ghostlabs.ai)
