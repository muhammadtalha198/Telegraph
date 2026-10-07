---
intent: GRID_POWER_PRICE
slug: grid-awattar-de
status: approved
captured_at: 2026-10-05T09:36:48Z
request_url: https://api.awattar.de/v1/marketdata
content_type: application/json
inputs: |
  {}
intent_description: |
  Ingests real-time nodal marginal locational prices (LMP) and day-ahead electricity spot rates from regional grid operators.
answer_requirement: |
  Must return current/day-ahead electricity spot prices for the grid region asked.
capture_note: |
  golden-test PASS: aWATTar
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides multiple market prices, one of which is the current/day-ahead price."
reviewed_at: 2026-10-05T11:32:17Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "object": "list",
  "data": [
    {
      "start_timestamp": 1791190800000,
      "end_timestamp": 1791194400000,
      "marketprice": 92.45,
      "unit": "Eur/MWh"
    },
    {
      "start_timestamp": 1791194400000,
      "end_timestamp": 1791198000000,
      "marketprice": 59.65,
      "unit": "Eur/MWh"
    },
    {
      "start_timestamp": 1791198000000,
      "end_timestamp": 1791201600000,
      "marketprice": 6.71,
      "unit": "Eur/MWh"
    },
    {
      "start_timestamp": 1791201600000,
      "end_timestamp": 1791205200000,
      "marketprice": 35.95,
      "unit": "Eur/MWh"
    },
    {
      "start_timestamp": 1791205200000,
      "end_timestamp": 1791208800000,
      "marketprice": 70.64,
      "unit": "Eur/MWh"
    },
    {
      "start_timestamp": 1791208800000,
      "end_timestamp": 1791212400000,
      "marketprice": 128.97,
      "unit": "Eur/MWh"
    },
    {
      "start_timestamp": 1791212400000,
      "end_timestamp": 1791216000000,
      "marketprice": 184.31,
      "unit": "Eur/MWh"
    },
    {
      "start_timestamp": 1791216000000,
      "end_timestamp": 1791219600000,
      "marketprice": 224.72,
      "unit": "Eur/MWh"
    },
    {
      "start_timestamp": 1791219600000,
      "end_timestamp": 1791223200000,
      "marketprice": 252.05,
      "unit": "Eur/MWh"
    },
    {
      "start_timestamp": 1791223200000,
      "end_timestamp": 1791226800000,
      "marketprice": 221.84,
      "unit": "Eur/MWh"
    },
    {
      "start_timestamp": 1791226800000,
      "end_timestamp": 1791230400000,
      "marketprice": 200.2,
      "unit": "Eur/MWh"
    },
    {
      "start_timestamp": 1791230400000,
      "end_timestamp": 1791234000000,
      "marketprice": 189.26,
      "unit": "Eur/MWh"
    },
    {
      "start_timestamp": 1791234000000,
      "end_timestamp": 1791237600000,
      "marketprice": 167.52,
      "unit": "Eur/MWh"
    }
  ],
  "url": "/de/v1/marketdata"
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides multiple market prices, one of which is the current/day-ahead price._
