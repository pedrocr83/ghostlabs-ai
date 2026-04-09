---
name: security-compliance
description: Comprehensive security compliance framework mappings - NIST CSF (5 functions, 23 categories), SOC 2, CIS Controls (18 controls, 3 implementation groups), ISO 27001, PCI DSS, HIPAA with incident response playbooks.
license: Apache-2.0
metadata:
  author: community
  version: "1.0"
  original_source: davila7/security-compliance
allowed-tools: correlate_threats, generate_report
---

# Security Compliance Framework Reference

Comprehensive reference for mapping security findings to compliance frameworks.

## NIST Cybersecurity Framework (CSF)

### Identify (ID)
- **ID.AM**: Asset Management — inventory hardware, software, data flows
- **ID.BE**: Business Environment — role in supply chain, critical infrastructure
- **ID.GV**: Governance — policies, legal/regulatory requirements, risk strategy
- **ID.RA**: Risk Assessment — threat identification, vulnerability analysis, risk determination
- **ID.RM**: Risk Management Strategy — risk tolerance, organizational processes
- **ID.SC**: Supply Chain Risk Management — supplier agreements, assessment, planning

### Protect (PR)
- **PR.AC**: Identity Management and Access Control — credentials, remote access, permissions
- **PR.AT**: Awareness and Training — security awareness, privileged user training
- **PR.DS**: Data Security — at-rest/in-transit protection, asset management, integrity checking
- **PR.IP**: Information Protection — configuration baselines, change control, backups, policy
- **PR.MA**: Maintenance — remote/local maintenance, tools approved
- **PR.PT**: Protective Technology — audit logs, removable media, least functionality, communications

### Detect (DE)
- **DE.AE**: Anomalies and Events — baseline operations, event analysis, impact determination
- **DE.CM**: Security Continuous Monitoring — network, physical, personnel, malware, unauthorized
- **DE.DP**: Detection Processes — roles, testing, communication, improvement

### Respond (RS)
- **RS.RP**: Response Planning — execute during/after incident
- **RS.CO**: Communications — personnel know roles, reporting, information sharing
- **RS.AN**: Analysis — investigate, understand impact, perform forensics
- **RS.MI**: Mitigation — contain, mitigate, resolve
- **RS.IM**: Improvements — incorporate lessons learned

### Recover (RC)
- **RC.RP**: Recovery Planning — execute during/after incident
- **RC.IM**: Improvements — incorporate lessons, update strategies
- **RC.CO**: Communications — manage public relations, reputation repair

## CIS Controls v8 (Top 18)

| # | Control | IG1 | IG2 | IG3 |
|---|---------|-----|-----|-----|
| 1 | Inventory and Control of Enterprise Assets | X | X | X |
| 2 | Inventory and Control of Software Assets | X | X | X |
| 3 | Data Protection | X | X | X |
| 4 | Secure Configuration | X | X | X |
| 5 | Account Management | X | X | X |
| 6 | Access Control Management | X | X | X |
| 7 | Continuous Vulnerability Management | | X | X |
| 8 | Audit Log Management | | X | X |
| 9 | Email and Web Browser Protections | | X | X |
| 10 | Malware Defenses | | X | X |
| 11 | Data Recovery | X | X | X |
| 12 | Network Infrastructure Management | | X | X |
| 13 | Network Monitoring and Defense | | | X |
| 14 | Security Awareness and Skills Training | X | X | X |
| 15 | Service Provider Management | | X | X |
| 16 | Application Software Security | | | X |
| 17 | Incident Response Management | | X | X |
| 18 | Penetration Testing | | | X |

## Incident Response Playbooks

### P0 — Critical (Active Compromise)
**Timeline**: Respond within 15 minutes
1. **Contain**: Isolate affected systems (network segmentation, disable accounts)
2. **Preserve**: Capture memory dumps, disk images, network logs before any changes
3. **Communicate**: Notify CISO, legal, PR. Begin 72-hour GDPR clock if personal data involved
4. **Investigate**: Determine scope, entry vector, lateral movement, data exfiltration
5. **Eradicate**: Remove attacker access, patch vulnerability, rotate all credentials
6. **Recover**: Restore from known-good backups, monitor for re-entry

### P1 — High (Imminent Threat)
**Timeline**: Respond within 1 hour
1. **Assess**: Determine if active exploitation is occurring
2. **Contain**: Apply temporary mitigations (WAF rules, IP blocks)
3. **Remediate**: Patch vulnerabilities, update configurations
4. **Verify**: Confirm remediation effectiveness

### P2 — Medium (Vulnerability Discovered)
**Timeline**: Remediate within 48 hours
1. **Classify**: Determine CVSS score, exploitability, asset criticality
2. **Plan**: Schedule remediation window
3. **Execute**: Apply patches or mitigations
4. **Validate**: Scan to confirm resolution

### P3 — Low (Informational)
**Timeline**: Address in next maintenance window
1. **Log**: Document finding
2. **Prioritize**: Add to remediation backlog
3. **Schedule**: Address during planned maintenance
