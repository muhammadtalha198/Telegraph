---
intent: THREAT_IP_REPUTATION
slug: ipr-ipapiis
status: pending_review
captured_at: 2026-10-08T04:43:50Z
request_url: https://api.ipapi.is/?q=1.1.1.1
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
  "ip": "1.1.1.1",
  "is_bogon": false,
  "company": "APNIC Research and Development",
  "asn": "AS13335 Cloudflare, Inc.",
  "city": "Brisbane",
  "region": "Queensland",
  "country": "Australia",
  "lat": -27.46754,
  "lon": 153.02809,
  "timezone": "Australia/Brisbane",
  "docs": "https://ipapi.is/free-tier.html?ref=api"
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
