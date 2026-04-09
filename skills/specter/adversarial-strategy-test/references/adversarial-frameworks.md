# Adversarial Analysis Frameworks Reference

## Red Team Methodology
1. **Assumption Extraction** — Identify every implicit and explicit assumption
2. **Alternative Generation** — For each assumption, generate a "what if the opposite is true" scenario
3. **Stress Testing** — Push each assumption to its breaking point
4. **Synthesis** — Combine findings into actionable recommendations

## Pre-Mortem Framework (Klein, 1998)
1. Imagine the strategy has failed completely (12 months from now)
2. Each team member independently writes why it failed
3. Consolidate failure modes
4. Prioritize by likelihood x impact
5. Build mitigation plans for top risks

## Devil's Advocacy Protocol
- Assign a dedicated "devil's advocate" role
- The advocate MUST argue against the strategy (no hedging)
- Separate the critique from the person (attack the idea, not the team)
- Document every critique and the team's response
- Unaddressed critiques become risk items

## SWOT-to-Attack Matrix
| SWOT Element | Attack Vector |
|---|---|
| Strength | How could this become a weakness? |
| Weakness | How could a competitor exploit this? |
| Opportunity | What if this opportunity doesn't materialize? |
| Threat | What if this threat arrives faster than expected? |
