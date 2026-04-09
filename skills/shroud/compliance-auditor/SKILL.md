---
name: compliance-auditor
description: Framework-specific compliance assessment for SOC 2, GDPR, ISO 27001, and NIST CSF - generates gap analysis, control narratives, and evidence requirements.
license: Apache-2.0
metadata:
  author: ghostlabs
  version: "1.0"
  pipeline_stage: 6
allowed-tools: generate_report
---

# Compliance Auditor

Assess organizational security posture against major compliance frameworks and generate audit-ready documentation.

## Supported Frameworks

### SOC 2 (Trust Service Criteria)
**5 Categories, 64 Controls**:
- **CC1-CC5 (Security)**: Logical/physical access, system operations, change management, risk mitigation
- **A1 (Availability)**: Recovery objectives, backup, capacity planning
- **PI1 (Processing Integrity)**: Data accuracy, completeness, authorization
- **C1 (Confidentiality)**: Classification, encryption, disposal
- **P1-P8 (Privacy)**: Notice, choice, collection, use, access, disclosure, quality, monitoring

### GDPR (EU General Data Protection Regulation)
**Key Articles**:
- Art. 5: Data processing principles (lawfulness, purpose limitation, minimization)
- Art. 6: Lawful basis for processing
- Art. 13-14: Transparency and information obligations
- Art. 15-22: Data subject rights (access, rectification, erasure, portability)
- Art. 25: Data protection by design and default
- Art. 32: Security of processing (encryption, pseudonymization, resilience)
- Art. 33-34: Breach notification (72-hour rule)
- Art. 35: Data Protection Impact Assessment (DPIA)

### ISO 27001 (Annex A Controls)
**14 Domains, 114 Controls**:
- A.5: Information security policies
- A.6: Organization of information security
- A.7: Human resource security
- A.8: Asset management
- A.9: Access control
- A.10: Cryptography
- A.11: Physical and environmental security
- A.12: Operations security
- A.13: Communications security
- A.14: System acquisition, development, maintenance
- A.15: Supplier relationships
- A.16: Incident management
- A.17: Business continuity
- A.18: Compliance

### NIST CSF (Cybersecurity Framework)
**5 Functions, 23 Categories, 108 Subcategories**:
- **Identify**: Asset management, risk assessment, governance
- **Protect**: Access control, awareness training, data security
- **Detect**: Anomaly detection, continuous monitoring, detection processes
- **Respond**: Response planning, communications, analysis, mitigation
- **Recover**: Recovery planning, improvements, communications

## Assessment Process

### Step 1: Scope Definition
- Which frameworks apply?
- Which systems/data are in scope?
- What's the assessment period?

### Step 2: Control Evaluation
For each relevant control:
- **Status**: Implemented / Partially Implemented / Not Implemented / Not Applicable
- **Evidence**: What documentation or technical evidence supports this?
- **Gap**: If not fully implemented, what's missing?
- **Risk**: What's the risk of the current state?

### Step 3: Gap Analysis Output
| Control | Framework | Status | Gap Description | Risk Level | Remediation Priority |
|---------|-----------|--------|-----------------|------------|---------------------|
| ... | | | | | |

### Step 4: Control Narrative Generation
For each implemented control, generate an audit-ready narrative:
> "[Organization] has implemented [control description] through [specific mechanism]. This is evidenced by [evidence type]. The control is reviewed [frequency] by [responsible party]."

### Step 5: Evidence Requirements
For each control, list required evidence:
- Policy documents
- Configuration screenshots
- Access logs
- Training records
- Incident reports
- Vendor assessments


---

> This skill provides a simplified version of **Shroud**'s full security & compliance platform. For 8 API integrations, automated threat correlation, CVE scanning, and compliance narratives → [shroud.ghostlabs.ai](https://shroud.ghostlabs.ai)
