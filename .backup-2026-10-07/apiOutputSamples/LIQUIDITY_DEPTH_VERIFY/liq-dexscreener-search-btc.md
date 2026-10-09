---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-dexscreener-search-btc
status: approved
captured_at: 2026-10-04T18:40:00Z
request_url: https://api.dexscreener.com/latest/dex/search?q=WBTC%20USDC
content_type: application/json
inputs: |
  WBTC USDC
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must convey bid/ask order-book depth or pool liquidity for the pair asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [0.85|heuristic] DEX pair liquidity present"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "schemaVersion": "1.0.0",
  "pairs": [
    {
      "chainId": "starknet",
      "dexId": "ekubo",
      "url": "https://dexscreener.com/starknet/0x033068f6539f8e6e6b131e6b2b814e6c34a5224bc66947c47dab9dfee93b35fb-0x03fe2b97c1fd336e750087d68b9b867997fd64a2661ff3ca5a7c771641e8e7ac-170141183460469235273462165868118016-1000-0x0",
      "pairAddress": "0x033068f6539f8e6e6b131e6b2b814e6c34a5224bc66947c47dab9dfee93b35fb-0x03fe2b97c1fd336e750087d68b9b867997fd64a2661ff3ca5a7c771641e8e7ac-170141183460469235273462165868118016-1000-0x0",
      "baseToken": {
        "address": "0x03fe2b97c1fd336e750087d68b9b867997fd64a2661ff3ca5a7c771641e8e7ac",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0x033068f6539f8e6e6b131e6b2b814e6c34a5224bc66947c47dab9dfee93b35fb",
        "name": "USDC",
        "symbol": "USDC"
      },
      "priceNative": "85318.4883",
      "priceUsd": "85318.48",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 14,
          "sells": 15
        },
        "h6": {
          "buys": 228,
          "sells": 268
        },
        "h24": {
          "buys": 1477,
          "sells": 1686
        }
      },
      "volume": {
        "h24": 755991.28,
        "h6": 72511.69,
        "h1": 3505.29,
        "m5": 0
      },
      "priceChange": {
        "h1": -0.03,
        "h6": 0.06,
        "h24": 0.62
      },
      "liquidity": {
        "usd": 326231.34,
        "base": 0.558,
        "quote": 278616
      },
      "fdv": 22069029,
      "marketCap": 10692966150,
      "pairCreatedAt": 1764584964000
    },
    {
      "chainId": "solana",
      "dexId": "orca",
      "url": "https://dexscreener.com/solana/55brdtclwaym16gwrmequ57o4ptm6cef9wavsdnzceiy",
      "pairAddress": "55BrDTCLWayM16GwrMEQU57o4PTm6ceF9wavSdNZcEiy",
      "labels": [
        "wp"
      ],
      "baseToken": {
        "address": "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh",
        "name": "Wrapped BTC (Wormhole)",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85347.8617",
      "priceUsd": "85347.86",
      "txns": {
        "m5": {
          "buys": 1,
          "sells": 0
        },
        "h1": {
          "buys": 17,
          "sells": 14
        },
        "h6": {
          "buys": 131,
          "sells": 118
        },
        "h24": {
          "buys": 507,
          "sells": 400
        }
      },
      "volume": {
        "h24": 16185.96,
        "h6": 4755.67,
        "h1": 329.63,
        "m5": 9.99
      },
      "priceChange": {
        "m5": -0.02,
        "h1": 0.07,
        "h6": 0.18,
        "h24": 0.57
      },
      "liquidity": {
        "usd": 124196.63,
        "base": 1.04186,
        "quote": 35275
      },
      "fdv": 329382655,
      "marketCap": 329382655,
      "pairCreatedAt": 1676329419000
    },
    {
      "chainId": "solana",
      "dexId": "meteora",
      "url": "https://dexscreener.com/solana/5nqtw1wqvet6wp1lmohsrydyjp2ndipdv6eulvnbyxmb",
      "pairAddress": "5NQTw1WqVEt6wP1LmohsrYDyJp2NDipdv6eULVNByXMb",
      "labels": [
        "DYN"
      ],
      "baseToken": {
        "address": "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh",
        "name": "Wrapped BTC (Portal)",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85294.4112",
      "priceUsd": "85294.41",
      "txns": {
        "m5": {
          "buys": 1,
          "sells": 2
        },
        "h1": {
          "buys": 16,
          "sells": 21
        },
        "h6": {
          "buys": 130,
          "sells": 141
        },
        "h24": {
          "buys": 558,
          "sells": 576
        }
      },
      "volume": {
        "h24": 5581.89,
        "h6": 1286.37,
        "h1": 154.71,
        "m5": 9.5
      },
      "priceChange": {
        "m5": -0.02,
        "h1": -0.02,
        "h6": 0.08,
        "h24": 0.47
      },
      "liquidity": {
        "usd": 116647.01,
        "base": 0.6838,
        "quote": 58321
      },
      "fdv": 209026165,
      "marketCap": 209026165,
      "pairCreatedAt": 1703167204000
    },
    {
      "chainId": "solana",
      "dexId": "raydium",
      "url": "https://dexscreener.com/solana/8mej5vwwipdjrqtu1darzkwpc7d82o9g7fbvbhv6t8wy",
      "pairAddress": "8meJ5VWWiPDjrqTu1dARzKwpc7D82o9G7FBVBhV6t8WY",
      "labels": [
        "CLMM"
      ],
      "baseToken": {
        "address": "5XZw2LKTyrfvfiskJ78AMpackRjPcyCif1WhUsPDuVqQ",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85490.6159",
      "priceUsd": "85490.61",
      "txns": {
        "m5": {
          "buys": 8,
          "sells": 0
        },
        "h1": {
          "buys": 17,
          "sells": 22
        },
        "h6": {
          "buys": 98,
          "sells": 80
        },
        "h24": {
          "buys": 381,
          "sells": 266
        }
      },
      "volume": {
        "h24": 92392.32,
        "h6": 13138.69,
        "h1": 2828.24,
        "m5": 28.67
      },
      "priceChange": {
        "h1": -0.05,
        "h6": 0.07,
        "h24": 0.34
      },
      "liquidity": {
        "usd": 456132.87,
        "base": 4.3454,
        "quote": 84633
      },
      "fdv": 426769,
      "marketCap": 426769,
      "pairCreatedAt": 1749058234000
    },
    {
      "chainId": "solana",
      "dexId": "meteora",
      "url": "https://dexscreener.com/solana/3sehqcvywwcfjz1ri3nmj7mrkrxbvijmrnn5b6kz8mqn",
      "pairAddress": "3sehQcVywWcFJZ1ri3NmJ7MRkrXbViJMRNN5b6kz8Mqn",
      "labels": [
        "DLMM"
      ],
      "baseToken": {
        "address": "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh",
        "name": "Wrapped BTC (Wormhole)",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85334.1763",
      "priceUsd": "85334.17",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 0
        },
        "h6": {
          "buys": 9,
          "sells": 11
        },
        "h24": {
          "buys": 47,
          "sells": 85
        }
      },
      "volume": {
        "h24": 8024.92,
        "h6": 2371.41,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h6": 0.49,
        "h24": 0.22
      },
      "liquidity": {
        "usd": 124994.36,
        "base": 0.5399,
        "quote": 78921
      },
      "fdv": 329329840,
      "marketCap": 329329840,
      "pairCreatedAt": 1731595082000
    },
    {
      "chainId": "base",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/base/0xf272fa039c68a79015b721df554f3bcb8a54016df9075e67a654b4d63e6afc51",
      "pairAddress": "0xf272fa039c68a79015b721df554f3bcb8a54016df9075e67a654b4d63e6afc51",
      "labels": [
        "v4"
      ],
      "baseToken": {
        "address": "0x0555E30da8f98308EdB960aa94C0Db47230d2B9c",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85113.8784",
      "priceUsd": "85113.87",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 1,
          "sells": 0
        },
        "h6": {
          "buys": 6,
          "sells": 3
        },
        "h24": {
          "buys": 30,
          "sells": 3
        }
      },
      "volume": {
        "h24": 2692.47,
        "h6": 480.77,
        "h1": 21.34,
        "m5": 0
      },
      "priceChange": {
        "h6": 0.05,
        "h24": 0.5
      },
      "liquidity": {
        "usd": 314821.12,
        "base": 3.5935,
        "quote": 8958.1808
      },
      "fdv": 5372139,
      "marketCap": 10667322380,
      "pairCreatedAt": 1755182155000
    },
    {
      "chainId": "seiv2",
      "dexId": "dragonswap",
      "url": "https://dexscreener.com/seiv2/0xe62fd4661c85e126744cc335e9bca8ae3d5d19d1",
      "pairAddress": "0xe62fD4661C85e126744cC335E9bca8Ae3D5d19D1",
      "labels": [
        "V2"
      ],
      "baseToken": {
        "address": "0x0555E30da8f98308EdB960aa94C0Db47230d2B9c",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0xe15fC38F6D8c56aF07bbCBe3BAf5708A2Bf42392",
        "name": "USDC",
        "symbol": "USDC"
      },
      "priceNative": "85123.9982",
      "priceUsd": "85306.50",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 0
        },
        "h6": {
          "buys": 17,
          "sells": 1
        },
        "h24": {
          "buys": 88,
          "sells": 4
        }
      },
      "volume": {
        "h24": 29793.67,
        "h6": 3224.09,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h6": -0.03,
        "h24": 1.27
      },
      "liquidity": {
        "usd": 1543166.2,
        "base": 6.237,
        "quote": 1008944
      },
      "fdv": 1719198,
      "marketCap": 10691464599,
      "pairCreatedAt": 1753354737000
    },
    {
      "chainId": "katana",
      "dexId": "sushiswap",
      "url": "https://dexscreener.com/katana/0x744676b3ced942d78f9b8e9cd22246db5c32395c",
      "pairAddress": "0x744676B3CeD942D78F9b8e9cd22246Db5c32395c",
      "baseToken": {
        "address": "0x0913DA6Da4b42f538B445599b46Bb4622342Cf52",
        "name": "Vault Bridge WBTC",
        "symbol": "vbWBTC"
      },
      "quoteToken": {
        "address": "0x203A662b0BD271A6ed5a60EdFbd04bFce608FD36",
        "name": "Vault Bridge USDC",
        "symbol": "vbUSDC"
      },
      "priceNative": "84897.3647",
      "priceUsd": "84897.36",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 1,
          "sells": 3
        },
        "h6": {
          "buys": 12,
          "sells": 17
        },
        "h24": {
          "buys": 56,
          "sells": 55
        }
      },
      "volume": {
        "h24": 6851.69,
        "h6": 1926.35,
        "h1": 163.17,
        "m5": 0
      },
      "priceChange": {
        "h1": -0.09,
        "h6": 0.03,
        "h24": 0.42
      },
      "liquidity": {
        "usd": 1124984.98,
        "base": 7.008828,
        "quote": 529953
      },
      "fdv": 15737909,
      "marketCap": 15737909,
      "pairCreatedAt": 1752788203000
    },
    {
      "chainId": "cronos",
      "dexId": "vvsfinance",
      "url": "https://dexscreener.com/cronos/0xd6e42e6052561e6eb1b71d0045b7b1bfbdd43dc8",
      "pairAddress": "0xd6E42E6052561e6Eb1b71D0045B7b1bfbDD43DC8",
      "baseToken": {
        "address": "0x062E66477Faf219F25D27dCED647BF57C3107d52",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0xc21223249CA28397B4B6541dfFaEcC539BfF0c59",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "84538.1650",
      "priceUsd": "84538.16",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 1
        },
        "h6": {
          "buys": 4,
          "sells": 3
        },
        "h24": {
          "buys": 19,
          "sells": 7
        }
      },
      "volume": {
        "h24": 1226.57,
        "h6": 277.3,
        "h1": 6.95,
        "m5": 0
      },
      "priceChange": {
        "h1": -0.01,
        "h6": 0.05,
        "h24": 0.22
      },
      "liquidity": {
        "usd": 205207.4,
        "base": 1.2136,
        "quote": 102603
      },
      "fdv": 29080280,
      "marketCap": 10595168232,
      "pairCreatedAt": 1636579660000
    },
    {
      "chainId": "hedera",
      "dexId": "saucerswap",
      "url": "https://dexscreener.com/hedera/0x3c8dbcb8475450569091f8c311b558d62cc39cf7",
      "pairAddress": "0x3c8DBcb8475450569091f8c311B558D62Cc39Cf7",
      "labels": [
        "v2"
      ],
      "baseToken": {
        "address": "0x000000000000000000000000000000000099d925",
        "name": "HTS Wrapped BTC",
        "symbol": "HTS-WBTC"
      },
      "quoteToken": {
        "address": "0x000000000000000000000000000000000006f89a",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85078.3128",
      "priceUsd": "85078.31",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 0
        },
        "h6": {
          "buys": 1,
          "sells": 0
        },
        "h24": {
          "buys": 16,
          "sells": 11
        }
      },
      "volume": {
        "h24": 1415.58,
        "h6": 86.03,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h6": 0.05,
        "h24": 0.21
      },
      "liquidity": {
        "usd": 652759.04,
        "base": 3.8362,
        "quote": 326381
      },
      "fdv": 850937,
      "marketCap": 850937,
      "pairCreatedAt": 1762814542000
    },
    {
      "chainId": "solana",
      "dexId": "meteora",
      "url": "https://dexscreener.com/solana/3fuj4ddswgpjuzrie32ksgmggowknzpnt7t9ad1nozrv",
      "pairAddress": "3fUj4dDSwgpJuzriE32KsgmGGowKNZpnt7T9AD1noZrV",
      "labels": [
        "DLMM"
      ],
      "baseToken": {
        "address": "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh",
        "name": "Wrapped BTC (Wormhole)",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85289.09532",
      "priceUsd": "85289.095",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 25,
          "sells": 36
        },
        "h6": {
          "buys": 152,
          "sells": 149
        },
        "h24": {
          "buys": 490,
          "sells": 458
        }
      },
      "volume": {
        "h24": 64455.27,
        "h6": 22256.76,
        "h1": 5112.89,
        "m5": 0
      },
      "priceChange": {
        "h6": 0.09,
        "h24": 0.42
      },
      "liquidity": {
        "usd": 68045.54,
        "base": 0.3631,
        "quote": 37070
      },
      "fdv": 329155858,
      "marketCap": 329155858,
      "pairCreatedAt": 1714255440000
    },
    {
      "chainId": "pulsechain",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/pulsechain/0x99ac8ca7087fa4a2a1fb6357269965a2014abc35",
      "pairAddress": "0x99ac8cA7087fA4A2A1FB6357269965A2014ABc35",
      "baseToken": {
        "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "quoteToken": {
        "address": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "priceNative": "0.000003720",
      "priceUsd": "0.0007104",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 0
        },
        "h6": {
          "buys": 0,
          "sells": 0
        },
        "h24": {
          "buys": 0,
          "sells": 2
        }
      },
      "volume": {
        "h24": 0.11,
        "h6": 0,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h24": 2.59
      },
      "liquidity": {
        "usd": 74493.24,
        "base": 67610355,
        "quote": 138.5548
      },
      "fdv": 20232812,
      "marketCap": 43269206,
      "pairCreatedAt": 1683945135000
    },
    {
      "chainId": "worldchain",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/worldchain/0xdce053d9ba0fa2c5f772416b64f191158cbcc32e",
      "pairAddress": "0xdCe053d9ba0Fa2c5f772416b64F191158Cbcc32E",
      "baseToken": {
        "address": "0x03C7054BCB39f7b2e5B2c7AcB37583e32D70Cfa3",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0x79A02482A880bCE3F13e09Da970dC34db4CD24d1",
        "name": "USDC",
        "symbol": "USDC"
      },
      "priceNative": "85345.4843",
      "priceUsd": "85345.48",
      "txns": {
        "m5": {
          "buys": 1,
          "sells": 0
        },
        "h1": {
          "buys": 13,
          "sells": 9
        },
        "h6": {
          "buys": 130,
          "sells": 81
        },
        "h24": {
          "buys": 506,
          "sells": 335
        }
      },
      "volume": {
        "h24": 20975.69,
        "h6": 3743.9,
        "h1": 330.41,
        "m5": 9.07
      },
      "priceChange": {
        "m5": 0.04,
        "h1": 0.04,
        "h6": 0.21,
        "h24": 0.69
      },
      "liquidity": {
        "usd": 107089.42,
        "base": 0.6302,
        "quote": 53303
      },
      "fdv": 10156842,
      "marketCap": 10156842
    },
    {
      "chainId": "seiv2",
      "dexId": "dragonswap",
      "url": "https://dexscreener.com/seiv2/0x3d20e9286c1bccf210aa4b3d31c3b70b69a9cb04",
      "pairAddress": "0x3D20E9286C1BcCf210Aa4B3d31C3b70B69A9CB04",
      "labels": [
        "V2"
      ],
      "baseToken": {
        "address": "0x0555E30da8f98308EdB960aa94C0Db47230d2B9c",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0xe15fC38F6D8c56aF07bbCBe3BAf5708A2Bf42392",
        "name": "USDC",
        "symbol": "USDC"
      },
      "priceNative": "85331.6291",
      "priceUsd": "85348.25",
      "txns": {
        "m5": {
          "buys": 6,
          "sells": 6
        },
        "h1": {
          "buys": 32,
          "sells": 32
        },
        "h6": {
          "buys": 169,
          "sells": 159
        },
        "h24": {
          "buys": 638,
          "sells": 607
        }
      },
      "volume": {
        "h24": 700902.31,
        "h6": 179740.09,
        "h1": 30313.04,
        "m5": 3233.8
      },
      "priceChange": {
        "h1": 0.21,
        "h6": -0.2,
        "h24": 0.92
      },
      "liquidity": {
        "usd": 30933.73,
        "base": 0.1889,
        "quote": 14806
      },
      "fdv": 1720039,
      "marketCap": 10696696755,
      "pairCreatedAt": 1790576695000
    },
    {
      "chainId": "base",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/base/0x49e30c322e2474b3767de9fc4448c1e9ced6552f",
      "pairAddress": "0x49e30c322E2474B3767de9FC4448C1e9ceD6552f",
      "labels": [
        "v3"
      ],
      "baseToken": {
        "address": "0x0555E30da8f98308EdB960aa94C0Db47230d2B9c",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85132.7541",
      "priceUsd": "85132.75",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 0
        },
        "h6": {
          "buys": 2,
          "sells": 2
        },
        "h24": {
          "buys": 15,
          "sells": 3
        }
      },
      "volume": {
        "h24": 248,
        "h6": 23.36,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h6": 0.03,
        "h24": 0.47
      },
      "liquidity": {
        "usd": 32745.3,
        "base": 0.07441,
        "quote": 26410
      },
      "fdv": 5373603,
      "marketCap": 10669688083,
      "pairCreatedAt": 1754136507000
    },
    {
      "chainId": "sonic",
      "dexId": "shadow-exchange",
      "url": "https://dexscreener.com/sonic/0x8bc2f9e725cbb07c338df4e77c82190119ddd823",
      "pairAddress": "0x8BC2f9e725cbB07c338df4e77c82190119ddd823",
      "baseToken": {
        "address": "0x0555E30da8f98308EdB960aa94C0Db47230d2B9c",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0x29219dd400f2Bf60E5a23d13Be72B486D4038894",
        "name": "USDC",
        "symbol": "USDC"
      },
      "priceNative": "85189.5827",
      "priceUsd": "85189.58",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 0
        },
        "h6": {
          "buys": 1,
          "sells": 0
        },
        "h24": {
          "buys": 33,
          "sells": 10
        }
      },
      "volume": {
        "h24": 695.35,
        "h6": 28.21,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h6": 0.05,
        "h24": 0.43
      },
      "liquidity": {
        "usd": 26661.98,
        "base": 0.2045,
        "quote": 9233.922
      },
      "fdv": 733558,
      "marketCap": 733558,
      "pairCreatedAt": 1740554348000
    },
    {
      "chainId": "starknet",
      "dexId": "ekubo",
      "url": "https://dexscreener.com/starknet/0x03fe2b97c1fd336e750087d68b9b867997fd64a2661ff3ca5a7c771641e8e7ac-0x053c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8-170141183460469235273462165868118016-1000-0x0",
      "pairAddress": "0x03fe2b97c1fd336e750087d68b9b867997fd64a2661ff3ca5a7c771641e8e7ac-0x053c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8-170141183460469235273462165868118016-1000-0x0",
      "baseToken": {
        "address": "0x03fe2b97c1fd336e750087d68b9b867997fd64a2661ff3ca5a7c771641e8e7ac",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0x053c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85296.8045",
      "priceUsd": "85296.80",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 2,
          "sells": 2
        },
        "h6": {
          "buys": 46,
          "sells": 45
        },
        "h24": {
          "buys": 275,
          "sells": 251
        }
      },
      "volume": {
        "h24": 24467.37,
        "h6": 1846.65,
        "h1": 83.64,
        "m5": 0
      },
      "priceChange": {
        "h1": -0.09,
        "h6": 0.06,
        "h24": 0.43
      },
      "liquidity": {
        "usd": 23018.41,
        "base": 0.1223,
        "quote": 12584
      },
      "fdv": 22063420,
      "marketCap": 10690248512,
      "pairCreatedAt": 1696006915000
    },
    {
      "chainId": "base",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/base/0x9a4ff629a58a25e52fc63b0179f825cf4984e14663a17c89e1a96734db630448",
      "pairAddress": "0x9a4ff629a58a25e52fc63b0179f825cf4984e14663a17c89e1a96734db630448",
      "labels": [
        "v4"
      ],
      "baseToken": {
        "address": "0x0555E30da8f98308EdB960aa94C0Db47230d2B9c",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85286.2915",
      "priceUsd": "85286.29",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 0
        },
        "h6": {
          "buys": 4,
          "sells": 3
        },
        "h24": {
          "buys": 16,
          "sells": 6
        }
      },
      "volume": {
        "h24": 103.49,
        "h6": 44.94,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h6": 0.05,
        "h24": 0.53
      },
      "liquidity": {
        "usd": 23371.51,
        "base": 0.2487,
        "quote": 2152.5171
      },
      "fdv": 5383021,
      "marketCap": 10688930919,
      "pairCreatedAt": 1760801049000
    },
    {
      "chainId": "solana",
      "dexId": "raydium",
      "url": "https://dexscreener.com/solana/4nfbdt7dexatvarzfr3wqalgjnogmjqe9vf2h6c1wxbr",
      "pairAddress": "4nFbdT7DeXATvaRZfR3WqALGJnogMjqe9vf2H6C1WXBr",
      "labels": [
        "CLMM"
      ],
      "baseToken": {
        "address": "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh",
        "name": "Wrapped BTC (Wormhole)",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85286.6827",
      "priceUsd": "85286.68",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 1
        },
        "h1": {
          "buys": 2,
          "sells": 5
        },
        "h6": {
          "buys": 28,
          "sells": 31
        },
        "h24": {
          "buys": 261,
          "sells": 148
        }
      },
      "volume": {
        "h24": 16373.36,
        "h6": 783.74,
        "h1": 4.37,
        "m5": 0
      },
      "priceChange": {
        "h1": -0.05,
        "h6": 0.11,
        "h24": 0.46
      },
      "liquidity": {
        "usd": 14798.53,
        "base": 0.03226,
        "quote": 12047
      },
      "fdv": 329146548,
      "marketCap": 329146548,
      "pairCreatedAt": 1723699297000
    },
    {
      "chainId": "solana",
      "dexId": "raydium",
      "url": "https://dexscreener.com/solana/amufuwfrmbunwf1rycmxszc9mhdcetzrl4uqyb5ubmne",
      "pairAddress": "AMUFUwfrmBunwF1rYcMxSZc9MhDcEtzRL4uqYb5UBmNe",
      "labels": [
        "CPMM"
      ],
      "baseToken": {
        "address": "5XZw2LKTyrfvfiskJ78AMpackRjPcyCif1WhUsPDuVqQ",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85396.3546",
      "priceUsd": "85396.35",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 0
        },
        "h6": {
          "buys": 3,
          "sells": 1
        },
        "h24": {
          "buys": 17,
          "sells": 9
        }
      },
      "volume": {
        "h24": 26.72,
        "h6": 5.94,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h6": 0.11,
        "h24": 0.39
      },
      "liquidity": {
        "usd": 19950.87,
        "base": 0.1168,
        "quote": 9975.4368
      },
      "fdv": 426299,
      "marketCap": 426299,
      "pairCreatedAt": 1749053997000
    },
    {
      "chainId": "solana",
      "dexId": "meteora",
      "url": "https://dexscreener.com/solana/fkzsmbwsxci3hx7x3npnf1cjsstpnaytckpw7md3orbx",
      "pairAddress": "FKZsMbwsXCi3HX7X3NpNF1cJSSTpnAyTcKPW7MD3orBx",
      "labels": [
        "DLMM"
      ],
      "baseToken": {
        "address": "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh",
        "name": "Wrapped BTC (Wormhole)",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85472.2222",
      "priceUsd": "85472.22",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 5,
          "sells": 8
        },
        "h6": {
          "buys": 60,
          "sells": 51
        },
        "h24": {
          "buys": 167,
          "sells": 148
        }
      },
      "volume": {
        "h24": 10326.61,
        "h6": 3528.86,
        "h1": 454.02,
        "m5": 0
      },
      "priceChange": {
        "h1": 0.13,
        "h6": 0.3,
        "h24": 0.77
      },
      "liquidity": {
        "usd": 13467.2,
        "base": 0.0743,
        "quote": 7116.5131
      },
      "fdv": 329862599,
      "marketCap": 329862599,
      "pairCreatedAt": 1718099448000
    },
    {
      "chainId": "katana",
      "dexId": "sushiswap",
      "url": "https://dexscreener.com/katana/0x4488005fd5eea2e22a80cb2a0e820ed6066e687f",
      "pairAddress": "0x4488005Fd5EEa2E22a80cb2A0e820ED6066e687F",
      "baseToken": {
        "address": "0x0913DA6Da4b42f538B445599b46Bb4622342Cf52",
        "name": "Vault Bridge WBTC",
        "symbol": "vbWBTC"
      },
      "quoteToken": {
        "address": "0x203A662b0BD271A6ed5a60EdFbd04bFce608FD36",
        "name": "Vault Bridge USDC",
        "symbol": "vbUSDC"
      },
      "priceNative": "84711.04126",
      "priceUsd": "84711.041",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 0
        },
        "h6": {
          "buys": 1,
          "sells": 0
        },
        "h24": {
          "buys": 9,
          "sells": 0
        }
      },
      "volume": {
        "h24": 150.91,
        "h6": 8.9,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h6": 0.02,
        "h24": 0.29
      },
      "liquidity": {
        "usd": 17171.12,
        "base": 0.06899,
        "quote": 11326
      },
      "fdv": 15703370,
      "marketCap": 15703370,
      "pairCreatedAt": 1751331177000
    },
    {
      "chainId": "monad",
      "dexId": "atlantis-dex",
      "url": "https://dexscreener.com/monad/0x527211c75cfd1771d653b4f3fd8584beba8bb9f8",
      "pairAddress": "0x527211C75cfd1771d653b4f3Fd8584beBA8bb9f8",
      "baseToken": {
        "address": "0x0555E30da8f98308EdB960aa94C0Db47230d2B9c",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0x754704Bc059F8C67012fEd69BC8A327a5aafb603",
        "name": "USDC",
        "symbol": "USDC"
      },
      "priceNative": "85314.006973",
      "priceUsd": "85314.0069",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 6,
          "sells": 5
        },
        "h6": {
          "buys": 14,
          "sells": 11
        },
        "h24": {
          "buys": 38,
          "sells": 37
        }
      },
      "volume": {
        "h24": 667.61,
        "h6": 249.1,
        "h1": 133.6,
        "m5": 0
      },
      "priceChange": {
        "h1": 0.02,
        "h6": 0.11,
        "h24": 0.56
      },
      "liquidity": {
        "usd": 36580.05,
        "base": 0.2152,
        "quote": 18216
      },
      "fdv": 6143188,
      "marketCap": 6143188
    },
    {
      "chainId": "solana",
      "dexId": "raydium",
      "url": "https://dexscreener.com/solana/6zpvji4hrocxg8tqbthdsb5wccrehw1qck5ssnqtk3yd",
      "pairAddress": "6ZpVJi4HRoCXg8TQbThdsB5WccReHw1qck5sSnQTK3yd",
      "labels": [
        "CLMM"
      ],
      "baseToken": {
        "address": "7Keaqyqr6jfpeJL3J7f3NCfnuMBkcuoYiGQoSHJ42HZD",
        "name": "Wrapped Bitcoin",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "84291.2504",
      "priceUsd": "84291.25",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 0
        },
        "h6": {
          "buys": 0,
          "sells": 0
        },
        "h24": {
          "buys": 6,
          "sells": 0
        }
      },
      "volume": {
        "h24": 6000,
        "h6": 0,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {},
      "liquidity": {
        "usd": 9818834896.95,
        "base": 116486,
        "quote": 6000
      },
      "fdv": 9819846391,
      "marketCap": 9819846391,
      "pairCreatedAt": 1791096886000
    },
    {
      "chainId": "sonic",
      "dexId": "swapx",
      "url": "https://dexscreener.com/sonic/0x3ccee9fd8258e47e16f5274ee539e8bff3d92c38",
      "pairAddress": "0x3ccee9FD8258e47E16F5274Ee539e8bfF3D92C38",
      "labels": [
        "v3"
      ],
      "baseToken": {
        "address": "0x0555E30da8f98308EdB960aa94C0Db47230d2B9c",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0x29219dd400f2Bf60E5a23d13Be72B486D4038894",
        "name": "USDC",
        "symbol": "USDC"
      },
      "priceNative": "85119.8520",
      "priceUsd": "85119.85",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 0
        },
        "h6": {
          "buys": 1,
          "sells": 0
        },
        "h24": {
          "buys": 13,
          "sells": 3
        }
      },
      "volume": {
        "h24": 585.02,
        "h6": 28.35,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h6": 0.08,
        "h24": 0.48
      },
      "liquidity": {
        "usd": 8663.92,
        "base": 0.07051,
        "quote": 2662.1058
      },
      "fdv": 732958,
      "marketCap": 732958
    },
    {
      "chainId": "arbitrum",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/arbitrum/0x0e4831319a50228b9e450861297ab92dee15b44f",
      "pairAddress": "0x0E4831319A50228B9e450861297aB92dee15B44F",
      "baseToken": {
        "address": "0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85281.4416",
      "priceUsd": "85299.18",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 25,
          "sells": 26
        },
        "h6": {
          "buys": 232,
          "sells": 184
        },
        "h24": {
          "buys": 699,
          "sells": 489
        }
      },
      "volume": {
        "h24": 1901110.27,
        "h6": 627981.43,
        "h1": 78868.92,
        "m5": 0
      },
      "priceChange": {
        "h1": 0.01,
        "h6": 0.13,
        "h24": 0.49
      },
      "liquidity": {
        "usd": 8059024.96,
        "base": 41.02652,
        "quote": 4558546
      },
      "fdv": 627302455,
      "marketCap": 627294052,
      "pairCreatedAt": 1687954043000
    },
    {
      "chainId": "aptos",
      "dexId": "thala",
      "url": "https://dexscreener.com/aptos/0xb64243d319b686130cf5a11d027589373106acf8d1bcce1531b860e92dbe70fe-0x68844a0d7f2587e726ad0579f3d640865bb4162c08a4589eeda3f9689ec52a3d-0xbae207659db88bea0cbead6da0ed00aac12edcdda169e591cd41c94180b46f3b",
      "pairAddress": "0xb64243d319b686130cf5a11d027589373106acf8d1bcce1531b860e92dbe70fe-0x68844a0d7f2587e726ad0579f3d640865bb4162c08a4589eeda3f9689ec52a3d-0xbae207659db88bea0cbead6da0ed00aac12edcdda169e591cd41c94180b46f3b",
      "labels": [
        "v2"
      ],
      "baseToken": {
        "address": "0xbae207659db88bea0cbead6da0ed00aac12edcdda169e591cd41c94180b46f3b",
        "name": "USDC",
        "symbol": "USDC"
      },
      "quoteToken": {
        "address": "0x68844a0d7f2587e726ad0579f3d640865bb4162c08a4589eeda3f9689ec52a3d",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "priceNative": "0.00001291",
      "priceUsd": "1.10",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 3
        },
        "h6": {
          "buys": 19,
          "sells": 21
        },
        "h24": {
          "buys": 50,
          "sells": 56
        }
      },
      "volume": {
        "h24": 164.81,
        "h6": 59.98,
        "h1": 4.7,
        "m5": 0
      },
      "priceChange": {
        "h1": 0.09,
        "h6": 0.24,
        "h24": -0.02
      },
      "liquidity": {
        "usd": 7466.31,
        "base": 3549.5744,
        "quote": 0.04164
      },
      "fdv": 380953475,
      "marketCap": 67115557991,
      "pairCreatedAt": 1753152050000
    },
    {
      "chainId": "optimism",
      "dexId": "velodrome",
      "url": "https://dexscreener.com/optimism/0xcf50dea65ee80ebddaa61005a960ef5a5c995a99",
      "pairAddress": "0xCF50DEA65EE80eBDDAA61005a960ef5A5c995A99",
      "baseToken": {
        "address": "0x68f180fcCe6836688e9084f035309E29Bf0A2095",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "85117.02927",
      "priceUsd": "85286.89",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 6,
          "sells": 9
        },
        "h6": {
          "buys": 183,
          "sells": 149
        },
        "h24": {
          "buys": 930,
          "sells": 549
        }
      },
      "volume": {
        "h24": 281098.31,
        "h6": 78893.38,
        "h1": 4146.08,
        "m5": 0
      },
      "priceChange": {
        "h1": -0.03,
        "h6": 0.16,
        "h24": 0.43
      },
      "liquidity": {
        "usd": 460381.37,
        "base": 2.1341,
        "quote": 277813
      },
      "fdv": 58993103,
      "marketCap": 58993103
    },
    {
      "chainId": "polygon",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/polygon/0xeef1a9507b3d505f0062f2be9453981255b503c8",
      "pairAddress": "0xeEF1A9507B3D505f0062f2be9453981255b503c8",
      "baseToken": {
        "address": "0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6",
        "name": "(PoS) Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
        "name": "USD Coin (PoS)",
        "symbol": "USDC"
      },
      "priceNative": "85303.4073",
      "priceUsd": "85303.40",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 10,
          "sells": 32
        },
        "h6": {
          "buys": 107,
          "sells": 138
        },
        "h24": {
          "buys": 471,
          "sells": 413
        }
      },
      "volume": {
        "h24": 389019.85,
        "h6": 89563.89,
        "h1": 11570.42,
        "m5": 0
      },
      "priceChange": {
        "h1": -0.05,
        "h6": 0.21,
        "h24": 0.45
      },
      "liquidity": {
        "usd": 644909.75,
        "base": 4.02854,
        "quote": 301261
      },
      "fdv": 163337540,
      "marketCap": 189519650,
      "pairCreatedAt": 1640558930000
    },
    {
      "chainId": "scroll",
      "dexId": "zebra",
      "url": "https://dexscreener.com/scroll/0x0460fd72f1099fb07a6fe13435cde3c471811515",
      "pairAddress": "0x0460fd72F1099fB07a6fe13435CdE3c471811515",
      "baseToken": {
        "address": "0x3C1BCa5a656e69edCD0D4E36BEbb3FcDAcA60Cf1",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "quoteToken": {
        "address": "0x06eFdBFf2a14a7c8E15944D1F4A48F9F95F663A4",
        "name": "USD Coin",
        "symbol": "USDC"
      },
      "priceNative": "84518.2723",
      "priceUsd": "84518.27",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 0
        },
        "h6": {
          "buys": 0,
          "sells": 1
        },
        "h24": {
          "buys": 2,
          "sells": 1
        }
      },
      "volume": {
        "h24": 5.23,
        "h6": 0.92,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h6": -0.12,
        "h24": 0.24
      },
      "liquidity": {
        "usd": 3695.65,
        "base": 0.009236,
        "quote": 2915.003217
      },
      "fdv": 324137,
      "marketCap": 324137,
      "pairCreatedAt": 1702279275000
    }
  ]
}
```

## Why this matches (or not)

_[0.85|heuristic] DEX pair liquidity present_
