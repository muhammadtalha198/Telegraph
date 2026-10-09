---
intent: THREAT_IP_REPUTATION
slug: ipr-stopforumspam
status: pending_review
captured_at: 2026-10-08T04:43:50Z
request_url: https://api.stopforumspam.org/api?ip=1.1.1.1&json
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
  "success": 1,
  "ip": {
    "value": "1.1.1.1",
    "frequency": 0,
    "appears": 0,
    "asn": 13335,
    "country": "us"
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
