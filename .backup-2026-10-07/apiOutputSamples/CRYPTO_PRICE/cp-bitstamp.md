---
intent: CRYPTO_PRICE
slug: cp-bitstamp
status: approved
captured_at: 2026-10-05T05:45:10Z
request_url: https://www.bitstamp.net/api/v2/ticker/btcusd/
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 22 keyless. Distinct operators. Quote asset differs (USD vs USDT) by ~0.1%, inside the 1.5% tolerance.
answer_requirement: |
  Must satisfy catalog intent CRYPTO_PRICE via upstream Bitstamp
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:31Z
---

## Raw API output

```json
{
  "timestamp": "1791179110",
  "open": "86490.27",
  "high": "86968.58",
  "low": "84880.44",
  "last": "85727.15",
  "volume": "1091.88155741",
  "vwap": "85932.62",
  "bid": "85732.21",
  "ask": "85732.22",
  "side": "0",
  "open_24": "84903.84",
  "percent_change_24": "0.97",
  "market_type": "SPOT"
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
