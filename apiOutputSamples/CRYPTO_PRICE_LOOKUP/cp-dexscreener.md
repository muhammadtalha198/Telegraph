---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-dexscreener
status: approved
captured_at: 2026-10-08T04:41:44Z
request_url: https://api.dexscreener.com/latest/dex/pairs/ethereum/0x99ac8cA7087fA4A2A1FB6357269965A2014ABc35
content_type: application/json
inputs: |
  {"sym": "BTC", "sym_lower": "btc", "deribit_idx": "btc_usd", "erc20": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", "dsx_pair": "0x99ac8cA7087fA4A2A1FB6357269965A2014ABc35", "ir": "xbt", "cl_feed": "0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the current price of BTC (Wrapped BTC) in USD (USDC)"
reviewed_at: 2026-10-08T04:54:24Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "schemaVersion": "1.0.0",
  "pairs": [
    {
      "chainId": "ethereum",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/ethereum/0x99ac8ca7087fa4a2a1fb6357269965a2014abc35",
      "pairAddress": "0x99ac8cA7087fA4A2A1FB6357269965A2014ABc35",
      "labels": [
        "v3"
      ],
      "baseToken": {
        "address": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "82597.3904",
      "priceUsd": "82597.39",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 10,
          "sells": 13
        },
        "h6": {
          "buys": 10,
          "sells": 30
        },
        "h24": {
          "buys": 51,
          "sells": 103
        }
      },
      "volume": {
        "h24": 1635261.14,
        "h6": 453712.65,
        "h1": 281450.96,
        "m5": 0
      },
      "priceChange": {
        "h1": -0.32,
        "h6": -0.84,
        "h24": -1.59
      },
      "liquidity": {
        "usd": 21955136.56,
        "base": 124.2909,
        "quote": 11689028
      },
      "fdv": 9592213654,
      "marketCap": 9592213654,
      "pairCreatedAt": 1620241995000
    }
  ],
  "pair": {
    "chainId": "ethereum",
    "dexId": "uniswap",
    "url": "https://dexscreener.com/ethereum/0x99ac8ca7087fa4a2a1fb6357269965a2014abc35",
    "pairAddress": "0x99ac8cA7087fA4A2A1FB6357269965A2014ABc35",
    "labels": [
      "v3"
    ],
    "baseToken": {
      "address": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
      "name": "Wrapped BTC",
      "symbol": "WBTC"
    },
    "quoteToken": {
      "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
      "name": "USD Coin",
      "symbol": "USDC"
    },
    "priceNative": "82597.3904",
    "priceUsd": "82597.39",
    "txns": {
      "m5": {
        "buys": 0,
        "sells": 0
      },
      "h1": {
        "buys": 10,
        "sells": 13
      },
      "h6": {
        "buys": 10,
        "sells": 30
      },
      "h24": {
        "buys": 51,
        "sells": 103
      }
    },
    "volume": {
      "h24": 1635261.14,
      "h6": 453712.65,
      "h1": 281450.96,
      "m5": 0
    },
    "priceChange": {
      "h1": -0.32,
      "h6": -0.84,
      "h24": -1.59
    },
    "liquidity": {
      "usd": 21955136.56,
      "base": 124.2909,
      "quote": 11689028
    },
    "fdv": 9592213654,
    "marketCap": 9592213654,
    "pairCreatedAt": 1620241995000
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the current price of BTC (Wrapped BTC) in USD (USDC)_
