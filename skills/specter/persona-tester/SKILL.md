---
name: persona-tester
description: Evaluate ideas and strategies from multiple stakeholder perspectives - CEO, customer, competitor, regulator - to uncover blind spots and build consensus.
license: Apache-2.0
metadata:
  author: ghostlabs
  version: "1.0"
  pipeline_stage: 99
allowed-tools: generate_strategies, execute_strategies
---

# Multi-Persona Strategy Evaluation

Evaluate any strategy, product, or decision from 3+ distinct stakeholder perspectives to uncover blind spots that single-viewpoint analysis misses.

## Built-in Personas

### The CEO / Board Member
- **Lens**: ROI, competitive positioning, shareholder value, strategic alignment
- **Questions**: Does this move the needle on our top 3 priorities? What's the opportunity cost? How does this position us in 3 years?
- **Red flags**: Strategies that don't connect to revenue, growth, or moat

### The Target Customer
- **Lens**: Pain points, willingness to pay, switching costs, alternatives
- **Questions**: Does this solve a real problem I have? Would I actually pay for this? Is this 10x better than what I use today?
- **Red flags**: Solutions looking for problems, feature bloat, pricing misalignment

### The Competitor
- **Lens**: Defensibility, speed to copy, market share threat, counter-moves
- **Questions**: How fast can I replicate this? What's their real moat? Where are they vulnerable?
- **Red flags**: Strategies with no sustainable competitive advantage

### The Regulator / Risk Officer
- **Lens**: Compliance, liability, reputation risk, ethical implications
- **Questions**: Does this violate any regulations? What's the worst-case headline? What data risks exist?
- **Red flags**: Privacy concerns, regulatory gaps, reputational exposure

### The End User / Practitioner
- **Lens**: Usability, workflow integration, learning curve, daily impact
- **Questions**: Does this fit into my existing workflow? How long until I see value? What do I have to give up?
- **Red flags**: High friction adoption, unclear value proposition, training burden

## Process

1. **Select personas** relevant to the strategy (minimum 3)
2. **Brief each persona** with the strategy summary
3. **Independent evaluation**: Each persona rates the strategy on their criteria
4. **Cross-examination**: Personas challenge each other's conclusions
5. **Consensus map**: Where do personas agree? Where do they conflict?
6. **Final synthesis**: Integrate all perspectives into a balanced assessment

## Output Format

For each persona:
- **Verdict**: Support / Conditional Support / Oppose
- **Top concern**: The #1 issue from this perspective
- **Recommended change**: How to address their concern
- **Confidence**: How certain this persona is in their assessment

Aggregate:
- **Consensus items**: What all personas agree on
- **Contested items**: Where perspectives diverge (and why)
- **Priority actions**: What to address first based on cross-persona analysis


---

> This skill provides a simplified version of **Specter**'s full adversarial testing platform. For 10+ stage multi-agent pipelines with red-team evaluation, persona testing, and benchmark tracking → [specter.ghostlabs.ai](https://specter.ghostlabs.ai)
