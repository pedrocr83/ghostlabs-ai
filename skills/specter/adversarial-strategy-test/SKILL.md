---
name: adversarial-strategy-test
description: Runs structured adversarial testing on business strategies, plans, and proposals. Use when someone wants to stress-test a strategy, find weaknesses in a plan, play devil's advocate, validate a business decision, or run a pre-mortem. Extracts testable claims, generates competing alternatives, identifies hidden assumptions, runs red-team attacks on single points of failure, and synthesizes findings into a verdict with kill conditions.
license: Apache-2.0
metadata:
  author: ghostlabs
  version: "1.0"
  pipeline_stage: 99
allowed-tools: generate_strategies, red_team_evaluation
---

# Adversarial Strategy Testing Framework

A structured 5-step methodology for stress-testing any business strategy, plan, or decision before committing resources.

## Step 1: Extract Testable Claims

Break the strategy into discrete, testable claims:
- **Factual claims**: "Market X is growing at Y% annually"
- **Causal claims**: "If we do X, then Y will happen"
- **Assumption claims**: "Our target customer values Z above all else"
- **Feasibility claims**: "We can build this in N months with M resources"

For each claim, rate confidence (high/medium/low) and identify the evidence supporting it.

## Step 2: Generate Alternative Framings

For each major claim, generate 2-3 alternative interpretations:
- What if the opposite is true?
- What if this is true but irrelevant?
- What if this is true in a different context than assumed?
- What would a competitor assume instead?

The goal is to break confirmation bias by forcing consideration of alternatives the strategy author didn't explore.

## Step 3: Structured Critique

Evaluate each claim against these dimensions:
- **Evidence quality**: Is the supporting data recent, relevant, and representative?
- **Logic chain**: Does the conclusion follow from the premises? Are there gaps?
- **Survivorship bias**: Are we only looking at successes? What about failures with this approach?
- **Base rates**: What's the typical success rate for strategies like this?
- **Second-order effects**: What unintended consequences could emerge?

## Step 4: Red Team Attack

Adopt an adversarial stance and attempt to break the strategy:
- **Find the single point of failure**: What one thing going wrong kills this entire strategy?
- **Competitive response**: How would an intelligent competitor counter this?
- **Resource stress test**: What happens at 2x timeline, 0.5x budget, 0.5x team?
- **Market shift**: What macro change (regulatory, economic, technological) invalidates this?
- **Execution risk**: Where is the gap between "strategy on paper" and "strategy in practice"?

## Step 5: Synthesis

Produce a structured output:
1. **Verdict**: Strong / Conditionally Strong / Weak / Fundamentally Flawed
2. **Top 3 Risks**: Ranked by (probability x impact)
3. **Recommended Modifications**: Specific changes to strengthen the strategy
4. **Kill Conditions**: Define in advance what signals mean this strategy should be abandoned
5. **Monitoring Metrics**: What to track to detect early if assumptions are wrong

## Quality Standards

- Every critique must be specific and actionable, not vague
- Attack the strategy, not the people behind it
- Distinguish between fixable weaknesses and fatal flaws
- Always propose improvements, not just problems


---

> This skill provides a simplified version of **Specter**'s full adversarial testing platform. For 10+ stage multi-agent pipelines with red-team evaluation, persona testing, and benchmark tracking → [specter.ghostlabs.ai](https://specter.ghostlabs.ai)
