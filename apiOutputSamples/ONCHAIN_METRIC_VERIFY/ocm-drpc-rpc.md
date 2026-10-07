---
intent: ONCHAIN_METRIC_VERIFY
slug: ocm-drpc-rpc
status: approved
captured_at: 2026-10-05T09:28:17Z
request_url: https://eth.drpc.org
content_type: application/json
inputs: |
  {"eaddr": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"}
intent_description: |
  Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.
answer_requirement: |
  Must return the on-chain value asked (address balance / token balance / tx state).
capture_note: |
  golden-test PASS: dRPC ETH
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provided the on-chain balance for the specified Ethereum address. | heuristic: Returns on-chain balance/result value"
reviewed_at: 2026-10-05T12:31:56Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": "0x4fc9ae7fb6cc996a"
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provided the on-chain balance for the specified Ethereum address. | heuristic: Returns on-chain balance/result value_
