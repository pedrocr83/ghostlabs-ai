#!/usr/bin/env python3
"""Quick DNS security check for a domain.

Usage: python dns_check.py example.com
Output: JSON with DNS, SPF, DMARC, and MX results.
"""
import sys
import json
import socket
import dns.resolver

def check_domain(domain: str) -> dict:
    results = {"domain": domain, "checks": {}}

    # MX records
    try:
        mx = dns.resolver.resolve(domain, 'MX')
        results["checks"]["mx"] = {"status": "ok", "records": [str(r.exchange).rstrip('.') for r in mx]}
    except Exception as e:
        results["checks"]["mx"] = {"status": "fail", "error": str(e)}

    # SPF
    try:
        txt = dns.resolver.resolve(domain, 'TXT')
        spf = [str(r) for r in txt if 'v=spf1' in str(r)]
        results["checks"]["spf"] = {"status": "ok" if spf else "missing", "records": spf}
    except Exception:
        results["checks"]["spf"] = {"status": "missing"}

    # DMARC
    try:
        dmarc = dns.resolver.resolve(f"_dmarc.{domain}", 'TXT')
        records = [str(r) for r in dmarc]
        results["checks"]["dmarc"] = {"status": "ok" if records else "missing", "records": records}
    except Exception:
        results["checks"]["dmarc"] = {"status": "missing"}

    # A record
    try:
        a = dns.resolver.resolve(domain, 'A')
        results["checks"]["a_record"] = {"status": "ok", "ips": [str(r) for r in a]}
    except Exception:
        results["checks"]["a_record"] = {"status": "fail"}

    # Score
    passed = sum(1 for c in results["checks"].values() if c.get("status") == "ok")
    results["score"] = f"{passed}/{len(results['checks'])}"

    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dns_check.py example.com")
        sys.exit(1)
    print(json.dumps(check_domain(sys.argv[1]), indent=2))
