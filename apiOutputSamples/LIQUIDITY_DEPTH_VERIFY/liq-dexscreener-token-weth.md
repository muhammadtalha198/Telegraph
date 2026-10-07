---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-dexscreener-token-weth
status: approved
captured_at: 2026-10-04T18:39:59Z
request_url: https://api.dexscreener.com/latest/dex/tokens/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
content_type: application/json
inputs: |
  WETH token pools
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
      "chainId": "pulsechain",
      "dexId": "pulsex",
      "url": "https://dexscreener.com/pulsechain/0x7994d526a127979bcb9ec7c98509bb5c7ebd78fd",
      "pairAddress": "0x7994d526A127979BcB9Ec7C98509BB5C7ebD78FD",
      "labels": [
        "v2"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0xA1077a294dDE1B09bB078844df40758a5D0f9a27",
        "name": "Wrapped Pulse",
        "symbol": "WPLS"
      },
      "priceNative": "1.001581",
      "priceUsd": "0.000009169",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 5
        },
        "h6": {
          "buys": 3,
          "sells": 10
        },
        "h24": {
          "buys": 35,
          "sells": 33
        }
      },
      "volume": {
        "h24": 74.92,
        "h6": 23.8,
        "h1": 4.81,
        "m5": 0
      },
      "priceChange": {
        "h1": 1.45,
        "h6": 2.16,
        "h24": 6.83
      },
      "liquidity": {
        "usd": 114354,
        "base": 6235877993,
        "quote": 6245743076
      },
      "fdv": 309648,
      "marketCap": 309648,
      "pairCreatedAt": 1685651285000
    },
    {
      "chainId": "pulsechain",
      "dexId": "pulsex",
      "url": "https://dexscreener.com/pulsechain/0x8f61d8fd20aef7f15019986ba277aeaf75b5062e",
      "pairAddress": "0x8f61d8Fd20aEF7f15019986BA277aeaf75B5062e",
      "labels": [
        "v1"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0xCc78A0acDF847A2C1714D2A925bB4477df5d48a6",
        "name": "Atropa",
        "symbol": "ATROPA"
      },
      "priceNative": "0.0002663",
      "priceUsd": "0.000009127",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 7,
          "sells": 0
        },
        "h6": {
          "buys": 27,
          "sells": 4
        },
        "h24": {
          "buys": 58,
          "sells": 41
        }
      },
      "volume": {
        "h24": 864.78,
        "h6": 283.25,
        "h1": 102.33,
        "m5": 0
      },
      "priceChange": {
        "h1": 1.01,
        "h6": 1.71,
        "h24": 6.9
      },
      "liquidity": {
        "usd": 27388.23,
        "base": 1500290304,
        "quote": 399677
      },
      "fdv": 308251,
      "marketCap": 308251,
      "pairCreatedAt": 1685332495000
    },
    {
      "chainId": "pulsechain",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/pulsechain/0xc2e9f25be6257c210d7adf0d4cd6e3e881ba25f8",
      "pairAddress": "0xC2e9F25Be6257c210d7Adf0D4Cd6E3E881ba25f8",
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
        "name": "Dai Stablecoin",
        "symbol": "DAI"
      },
      "priceNative": "0.005456",
      "priceUsd": "0.000009124",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 13,
          "sells": 0
        },
        "h6": {
          "buys": 18,
          "sells": 3
        },
        "h24": {
          "buys": 41,
          "sells": 48
        }
      },
      "volume": {
        "h24": 1029.76,
        "h6": 263.4,
        "h1": 195.14,
        "m5": 0
      },
      "priceChange": {
        "h1": 0.98,
        "h6": 1.6,
        "h24": 6.5
      },
      "liquidity": {
        "usd": 23097.36,
        "base": 1001324013,
        "quote": 8348171
      },
      "fdv": 308152,
      "marketCap": 308152,
      "pairCreatedAt": 1683944525000
    },
    {
      "chainId": "pulsechain",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/pulsechain/0x4e68ccd3e89f51c3074ca5072bbac773960dfa36",
      "pairAddress": "0x4e68Ccd3E89f51C3074ca5072bbAC773960dFa36",
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
        "name": "Tether USD",
        "symbol": "USDT"
      },
      "priceNative": "0.01270",
      "priceUsd": "0.000009108",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 2,
          "sells": 0
        },
        "h6": {
          "buys": 6,
          "sells": 2
        },
        "h24": {
          "buys": 10,
          "sells": 21
        }
      },
      "volume": {
        "h24": 75.46,
        "h6": 27.53,
        "h1": 6.76,
        "m5": 0
      },
      "priceChange": {
        "h1": 1.88,
        "h6": 4.53,
        "h24": 4.87
      },
      "liquidity": {
        "usd": 14442.51,
        "base": 227896198,
        "quote": 17248181
      },
      "fdv": 307598,
      "marketCap": 307598,
      "pairCreatedAt": 1683944585000
    },
    {
      "chainId": "ethereum",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/ethereum/0xe0554a476a092703abdb3ef35c80e0d76d32939f",
      "pairAddress": "0xE0554a476A092703abdB3Ef35c80e0D76d32939F",
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
      "priceNative": "2700.9926",
      "priceUsd": "2700.99",
      "txns": {
        "m5": {
          "buys": 41,
          "sells": 29
        },
        "h1": {
          "buys": 621,
          "sells": 448
        },
        "h6": {
          "buys": 3141,
          "sells": 2961
        },
        "h24": {
          "buys": 12260,
          "sells": 11979
        }
      },
      "volume": {
        "h24": 45689482.88,
        "h6": 19661139.12,
        "h1": 1603739.88,
        "m5": 77811.92
      },
      "priceChange": {
        "h1": -0.03,
        "h6": -0.01,
        "h24": 0.61
      },
      "liquidity": {
        "usd": 6996535.41,
        "base": 1238.5294,
        "quote": 3651276
      },
      "fdv": 5527801937,
      "marketCap": 5530035359,
      "pairCreatedAt": 1636926269000,
      "info": {
        "imageUrl": "https://cdn.dexscreener.com/cms/images/e7ad3f643e8706e541538413f2afad46f18cafb430606caae3c70c0f7425c16e?width=800&height=800&quality=95&format=auto",
        "openGraph": "https://cdn.dexscreener.com/token-images/og/ethereum/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2?timestamp=1791138900000",
        "websites": [],
        "socials": []
      }
    },
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
    },
    {
      "chainId": "ethereum",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/ethereum/0xc7bbec68d12a0d1830360f8ec58fa599ba1b0e9b",
      "pairAddress": "0xc7bBeC68d12a0d1830360F8Ec58fA599bA1b0e9b",
      "labels": [
        "v3"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
        "name": "Tether USD",
        "symbol": "USDT"
      },
      "priceNative": "2701.3693",
      "priceUsd": "2701.36",
      "txns": {
        "m5": {
          "buys": 9,
          "sells": 15
        },
        "h1": {
          "buys": 181,
          "sells": 184
        },
        "h6": {
          "buys": 1314,
          "sells": 1100
        },
        "h24": {
          "buys": 5034,
          "sells": 4431
        }
      },
      "volume": {
        "h24": 5606352.08,
        "h6": 1406597.98,
        "h1": 177313.2,
        "m5": 6034.32
      },
      "priceChange": {
        "h1": -0.03,
        "h6": -0.01,
        "h24": 0.6
      },
      "liquidity": {
        "usd": 3924082.34,
        "base": 995.6761,
        "quote": 1234393
      },
      "fdv": 5528572773,
      "marketCap": 5530806507,
      "pairCreatedAt": 1672029467000,
      "info": {
        "imageUrl": "https://cdn.dexscreener.com/cms/images/e7ad3f643e8706e541538413f2afad46f18cafb430606caae3c70c0f7425c16e?width=800&height=800&quality=95&format=auto",
        "openGraph": "https://cdn.dexscreener.com/token-images/og/ethereum/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2?timestamp=1791138900000",
        "websites": [],
        "socials": []
      }
    },
    {
      "chainId": "ethereum",
      "dexId": "pancakeswap",
      "url": "https://dexscreener.com/ethereum/0x1445f32d1a74872ba41f3d8cf4022e9996120b31",
      "pairAddress": "0x1445F32D1A74872bA41f3D8cF4022E9996120b31",
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
      "priceNative": "2701.2248",
      "priceUsd": "2701.22",
      "txns": {
        "m5": {
          "buys": 5,
          "sells": 1
        },
        "h1": {
          "buys": 57,
          "sells": 45
        },
        "h6": {
          "buys": 410,
          "sells": 437
        },
        "h24": {
          "buys": 2223,
          "sells": 2077
        }
      },
      "volume": {
        "h24": 1632060,
        "h6": 380269.61,
        "h1": 8715.35,
        "m5": 328.78
      },
      "priceChange": {
        "m5": 0.02,
        "h1": -0.04,
        "h6": -0.05,
        "h24": 0.62
      },
      "liquidity": {
        "usd": 613318.9,
        "base": 96.728,
        "quote": 352034
      },
      "fdv": 5539891919,
      "marketCap": 5530510769,
      "pairCreatedAt": 1710314003000,
      "info": {
        "imageUrl": "https://cdn.dexscreener.com/cms/images/e7ad3f643e8706e541538413f2afad46f18cafb430606caae3c70c0f7425c16e?width=800&height=800&quality=95&format=auto",
        "openGraph": "https://cdn.dexscreener.com/token-images/og/ethereum/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2?timestamp=1791138900000",
        "websites": [],
        "socials": []
      }
    },
    {
      "chainId": "ethereum",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/ethereum/0xe500210c7ea6bfd9f69dce044b09ef384ec2b34832f132baec3b418208e3a657",
      "pairAddress": "0xe500210c7ea6bfd9f69dce044b09ef384ec2b34832f132baec3b418208e3a657",
      "labels": [
        "v4"
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
      "priceNative": "2700.7415",
      "priceUsd": "2700.74",
      "txns": {
        "m5": {
          "buys": 1,
          "sells": 0
        },
        "h1": {
          "buys": 67,
          "sells": 61
        },
        "h6": {
          "buys": 526,
          "sells": 454
        },
        "h24": {
          "buys": 1739,
          "sells": 1672
        }
      },
      "volume": {
        "h24": 4040556.67,
        "h6": 1240568.88,
        "h1": 123691.44,
        "m5": 8.84
      },
      "priceChange": {
        "h1": -0.03,
        "h24": 0.63
      },
      "liquidity": {
        "usd": 3325398.71,
        "base": 536.7586,
        "quote": 1875752
      },
      "fdv": 5531873832,
      "marketCap": 5529521168,
      "pairCreatedAt": 1753154627000,
      "info": {
        "imageUrl": "https://cdn.dexscreener.com/cms/images/e7ad3f643e8706e541538413f2afad46f18cafb430606caae3c70c0f7425c16e?width=800&height=800&quality=95&format=auto",
        "openGraph": "https://cdn.dexscreener.com/token-images/og/ethereum/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2?timestamp=1791138900000",
        "websites": [],
        "socials": []
      }
    },
    {
      "chainId": "ethereum",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/ethereum/0x90078845bceb849b171873cfbc92db8540e9c803ff57d9d21b1215ec158e79b3",
      "pairAddress": "0x90078845bceb849b171873cfbc92db8540e9c803ff57d9d21b1215ec158e79b3",
      "labels": [
        "v4"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
        "name": "Tether USD",
        "symbol": "USDT"
      },
      "priceNative": "2701.09290",
      "priceUsd": "2701.092",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 59,
          "sells": 67
        },
        "h6": {
          "buys": 480,
          "sells": 407
        },
        "h24": {
          "buys": 1651,
          "sells": 1597
        }
      },
      "volume": {
        "h24": 3457505.99,
        "h6": 1036341.9,
        "h1": 96868.64,
        "m5": 0
      },
      "priceChange": {
        "h1": -0.03,
        "h24": 0.62
      },
      "liquidity": {
        "usd": 2297667.56,
        "base": 242.7544,
        "quote": 1641965
      },
      "fdv": 5532593522,
      "marketCap": 5530240551,
      "pairCreatedAt": 1753154627000,
      "info": {
        "imageUrl": "https://cdn.dexscreener.com/cms/images/e7ad3f643e8706e541538413f2afad46f18cafb430606caae3c70c0f7425c16e?width=800&height=800&quality=95&format=auto",
        "openGraph": "https://cdn.dexscreener.com/token-images/og/ethereum/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2?timestamp=1791138900000",
        "websites": [],
        "socials": []
      }
    },
    {
      "chainId": "ethereum",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/ethereum/0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc",
      "pairAddress": "0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc",
      "labels": [
        "v2"
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
      "priceNative": "2703.1859",
      "priceUsd": "2703.18",
      "txns": {
        "m5": {
          "buys": 2,
          "sells": 1
        },
        "h1": {
          "buys": 19,
          "sells": 9
        },
        "h6": {
          "buys": 502,
          "sells": 461
        },
        "h24": {
          "buys": 1453,
          "sells": 1039
        }
      },
      "volume": {
        "h24": 336654.32,
        "h6": 123808.58,
        "h1": 4335.88,
        "m5": 1122.85
      },
      "priceChange": {
        "m5": -0.01,
        "h1": 0.02,
        "h6": -0.03,
        "h24": 0.73
      },
      "liquidity": {
        "usd": 21033976.12,
        "base": 3890.5899,
        "quote": 10516988
      },
      "fdv": 5532290692,
      "marketCap": 5534525928,
      "info": {
        "imageUrl": "https://cdn.dexscreener.com/cms/images/e7ad3f643e8706e541538413f2afad46f18cafb430606caae3c70c0f7425c16e?width=800&height=800&quality=95&format=auto",
        "openGraph": "https://cdn.dexscreener.com/token-images/og/ethereum/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2?timestamp=1791138900000",
        "websites": [],
        "socials": []
      }
    },
    {
      "chainId": "ethereum",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/ethereum/0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8",
      "pairAddress": "0x8ad599c3A0ff1De082011EFDDc58f1908eb6e6D8",
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
      "priceNative": "2704.1880",
      "priceUsd": "2704.18",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 1
        },
        "h1": {
          "buys": 10,
          "sells": 8
        },
        "h6": {
          "buys": 393,
          "sells": 350
        },
        "h24": {
          "buys": 1104,
          "sells": 1015
        }
      },
      "volume": {
        "h24": 1510186.13,
        "h6": 468839.76,
        "h1": 1553.54,
        "m5": 0.26
      },
      "priceChange": {
        "h6": 0.19,
        "h24": 0.84
      },
      "liquidity": {
        "usd": 47642488.45,
        "base": 7955.4765,
        "quote": 26129383
      },
      "fdv": 5534341539,
      "marketCap": 5536577604,
      "pairCreatedAt": 1620169800000,
      "info": {
        "imageUrl": "https://cdn.dexscreener.com/cms/images/e7ad3f643e8706e541538413f2afad46f18cafb430606caae3c70c0f7425c16e?width=800&height=800&quality=95&format=auto",
        "openGraph": "https://cdn.dexscreener.com/token-images/og/ethereum/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2?timestamp=1791138900000",
        "websites": [],
        "socials": []
      }
    },
    {
      "chainId": "ethereum",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/ethereum/0x11b815efb8f581194ae79006d24e0d814b7697f6",
      "pairAddress": "0x11b815efB8f581194ae79006d24E0d814B7697F6",
      "labels": [
        "v3"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
        "name": "Tether USD",
        "symbol": "USDT"
      },
      "priceNative": "2701.6992",
      "priceUsd": "2701.69",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 14,
          "sells": 27
        },
        "h6": {
          "buys": 254,
          "sells": 176
        },
        "h24": {
          "buys": 888,
          "sells": 584
        }
      },
      "volume": {
        "h24": 3937322.99,
        "h6": 1107919.31,
        "h1": 56936.06,
        "m5": 0
      },
      "priceChange": {
        "h1": -0.04,
        "h6": -0.01,
        "h24": 0.59
      },
      "liquidity": {
        "usd": 10385744.83,
        "base": 1590.6535,
        "quote": 6088277
      },
      "fdv": 5529248066,
      "marketCap": 5531482072,
      "pairCreatedAt": 1620251172000,
      "info": {
        "imageUrl": "https://cdn.dexscreener.com/cms/images/e7ad3f643e8706e541538413f2afad46f18cafb430606caae3c70c0f7425c16e?width=800&height=800&quality=95&format=auto",
        "openGraph": "https://cdn.dexscreener.com/token-images/og/ethereum/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2?timestamp=1791138900000",
        "websites": [],
        "socials": []
      }
    },
    {
      "chainId": "pulsechain",
      "dexId": "pulsex",
      "url": "https://dexscreener.com/pulsechain/0x2a0bf9c4c85ef6462777425945714e1234cd232b",
      "pairAddress": "0x2a0BF9c4c85ef6462777425945714e1234Cd232B",
      "labels": [
        "v2"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0x02DcdD04e3F455D838cd1249292C58f3B79e3C3C",
        "name": "Wrapped Ether from Ethereum",
        "symbol": "WETH"
      },
      "priceNative": "0.000000003399",
      "priceUsd": "0.000009183",
      "txns": {
        "m5": {
          "buys": 1,
          "sells": 0
        },
        "h1": {
          "buys": 3,
          "sells": 1
        },
        "h6": {
          "buys": 12,
          "sells": 2
        },
        "h24": {
          "buys": 39,
          "sells": 12
        }
      },
      "volume": {
        "h24": 180.68,
        "h6": 54.47,
        "h1": 15.26,
        "m5": 5.83
      },
      "priceChange": {
        "m5": 0.43,
        "h1": 2.06,
        "h6": 2.16,
        "h24": 7.08
      },
      "liquidity": {
        "usd": 8025.33,
        "base": 436962843,
        "quote": 1.4853
      },
      "fdv": 310123,
      "marketCap": 310123,
      "pairCreatedAt": 1685652315000
    },
    {
      "chainId": "pulsechain",
      "dexId": "pulsex",
      "url": "https://dexscreener.com/pulsechain/0x7fcba88269633042e603ae9a139c06561cfe7672",
      "pairAddress": "0x7FCbA88269633042e603Ae9a139c06561Cfe7672",
      "labels": [
        "v1"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0x037645963Aece8C5Beb947dA5621362c9f7dB5a6",
        "name": "Mintables",
        "symbol": "🌨️"
      },
      "priceNative": "0.01231",
      "priceUsd": "0.000009003",
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
          "sells": 3
        }
      },
      "volume": {
        "h24": 10.92,
        "h6": 0,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h24": -0.37
      },
      "liquidity": {
        "usd": 8883.99,
        "base": 493365295,
        "quote": 6075949
      },
      "fdv": 304057,
      "marketCap": 304057,
      "pairCreatedAt": 1778023725000
    },
    {
      "chainId": "pulsechain",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/pulsechain/0xcbcdf9626bc03e24f779434178a73a0b4bad62ed",
      "pairAddress": "0xCBCdF9626bC03E24f779434178A73a0B4bad62eD",
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "priceNative": "0.00000004470",
      "priceUsd": "0.000008799",
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
          "sells": 1
        }
      },
      "volume": {
        "h24": 0.02,
        "h6": 0,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {},
      "liquidity": {
        "usd": 8886.96,
        "base": 494876,
        "quote": 45.1321
      },
      "fdv": 297167,
      "marketCap": 297167,
      "pairCreatedAt": 1683945065000
    },
    {
      "chainId": "pulsechain",
      "dexId": "9mm",
      "url": "https://dexscreener.com/pulsechain/0x6b7a5b3754c15b8948f8c100b626b844ab6b44b5",
      "pairAddress": "0x6B7a5b3754c15b8948f8c100b626b844aB6b44b5",
      "labels": [
        "V3"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0xA1077a294dDE1B09bB078844df40758a5D0f9a27",
        "name": "Wrapped Pulse",
        "symbol": "WPLS"
      },
      "priceNative": "0.9998",
      "priceUsd": "0.000009138",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 1
        },
        "h1": {
          "buys": 2,
          "sells": 35
        },
        "h6": {
          "buys": 18,
          "sells": 58
        },
        "h24": {
          "buys": 235,
          "sells": 116
        }
      },
      "volume": {
        "h24": 2282.12,
        "h6": 441.61,
        "h1": 263.76,
        "m5": 5.79
      },
      "priceChange": {
        "m5": -0.39,
        "h1": 0.91,
        "h6": 1.43,
        "h24": 6.63
      },
      "liquidity": {
        "usd": 1396.15,
        "base": 98954193,
        "quote": 53816926
      },
      "fdv": 307762,
      "marketCap": 307762,
      "pairCreatedAt": 1704961315000
    },
    {
      "chainId": "pulsechain",
      "dexId": "sushiswap",
      "url": "https://dexscreener.com/pulsechain/0x397ff1542f962076d0bfe58ea045ffa2d347aca0",
      "pairAddress": "0x397FF1542f962076d0BFE58eA045FfA2d347ACa0",
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
      "priceNative": "0.01232",
      "priceUsd": "0.000009134",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 4,
          "sells": 2
        },
        "h6": {
          "buys": 13,
          "sells": 4
        },
        "h24": {
          "buys": 15,
          "sells": 25
        }
      },
      "volume": {
        "h24": 87.04,
        "h6": 39.88,
        "h1": 13.9,
        "m5": 0
      },
      "priceChange": {
        "h1": 7.83,
        "h6": 7.98,
        "h24": 4.47
      },
      "liquidity": {
        "usd": 3522.62,
        "base": 192818148,
        "quote": 2376298
      },
      "fdv": 308485,
      "marketCap": 308485,
      "pairCreatedAt": 1683949415000
    },
    {
      "chainId": "pulsechain",
      "dexId": "9mm",
      "url": "https://dexscreener.com/pulsechain/0x402eda7f4bb1d9c27f46a35b93c485458331eca2",
      "pairAddress": "0x402EDA7f4bB1d9c27F46A35b93c485458331Eca2",
      "labels": [
        "V3"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0xA1077a294dDE1B09bB078844df40758a5D0f9a27",
        "name": "Wrapped Pulse",
        "symbol": "WPLS"
      },
      "priceNative": "1.0002810",
      "priceUsd": "0.000009205",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 0,
          "sells": 6
        },
        "h6": {
          "buys": 5,
          "sells": 17
        },
        "h24": {
          "buys": 31,
          "sells": 45
        }
      },
      "volume": {
        "h24": 434.28,
        "h6": 143.12,
        "h1": 80.77,
        "m5": 0
      },
      "priceChange": {
        "h1": 1.63,
        "h6": 2.12,
        "h24": 7.37
      },
      "liquidity": {
        "usd": 2843.77,
        "base": 87120239,
        "quote": 221863787
      },
      "fdv": 310019,
      "marketCap": 310019,
      "pairCreatedAt": 1701500455000
    },
    {
      "chainId": "pulsechain",
      "dexId": "pulsex",
      "url": "https://dexscreener.com/pulsechain/0x6ee4e499c1570ea28a7a72500254a322d17f6c75",
      "pairAddress": "0x6Ee4e499c1570ea28a7A72500254a322d17F6C75",
      "labels": [
        "v2"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0xD49688BDd162feaC18026CEA6c7546b4eaD67089",
        "name": "mEthLab",
        "symbol": "mETH"
      },
      "priceNative": "0.001672",
      "priceUsd": "0.000008962",
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
          "buys": 1,
          "sells": 5
        }
      },
      "volume": {
        "h24": 17.41,
        "h6": 0,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h24": -0.35
      },
      "liquidity": {
        "usd": 3732.95,
        "base": 208259877,
        "quote": 348356
      },
      "fdv": 302665,
      "marketCap": 302665,
      "pairCreatedAt": 1704563985000
    },
    {
      "chainId": "pulsechain",
      "dexId": "sushiswap",
      "url": "https://dexscreener.com/pulsechain/0x06da0fd433c1a5d7a4faa01111c044910a184553",
      "pairAddress": "0x06da0fd433C1A5d7a4faa01111c044910A184553",
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
        "name": "Tether USD",
        "symbol": "USDT"
      },
      "priceNative": "0.01270",
      "priceUsd": "0.000009112",
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
          "buys": 5,
          "sells": 2
        },
        "h24": {
          "buys": 9,
          "sells": 19
        }
      },
      "volume": {
        "h24": 37.5,
        "h6": 14.39,
        "h1": 2.28,
        "m5": 0
      },
      "priceChange": {
        "h1": 1.54,
        "h6": 4.88,
        "h24": 4.61
      },
      "liquidity": {
        "usd": 1476.44,
        "base": 81010919,
        "quote": 1029614
      },
      "fdv": 307744,
      "marketCap": 307744,
      "pairCreatedAt": 1683945595000
    },
    {
      "chainId": "pulsechain",
      "dexId": "sushiswap",
      "url": "https://dexscreener.com/pulsechain/0xceff51756c56ceffca006cd410b03ffc46dd3a58",
      "pairAddress": "0xCEfF51756c56CeFFCA006cD410B03FFC46dd3a58",
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "priceNative": "0.00000004603",
      "priceUsd": "0.000009063",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 2,
          "sells": 0
        },
        "h6": {
          "buys": 4,
          "sells": 2
        },
        "h24": {
          "buys": 18,
          "sells": 15
        }
      },
      "volume": {
        "h24": 27.57,
        "h6": 5.29,
        "h1": 2,
        "m5": 0
      },
      "priceChange": {
        "h1": 1.28,
        "h6": 1.26,
        "h24": 6.31
      },
      "liquidity": {
        "usd": 863.77,
        "base": 47650109,
        "quote": 2.1935
      },
      "fdv": 306090,
      "marketCap": 306090,
      "pairCreatedAt": 1683945245000
    },
    {
      "chainId": "pulsechain",
      "dexId": "sushiswap",
      "url": "https://dexscreener.com/pulsechain/0xc3d03e4f041fd4cd388c549ee2a29a9e5075882f",
      "pairAddress": "0xC3D03e4F041Fd4cD388c549Ee2A29a9E5075882f",
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
        "name": "Dai Stablecoin",
        "symbol": "DAI"
      },
      "priceNative": "0.005445",
      "priceUsd": "0.000009141",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 4,
          "sells": 0
        },
        "h6": {
          "buys": 6,
          "sells": 1
        },
        "h24": {
          "buys": 13,
          "sells": 20
        }
      },
      "volume": {
        "h24": 27.79,
        "h6": 6.99,
        "h1": 4.73,
        "m5": 0
      },
      "priceChange": {
        "h1": 0.96,
        "h6": 1.75,
        "h24": 6.69
      },
      "liquidity": {
        "usd": 997.78,
        "base": 54572992,
        "quote": 297151
      },
      "fdv": 308726,
      "marketCap": 308726,
      "pairCreatedAt": 1683945855000
    },
    {
      "chainId": "pulsechain",
      "dexId": "pulsex",
      "url": "https://dexscreener.com/pulsechain/0xf581344e5615119069ee4fe645513ac7837179a5",
      "pairAddress": "0xf581344e5615119069eE4fE645513aC7837179A5",
      "labels": [
        "v2"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0x5203fD77B8E04681dEDB38CBEb4Dc160c21f8A18",
        "name": "Kudos",
        "symbol": "KUDOS"
      },
      "priceNative": "0.002823",
      "priceUsd": "0.000008680",
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
          "sells": 3
        }
      },
      "volume": {
        "h24": 1.25,
        "h6": 0,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h24": -0.73
      },
      "liquidity": {
        "usd": 1166.5,
        "base": 67188170,
        "quote": 189726
      },
      "fdv": 293164,
      "marketCap": 293164,
      "pairCreatedAt": 1737482575000
    },
    {
      "chainId": "pulsechain",
      "dexId": "pulsex",
      "url": "https://dexscreener.com/pulsechain/0x80e4503fe5f511a65715deb9f61265dabc2d2797",
      "pairAddress": "0x80e4503fe5f511A65715Deb9f61265DABc2d2797",
      "labels": [
        "v2"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0xe3B3f5F95d263edc6A5e3D4b7314728A390a4342",
        "name": "PLSPUPPY",
        "symbol": "PLSPUP"
      },
      "priceNative": "0.0000002115",
      "priceUsd": "0.000008658",
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
          "sells": 4
        }
      },
      "volume": {
        "h24": 0.61,
        "h6": 0,
        "h1": 0,
        "m5": 0
      },
      "priceChange": {
        "h24": -3.73
      },
      "liquidity": {
        "usd": 936.34,
        "base": 54072271,
        "quote": 11.4408
      },
      "fdv": 292400,
      "marketCap": 292400,
      "pairCreatedAt": 1704569385000
    },
    {
      "chainId": "pulsechain",
      "dexId": "pulsex",
      "url": "https://dexscreener.com/pulsechain/0x7835a696e2d95389b059bc91e68dfd306733651e",
      "pairAddress": "0x7835A696e2d95389b059Bc91e68DFd306733651E",
      "labels": [
        "v2"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
        "name": "Wrapped BTC",
        "symbol": "WBTC"
      },
      "priceNative": "0.00000004616",
      "priceUsd": "0.000009090",
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
          "buys": 2,
          "sells": 1
        },
        "h24": {
          "buys": 16,
          "sells": 13
        }
      },
      "volume": {
        "h24": 12.37,
        "h6": 1.51,
        "h1": 0.74,
        "m5": 0
      },
      "priceChange": {
        "h1": 0.76,
        "h6": 1.59,
        "h24": 6.81
      },
      "liquidity": {
        "usd": 391.8,
        "base": 21550989,
        "quote": 0.9949
      },
      "fdv": 306984,
      "marketCap": 306984,
      "pairCreatedAt": 1686076835000
    },
    {
      "chainId": "pulsechain",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/pulsechain/0xd116a786f81409c11f145b173f8c80f0cc87486a",
      "pairAddress": "0xD116a786F81409C11F145b173f8c80F0CC87486a",
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0x5A9780Bfe63f3ec57f01b087cD65BD656C9034A8",
        "name": "Communis",
        "symbol": "COM"
      },
      "priceNative": "2451679.1283",
      "priceUsd": "0.000009248",
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
          "buys": 0,
          "sells": 5
        },
        "h24": {
          "buys": 0,
          "sells": 8
        }
      },
      "volume": {
        "h24": 12.39,
        "h6": 9.4,
        "h1": 2.32,
        "m5": 0
      },
      "priceChange": {
        "h1": 0.99,
        "h6": 6.17,
        "h24": 6.34
      },
      "liquidity": {
        "usd": 771.53,
        "base": 37407920,
        "quote": 112824856329348
      },
      "fdv": 312316,
      "marketCap": 312316,
      "pairCreatedAt": 1684008905000
    },
    {
      "chainId": "pulsechain",
      "dexId": "pulsex",
      "url": "https://dexscreener.com/pulsechain/0x3ac19ae0352aa0b12557349571ae7cd17bfa2218",
      "pairAddress": "0x3AC19aE0352Aa0b12557349571ae7cd17Bfa2218",
      "labels": [
        "v2"
      ],
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
        "name": "Dai Stablecoin",
        "symbol": "DAI"
      },
      "priceNative": "0.005452",
      "priceUsd": "0.000009153",
      "txns": {
        "m5": {
          "buys": 0,
          "sells": 0
        },
        "h1": {
          "buys": 3,
          "sells": 0
        },
        "h6": {
          "buys": 3,
          "sells": 0
        },
        "h24": {
          "buys": 6,
          "sells": 14
        }
      },
      "volume": {
        "h24": 8.46,
        "h6": 1.68,
        "h1": 1.68,
        "m5": 0
      },
      "priceChange": {
        "h1": 1.25,
        "h6": 1.25,
        "h24": 6.75
      },
      "liquidity": {
        "usd": 273.14,
        "base": 14919769,
        "quote": 81346
      },
      "fdv": 309137,
      "marketCap": 309137,
      "pairCreatedAt": 1686508105000
    },
    {
      "chainId": "pulsechain",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/pulsechain/0x65b554994271a445a339d17c993cdebb4dd49ee8",
      "pairAddress": "0x65B554994271a445a339D17c993CdEBB4DD49Ee8",
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0x4243568Fa2bbad327ee36e06c16824cAd8B37819",
        "name": "TSFi",
        "symbol": "TSFi"
      },
      "priceNative": "0.00001414",
      "priceUsd": "0.000009178",
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
          "buys": 2,
          "sells": 0
        },
        "h24": {
          "buys": 2,
          "sells": 8
        }
      },
      "volume": {
        "h24": 6.47,
        "h6": 2.08,
        "h1": 1.1,
        "m5": 0
      },
      "priceChange": {
        "h1": 0.72,
        "h6": 5.16,
        "h24": 6.09
      },
      "liquidity": {
        "usd": 419.06,
        "base": 22922779,
        "quote": 321.4451
      },
      "fdv": 309985,
      "marketCap": 309985,
      "pairCreatedAt": 1789891075000
    },
    {
      "chainId": "pulsechain",
      "dexId": "uniswap",
      "url": "https://dexscreener.com/pulsechain/0xfc6abba29372e2ca009c6c5e0f03e1fca660355d",
      "pairAddress": "0xfC6aBBa29372E2Ca009C6C5e0F03E1fca660355d",
      "baseToken": {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "name": "Wrapped Ether",
        "symbol": "WETH"
      },
      "quoteToken": {
        "address": "0x4243568Fa2bbad327ee36e06c16824cAd8B37819",
        "name": "TSFi",
        "symbol": "TSFi"
      },
      "priceNative": "0.00001402",
      "priceUsd": "0.000009106",
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
          "buys": 1,
          "sells": 1
        },
        "h24": {
          "buys": 1,
          "sells": 6
        }
      },
      "volume": {
        "h24": 5.07,
        "h6": 2.12,
        "h1": 1.12,
        "m5": 0
      },
      "priceChange": {
        "h1": 4.19,
        "h6": 3.18,
        "h24": 4.44
      },
      "liquidity": {
        "usd": 421.07,
        "base": 23215350,
        "quote": 323.005414
      },
      "fdv": 307529,
      "marketCap": 307529,
      "pairCreatedAt": 1789891125000
    }
  ]
}
```

## Why this matches (or not)

_[0.85|heuristic] DEX pair liquidity present_
