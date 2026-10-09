---
intent: LOAN_INTEREST_RATE_QUOTE
slug: lnr-snb
status: rejected
captured_at: 2026-10-08T04:42:07Z
request_url: https://data.snb.ch/api/cube/snbgwdzid/data/json/en?fromDate=2025-06-18&toDate=2025-06-18
content_type: application/json
inputs: |
  {"bis_area": "CH", "d": "2025-06-18", "snb_date": "2025-06-18"}
intent_description: |
  Aggregates residential mortgage APRs, prime lending rates, and personal loan interest quotes.
answer_requirement: |
  Must return a published lending / policy / benchmark interest rate (percent) for the pinned country and date or period.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides various interest rates but does not include the requested residential mortgage APR, prime lending rate, or personal loan interest quote for the specified date and country."
reviewed_at: 2026-10-08T04:56:43Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "timeseries": [
    {
      "header": [
        {
          "dim": "Overview",
          "dimItem": "SNB policy rate"
        }
      ],
      "metadata": {
        "key": "EPB@SNB.snbgwdzid{LZ}",
        "frequency": "P1D_L",
        "scale": "",
        "unit": "In percent"
      },
      "values": [
        {
          "date": "2025-06-18",
          "value": 0.25
        }
      ]
    },
    {
      "header": [
        {
          "dim": "Overview",
          "dimItem": "SARON fixing at the close of the trading day"
        }
      ],
      "metadata": {
        "key": "EPB@SNB.snbgwdzid{SARON}",
        "frequency": "P1D_L",
        "scale": "",
        "unit": "In percent"
      },
      "values": [
        {
          "date": "2025-06-18",
          "value": 0.2
        }
      ]
    },
    {
      "header": [
        {
          "dim": "Overview",
          "dimItem": "Special rate  (Liquidity-shortage financing facility)"
        }
      ],
      "metadata": {
        "key": "EPB@SNB.snbgwdzid{ENG}",
        "frequency": "P1D_L",
        "scale": "",
        "unit": "In percent"
      },
      "values": [
        {
          "date": "2025-06-18",
          "value": 0.75
        }
      ]
    },
    {
      "header": [
        {
          "dim": "Overview",
          "dimItem": "Interest rate on sight deposits up to threshold"
        }
      ],
      "metadata": {
        "key": "EPB@SNB.snbgwdzid{ZIGBL}",
        "frequency": "P1D_L",
        "scale": "",
        "unit": "In percent"
      },
      "values": [
        {
          "date": "2025-06-18",
          "value": 0.25
        }
      ]
    },
    {
      "header": [
        {
          "dim": "Overview",
          "dimItem": "Interest rate on sight deposits above threshold"
        }
      ],
      "metadata": {
        "key": "EPB@SNB.snbgwdzid{ZIG}",
        "frequency": "P1D_L",
        "scale": "",
        "unit": "In percent"
      },
      "values": [
        {
          "date": "2025-06-18",
          "value": 0.0
        }
      ]
    },
    {
      "header": [
        {
          "dim": "Overview",
          "dimItem": "Discount in basis points"
        }
      ],
      "metadata": {
        "key": "EPB@SNB.snbgwdzid{ZIABP}",
        "frequency": "P1D_L",
        "scale": "",
        "unit": "In percent"
      },
      "values": [
        {
          "date": "2025-06-18",
          "value": 25.0
        }
      ]
    },
    {
      "header": [
        {
          "dim": "Overview",
          "dimItem": "Threshold factor"
        }
      ],
      "metadata": {
        "key": "EPB@SNB.snbgwdzid{FREI}",
        "frequency": "P1D_L",
        "scale": "",
        "unit": "In percent"
      },
      "values": [
        {
          "date": "2025-06-18",
          "value": 18.0
        }
      ]
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides various interest rates but does not include the requested residential mortgage APR, prime lending rate, or personal loan interest quote for the specified date and country._
