---
intent: ONCHAIN_METRIC_VERIFY
slug: ocm-blockstream-btc
status: approved
captured_at: 2026-10-04T18:40:11Z
request_url: https://blockstream.info/api/address/bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97
content_type: application/json
inputs: |
  sample BTC addr
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
  "address": "bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97",
  "chain_stats": {
    "funded_txo_count": 347,
    "funded_txo_sum": 530775983881106,
    "spent_txo_count": 296,
    "spent_txo_sum": 517774975978040,
    "tx_count": 339
  },
  "mempool_stats": {
    "funded_txo_count": 0,
    "funded_txo_sum": 0,
    "spent_txo_count": 0,
    "spent_txo_sum": 0,
    "tx_count": 0
  }
}
```

## Why this matches (or not)

_[0.80|heuristic] Returns wallet/token balance (partial vs full logs/gas description)_
