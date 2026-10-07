---
intent: ONCHAIN_METRIC_VERIFY
slug: ocm-bitaps
status: rejected
captured_at: 2026-10-05T09:28:17Z
request_url: https://api.bitaps.com/btc/v1/blockchain/address/state/1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
content_type: application/json
inputs: |
  {"addr": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"}
intent_description: |
  Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.
answer_requirement: |
  Must return the on-chain value asked (address balance / token balance / tx state).
capture_note: |
  golden-test PASS: Bitaps
reviewer_note: "auto_review: [0.75|heuristic] no balance / on-chain value field found"
reviewed_at: 2026-10-05T09:43:44Z
review_source: auto_review
review_mode: heuristic
llm_used: false
review_confidence: 0.750
---

## Raw API output

```json
{
  "data": {
    "balance": 10758408766,
    "receivedAmount": 10758408766,
    "receivedTxCount": 66816,
    "sentAmount": 0,
    "sentTxCount": 0,
    "firstReceivedTxPointer": "0:0",
    "firstSentTxPointer": null,
    "lastTxPointer": "969962:725",
    "largestReceivedTxAmount": 5989,
    "largestReceivedTxPointer": "969962:725",
    "largestSpentTxAmount": 0,
    "largestSpentTxPointer": null,
    "receivedOutsCount": 80246,
    "spentOutsCount": 0,
    "pendingReceivedAmount": 0,
    "pendingSentAmount": 0,
    "pendingReceivedTxCount": 0,
    "pendingSentTxCount": 0,
    "pendingReceivedOutsCount": 0,
    "pendingSpentOutsCount": 0,
    "type": "PUBKEY+P2PKH"
  },
  "time": 0.0146
}
```

## Why this matches (or not)

_[0.75|heuristic] no balance / on-chain value field found_
