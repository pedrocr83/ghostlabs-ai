---
name: data-storytelling
description: Convert data analysis findings into compelling narratives - executive summary structure, insight extraction, actionable recommendation formatting, and audience-appropriate presentation.
license: Apache-2.0
metadata:
  author: community
  version: "1.0"
  original_source: wshobson/data-storytelling
allowed-tools: database_agent_tool, synthesize_report
---

# Data Storytelling

Transform raw data analysis into clear, compelling narratives that drive action.

## The Narrative Arc

Every data story follows: **Context → Tension → Resolution**

1. **Context**: What's the situation? What does the audience already know?
2. **Tension**: What changed? What's surprising? What's at risk?
3. **Resolution**: What should we do? What happens if we act/don't act?

## Executive Summary Template

**One paragraph, 3-4 sentences:**
> [HEADLINE METRIC] has [DIRECTION] by [AMOUNT] over [PERIOD], driven primarily by [CAUSE]. This represents [CONTEXT — better/worse than benchmark, acceleration/deceleration of trend]. If current trajectory continues, [PROJECTION]. We recommend [TOP ACTION] to [EXPECTED OUTCOME].

**Example:**
> Monthly recurring revenue grew 12% QoQ to $2.4M, driven primarily by enterprise tier upgrades. This outpaces our 8% quarterly target and represents an acceleration from 7% growth last quarter. If we maintain this trajectory, we'll hit $3.2M ARR by Q4. We recommend doubling enterprise SDR headcount to capitalize on the pipeline momentum.

## Insight Hierarchy

Present findings in order of business impact, not the order you discovered them:

### Level 1: "So What?" Insights (Lead with these)
- Directly answer the business question
- Quantified impact on revenue, cost, or risk
- Require action from leadership

### Level 2: Supporting Evidence
- Data that supports Level 1 insights
- Trend context and comparisons
- Statistical significance notes

### Level 3: Methodology Notes (Appendix)
- Data sources and quality notes
- Assumptions and limitations
- Alternative interpretations

## Formatting for Impact

### Numbers
- **Use relative comparisons**: "3x faster" not "300% improvement"
- **Anchor to familiar scales**: "equivalent to losing a customer per day"
- **Round appropriately**: "$2.4M" not "$2,387,491.23"
- **Add direction**: "up 12%" not just "12%"

### Comparisons
- **vs. Previous Period**: "Revenue up 12% QoQ (vs. 7% last quarter)"
- **vs. Target**: "Churn at 4.2%, above our 3% target"
- **vs. Benchmark**: "NPS of 52, above SaaS median of 36"
- **vs. Peer**: "Growing 2x faster than industry average"

### Visualizations (When Recommending Charts)
- **Trend over time**: Line chart (never pie chart for time series)
- **Part of whole**: Stacked bar or treemap (pie only for 2-4 segments)
- **Comparison**: Horizontal bar chart (easier to read labels)
- **Distribution**: Histogram or box plot
- **Correlation**: Scatter plot
- **Single KPI**: Large number with sparkline

## Audience Adaptation

### For Executives (C-Suite / Board)
- Lead with business impact, not methodology
- 3-5 key metrics max
- Clear recommendations with expected ROI
- No jargon, no caveats in the headline

### For Managers (Operational Leaders)
- Include trend analysis and leading indicators
- Segment by team/product/region
- Actionable next steps with owners and timelines
- Flag risks that need escalation

### For Analysts (Technical Audience)
- Include methodology and statistical details
- Provide data tables alongside visualizations
- Note confidence intervals and sample sizes
- Share the queries or notebooks used

## Anti-Patterns to Avoid

| Anti-Pattern | Fix |
|-------------|-----|
| "Revenue is $2.4M" (no context) | "Revenue is $2.4M, up 12% QoQ" |
| "We found 47 insights" (data dump) | Lead with the 3 that matter |
| "As you can see..." (passive) | "This means we should..." (active) |
| Burying the lead in methodology | Start with the conclusion |
| Using averages that hide distribution | Show distribution or segments |
| Presenting correlation as causation | "Correlated with" not "caused by" |
