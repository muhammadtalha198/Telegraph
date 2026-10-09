---
intent: CRYPTO_PRICE
slug: cp-gate
status: approved
captured_at: 2026-10-05T05:45:13Z
request_url: https://api.gateio.ws/api/v4/spot/tickers?currency_pair=BTC_USDT
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 22 keyless. Distinct operators. Quote asset differs (USD vs USDT) by ~0.1%, inside the 1.5% tolerance.
answer_requirement: |
  Must satisfy catalog intent CRYPTO_PRICE via upstream Gate.io
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:32Z
---

## Raw API output

```json
[
  {
    "currency_pair": "BTC_USDT",
    "last": "85772.9",
    "lowest_ask": "85773",
    "lowest_size": "1.2449",
    "highest_bid": "85772.9",
    "highest_size": "3.509188",
    "change_percentage": "1",
    "base_volume": "4263.248795",
    "quote_volume": "366426509.6078934",
    "high_24h": "86989.4",
    "low_24h": "84872.3"
  }
]
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
