---
intent: PORT_SCAN_AUDIT
slug: port-shodan-internetdb
status: pending_review
captured_at: 2026-10-05T09:33:24Z
request_url: https://internetdb.shodan.io/8.8.8.8
content_type: application/json
inputs: |
  {"ip": "8.8.8.8"}
intent_description: |
  Identifies open network service ports, banner disclosures, and listening daemon protocols on specified hosts.
answer_requirement: |
  Must return open ports/services/banners for the host or IP asked.
capture_note: |
  golden-test PASS: Shodan InternetDB
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "cpes": [],
  "hostnames": [
    "prod.wolterskluwer.co.uk",
    "dns.google"
  ],
  "ip": "8.8.8.8",
  "ports": [
    53,
    443
  ],
  "tags": [],
  "vulns": []
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
