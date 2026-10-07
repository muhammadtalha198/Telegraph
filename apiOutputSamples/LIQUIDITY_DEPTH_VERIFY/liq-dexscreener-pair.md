---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-dexscreener-pair
status: approved
captured_at: 2026-10-04T18:39:59Z
request_url: https://api.dexscreener.com/latest/dex/pairs/ethereum/0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640
content_type: application/json
inputs: |
  0x88e6…5640 eth
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must convey bid/ask order-book depth or pool liquidity for the pair asked.
capture_note: |
  liquidity.usd + depth-ish metrics
reviewer_note: "auto_review: [0.85|heuristic] DEX pair liquidity present"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "schemaVersion": "1.0.0",
  "pairs": [
    {
      "chainId": "ethereum",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/ethereum/0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
      "pairAddress": "0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640",
      "labels": [
        "v3"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "2701.3735",
      "priceUsd": "2701.37",
      "txns": {
        "m5": {
          "buys": 5,
          "sells": 3
        },
        "h1": {
          "buys": 125,
          "sells": 255
        },
        "h6": {
          "buys": 2176,
          "sells": 2519
        },
        "h24": {
          "buys": 6104,
          "sells": 6834
        }
      },
      "volume": {
        "h24": 17174868.85,
        "h6": 4517308.87,
        "h1": 1086321.32,
        "m5": 1053.34
      },
      "priceChange": {
        "h1": -0.05,
        "h6": 0.01,
        "h24": 0.58
      },
      "liquidity": {
        "usd": 98107272.35,
        "base": 8602.7839,
        "quote": 74867938
      },
      "fdv": 5528581517,
      "marketCap": 5530815254,
      "pairCreatedAt": 1620250931000,
      "info": {
        "imageUrl": "https://cdn.dexscreener.com/cms/images/e7ad3f643e8706e541538413f2afad46f18cafb430606caae3c70c0f7425c16e?width=800&height=800&quality=95&format=auto",
        "openGraph": "https://cdn.dexscreener.com/token-images/og/ethereum/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2?timestamp=1791138900000",
        "websites": [],
        "socials": []
      }
    }
  ],
  "pair": {
    "chainId": "ethereum",
    "dexId": "uniswap",
    "url": "https://dexscreener.com/ethereum/0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
    "pairAddress": "0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640",
    "labels": [
      "v3"
    ],
    "baseToken": {
      "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
      "name": "Wrapped Ether",
      "symbol": "WETH"
    },
    "quoteToken": {
      "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
      "name": "USD Coin",
      "symbol": "USDC"
    },
    "priceNative": "2701.3735",
    "priceUsd": "2701.37",
    "txns": {
      "m5": {
        "buys": 5,
        "sells": 3
      },
      "h1": {
        "buys": 125,
        "sells": 255
      },
      "h6": {
        "buys": 2176,
        "sells": 2519
      },
      "h24": {
        "buys": 6104,
        "sells": 6834
      }
    },
    "volume": {
      "h24": 17174868.85,
      "h6": 4517308.87,
      "h1": 1086321.32,
      "m5": 1053.34
    },
    "priceChange": {
      "h1": -0.05,
      "h6": 0.01,
      "h24": 0.58
    },
    "liquidity": {
      "usd": 98107272.35,
      "base": 8602.7839,
      "quote": 74867938
    },
    "fdv": 5528581517,
    "marketCap": 5530815254,
    "pairCreatedAt": 1620250931000,
    "info": {
      "imageUrl": "https://cdn.dexscreener.com/cms/images/e7ad3f643e8706e541538413f2afad46f18cafb430606caae3c70c0f7425c16e?width=800&height=800&quality=95&format=auto",
      "openGraph": "https://cdn.dexscreener.com/token-images/og/ethereum/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2?timestamp=1791138900000",
      "websites": [],
      "socials": []
    }
  }
}
```

## Why this matches (or not)

_[0.85|heuristic] DEX pair liquidity present_
