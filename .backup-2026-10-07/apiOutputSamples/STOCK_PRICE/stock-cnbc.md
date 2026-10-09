---
intent: STOCK_PRICE
slug: stock-cnbc
status: approved
captured_at: 2026-10-05T05:45:08Z
request_url: https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=BTC&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json&events=1
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 4 keyless.
answer_requirement: |
  Must satisfy catalog intent STOCK_PRICE via upstream CNBC
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:33Z
---

## Raw API output

```json
{
  "FormattedQuoteResult": {
    "FormattedQuote": [
      {
        "symbol": "BTC",
        "symbolType": "symbol",
        "code": 0,
        "name": "Grayscale Bitcoin Mini Trust ETF",
        "shortName": "BTC",
        "onAirName": "Grayscale Bitcoin Mini Trust ETF",
        "altName": "Grayscale Bitcoin Mini Trust ETF",
        "last": "37.25",
        "last_timedate": "10/02/26 EDT",
        "last_time": "2026-10-02",
        "changetype": "DOWN",
        "type": "STOCK",
        "subType": "Exchange Traded Fund",
        "exchange": "NYSE Arca",
        "source": "Last NYSE Arca, VOL From CTA",
        "open": "38.28",
        "high": "38.55",
        "low": "37.07",
        "change": "-0.19",
        "change_pct": "-0.51%",
        "currencyCode": "USD",
        "volume": "2,867,801",
        "volume_alt": "2.9M",
        "provider": "CNBC QUOTE CACHE",
        "previous_day_closing": "37.25",
        "altSymbol": "BTC",
        "realTime": "true",
        "curmktstatus": "POST_MKT",
        "tendayavgvol": "1.73M",
        "pcttendayvol": "1.693",
        "yrhiprice": "55.96",
        "yrhidate": "10/06/25",
        "yrloprice": "25.65",
        "yrlodate": "06/25/26",
        "streamable": "1",
        "issue_id": "918663849",
        "countryCode": "US",
        "timeZone": "EDT",
        "feedSymbol": "BTC",
        "portfolioindicator": "N",
        "ExtendedMktQuote": {
          "type": "POST_MKT",
          "source": "Last NYSE Arca, VOL From CTA",
          "last": "37.40",
          "last_timedate": "10/02/26 EDT",
          "last_time": "2026-10-02",
          "change": "+0.15",
          "change_pct": "+0.40%",
          "volume": "4,649",
          "volume_alt": "4.6K",
          "changetype": "UP"
        },
        "EventData": {
          "yrhiind": "N",
          "yrloind": "N",
          "is_halted": "N"
        }
      }
    ]
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
