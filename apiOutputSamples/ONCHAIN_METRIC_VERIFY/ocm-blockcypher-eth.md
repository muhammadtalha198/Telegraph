---
intent: ONCHAIN_METRIC_VERIFY
slug: ocm-blockcypher-eth
status: approved
captured_at: 2026-10-04T18:40:10Z
request_url: https://api.blockcypher.com/v1/eth/main/addrs/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045/balance
content_type: application/json
inputs: |
  vitalik eth
intent_description: |
  Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.
answer_requirement: |
  Must convey the on-chain value asked (wallet/token balance or tx state) for the address given.
capture_note: |
  (none)
reviewer_note: "auto_review: [0.80|heuristic] Returns wallet/token balance (partial vs full logs/gas description)"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "address": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
  "total_received": 87406400793825658477236,
  "total_sent": 87589693539564895377156,
  "balance": 5747636114588065915,
  "unconfirmed_balance": 0,
  "final_balance": 5747636114588065915,
  "n_tx": 130378,
  "unconfirmed_n_tx": 0,
  "final_n_tx": 130378,
  "nonce": 5967,
  "pool_nonce": 5967
}
```

## Why this matches (or not)

_[0.80|heuristic] Returns wallet/token balance (partial vs full logs/gas description)_
