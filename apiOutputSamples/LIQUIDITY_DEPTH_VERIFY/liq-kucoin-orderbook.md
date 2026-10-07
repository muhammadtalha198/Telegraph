---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-kucoin-orderbook
status: pending_review
captured_at: 2026-10-04T18:40:01Z
request_url: https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=BTC-USDT
content_type: application/json
inputs: |
  BTC-USDT
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must convey bid/ask order-book depth or pool liquidity for the pair asked.
capture_note: |
  CEX
reviewer_note: "re-review after heuristic fix"
reviewed_at: ""
---

## Raw API output

```json
{
  "code": "200000",
  "data": {
    "time": 1791139201741,
    "sequence": "38167273261",
    "bids": [
      [
        "85312",
        "0.41403412"
      ],
      [
        "85311.6",
        "0.0025"
      ],
      [
        "85311.2",
        "0.00004405"
      ],
      [
        "85311",
        "0.01"
      ],
      [
        "85310.7",
        "0.04131003"
      ],
      [
        "85310.6",
        "0.0025"
      ],
      [
        "85310",
        "0.01"
      ],
      [
        "85309.6",
        "0.0025"
      ],
      [
        "85309.2",
        "0.02309773"
      ],
      [
        "85309",
        "0.04516541"
      ],
      [
        "85308.9",
        "0.01762406"
      ],
      [
        "85308.6",
        "0.0025"
      ],
      [
        "85308.3",
        "0.01758"
      ],
      [
        "85308",
        "0.01"
      ],
      [
        "85307.8",
        "0.01997923"
      ],
      [
        "85307.6",
        "0.0025"
      ],
      [
        "85307.3",
        "0.02309773"
      ],
      [
        "85307.2",
        "0.09976607"
      ],
      [
        "85307.1",
        "0.07863101"
      ],
      [
        "85307",
        "0.01"
      ]
    ],
    "asks": [
      [
        "85312.1",
        "0.17962569"
      ],
      [
        "85313.2",
        "0.06723056"
      ],
      [
        "85313.5",
        "0.08670289"
      ],
      [
        "85314",
        "0.01047718"
      ],
      [
        "85314.9",
        "0.05962654"
      ],
      [
        "85315.2",
        "0.04495776"
      ],
      [
        "85316.6",
        "0.09603617"
      ],
      [
        "85316.9",
        "0.07884588"
      ],
      [
        "85318.3",
        "0.00986149"
      ],
      [
        "85318.7",
        "0.00004404"
      ],
      [
        "85320.1",
        "0.3179858"
      ],
      [
        "85320.2",
        "1.06527905"
      ],
      [
        "85321",
        "0.00004403"
      ],
      [
        "85322.5",
        "0.00586073"
      ],
      [
        "85323.9",
        "0.01282844"
      ],
      [
        "85324",
        "0.04297635"
      ],
      [
        "85325",
        "0.00004402"
      ],
      [
        "85325.5",
        "0.11776964"
      ],
      [
        "85325.6",
        "0.39449414"
      ],
      [
        "85327.4",
        "0.00004401"
      ]
    ]
  }
}
```

## Why this matches (or not)

_[0.80|heuristic] no bid/ask depth or pool liquidity structure found_
