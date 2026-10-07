---
intent: FX_NOW
slug: fx-yahoo
status: approved
captured_at: 2026-10-05T09:37:51Z
request_url: https://query1.finance.yahoo.com/v8/finance/chart/USDEUR=X?interval=1d&range=1d
content_type: application/json
inputs: |
  {"base": "USD", "quote": "EUR", "pair": "USDEUR"}
intent_description: |
  Provides real-time institutional foreign exchange mid-market rates, spreads, and currency conversion quotes.
answer_requirement: |
  Must return the current exchange rate between the two currencies asked.
capture_note: |
  golden-test PASS: Yahoo Finance
reviewer_note: "auto_review: [0.90|heuristic+llm] The API response provides the current exchange rate between USD and EUR, which is relevant to the intent."
reviewed_at: 2026-10-05T12:20:11Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 0.900
---

## Raw API output

```json
{
  "chart": {
    "result": [
      {
        "meta": {
          "currency": "EUR",
          "symbol": "EUR=X",
          "exchangeName": "CCY",
          "fullExchangeName": "CCY",
          "instrumentType": "CURRENCY",
          "firstTradeDate": 1070236800,
          "regularMarketTime": 1791193009,
          "hasPrePostMarketData": false,
          "gmtoffset": 3600,
          "timezone": "BST",
          "exchangeTimezoneName": "Europe/London",
          "regularMarketPrice": 0.8914,
          "regularMarketChangePercent": 0.3489,
          "fulldayPrice": 0.8914,
          "fulldayChange": 0.0031,
          "fulldayChangePercent": 0.3489,
          "fiftyTwoWeekHigh": 0.8956,
          "fiftyTwoWeekLow": 0.8317,
          "regularMarketDayHigh": 0.8956,
          "regularMarketDayLow": 0.8876,
          "regularMarketVolume": 0,
          "longName": "USD/EUR",
          "shortName": "USD/EUR",
          "chartPreviousClose": 0.8883,
          "priceHint": 4,
          "currentTradingPeriod": {
            "pre": {
              "timezone": "BST",
              "start": 1791154800,
              "end": 1791154800,
              "gmtoffset": 3600
            },
            "regular": {
              "timezone": "BST",
              "start": 1791154800,
              "end": 1791241140,
              "gmtoffset": 3600
            },
            "post": {
              "timezone": "BST",
              "start": 1791241140,
              "end": 1791241140,
              "gmtoffset": 3600
            }
          },
          "dataGranularity": "1d",
          "range": "1d",
          "validRanges": [
            "1d",
            "5d",
            "1mo",
            "3mo",
            "6mo",
            "1y",
            "2y",
            "5y",
            "10y",
            "ytd",
            "max"
          ]
        },
        "timestamp": [
          1791193009
        ],
        "indicators": {
          "quote": [
            {
              "open": [
                0.8876000046730042
              ],
              "volume": [
                0
              ],
              "high": [
                0.8956000208854675
              ],
              "low": [
                0.8876000046730042
              ],
              "close": [
                0.8913999795913696
              ]
            }
          ],
          "adjclose": [
            {
              "adjclose": [
                0.8913999795913696
              ]
            }
          ]
        }
      }
    ],
    "error": null
  }
}
```

## Why this matches (or not)

_[0.90|heuristic+llm] The API response provides the current exchange rate between USD and EUR, which is relevant to the intent._
