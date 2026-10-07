---
intent: CRYPTO_PRICE
slug: cp-bitget
status: approved
captured_at: 2026-10-05T05:45:16Z
request_url: https://api.bitget.com/api/v2/spot/market/tickers?symbol=BTCUSDT
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 22 keyless. Distinct operators. Quote asset differs (USD vs USDT) by ~0.1%, inside the 1.5% tolerance.
answer_requirement: |
  Must satisfy catalog intent CRYPTO_PRICE via upstream Bitget
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:31Z
---

## Raw API output

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1791179116418,
  "data": [
    {
      "open": "84926.45",
      "symbol": "BTCUSDT",
      "high24h": "86993.9",
      "low24h": "84873.31",
      "lastPr": "85768.48",
      "quoteVolume": "150814327.536654",
      "baseVolume": "1758.814845",
      "usdtVolume": "150814327.53665378",
      "ts": "1791179114578",
      "bidPr": "85768.48",
      "askPr": "85768.49",
      "bidSz": "0.515137",
      "askSz": "0.00115",
      "openUtc": "86511",
      "changeUtc24h": "-0.00845",
      "change24h": "0.00991"
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
