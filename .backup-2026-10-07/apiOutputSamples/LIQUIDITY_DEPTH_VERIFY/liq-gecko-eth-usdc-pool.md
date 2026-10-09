---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-gecko-eth-usdc-pool
status: approved
captured_at: 2026-10-04T18:39:56Z
request_url: https://api.geckoterminal.com/api/v2/networks/eth/pools/0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640
content_type: application/json
inputs: |
  Uniswap V3 WETH/USDC pool
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must convey bid/ask order-book depth or pool liquidity for the pair asked.
capture_note: |
  DEX pool reserve/liquidity — best catalog fit (prefer over CEX books)
reviewer_note: "auto_review: [0.85|heuristic] DEX pool reserves/liquidity present"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "data": {
    "id": "eth_0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
    "type": "pool",
    "attributes": {
      "base_token_price_usd": "2700.79",
      "base_token_price_native_currency": "1.0",
      "quote_token_price_usd": "0.99928623215785",
      "quote_token_price_native_currency": "0.000369998873370117",
      "base_token_price_quote_token": "2702.710932311",
      "quote_token_price_base_token": "0.0003699988734",
      "address": "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
      "name": "WETH / USDC 0.05%",
      "pool_name": "WETH / USDC",
      "pool_fee_percentage": "0.05",
      "pool_created_at": "2021-12-29T12:35:14Z",
      "fdv_usd": "5530979861.88509",
      "market_cap_usd": "5533831201.00416",
      "price_change_percentage": {
        "m5": "-0.001",
        "m15": "0.009",
        "m30": "0.01",
        "h1": "-0.031",
        "h6": "-0.023",
        "h24": "0.575"
      },
      "transactions": {
        "m5": {
          "buys": 5,
          "sells": 3,
          "buyers": 5,
          "sellers": 3
        },
        "m15": {
          "buys": 35,
          "sells": 57,
          "buyers": 35,
          "sellers": 49
        },
        "m30": {
          "buys": 55,
          "sells": 165,
          "buyers": 54,
          "sellers": 151
        },
        "h1": {
          "buys": 125,
          "sells": 255,
          "buyers": 101,
          "sellers": 205
        },
        "h6": {
          "buys": 2176,
          "sells": 2516,
          "buyers": 943,
          "sellers": 1169
        },
        "h24": {
          "buys": 6104,
          "sells": 6826,
          "buyers": 1837,
          "sellers": 2319
        }
      },
      "volume_usd": {
        "m5": "1052.9924549786",
        "m15": "21256.8792124062",
        "m30": "469951.374132175",
        "h1": "1084859.26381408",
        "h6": "4515489.59674033",
        "h24": "17180059.2875897"
      },
      "reserve_in_usd": "98049483.9936",
      "locked_liquidity_percentage": "0.0"
    },
    "relationships": {
      "base_token": {
        "data": {
          "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
          "type": "token"
        }
      },
      "quote_token": {
        "data": {
          "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
          "type": "token"
        }
      },
      "dex": {
        "data": {
          "id": "uniswap_v3",
          "type": "dex"
        }
      }
    }
  }
}
```

## Why this matches (or not)

_[0.85|heuristic] DEX pool reserves/liquidity present_
