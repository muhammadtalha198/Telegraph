---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-kraken
status: pending_review
captured_at: 2026-10-05T09:37:27Z
request_url: https://api.kraken.com/0/public/Ticker?pair=XBTUSD
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: Kraken
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "error": [],
  "result": {
    "XXBTZUSD": {
      "a": [
        "85861.30000",
        "1",
        "1.000"
      ],
      "b": [
        "85861.20000",
        "1",
        "1.000"
      ],
      "c": [
        "85861.20000",
        "0.00048760"
      ],
      "v": [
        "895.28398075",
        "1686.88628419"
      ],
      "p": [
        "86097.45668",
        "85952.00623"
      ],
      "t": [
        55819,
        109023
      ],
      "l": [
        "85394.00000",
        "85100.00000"
      ],
      "h": [
        "86973.60000",
        "86973.60000"
      ],
      "o": "86506.60000"
    }
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
