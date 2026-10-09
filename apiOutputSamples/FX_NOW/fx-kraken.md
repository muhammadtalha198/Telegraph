---
intent: FX_NOW
slug: fx-kraken
status: approved
captured_at: 2026-10-08T04:41:58Z
request_url: https://api.kraken.com/0/public/Ticker?pair=USDCAD
content_type: application/json
inputs: |
  {"base": "USD", "quote": "CAD", "pair": "USDCAD"}
intent_description: |
  Provides real-time institutional foreign exchange mid-market rates, spreads, and currency conversion quotes.
answer_requirement: |
  Must return the current exchange rate (units of quote currency per 1 unit of base currency) for the pair asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the current exchange rate for the USDCAD pair."
reviewed_at: 2026-10-08T04:55:38Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "error": [],
  "result": {
    "ZUSDZCAD": {
      "a": [
        "1.42715",
        "500",
        "500.000"
      ],
      "b": [
        "1.42708",
        "12302",
        "12302.000"
      ],
      "c": [
        "1.42717",
        "34.51580000"
      ],
      "v": [
        "633962.92138285",
        "3225104.50573192"
      ],
      "p": [
        "1.42708",
        "1.42589"
      ],
      "t": [
        2012,
        8491
      ],
      "l": [
        "1.42503",
        "1.42248"
      ],
      "h": [
        "1.43000",
        "1.43000"
      ],
      "o": "1.42674"
    }
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the current exchange rate for the USDCAD pair._
