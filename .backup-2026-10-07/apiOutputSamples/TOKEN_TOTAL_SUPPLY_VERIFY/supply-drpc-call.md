---
intent: TOKEN_TOTAL_SUPPLY_VERIFY
slug: supply-drpc-call
status: pending_review
captured_at: 2026-10-05T09:28:22Z
request_url: https://eth.drpc.org
content_type: application/json
inputs: |
  {"token": "0x514910771AF9Ca656af840dff83E8264EcF986CA", "cg": "chainlink", "paprika": "link-chainlink"}
intent_description: |
  Verifies token circulating supply, burnt token balances, and total minted token counts on-chain.
answer_requirement: |
  Must return the token's total supply (minted/circulating count).
capture_note: |
  golden-test PASS: dRPC ETH
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": "0x0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000"
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
