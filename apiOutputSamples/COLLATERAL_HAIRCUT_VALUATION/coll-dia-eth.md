---
intent: COLLATERAL_HAIRCUT_VALUATION
slug: coll-dia-eth
status: approved
captured_at: 2026-10-08T04:42:19Z
request_url: https://api.diadata.org/v1/assetQuotation/Ethereum/0x0000000000000000000000000000000000000000
content_type: application/json
inputs: |
  {}
intent_description: |
  Calculates mark-to-market valuations and risk haircuts for pledged securities and digital collateral.
answer_requirement: |
  Must return the mark-to-market USD price of ONE ETH (pledged collateral unit) from an independent price oracle; value of N ETH = N x price, haircut applied downstream. Only the observable market input is scored; the haircut model is judgment (hybrid intent).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the ETH price from an independent oracle, which is the observable market input required for the intent."
reviewed_at: 2026-10-08T04:57:49Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "Symbol": "ETH",
  "Name": "Ether",
  "Address": "0x0000000000000000000000000000000000000000",
  "Blockchain": "Ethereum",
  "Price": 2558.4172887550144,
  "PriceYesterday": 2611.316967084107,
  "VolumeYesterdayUSD": 5017396596.829805,
  "Time": "2026-10-08T04:41:59Z",
  "Source": "diadata.org",
  "Signature": "0xf8c1540e423f371164a039903db0b70822b3bd68569876c7bf1ee5a3be8f4c2a004f149fdb8f48625cc941eacbf2e809836d4b1def32d6e9ea8a81ac5b9de3e101"
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the ETH price from an independent oracle, which is the observable market input required for the intent._
