---
intent: ONCHAIN_METRIC_VERIFY
slug: ocm-publicnode-rpc
status: approved
captured_at: 2026-10-05T09:28:17Z
request_url: https://ethereum-rpc.publicnode.com
content_type: application/json
inputs: |
  {"eaddr": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"}
intent_description: |
  Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.
answer_requirement: |
  Must return the on-chain value asked (address balance / token balance / tx state).
capture_note: |
  golden-test PASS: PublicNode ETH RPC
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the on-chain balance for the specified Ethereum address. | heuristic: Returns on-chain balance/result value"
reviewed_at: 2026-10-05T11:48:43Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x4fc9ae7fb6cc996a"
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the on-chain balance for the specified Ethereum address. | heuristic: Returns on-chain balance/result value_
