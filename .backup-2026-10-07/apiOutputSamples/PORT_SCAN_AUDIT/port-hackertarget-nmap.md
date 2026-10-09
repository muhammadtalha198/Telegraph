---
intent: PORT_SCAN_AUDIT
slug: port-hackertarget-nmap
status: approved
captured_at: 2026-10-05T05:44:48Z
request_url: https://api.hackertarget.com/nmap/?q=example.com
content_type: text/plain
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - only 4 candidates; 2 keyless. Realistic keyless ceiling is 2. Others need free keys. Distinct publishers: 4.
answer_requirement: |
  Must satisfy catalog intent PORT_SCAN_AUDIT via upstream HackerTarget (nmap)
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:33Z
---

## Raw API output

```text
error valid key required
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
