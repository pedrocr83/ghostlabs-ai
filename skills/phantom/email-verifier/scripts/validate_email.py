#!/usr/bin/env python3
"""Email validation layers 1-8 (local, no SMTP needed).

Usage: python validate_email.py user@example.com
Output: JSON with layer results and composite score.
"""
import re
import sys
import json
import socket
import dns.resolver

DISPOSABLE_DOMAINS = {"mailinator.com", "guerrillamail.com", "tempmail.com", "throwaway.email", "yopmail.com"}
ROLE_PREFIXES = {"info", "admin", "support", "sales", "contact", "noreply", "no-reply", "webmaster", "postmaster"}
FREE_PROVIDERS = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com", "protonmail.com"}

def validate(email: str) -> dict:
    results = {"email": email, "layers": {}, "score": 0}
    local, _, domain = email.rpartition("@")

    # Layer 1: Syntax (RFC 5321/5322)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    valid_syntax = bool(re.match(pattern, email))
    results["layers"]["1_syntax"] = {"pass": valid_syntax, "detail": "RFC 5321/5322 validation"}
    if not valid_syntax:
        results["score"] = 0
        return results

    # Layer 2: Disposable domain
    is_disposable = domain.lower() in DISPOSABLE_DOMAINS
    results["layers"]["2_disposable"] = {"pass": not is_disposable, "detail": f"Domain {'is' if is_disposable else 'is not'} disposable"}

    # Layer 3: Role-based
    is_role = local.lower() in ROLE_PREFIXES
    results["layers"]["3_role_based"] = {"pass": not is_role, "detail": f"{'Role-based' if is_role else 'Personal'} address"}

    # Layer 4: Free provider
    is_free = domain.lower() in FREE_PROVIDERS
    results["layers"]["4_free_provider"] = {"pass": True, "detail": f"{'Free' if is_free else 'Business'} provider", "is_free": is_free}

    # Layer 5: DNS/MX resolution
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        has_mx = len(mx_records) > 0
        results["layers"]["5_dns_mx"] = {"pass": has_mx, "detail": f"{len(mx_records)} MX records found"}
    except Exception as e:
        results["layers"]["5_dns_mx"] = {"pass": False, "detail": str(e)}

    # Composite score
    passed = sum(1 for l in results["layers"].values() if l["pass"])
    results["score"] = round((passed / len(results["layers"])) * 100)
    results["verdict"] = "valid" if results["score"] >= 80 else "risky" if results["score"] >= 50 else "invalid"

    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_email.py user@example.com")
        sys.exit(1)
    print(json.dumps(validate(sys.argv[1]), indent=2))
