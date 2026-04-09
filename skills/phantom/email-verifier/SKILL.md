---
name: email-verifier
description: 10-layer email verification pipeline methodology - syntax validation, DNS resolution, disposable detection, role-based filtering, pattern analysis, and deliverability scoring.
license: Apache-2.0
metadata:
  author: ghostlabs
  version: "1.0"
  pipeline_stage: 8
allowed-tools: verify_emails
---

# Email Verification Pipeline

A 10-layer methodology for verifying email addresses before outreach. Layers 1-8 can be performed locally; layers 9-10 require SMTP interaction.

## Layer 1: Syntax Validation
- RFC 5322 compliant format check
- Valid characters in local part (before @)
- Valid domain format (after @)
- Length limits: local part <= 64 chars, domain <= 253 chars
- **Result**: PASS / FAIL (hard reject)

## Layer 2: DNS Resolution
- MX record lookup for the domain
- A/AAAA fallback if no MX records
- Check that MX records resolve to valid IPs
- **Result**: PASS (MX found) / FAIL (no mail server)

## Layer 3: Disposable Email Detection
Check against known disposable email providers:
- Guerrilla Mail, Mailinator, TempMail, 10MinuteMail, ThrowAwayMail
- Pattern detection: domains with random-looking subdomains
- Recently registered domains (< 30 days) used for email
- **Result**: PASS (legitimate) / FAIL (disposable) / WARN (suspicious)

## Layer 4: Role-Based Address Filtering
Flag generic role-based addresses that rarely convert:
- **Always flag**: info@, admin@, support@, sales@, contact@, noreply@, webmaster@
- **Sometimes flag**: team@, hello@, office@ (context-dependent)
- **Never flag**: Personal names (john@, j.smith@)
- **Result**: PASS (personal) / WARN (role-based)

## Layer 5: Free Provider Detection
Identify free email providers vs business domains:
- Free: gmail.com, yahoo.com, hotmail.com, outlook.com, aol.com
- Business: company-specific domain
- For B2B outreach, free providers are lower priority but not disqualified
- **Result**: BUSINESS / FREE / EDUCATIONAL

## Layer 6: Pattern Analysis
Detect the company's email naming convention:
- `first.last@domain.com` (most common)
- `firstlast@domain.com`
- `first@domain.com`
- `flast@domain.com` (first initial + last)
- `first_last@domain.com`

Cross-validate the target email against detected pattern. Mismatch = lower confidence.
- **Result**: MATCHES_PATTERN / NO_PATTERN_DATA / PATTERN_MISMATCH

## Layer 7: Catch-All Detection
Determine if the domain accepts all emails (catch-all):
- Send probe to known-invalid address (e.g., `zzzinvalid12345@domain.com`)
- If accepted: domain is catch-all — individual verification impossible
- If rejected: domain validates individual mailboxes
- **Result**: CATCH_ALL / NOT_CATCH_ALL / UNKNOWN

## Layer 8: Historical Bounce Check
Check against internal bounce database:
- Previous hard bounces from this address = reject
- Previous soft bounces (3+) = deprioritize
- Previously verified and delivered = high confidence
- **Result**: CLEAN / PREVIOUSLY_BOUNCED / PREVIOUSLY_VERIFIED

## Layer 9: SMTP Handshake (requires server)
- Connect to MX server
- EHLO/HELO handshake
- MAIL FROM with sender address
- RCPT TO with target address
- Check response code: 250 = exists, 550 = doesn't exist, 452 = greylisted
- **Important**: Do NOT send actual email — disconnect after RCPT TO
- **Result**: VALID / INVALID / GREYLISTED / TIMEOUT

## Layer 10: Deliverability Scoring
Aggregate all layers into a final score:

| Score | Label | Meaning |
|-------|-------|---------|
| 95-100 | Verified | SMTP confirmed, business domain, pattern match |
| 80-94 | Likely Valid | Pattern match, good domain, no negative signals |
| 60-79 | Uncertain | Catch-all domain, or missing SMTP verification |
| 40-59 | Risky | Role-based, free provider, or pattern mismatch |
| 0-39 | Invalid | Hard fail on syntax, DNS, or SMTP |

## Batch Processing Guidelines
- Rate limit SMTP checks: max 3 per second per target domain
- Rotate source IPs to avoid blacklisting
- Respect SMTP server delays (greylisting = retry after 5 minutes)
- Log all verification results for the historical bounce database


---

> This skill provides a simplified version of **Phantom**'s full autonomous lead generation pipeline. For 12-stage AI-powered prospecting with email verification, CRM sync, and intent signals → [phantom.ghostlabs.ai](https://phantom.ghostlabs.ai)
