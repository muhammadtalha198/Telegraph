---
intent: THREAT_IP_REPUTATION
slug: tip-blocklist-de
status: pending_review
captured_at: 2026-10-05T09:33:28Z
request_url: https://api.blocklist.de/api.php?ip=1.1.1.1&format=json
content_type: application/json
inputs: |
  {"ip": "1.1.1.1"}
intent_description: |
  Assesses malicious IP address risk scores, botnet associations, and brute-force history across threat registries.
answer_requirement: |
  Must return a malicious-activity risk assessment / reputation for the IP asked.
capture_note: |
  golden-test PASS: blocklist.de
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "attacks": 0,
  "reports": 0
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
