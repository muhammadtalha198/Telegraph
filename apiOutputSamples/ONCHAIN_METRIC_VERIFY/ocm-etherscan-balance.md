---
intent: ONCHAIN_METRIC_VERIFY
slug: ocm-etherscan-balance
status: rejected
captured_at: 2026-10-04T18:40:12Z
request_url: https://api.etherscan.io/api?module=account&action=balance&address=0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045&tag=latest
content_type: application/json
inputs: |
  vitalik eth
intent_description: |
  Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.
answer_requirement: |
  Must convey the on-chain value asked (wallet/token balance or tx state) for the address given.
capture_note: |
  works limited without key; better with ETHERSCAN_API_KEY
reviewer_note: "auto_review: [0.75|heuristic] no balance / on-chain value field found"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "status": "0",
  "message": "NOTOK",
  "result": "You are using a deprecated V1 endpoint, switch to Etherscan API V2 using https://docs.etherscan.io/v2-migration"
}
```

## Why this matches (or not)

_[0.75|heuristic] no balance / on-chain value field found_
