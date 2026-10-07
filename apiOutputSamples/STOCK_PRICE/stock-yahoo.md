---
intent: STOCK_PRICE
slug: stock-yahoo
status: approved
captured_at: 2026-10-05T05:45:03Z
request_url: https://query1.finance.yahoo.com/v8/finance/chart/BTC?interval=1d&range=1d
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 4 keyless.
answer_requirement: |
  Must satisfy catalog intent STOCK_PRICE via upstream Yahoo Finance
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:34Z
---

## Raw API output

```json
{
  "chart": {
    "result": [
      {
        "meta": {
          "currency": "USD",
          "symbol": "BTC",
          "exchangeName": "PCX",
          "fullExchangeName": "NYSEArca",
          "instrumentType": "ETF",
          "firstTradeDate": 1722432600,
          "regularMarketTime": 1790971200,
          "hasPrePostMarketData": true,
          "gmtoffset": -14400,
          "timezone": "EDT",
          "exchangeTimezoneName": "America/New_York",
          "regularMarketPrice": 37.25,
          "regularMarketChangePercent": -0.507,
          "fulldayPrice": 37.94,
          "fulldayChange": 0.5,
          "fulldayChangePercent": 1.335,
          "fiftyTwoWeekHigh": 55.96,
          "fiftyTwoWeekLow": 25.65,
          "regularMarketDayHigh": 38.547,
          "regularMarketDayLow": 37.07,
          "regularMarketVolume": 2932330,
          "longName": "Grayscale Bitcoin Mini Trust ETF",
          "shortName": "Grayscale Bitcoin Mini Trust (B",
          "chartPreviousClose": 37.44,
          "priceHint": 2,
          "currentTradingPeriod": {
            "pre": {
              "timezone": "EDT",
              "start": 1791187200,
              "end": 1791207000,
              "gmtoffset": -14400
            },
            "regular": {
              "timezone": "EDT",
              "start": 1791207000,
              "end": 1791230400,
              "gmtoffset": -14400
            },
            "post": {
              "timezone": "EDT",
              "start": 1791230400,
              "end": 1791244800,
              "gmtoffset": -14400
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
            "ytd",
            "max"
          ]
        },
        "timestamp": [
          1790947800
        ],
        "indicators": {
          "quote": [
            {
              "low": [
                37.06999969482422
              ],
              "open": [
                38.279998779296875
              ],
              "volume": [
                2932600
              ],
              "close": [
                37.25
              ],
              "high": [
                38.54999923706055
              ]
            }
          ],
          "adjclose": [
            {
              "adjclose": [
                37.25
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

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
