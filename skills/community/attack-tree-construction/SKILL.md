---
name: attack-tree-construction
description: Formal attack tree methodology for adversarial analysis - goal decomposition, AND/OR gates, probability assignment, cost-benefit calculation, and risk prioritization.
license: Apache-2.0
metadata:
  author: community
  version: "1.0"
  original_source: wshobson/attack-tree-construction
allowed-tools: red_team_evaluation, generate_strategies
---

# Attack Tree Construction

Formal methodology for decomposing a goal (or threat) into a tree of sub-goals with logical relationships, enabling systematic risk analysis.

## What is an Attack Tree?

An attack tree models how an objective can be achieved through combinations of actions. Originally developed for security (Bruce Schneier, 1999), the methodology applies to any adversarial analysis: competitive strategy, regulatory risk, market failure modes.

## Building an Attack Tree

### Step 1: Define the Root Goal
The top node is the attacker's (or failure's) objective:
- Security: "Exfiltrate customer database"
- Business: "Competitor captures 30% market share"
- Product: "User abandons onboarding"

### Step 2: Decompose into Sub-Goals
Each node decomposes into child nodes connected by:

**OR Gate**: ANY child achieves the parent goal
```
Gain Admin Access
├── OR: Steal credentials
├── OR: Exploit vulnerability
└── OR: Social engineering
```

**AND Gate**: ALL children must be achieved together
```
Exfiltrate Data
├── AND: Gain access to database
├── AND: Bypass DLP controls
└── AND: Establish exfil channel
```

### Step 3: Assign Attributes to Leaf Nodes

For each leaf (bottom-level action):

| Attribute | Scale | Description |
|-----------|-------|-------------|
| **Probability** | 0.0-1.0 | Likelihood this action succeeds |
| **Cost** | $ | Resources required by the attacker |
| **Difficulty** | 1-5 | Technical skill required |
| **Detectability** | 1-5 | How likely defenders detect this (1=easy to detect) |
| **Impact** | 1-5 | Damage if this node is achieved |

### Step 4: Calculate Composite Scores

**OR nodes**: Take the MAX probability path (attacker chooses easiest)
- Probability = max(child probabilities)
- Cost = min(child costs)
- Risk = highest risk child path

**AND nodes**: Multiply probabilities (all must succeed)
- Probability = product(child probabilities)
- Cost = sum(child costs)
- Risk = aggregate of all children

### Step 5: Identify Critical Paths

The **critical path** is the highest-probability, lowest-cost route to the root goal. This is where defenses should focus.

**Path risk score**: Probability x Impact / (Cost x Detectability)

Sort all paths by risk score. The top 3 are your priority attack vectors.

## Output Format

### Tree Notation
```
[ROOT] Achieve Goal (P=0.72, Impact=5)
├── [OR] Path A (P=0.72)
│   ├── [AND] Step A.1 (P=0.9, Cost=$100, Difficulty=1)
│   └── [AND] Step A.2 (P=0.8, Cost=$500, Difficulty=3)
├── [OR] Path B (P=0.45)
│   └── [LEAF] Step B.1 (P=0.45, Cost=$10K, Difficulty=5)
└── [OR] Path C (P=0.30)
    ├── [AND] Step C.1 (P=0.6, Cost=$200, Difficulty=2)
    └── [AND] Step C.2 (P=0.5, Cost=$300, Difficulty=2)
```

### Risk Priority Table
| Rank | Path | Probability | Impact | Cost | Risk Score | Mitigation |
|------|------|-------------|--------|------|------------|------------|
| 1 | A | 0.72 | 5 | $600 | 6.0 | [specific action] |
| 2 | B | 0.45 | 5 | $10K | 0.23 | [specific action] |
| 3 | C | 0.30 | 5 | $500 | 3.0 | [specific action] |

## Applying to Business Strategy

Replace "attack" with "competitive threat" or "failure mode":
- **Root**: "Our product fails in market"
- **Sub-goals**: Pricing undercut, feature parity achieved by competitor, regulatory change, key hire poached
- **Leaf actions**: Specific competitive moves, market shifts, internal risks
- **Analysis**: Which path has highest probability x impact? That's your strategic priority.
