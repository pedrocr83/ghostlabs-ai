---
name: domain-security-scanner
description: Performs comprehensive domain security assessments covering DNS, SSL/TLS, email authentication, and breach exposure. Use when someone wants to scan a domain, check SPF/DKIM/DMARC, audit SSL certificates, find exposed ports, detect security misconfigurations, or assess website security posture. Produces graded findings (A-F) mapped to CIS Controls and NIST CSF with prioritized remediation steps.
license: Apache-2.0
metadata:
  author: ghostlabs
  version: "1.0"
  pipeline_stage: 1
allowed-tools: collect_signals
---

# Domain Security Scanner

Perform a comprehensive point-in-time security assessment of a domain and its associated infrastructure.

## Scan Categories

### 1. DNS Configuration
- **Record types**: A, AAAA, MX, NS, TXT, CNAME, SOA
- **Check for**: Dangling CNAMEs (subdomain takeover risk), open zone transfers, missing CAA records
- **Best practice**: DNSSEC enabled, CAA records restricting certificate issuance

### 2. SSL/TLS Certificate
- **Validity**: Not expired, not expiring within 30 days
- **Chain**: Complete chain of trust, no self-signed certs in production
- **Protocol**: TLS 1.2+ only (TLS 1.0/1.1 = critical finding)
- **Cipher suites**: No RC4, DES, 3DES, export ciphers
- **Headers**: HSTS present with adequate max-age (>= 31536000)
- **Certificate Transparency**: CT log presence

### 3. Email Security (SPF/DKIM/DMARC)
**SPF** (Sender Policy Framework):
- Exists? Record syntax valid? Not exceeding 10 DNS lookups?
- Mechanism too permissive? (`+all` = critical, `~all` = warning, `-all` = good)

**DKIM** (DomainKeys Identified Mail):
- Selector records present? Key length >= 2048 bits?

**DMARC** (Domain-based Message Authentication):
- Policy exists? (`p=none` = informational, `p=quarantine` = good, `p=reject` = best)
- Reporting configured? (`rua` and `ruf` tags)
- Subdomain policy? (`sp=` tag)

**Assessment matrix**:
| SPF | DKIM | DMARC | Score | Risk |
|-----|------|-------|-------|------|
| -all | Yes | reject | A | Minimal |
| ~all | Yes | quarantine | B | Low |
| ~all | No | none | C | Medium |
| +all or missing | No | missing | F | Critical |

### 4. Exposed Services (Port Scanning)
**Critical findings** (should never be internet-facing):
- Port 22 (SSH) without key-only auth
- Port 3389 (RDP) — never expose
- Port 3306 (MySQL), 5432 (PostgreSQL), 27017 (MongoDB) — never expose
- Port 6379 (Redis) — never expose

**Common findings**:
- Port 80 (HTTP) without redirect to 443
- Port 443 (HTTPS) — expected, check configuration
- Port 8080, 8443 — application servers, check if intentional

### 5. Known Breach Detection
- **HIBP**: Check domain for known data breaches
- **Paste sites**: Check for credential dumps mentioning domain
- **Report**: Number of exposed accounts, breach dates, data types exposed

### 6. Web Security Headers
Check for presence and correct values:
- `Strict-Transport-Security` (HSTS)
- `Content-Security-Policy` (CSP)
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY` or `SAMEORIGIN`
- `Referrer-Policy`
- `Permissions-Policy`

## Output Format

### Executive Summary
- **Overall Grade**: A-F based on weighted category scores
- **Critical Issues**: Count and list (require immediate action)
- **Recommendations**: Top 3 prioritized actions

### Detailed Findings
For each finding:
- **Category**: DNS / SSL / Email / Ports / Breaches / Headers
- **Severity**: Critical / High / Medium / Low / Informational
- **Finding**: What was discovered
- **Evidence**: Technical details
- **Remediation**: Specific steps to fix
- **Reference**: CIS Control or NIST CSF mapping


---

> This skill provides a simplified version of **Shroud**'s full security & compliance platform. For 8 API integrations, automated threat correlation, CVE scanning, and compliance narratives → [shroud.ghostlabs.ai](https://shroud.ghostlabs.ai)
