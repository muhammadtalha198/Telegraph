---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-gecko-search-eth
status: approved
captured_at: 2026-10-04T18:39:58Z
request_url: https://api.geckoterminal.com/api/v2/search/pools?query=WETH%20USDC&network=eth
content_type: application/json
inputs: |
  WETH USDC eth
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must convey bid/ask order-book depth or pool liquidity for the pair asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [0.80|heuristic] DEX pool list with reserve/liquidity fields"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "data": [
    {
      "id": "eth_0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "2700.84",
        "base_token_price_native_currency": "1.0",
        "quote_token_price_usd": "1.00030147483615",
        "quote_token_price_native_currency": "0.00037036729769353",
        "base_token_price_quote_token": "2700.0224",
        "quote_token_price_base_token": "0.0003703672977",
        "address": "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        "name": "WETH / USDC 0.05%",
        "pool_created_at": "2021-12-29T12:35:14Z",
        "fdv_usd": "5531082257.47789",
        "market_cap_usd": "5533933649.3841",
        "price_change_percentage": {
          "m5": "0.001",
          "m15": "0.011",
          "m30": "0.012",
          "h1": "-0.03",
          "h6": "-0.021",
          "h24": "0.577"
        },
        "transactions": {
          "m5": {
            "buys": 7,
            "sells": 5,
            "buyers": 7,
            "sellers": 4
          },
          "m15": {
            "buys": 37,
            "sells": 59,
            "buyers": 37,
            "sellers": 50
          },
          "m30": {
            "buys": 57,
            "sells": 167,
            "buyers": 56,
            "sellers": 152
          },
          "h1": {
            "buys": 127,
            "sells": 257,
            "buyers": 103,
            "sellers": 206
          },
          "h6": {
            "buys": 2178,
            "sells": 2518,
            "buyers": 944,
            "sellers": 1170
          },
          "h24": {
            "buys": 6106,
            "sells": 6828,
            "buyers": 1837,
            "sellers": 2320
          }
        },
        "volume_usd": {
          "m5": "1245.2100527786",
          "m15": "21449.0968102062",
          "m30": "470143.591729975",
          "h1": "1085051.48141188",
          "h6": "4515681.81433813",
          "h24": "17180251.5051875"
        },
        "reserve_in_usd": "98125716.2472"
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
    },
    {
      "id": "eth_0xe0554a476a092703abdb3ef35c80e0d76d32939f",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.999875115600493",
        "base_token_price_native_currency": "0.000370366802489651",
        "quote_token_price_usd": "2700.85",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0003703668025",
        "quote_token_price_base_token": "2700.026010101",
        "address": "0xe0554a476a092703abdb3ef35c80e0d76d32939f",
        "name": "USDC / WETH 0.01%",
        "pool_created_at": "2021-12-30T20:32:10Z",
        "fdv_usd": "48991568848.9462",
        "market_cap_usd": "74111714307.48",
        "price_change_percentage": {
          "m5": "-0.017",
          "m15": "0.01",
          "m30": "0.014",
          "h1": "0.014",
          "h6": "0.002",
          "h24": "-0.013"
        },
        "transactions": {
          "m5": {
            "buys": 35,
            "sells": 51,
            "buyers": 34,
            "sellers": 30
          },
          "m15": {
            "buys": 122,
            "sells": 156,
            "buyers": 101,
            "sellers": 92
          },
          "m30": {
            "buys": 227,
            "sells": 297,
            "buyers": 170,
            "sellers": 152
          },
          "h1": {
            "buys": 454,
            "sells": 631,
            "buyers": 300,
            "sellers": 264
          },
          "h6": {
            "buys": 2965,
            "sells": 3150,
            "buyers": 1395,
            "sellers": 1148
          },
          "h24": {
            "buys": 11896,
            "sells": 12267,
            "buyers": 4137,
            "sellers": 2937
          }
        },
        "volume_usd": {
          "m5": "106188.763374101",
          "m15": "347032.579923584",
          "m30": "798877.981969433",
          "h1": "1632044.75788458",
          "h6": "18666377.3698825",
          "h24": "44390942.0858611"
        },
        "reserve_in_usd": "6997480.2071"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
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
    },
    {
      "id": "eth_0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "1.00177268827437",
        "base_token_price_native_currency": "0.000369998029087404",
        "quote_token_price_usd": "2700.85",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0003699980291",
        "quote_token_price_base_token": "2702.717099511",
        "address": "0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8",
        "name": "USDC / WETH 0.3%",
        "pool_created_at": "2021-12-29T13:21:42Z",
        "fdv_usd": "49077316047.6696",
        "market_cap_usd": "74241427889.7098",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0.589",
          "m30": "0.61",
          "h1": "0.562",
          "h6": "0.404",
          "h24": "0.373"
        },
        "transactions": {
          "m5": {
            "buys": 1,
            "sells": 0,
            "buyers": 1,
            "sellers": 0
          },
          "m15": {
            "buys": 1,
            "sells": 1,
            "buyers": 1,
            "sellers": 1
          },
          "m30": {
            "buys": 1,
            "sells": 3,
            "buyers": 1,
            "sellers": 2
          },
          "h1": {
            "buys": 8,
            "sells": 10,
            "buyers": 8,
            "sellers": 7
          },
          "h6": {
            "buys": 350,
            "sells": 393,
            "buyers": 125,
            "sellers": 126
          },
          "h24": {
            "buys": 1015,
            "sells": 1103,
            "buyers": 229,
            "sellers": 252
          }
        },
        "volume_usd": {
          "m5": "0.26738415",
          "m15": "254.2579955355",
          "m30": "348.736083825",
          "h1": "1552.5123310326",
          "h6": "467912.001549739",
          "h24": "1508667.36987838"
        },
        "reserve_in_usd": "47597881.7025"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
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
    },
    {
      "id": "eth_0xe500210c7ea6bfd9f69dce044b09ef384ec2b34832f132baec3b418208e3a657",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "1.00001821055452",
        "base_token_price_native_currency": "0.000374227038863523",
        "quote_token_price_usd": "2700.79",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0003742270389",
        "quote_token_price_base_token": "2672.174632375",
        "address": "0xe500210c7ea6bfd9f69dce044b09ef384ec2b34832f132baec3b418208e3a657",
        "name": "USDC / WETH",
        "pool_created_at": "2025-07-22T03:23:47Z",
        "fdv_usd": "48991363358.4147",
        "market_cap_usd": "74111403452.8591",
        "price_change_percentage": {
          "m5": "0",
          "m15": "-0.013",
          "m30": "-0.004",
          "h1": "-0.004",
          "h6": "-0.023",
          "h24": "-0.05"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 1,
            "buyers": 0,
            "sellers": 1
          },
          "m15": {
            "buys": 4,
            "sells": 19,
            "buyers": 3,
            "sellers": 3
          },
          "m30": {
            "buys": 16,
            "sells": 35,
            "buyers": 3,
            "sellers": 3
          },
          "h1": {
            "buys": 61,
            "sells": 67,
            "buyers": 3,
            "sellers": 4
          },
          "h6": {
            "buys": 454,
            "sells": 526,
            "buyers": 7,
            "sellers": 10
          },
          "h24": {
            "buys": 1672,
            "sells": 1739,
            "buyers": 10,
            "sellers": 66
          }
        },
        "volume_usd": {
          "m5": "8.8444030586",
          "m15": "21109.5497314554",
          "m30": "40001.4980136631",
          "h1": "123693.643115178",
          "h6": "1240541.6616214",
          "h24": "4040787.23956787"
        },
        "reserve_in_usd": "3345511.5156"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "uniswap-v4-ethereum",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "2700.8",
        "base_token_price_native_currency": "1.0",
        "quote_token_price_usd": "0.996136950795404",
        "quote_token_price_native_currency": "0.000369933851919617",
        "base_token_price_quote_token": "2703.185974495",
        "quote_token_price_base_token": "0.0003699338519",
        "address": "0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc",
        "name": "WETH / USDC",
        "pool_created_at": "2021-10-11T01:35:30Z",
        "fdv_usd": "5531000341.00365",
        "market_cap_usd": "5533851690.68015",
        "price_change_percentage": {
          "m5": "-0.002",
          "m15": "0.018",
          "m30": "0.006",
          "h1": "-0.034",
          "h6": "-0.023",
          "h24": "0.575"
        },
        "transactions": {
          "m5": {
            "buys": 2,
            "sells": 1,
            "buyers": 2,
            "sellers": 1
          },
          "m15": {
            "buys": 11,
            "sells": 6,
            "buyers": 11,
            "sellers": 6
          },
          "m30": {
            "buys": 14,
            "sells": 8,
            "buyers": 12,
            "sellers": 8
          },
          "h1": {
            "buys": 19,
            "sells": 9,
            "buyers": 16,
            "sellers": 9
          },
          "h6": {
            "buys": 502,
            "sells": 461,
            "buyers": 280,
            "sellers": 271
          },
          "h24": {
            "buys": 1452,
            "sells": 1038,
            "buyers": 605,
            "sellers": 506
          }
        },
        "volume_usd": {
          "m5": "1124.1230489106",
          "m15": "3886.7955003311",
          "m30": "4211.4286768155",
          "h1": "4328.9269693882",
          "h6": "123687.108911829",
          "h24": "336371.393850323"
        },
        "reserve_in_usd": "21015767.1795"
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
            "id": "uniswap_v2",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0x1445f32d1a74872ba41f3d8cf4022e9996120b31",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.999788377556143",
        "base_token_price_native_currency": "0.000369998047261299",
        "quote_token_price_usd": "2700.85",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0003699980473",
        "quote_token_price_base_token": "2702.716966757",
        "address": "0x1445f32d1a74872ba41f3d8cf4022e9996120b31",
        "name": "USDC / WETH 0.01%",
        "pool_created_at": "2024-03-13T07:13:23Z",
        "fdv_usd": "48989961358.9077",
        "market_cap_usd": "74109282586.1596",
        "price_change_percentage": {
          "m5": "0.01",
          "m15": "-0.001",
          "m30": "-0.009",
          "h1": "0.001",
          "h6": "0.008",
          "h24": "-0.001"
        },
        "transactions": {
          "m5": {
            "buys": 1,
            "sells": 5,
            "buyers": 1,
            "sellers": 4
          },
          "m15": {
            "buys": 7,
            "sells": 16,
            "buyers": 7,
            "sellers": 12
          },
          "m30": {
            "buys": 14,
            "sells": 24,
            "buyers": 13,
            "sellers": 14
          },
          "h1": {
            "buys": 45,
            "sells": 57,
            "buyers": 39,
            "sellers": 31
          },
          "h6": {
            "buys": 437,
            "sells": 410,
            "buyers": 258,
            "sellers": 178
          },
          "h24": {
            "buys": 2077,
            "sells": 2223,
            "buyers": 801,
            "sellers": 534
          }
        },
        "volume_usd": {
          "m5": "328.767849547",
          "m15": "1261.0487644226",
          "m30": "2161.3170353425",
          "h1": "8714.1911395428",
          "h6": "375571.311838172",
          "h24": "1646254.93465881"
        },
        "reserve_in_usd": "613025.8544"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "pancakeswap-v3-ethereum",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0x7f86bf177dd4f3494b841a37e810a34dd56c829b",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "1.00117407407407",
        "base_token_price_native_currency": "0.00037037037037037",
        "quote_token_price_usd": "85458.3720054111",
        "quote_token_price_native_currency": "31.6141315586556",
        "base_token_price_quote_token": "0.00001171534223",
        "quote_token_price_base_token": "85358.1552083702",
        "address": "0x7f86bf177dd4f3494b841a37e810a34dd56c829b",
        "name": "USDC / WBTC / WETH",
        "pool_created_at": "2023-09-19T13:18:26Z",
        "fdv_usd": "49047989655.9371",
        "market_cap_usd": "74197064559.1039",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "0",
          "h1": "0",
          "h6": "0.21",
          "h24": "0.21"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 0,
            "buyers": null,
            "sellers": null
          },
          "m15": {
            "buys": 0,
            "sells": 0,
            "buyers": null,
            "sellers": null
          },
          "m30": {
            "buys": 0,
            "sells": 0,
            "buyers": null,
            "sellers": null
          },
          "h1": {
            "buys": 1,
            "sells": 1,
            "buyers": null,
            "sellers": null
          },
          "h6": {
            "buys": 8,
            "sells": 3,
            "buyers": null,
            "sellers": null
          },
          "h24": {
            "buys": 13,
            "sells": 27,
            "buyers": null,
            "sellers": null
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "0.0",
          "m30": "0.0",
          "h1": "13.5305637350672",
          "h6": "3807.6691765096",
          "h24": "18108.731765486"
        },
        "reserve_in_usd": "6008893.8208"
      },
      "relationships": {
        "quote_tokens": {
          "data": [
            {
              "id": "eth_0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
              "type": "token"
            },
            {
              "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
              "type": "token"
            }
          ]
        },
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "curve",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0x763d3b7296e7c9718ad5b058ac2692a19e5b3638",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.998184675733164",
        "base_token_price_native_currency": "0.000369865555941662",
        "quote_token_price_usd": "2701.31",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0003698655559",
        "quote_token_price_base_token": "2703.68512",
        "address": "0x763d3b7296e7c9718ad5b058ac2692a19e5b3638",
        "name": "USDC / WETH 0.3%",
        "pool_created_at": "2023-10-30T08:36:59Z",
        "fdv_usd": "48913957293.7127",
        "market_cap_usd": "73975520082.658",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "0",
          "h1": "0",
          "h6": "0",
          "h24": "-0.067"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m15": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m30": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h1": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h6": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h24": {
            "buys": 0,
            "sells": 17,
            "buyers": 0,
            "sellers": 10
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "0.0",
          "m30": "0.0",
          "h1": "0.0",
          "h6": "0.0",
          "h24": "14855.2380067997"
        },
        "reserve_in_usd": "2369582.0486"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "sushiswap-v3-ethereum",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0xe2cd94c812aed174b2e09750ff146f45d845d668",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "1.00044554086741",
        "base_token_price_native_currency": "0.000370109495058476",
        "quote_token_price_usd": "2701.0",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0003701094951",
        "quote_token_price_base_token": "2701.903121513",
        "address": "0xe2cd94c812aed174b2e09750ff146f45d845d668",
        "name": "USDC / WETH",
        "pool_created_at": "2026-02-25T03:01:30Z",
        "fdv_usd": "49012298471.1751",
        "market_cap_usd": "74143072924.4099",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "0",
          "h1": "0.044",
          "h6": "0.021",
          "h24": "0.022"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m15": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m30": {
            "buys": 1,
            "sells": 0,
            "buyers": 1,
            "sellers": 0
          },
          "h1": {
            "buys": 9,
            "sells": 2,
            "buyers": 9,
            "sellers": 2
          },
          "h6": {
            "buys": 42,
            "sells": 41,
            "buyers": 35,
            "sellers": 36
          },
          "h24": {
            "buys": 138,
            "sells": 134,
            "buyers": 108,
            "sellers": 86
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "0.0",
          "m30": "30.11615",
          "h1": "1468.7117914224",
          "h6": "44522.972535655",
          "h24": "123106.410627503"
        },
        "reserve_in_usd": "34829.3635"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "supernova-cl",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0x5a5c7cab5f55c7ea020e97d4fa6dd5d99270e56ce76afa61d8cbddec0af92060",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.999311428402385",
        "base_token_price_native_currency": "0.000374227038863523",
        "quote_token_price_usd": "2700.85",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0003742270389",
        "quote_token_price_base_token": "2672.174632375",
        "address": "0x5a5c7cab5f55c7ea020e97d4fa6dd5d99270e56ce76afa61d8cbddec0af92060",
        "name": "USDC / WETH 0.02%",
        "pool_created_at": "2026-01-26T13:04:47Z",
        "fdv_usd": "48956737765.3921",
        "market_cap_usd": "74059023785.9468",
        "price_change_percentage": {
          "m5": "-0.043",
          "m15": "-0.052",
          "m30": "-0.096",
          "h1": "0.018",
          "h6": "-0.093",
          "h24": "-0.103"
        },
        "transactions": {
          "m5": {
            "buys": 1,
            "sells": 2,
            "buyers": 1,
            "sellers": 2
          },
          "m15": {
            "buys": 7,
            "sells": 5,
            "buyers": 7,
            "sellers": 4
          },
          "m30": {
            "buys": 14,
            "sells": 11,
            "buyers": 14,
            "sellers": 7
          },
          "h1": {
            "buys": 39,
            "sells": 33,
            "buyers": 37,
            "sellers": 26
          },
          "h6": {
            "buys": 141,
            "sells": 137,
            "buyers": 120,
            "sellers": 99
          },
          "h24": {
            "buys": 452,
            "sells": 410,
            "buyers": 332,
            "sellers": 261
          }
        },
        "volume_usd": {
          "m5": "168.4688232489",
          "m15": "377.7684260219",
          "m30": "2420.4151383826",
          "h1": "9831.4775419958",
          "h6": "50780.9655991852",
          "h24": "119140.814820136"
        },
        "reserve_in_usd": "20667.9845"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "uniswap-v4-ethereum",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0x55cd2060d9ad3c05fff7061604a332a29adcd0aa557efa63973f26d00553ec5f",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.998915238004562",
        "base_token_price_native_currency": "0.000413971705768676",
        "quote_token_price_usd": "2700.84",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0004139717058",
        "quote_token_price_base_token": "2415.624029529",
        "address": "0x55cd2060d9ad3c05fff7061604a332a29adcd0aa557efa63973f26d00553ec5f",
        "name": "USDC / WETH 0.01%",
        "pool_created_at": "2025-10-04T23:04:59Z",
        "fdv_usd": "48937328211.0062",
        "market_cap_usd": "74029662094.0622",
        "price_change_percentage": {
          "m5": "0",
          "m15": "-0.108",
          "m30": "-0.127",
          "h1": "-0.07",
          "h6": "-0.116",
          "h24": "-0.148"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 1,
            "buyers": 0,
            "sellers": 1
          },
          "m15": {
            "buys": 0,
            "sells": 3,
            "buyers": 0,
            "sellers": 3
          },
          "m30": {
            "buys": 1,
            "sells": 6,
            "buyers": 1,
            "sellers": 6
          },
          "h1": {
            "buys": 8,
            "sells": 11,
            "buyers": 8,
            "sellers": 11
          },
          "h6": {
            "buys": 45,
            "sells": 53,
            "buyers": 43,
            "sellers": 48
          },
          "h24": {
            "buys": 216,
            "sells": 191,
            "buyers": 183,
            "sellers": 158
          }
        },
        "volume_usd": {
          "m5": "48.9932732457",
          "m15": "51.9111175844",
          "m30": "63.7039100898",
          "h1": "323.1214631147",
          "h6": "1423.896751665",
          "h24": "28177.7828416047"
        },
        "reserve_in_usd": "27860.6182"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "uniswap-v4-ethereum",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0x3aa370aacf4cb08c7e1e7aa8e8ff9418d73c7e0f",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.996362903899366",
        "base_token_price_native_currency": "0.000370594757397135",
        "quote_token_price_usd": "2696.64",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0003705947574",
        "quote_token_price_base_token": "2698.365209005",
        "address": "0x3aa370aacf4cb08c7e1e7aa8e8ff9418d73c7e0f",
        "name": "USDC / WETH",
        "pool_created_at": "2022-07-13T01:42:50Z",
        "fdv_usd": "48824685167.8292",
        "market_cap_usd": "73840508476.4315",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "0",
          "h1": "0",
          "h6": "-0.174",
          "h24": "-0.28"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m15": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m30": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h1": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h6": {
            "buys": 0,
            "sells": 3,
            "buyers": 0,
            "sellers": 1
          },
          "h24": {
            "buys": 0,
            "sells": 21,
            "buyers": 0,
            "sellers": 13
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "0.0",
          "m30": "0.0",
          "h1": "0.0",
          "h6": "0.2536265469",
          "h24": "916.8803100475"
        },
        "reserve_in_usd": "586485.6547"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "defi_swap",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0x397ff1542f962076d0bfe58ea045ffa2d347aca0",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "1.00420192504753",
        "base_token_price_native_currency": "0.000370058247477238",
        "quote_token_price_usd": "2705.52",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0003700582475",
        "quote_token_price_base_token": "2702.27729504",
        "address": "0x397ff1542f962076d0bfe58ea045ffa2d347aca0",
        "name": "USDC / WETH",
        "pool_created_at": "2021-10-11T01:22:00Z",
        "fdv_usd": "49208820040.508",
        "market_cap_usd": "74421458752.396",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "0",
          "h1": "0",
          "h6": "0.298",
          "h24": "0.244"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m15": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m30": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h1": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h6": {
            "buys": 16,
            "sells": 1,
            "buyers": 14,
            "sellers": 1
          },
          "h24": {
            "buys": 36,
            "sells": 31,
            "buyers": 29,
            "sellers": 23
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "0.0",
          "m30": "0.0",
          "h1": "0.0",
          "h6": "271.8400719741",
          "h24": "1171.1170652076"
        },
        "reserve_in_usd": "288829.3073"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "sushiswap",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0x96646936b91d6b9d7d0c47c496afbf3d6ec7b6f8",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.995362398509567",
        "base_token_price_native_currency": "0.000371456396894742",
        "quote_token_price_usd": "2693.23",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0003714563969",
        "quote_token_price_base_token": "2692.106013949",
        "address": "0x96646936b91d6b9d7d0c47c496afbf3d6ec7b6f8",
        "name": "USDC / WETH 0.3%",
        "pool_created_at": "2023-01-09T03:54:40Z",
        "fdv_usd": "48775657488.2834",
        "market_cap_usd": "73766360967.346",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "0",
          "h1": "0",
          "h6": "0",
          "h24": "-0.275"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m15": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m30": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h1": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h6": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h24": {
            "buys": 18,
            "sells": 18,
            "buyers": 18,
            "sellers": 15
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "0.0",
          "m30": "0.0",
          "h1": "0.0",
          "h6": "0.0",
          "h24": "2059.8066701176"
        },
        "reserve_in_usd": "202662.8418"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "balancer_ethereum",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0x1ac1a8feaaea1900c4166deeed0c11cc10669d36",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.999717878920691",
        "base_token_price_native_currency": "0.000370371419963901",
        "quote_token_price_usd": "2700.41",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.00037037142",
        "quote_token_price_base_token": "2699.992348485",
        "address": "0x1ac1a8feaaea1900c4166deeed0c11cc10669d36",
        "name": "USDC / WETH 0.05%",
        "pool_created_at": "2023-04-02T10:30:10Z",
        "fdv_usd": "48976649966.9117",
        "market_cap_usd": "74089145854.3949",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "0",
          "h1": "-0.01",
          "h6": "0.032",
          "h24": "0.002"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m15": {
            "buys": 1,
            "sells": 0,
            "buyers": 1,
            "sellers": 0
          },
          "m30": {
            "buys": 1,
            "sells": 0,
            "buyers": 1,
            "sellers": 0
          },
          "h1": {
            "buys": 2,
            "sells": 0,
            "buyers": 2,
            "sellers": 0
          },
          "h6": {
            "buys": 12,
            "sells": 9,
            "buyers": 12,
            "sellers": 9
          },
          "h24": {
            "buys": 41,
            "sells": 33,
            "buyers": 41,
            "sellers": 27
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "7.5806067475",
          "m30": "7.5806067475",
          "h1": "10.8440773241",
          "h6": "336.9177821117",
          "h24": "1137.1279063875"
        },
        "reserve_in_usd": "288231.2272"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "pancakeswap-v3-ethereum",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0xaa8a8a383fffcc4f370e1840b38766211fddb9e3",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "2700.85",
        "base_token_price_native_currency": "1.0",
        "quote_token_price_usd": "0.999879244842618",
        "quote_token_price_native_currency": "0.000369998047261299",
        "base_token_price_quote_token": "2702.716966757",
        "quote_token_price_base_token": "0.0003699980473",
        "address": "0xaa8a8a383fffcc4f370e1840b38766211fddb9e3",
        "name": "WETH / USDC 0.05%",
        "pool_created_at": "2026-08-12T20:06:47Z",
        "fdv_usd": "5531102736.59645",
        "market_cap_usd": "5533954139.06009",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "0.007",
          "h1": "-0.115",
          "h6": "0.1",
          "h24": "0.639"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 1,
            "buyers": 0,
            "sellers": 1
          },
          "m15": {
            "buys": 0,
            "sells": 1,
            "buyers": 0,
            "sellers": 1
          },
          "m30": {
            "buys": 0,
            "sells": 3,
            "buyers": 0,
            "sellers": 3
          },
          "h1": {
            "buys": 1,
            "sells": 4,
            "buyers": 1,
            "sellers": 4
          },
          "h6": {
            "buys": 13,
            "sells": 19,
            "buyers": 10,
            "sellers": 18
          },
          "h24": {
            "buys": 48,
            "sells": 54,
            "buyers": 33,
            "sellers": 51
          }
        },
        "volume_usd": {
          "m5": "18.5380701621",
          "m15": "18.5380701621",
          "m30": "44.006334435",
          "h1": "102.899754478",
          "h6": "4685.8681551303",
          "h24": "9495.424191859"
        },
        "reserve_in_usd": "22506.7232"
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
            "id": "balancer-v3-ethereum",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0x2e8135be71230c6b1b4045696d41c09db0414226",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.998145426187964",
        "base_token_price_native_currency": "0.000370320404545667",
        "quote_token_price_usd": "2702.11",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0003703204045",
        "quote_token_price_base_token": "2700.364300009",
        "address": "0x2e8135be71230c6b1b4045696d41c09db0414226",
        "name": "USDC / WETH",
        "pool_created_at": "2022-10-20T03:01:23Z",
        "fdv_usd": "48899614768.1793",
        "market_cap_usd": "73972611300.0989",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "0",
          "h1": "0",
          "h6": "-0.356",
          "h24": "-0.484"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m15": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m30": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h1": {
            "buys": 0,
            "sells": 1,
            "buyers": 0,
            "sellers": 1
          },
          "h6": {
            "buys": 4,
            "sells": 7,
            "buyers": 4,
            "sellers": 7
          },
          "h24": {
            "buys": 19,
            "sells": 45,
            "buyers": 17,
            "sellers": 27
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "0.0",
          "m30": "0.0",
          "h1": "0.08808134313",
          "h6": "66.8196672873",
          "h24": "577.957225097"
        },
        "reserve_in_usd": "306939.6065"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "pancakeswap_ethereum",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0x84f2195dc84d540a3ab92e659603d770014f0440",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "2700.55",
        "base_token_price_native_currency": "1.0",
        "quote_token_price_usd": "0.999768442424985",
        "quote_token_price_native_currency": "0.000370331965573941",
        "base_token_price_quote_token": "2700.28",
        "quote_token_price_base_token": "0.0003703319656",
        "address": "0x84f2195dc84d540a3ab92e659603d770014f0440",
        "name": "WETH / USDC 0.05%",
        "pool_created_at": "2026-08-12T20:06:47Z",
        "fdv_usd": "5530488363.03962",
        "market_cap_usd": "5533339448.78047",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "0",
          "h1": "0",
          "h6": "0.031",
          "h24": "0.632"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m15": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m30": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h1": {
            "buys": 0,
            "sells": 1,
            "buyers": 0,
            "sellers": 1
          },
          "h6": {
            "buys": 10,
            "sells": 6,
            "buyers": 10,
            "sellers": 6
          },
          "h24": {
            "buys": 45,
            "sells": 45,
            "buyers": 30,
            "sellers": 42
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "0.0",
          "m30": "0.0",
          "h1": "107.9895934",
          "h6": "1020.9553937597",
          "h24": "5873.0645101095"
        },
        "reserve_in_usd": "22643.7587"
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
            "id": "balancer-v3-ethereum",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0x4f88f7c99022eace4740c6898f59ce6a2e798a1e64ce54589720b7153eb224a7",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.999231843434099",
        "base_token_price_native_currency": "0.000374135206123566",
        "quote_token_price_usd": "2700.84",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0003741352061",
        "quote_token_price_base_token": "2672.830526592",
        "address": "0x4f88f7c99022eace4740c6898f59ce6a2e798a1e64ce54589720b7153eb224a7",
        "name": "USDC / WETH 0.05%",
        "pool_created_at": "2025-01-24T17:48:23Z",
        "fdv_usd": "48952838858.7407",
        "market_cap_usd": "74053125737.31",
        "price_change_percentage": {
          "m5": "0",
          "m15": "-0.024",
          "m30": "-0.079",
          "h1": "-0.006",
          "h6": "-0.059",
          "h24": "-0.106"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 1,
            "buyers": 0,
            "sellers": 1
          },
          "m15": {
            "buys": 0,
            "sells": 2,
            "buyers": 0,
            "sellers": 2
          },
          "m30": {
            "buys": 2,
            "sells": 3,
            "buyers": 2,
            "sellers": 3
          },
          "h1": {
            "buys": 3,
            "sells": 5,
            "buyers": 3,
            "sellers": 4
          },
          "h6": {
            "buys": 20,
            "sells": 28,
            "buyers": 19,
            "sellers": 19
          },
          "h24": {
            "buys": 88,
            "sells": 84,
            "buyers": 81,
            "sellers": 66
          }
        },
        "volume_usd": {
          "m5": "7.8574795855",
          "m15": "10.2278776692",
          "m30": "44.5686889857",
          "h1": "91.9304197098",
          "h6": "1313.4907120023",
          "h24": "3304.6075819866"
        },
        "reserve_in_usd": "33098.3766"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "uniswap-v4-ethereum",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "eth_0x7bea39867e4169dbe237d55c8242a8f2fcdcc387",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.998703579487187",
        "base_token_price_native_currency": "0.000369602925837844",
        "quote_token_price_usd": "2702.88",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0003696029258",
        "quote_token_price_base_token": "2705.606287432",
        "address": "0x7bea39867e4169dbe237d55c8242a8f2fcdcc387",
        "name": "USDC / WETH 1%",
        "pool_created_at": "2021-12-29T13:39:15Z",
        "fdv_usd": "48939385091.7251",
        "market_cap_usd": "74013976071.2264",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "0",
          "h1": "0",
          "h6": "0",
          "h24": "-0.116"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m15": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m30": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h1": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "h6": {
            "buys": 0,
            "sells": 1,
            "buyers": 0,
            "sellers": 1
          },
          "h24": {
            "buys": 0,
            "sells": 3,
            "buyers": 0,
            "sellers": 3
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "0.0",
          "m30": "0.0",
          "h1": "0.0",
          "h6": "27.1531124524",
          "h24": "58.1401469382"
        },
        "reserve_in_usd": "863393.1506"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "eth_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "eth_0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
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
  ]
}
```

## Why this matches (or not)

_[0.80|heuristic] DEX pool list with reserve/liquidity fields_
