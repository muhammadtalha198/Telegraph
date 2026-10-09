---
intent: CRYPTO_TRANSFER_VERIFY
slug: xfer-bitcore
status: pending_review
captured_at: 2026-10-08T04:42:19Z
request_url: https://api.bitcore.io/api/BTC/mainnet/tx/a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d
content_type: application/json
inputs: |
  {"txid": "a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"}
intent_description: |
  Verifies on-chain transaction status, gas fee burn, sender/recipient addresses, and block confirmations.
answer_requirement: |
  Must return the on-chain status of the pinned transaction: confirmed + block height (and parties/amounts).
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "txid": "a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d",
  "network": "mainnet",
  "chain": "BTC",
  "blockHeight": 57043,
  "blockHash": "00000000152340ca42227603908689183edc47355204e7aca59383b0aaac1fd8",
  "blockTime": "2010-05-22T18:16:31.000Z",
  "blockTimeNormalized": "2010-05-22T18:16:31.000Z",
  "coinbase": false,
  "locktime": -1,
  "inputCount": -1,
  "outputCount": -1,
  "size": 23620,
  "fee": 99000000,
  "value": 1000000000000,
  "confirmations": 913337
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
