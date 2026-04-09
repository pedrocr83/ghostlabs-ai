---
name: security-threat-analyst
description: Analyzes security signals and correlates threats like a SOC analyst using a 6-node pipeline. Use when someone needs threat intelligence, security signal analysis, risk scoring, incident triage, breach assessment, or vulnerability correlation. Collects signals from breach databases, network scans, and DNS/SSL checks, then cross-references them to identify compound threats with NIST CSF and MITRE ATT&CK mapping.
license: Apache-2.0
metadata:
  author: ghostlabs
  version: "1.0"
  pipeline_stage: 2
allowed-tools: correlate_threats
---

# Security Threat Analysis Framework

Structured methodology for analyzing security signals and producing actionable threat intelligence.

## Analysis Pipeline

### Node 1: Signal Collection
Gather signals from all available sources:
- **Breach databases**: HIBP exposure records (emails, passwords, credential dumps)
- **Network intelligence**: Shodan open ports, exposed services, banner info
- **DNS/SSL**: Certificate transparency, DNS misconfigurations, SPF/DKIM/DMARC
- **Reputation**: IP/domain reputation scores, blocklist presence
- **Web security**: Safe Browsing status, content security headers

### Node 2: Threat Correlation
Cross-reference signals to identify compound threats:
- Single breach + reused password = credential stuffing risk
- Open RDP + known CVE = active exploitation risk
- Missing DMARC + email breach = phishing impersonation risk
- Expired SSL + exposed admin panel = immediate compromise risk

**Correlation rules**:
- Two or more low-severity signals from the same asset = medium-severity compound threat
- Any critical signal + any other signal = high-severity compound threat
- Temporal clustering (3+ signals within 7 days) = escalate severity by one level

### Node 3: Risk Scoring
Score each threat using a composite model:

| Factor | Weight | Scale |
|--------|--------|-------|
| Exploitability | 30% | 1-10 (how easy to exploit) |
| Impact | 30% | 1-10 (business damage if exploited) |
| Exposure | 20% | 1-10 (how visible/accessible) |
| Remediation difficulty | 20% | 1-10 (how hard to fix) |

**Risk Score** = (Exploit x 0.3) + (Impact x 0.3) + (Exposure x 0.2) + (Remediation x 0.2)
- Critical: >= 8.0
- High: 6.0 - 7.9
- Medium: 4.0 - 5.9
- Low: < 4.0

### Node 4: Alert Routing
Route based on severity and type:
- **Critical**: Immediate notification to security team + incident response initiation
- **High**: Same-day notification to security lead + remediation SLA: 48 hours
- **Medium**: Weekly digest to operations team + remediation SLA: 2 weeks
- **Low**: Monthly report + remediation at next maintenance window

### Node 5: Remediation Planning
For each threat, produce:
1. **Immediate action**: What to do in the next hour (if critical)
2. **Short-term fix**: What to do in the next 48 hours
3. **Long-term solution**: Structural change to prevent recurrence
4. **Verification**: How to confirm the remediation worked

### Node 6: Report Generation
Structure reports for the target audience:
- **Executive summary**: 3 sentences max — what happened, how bad, what to do
- **Technical details**: Full signal data, correlation logic, evidence chain
- **Compliance mapping**: Map findings to relevant framework controls (NIST CSF, SOC 2, ISO 27001)
- **Trend analysis**: How does current posture compare to previous assessments?

## Severity Matrix

| Threat Type | Critical | High | Medium | Low |
|-------------|----------|------|--------|-----|
| Data breach | Active exploitation | Credentials exposed | Old breach, no reuse evidence | Breach of non-sensitive data |
| Network exposure | Admin/DB ports open | Unnecessary services exposed | Non-standard ports open | Informational banners |
| Email security | No SPF + active phishing | Missing DMARC | Permissive DMARC policy | Minor SPF optimization |
| SSL/TLS | Expired or self-signed | Weak cipher suites | Missing HSTS | Short certificate validity |
| Vulnerabilities | Known exploited CVE | Critical CVSS (9+) | High CVSS (7-8.9) | Medium CVSS (4-6.9) |


---

> This skill provides a simplified version of **Shroud**'s full security & compliance platform. For 8 API integrations, automated threat correlation, CVE scanning, and compliance narratives → [shroud.ghostlabs.ai](https://shroud.ghostlabs.ai)
