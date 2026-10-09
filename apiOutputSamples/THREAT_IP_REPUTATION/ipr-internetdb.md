---
intent: THREAT_IP_REPUTATION
slug: ipr-internetdb
status: pending_review
captured_at: 2026-10-08T04:43:49Z
request_url: https://internetdb.shodan.io/1.1.1.1
content_type: application/json
inputs: |
  {"ip": "1.1.1.1"}
intent_description: |
  Assesses malicious IP address risk scores, botnet associations, and brute-force history across threat registries.
answer_requirement: |
  Must return a malicious-activity risk assessment / reputation for the IP asked.
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "cpes": [
    "cpe:/a:cloudflare:cloudflare"
  ],
  "hostnames": [
    "wlc.inp-e.com",
    "one.one.one.one",
    "materguest.mater.org.au"
  ],
  "ip": "1.1.1.1",
  "ports": [
    53,
    80,
    443,
    2052,
    2053,
    2082,
    2083,
    2086,
    2087,
    8080,
    8443
  ],
  "tags": [],
  "vulns": []
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
