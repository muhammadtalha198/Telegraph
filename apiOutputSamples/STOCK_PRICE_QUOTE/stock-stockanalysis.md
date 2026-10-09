---
intent: STOCK_PRICE_QUOTE
slug: stock-stockanalysis
status: approved
captured_at: 2026-10-09T10:35:29Z
request_url: https://stockanalysis.com/api/quotes/s/AAPL
content_type: application/json
inputs: |
  AAPL
intent_description: |
  Retrieves live and official market-close equity quotes, bid-ask spreads, and trading volume.
answer_requirement: |
  Must return the current market price of the ticker asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the current market price (p) of AAPL stock, which matches the intent of the input."
reviewed_at: 2026-10-09T10:40:59Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "status": 200,
  "data": {
    "p": 340.42,
    "pd": 340.42,
    "c": 3.75,
    "cp": 1.11,
    "cl": 336.67,
    "cdr": 1,
    "o": 336.82,
    "h": 341.57,
    "l": 335.9,
    "v": 35332449.596014,
    "ts": 1791489600000,
    "u": "Oct 8, 2026, 4:00 PM EDT",
    "td": "2026-10-08",
    "h52": 345.34,
    "l52": 243.42,
    "ex": "NASDAQ",
    "ms": "closed",
    "fms": "pre",
    "e": true,
    "ep": 333.64,
    "epd": 333.64,
    "ec": -6.78,
    "ecp": -1.99,
    "eu": "Oct 9, 2026, 6:34 AM EDT",
    "es": "Pre-market",
    "ets": 1791542083175.8079,
    "etd": "2026-10-09",
    "epv": 583157,
    "days": 0,
    "exp": 1791542133412,
    "symbol": "AAPL",
    "uid": "AAPL"
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the current market price (p) of AAPL stock, which matches the intent of the input._
