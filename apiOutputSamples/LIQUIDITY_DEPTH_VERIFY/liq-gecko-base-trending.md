---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-gecko-base-trending
status: approved
captured_at: 2026-10-04T18:39:57Z
request_url: https://api.geckoterminal.com/api/v2/networks/base/trending_pools
content_type: application/json
inputs: |
  base trending pools
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must convey bid/ask order-book depth or pool liquidity for the pair asked.
capture_note: |
  list of pools with liquidity USD
reviewer_note: "auto_review: [0.80|heuristic] DEX pool list with reserve/liquidity fields"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "data": [
    {
      "id": "base_0x2df380544b88adb3ad0a94100dcc45fd705aae2d",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.020789127359971",
        "base_token_price_native_currency": "0.00000769804013744228811929630688925",
        "quote_token_price_usd": "0.997587383249271",
        "quote_token_price_native_currency": "0.000369360528444479",
        "base_token_price_quote_token": "0.02084153434",
        "quote_token_price_base_token": "47.9811123156",
        "address": "0x2df380544b88adb3ad0a94100dcc45fd705aae2d",
        "name": "xdp / USDC 0.01%",
        "pool_created_at": "2026-09-28T12:52:05Z",
        "fdv_usd": "207932709.397865",
        "market_cap_usd": "20793270.95",
        "price_change_percentage": {
          "m5": "-0.855",
          "m15": "-0.002",
          "m30": "-0.017",
          "h1": "0.093",
          "h6": "-0.761",
          "h24": "0.805"
        },
        "transactions": {
          "m5": {
            "buys": 772,
            "sells": 758,
            "buyers": 192,
            "sellers": 185
          },
          "m15": {
            "buys": 2487,
            "sells": 2453,
            "buyers": 233,
            "sellers": 219
          },
          "m30": {
            "buys": 4947,
            "sells": 4910,
            "buyers": 241,
            "sellers": 235
          },
          "h1": {
            "buys": 9536,
            "sells": 9295,
            "buyers": 346,
            "sellers": 351
          },
          "h6": {
            "buys": 59478,
            "sells": 59248,
            "buyers": 1094,
            "sellers": 1125
          },
          "h24": {
            "buys": 235909,
            "sells": 233620,
            "buyers": 2852,
            "sellers": 2946
          }
        },
        "volume_usd": {
          "m5": "596050.97756701",
          "m15": "2010597.93682437",
          "m30": "3918159.33441063",
          "h1": "7516966.12792686",
          "h6": "47558220.9172009",
          "h24": "191376804.672614"
        },
        "reserve_in_usd": "1873643.6551"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0x07b3d902783c3c12b077508c3b5c00113d1291d0",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "uniswap-v3-base",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0x215b2146c3164aba3f5b18e8619b737c7f7dd11e5ba693646dcd9a336c5a30ba",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.0148170157653167",
        "base_token_price_native_currency": "0.00000482400946926063",
        "quote_token_price_usd": "2700.85",
        "quote_token_price_native_currency": "0.999999999999994",
        "base_token_price_quote_token": "0.000004824009469",
        "quote_token_price_base_token": "207296.442175779",
        "address": "0x215b2146c3164aba3f5b18e8619b737c7f7dd11e5ba693646dcd9a336c5a30ba",
        "name": "Basecat / ETH",
        "pool_created_at": "2026-08-15T18:03:49Z",
        "fdv_usd": "14817014.7241875",
        "market_cap_usd": "14817015.77",
        "price_change_percentage": {
          "m5": "0.262",
          "m15": "-1.352",
          "m30": "-0.26",
          "h1": "-2.929",
          "h6": "15.224",
          "h24": "29.35"
        },
        "transactions": {
          "m5": {
            "buys": 13,
            "sells": 0,
            "buyers": 10,
            "sellers": 0
          },
          "m15": {
            "buys": 46,
            "sells": 5,
            "buyers": 29,
            "sellers": 3
          },
          "m30": {
            "buys": 72,
            "sells": 6,
            "buyers": 36,
            "sellers": 4
          },
          "h1": {
            "buys": 108,
            "sells": 80,
            "buyers": 52,
            "sellers": 45
          },
          "h6": {
            "buys": 577,
            "sells": 454,
            "buyers": 168,
            "sellers": 121
          },
          "h24": {
            "buys": 1225,
            "sells": 886,
            "buyers": 253,
            "sellers": 202
          }
        },
        "volume_usd": {
          "m5": "511.1395098389",
          "m15": "10418.7434887375",
          "m30": "13225.0007648383",
          "h1": "50328.8797232835",
          "h6": "267320.017661363",
          "h24": "471528.130915092"
        },
        "reserve_in_usd": "556017.5075"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0xb2000000000000000000004c27f6523082f41d01",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x0000000000000000000000000000000000000000",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "o1-launchpad",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0x6cdcb1c4a4d1c3c6d054b27ac5b77e89eafb971d",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.857257867918479",
        "base_token_price_native_currency": "0.000318355274506610942955414382071110276053996",
        "quote_token_price_usd": "0.997587383249271",
        "quote_token_price_native_currency": "0.000369360528444479",
        "base_token_price_quote_token": "0.8619093",
        "quote_token_price_base_token": "1.1602148858",
        "address": "0x6cdcb1c4a4d1c3c6d054b27ac5b77e89eafb971d",
        "name": "AERO / USDC",
        "pool_created_at": "2023-09-07T22:50:55Z",
        "fdv_usd": "1708511285.5141",
        "market_cap_usd": "857330688.788161",
        "price_change_percentage": {
          "m5": "-0.853",
          "m15": "0.008",
          "m30": "0.124",
          "h1": "-0.184",
          "h6": "0.201",
          "h24": "6.099"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 16,
            "buyers": 0,
            "sellers": 6
          },
          "m15": {
            "buys": 0,
            "sells": 34,
            "buyers": 0,
            "sellers": 9
          },
          "m30": {
            "buys": 7,
            "sells": 76,
            "buyers": 5,
            "sellers": 17
          },
          "h1": {
            "buys": 7,
            "sells": 205,
            "buyers": 5,
            "sellers": 51
          },
          "h6": {
            "buys": 190,
            "sells": 1280,
            "buyers": 106,
            "sellers": 153
          },
          "h24": {
            "buys": 915,
            "sells": 4854,
            "buyers": 262,
            "sellers": 357
          }
        },
        "volume_usd": {
          "m5": "58.5630193695",
          "m15": "324.4344080191",
          "m30": "13056.4146868568",
          "h1": "42318.9748558607",
          "h6": "1010006.0925485",
          "h24": "3735580.28119372"
        },
        "reserve_in_usd": "43914815.7379"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0x940181a94a35a4569e4529a3cdfb74e38fd98631",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "aerodrome-base",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0xef256e214c45aab706ca54d6e2c5d0ca42b87895a43e97b382ea012d13e78e49",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.00000931131198137051",
        "base_token_price_native_currency": "0.00000000379153656912049",
        "quote_token_price_usd": "2700.79",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.000000003791536569",
        "quote_token_price_base_token": "263745313.217951",
        "address": "0xef256e214c45aab706ca54d6e2c5d0ca42b87895a43e97b382ea012d13e78e49",
        "name": "boar / WETH",
        "pool_created_at": "2026-09-26T02:58:01Z",
        "fdv_usd": "921819.873838079",
        "market_cap_usd": "931131.1981",
        "price_change_percentage": {
          "m5": "-2.084",
          "m15": "-1.295",
          "m30": "-0.555",
          "h1": "5.021",
          "h6": "-13.26",
          "h24": "26.117"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 3,
            "buyers": 0,
            "sellers": 3
          },
          "m15": {
            "buys": 16,
            "sells": 8,
            "buyers": 14,
            "sellers": 8
          },
          "m30": {
            "buys": 25,
            "sells": 11,
            "buyers": 21,
            "sellers": 11
          },
          "h1": {
            "buys": 36,
            "sells": 13,
            "buyers": 28,
            "sellers": 13
          },
          "h6": {
            "buys": 185,
            "sells": 127,
            "buyers": 120,
            "sellers": 94
          },
          "h24": {
            "buys": 1022,
            "sells": 972,
            "buyers": 379,
            "sellers": 391
          }
        },
        "volume_usd": {
          "m5": "2042.5646674918",
          "m15": "4763.5137124826",
          "m30": "5459.10880128",
          "h1": "8214.2260745872",
          "h6": "80646.3024935012",
          "h24": "665375.027438768"
        },
        "reserve_in_usd": "303495.1078"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0x0cbf291ba052174879d90bf781df1a5f2bc5bb07",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x4200000000000000000000000000000000000006",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "uniswap-v4-base",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0x3dfdecc334a8f2618321c78a9de0e9428438f871",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.00908909745162961",
        "base_token_price_native_currency": "0.00000338745369673952600336361678726838300166",
        "quote_token_price_usd": "0.997583898941847",
        "quote_token_price_native_currency": "0.000369360528444479",
        "base_token_price_quote_token": "0.00917113074",
        "quote_token_price_base_token": "109.0378087824",
        "address": "0x3dfdecc334a8f2618321c78a9de0e9428438f871",
        "name": "BLUECHIP / USDC 0.004%",
        "pool_created_at": "2026-08-26T18:55:09Z",
        "fdv_usd": "9089097.420852",
        "market_cap_usd": "9089097.452",
        "price_change_percentage": {
          "m5": "-1.145",
          "m15": "-2.401",
          "m30": "-2.58",
          "h1": "-1.71",
          "h6": "11.19",
          "h24": "10.066"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 8,
            "buyers": 0,
            "sellers": 4
          },
          "m15": {
            "buys": 2,
            "sells": 14,
            "buyers": 2,
            "sellers": 5
          },
          "m30": {
            "buys": 7,
            "sells": 20,
            "buyers": 6,
            "sellers": 11
          },
          "h1": {
            "buys": 22,
            "sells": 25,
            "buyers": 15,
            "sellers": 14
          },
          "h6": {
            "buys": 337,
            "sells": 180,
            "buyers": 97,
            "sellers": 70
          },
          "h24": {
            "buys": 760,
            "sells": 460,
            "buyers": 161,
            "sellers": 136
          }
        },
        "volume_usd": {
          "m5": "2551.507983286",
          "m15": "7614.2868228191",
          "m30": "11977.4249206205",
          "h1": "20692.1192001484",
          "h6": "179073.383914858",
          "h24": "337458.476414424"
        },
        "reserve_in_usd": "102805.0438"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0xb200000000000000000000cfbdf64a8706a94a01",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "aerodrome-slipstream-3",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0x0c3b466104545efa096b8f944c1e524e1d0d4888",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.240030734593712",
        "base_token_price_native_currency": "0.0000891396430180709",
        "quote_token_price_usd": "0.845840090229699",
        "quote_token_price_native_currency": "0.000313188270707176",
        "base_token_price_quote_token": "0.2846199917",
        "quote_token_price_base_token": "3.5134566407",
        "address": "0x0c3b466104545efa096b8f944c1e524e1d0d4888",
        "name": "TIBBIR / VIRTUAL",
        "pool_created_at": "2025-01-12T00:30:03Z",
        "fdv_usd": "171591328.041287",
        "market_cap_usd": "227865292.160812",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "-0.078",
          "h1": "-2.417",
          "h6": "9.274",
          "h24": "2.715"
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
            "sells": 1,
            "buyers": 0,
            "sellers": 1
          },
          "m30": {
            "buys": 0,
            "sells": 4,
            "buyers": 0,
            "sellers": 4
          },
          "h1": {
            "buys": 4,
            "sells": 18,
            "buyers": 1,
            "sellers": 16
          },
          "h6": {
            "buys": 86,
            "sells": 303,
            "buyers": 37,
            "sellers": 101
          },
          "h24": {
            "buys": 297,
            "sells": 531,
            "buyers": 125,
            "sellers": 172
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "76.597650583",
          "m30": "873.5364060838",
          "h1": "15229.1847003898",
          "h6": "128761.783193133",
          "h24": "308168.754818293"
        },
        "reserve_in_usd": "3701505.472"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0xa4a2e2ca3fbfe21aed83471d28b6f65a233c6e00",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x0b3e328455c4059eeb9e3f84b5543f74e24e7e1b",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "uniswap-v2-base",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0xfc25fdd217e288d03a877f0b7d49e0bbe52b2288c88de929125062569fc7eb2a",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.0000990039178659995",
        "base_token_price_native_currency": "0.0000000248589497904931",
        "quote_token_price_usd": "2700.84",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.00000002485894979",
        "quote_token_price_base_token": "40226960.85023",
        "address": "0xfc25fdd217e288d03a877f0b7d49e0bbe52b2288c88de929125062569fc7eb2a",
        "name": "Surplus / WETH",
        "pool_created_at": "2026-05-16T15:20:31Z",
        "fdv_usd": "9900370.39220728",
        "market_cap_usd": "9900391.787",
        "price_change_percentage": {
          "m5": "0.101",
          "m15": "0.101",
          "m30": "-0.353",
          "h1": "-0.683",
          "h6": "-24.126",
          "h24": "-17.434"
        },
        "transactions": {
          "m5": {
            "buys": 4,
            "sells": 0,
            "buyers": 4,
            "sellers": 0
          },
          "m15": {
            "buys": 4,
            "sells": 0,
            "buyers": 4,
            "sellers": 0
          },
          "m30": {
            "buys": 5,
            "sells": 4,
            "buyers": 5,
            "sellers": 3
          },
          "h1": {
            "buys": 8,
            "sells": 15,
            "buyers": 8,
            "sellers": 14
          },
          "h6": {
            "buys": 85,
            "sells": 74,
            "buyers": 68,
            "sellers": 58
          },
          "h24": {
            "buys": 370,
            "sells": 232,
            "buyers": 182,
            "sellers": 155
          }
        },
        "volume_usd": {
          "m5": "452.1506449947",
          "m15": "452.1506449947",
          "m30": "1768.6657814398",
          "h1": "4409.3216531853",
          "h6": "146471.022090576",
          "h24": "342217.47646978"
        },
        "reserve_in_usd": "846132.1192"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0xc52aedec3374422d7510e294cfaa90799595cba3",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x4200000000000000000000000000000000000006",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "uniswap-v4-base",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0x566bee7ef7b39f29d150ab3be6b6242c17cc5a31",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.0487892710872152",
        "base_token_price_native_currency": "0.0000178146803732314",
        "quote_token_price_usd": "2700.85",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.00001781468037",
        "quote_token_price_base_token": "56133.4797509258",
        "address": "0x566bee7ef7b39f29d150ab3be6b6242c17cc5a31",
        "name": "EDEL / WETH",
        "pool_created_at": "2025-11-12T17:00:57Z",
        "fdv_usd": "48789268.0210566",
        "market_cap_usd": "33284190.0690023",
        "price_change_percentage": {
          "m5": "1.443",
          "m15": "-0.025",
          "m30": "2.734",
          "h1": "1.116",
          "h6": "0.511",
          "h24": "7.564"
        },
        "transactions": {
          "m5": {
            "buys": 25,
            "sells": 14,
            "buyers": 7,
            "sellers": 4
          },
          "m15": {
            "buys": 80,
            "sells": 46,
            "buyers": 8,
            "sellers": 6
          },
          "m30": {
            "buys": 156,
            "sells": 96,
            "buyers": 9,
            "sellers": 8
          },
          "h1": {
            "buys": 310,
            "sells": 193,
            "buyers": 10,
            "sellers": 10
          },
          "h6": {
            "buys": 645,
            "sells": 529,
            "buyers": 26,
            "sellers": 45
          },
          "h24": {
            "buys": 1715,
            "sells": 1511,
            "buyers": 339,
            "sellers": 336
          }
        },
        "volume_usd": {
          "m5": "2309.9053754066",
          "m15": "7295.9264203278",
          "m30": "21850.593629097",
          "h1": "36839.4116281112",
          "h6": "83592.3375687448",
          "h24": "1408112.44245567"
        },
        "reserve_in_usd": "1486614.551"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0xfb31f85a8367210b2e4ed2360d2da9dc2d2ccc95",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x4200000000000000000000000000000000000006",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "aerodrome-base",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0x1ef035205f94c7734827961c438474d089a334a0",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.0207887799723411",
        "base_token_price_native_currency": "0.00000769980579953841329830431621947",
        "quote_token_price_usd": "0.997587383249271",
        "quote_token_price_native_currency": "0.000369360528444479",
        "base_token_price_quote_token": "0.02084631466",
        "quote_token_price_base_token": "47.9701096444",
        "address": "0x1ef035205f94c7734827961c438474d089a334a0",
        "name": "xdp / USDC 2%",
        "pool_created_at": "2026-09-28T13:07:23Z",
        "fdv_usd": "207888808.197886",
        "market_cap_usd": "20788880.83",
        "price_change_percentage": {
          "m5": "-0.843",
          "m15": "-0.027",
          "m30": "-0.06",
          "h1": "0.08",
          "h6": "-0.792",
          "h24": "0.83"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 13,
            "buyers": 0,
            "sellers": 12
          },
          "m15": {
            "buys": 82,
            "sells": 49,
            "buyers": 64,
            "sellers": 39
          },
          "m30": {
            "buys": 133,
            "sells": 100,
            "buyers": 85,
            "sellers": 63
          },
          "h1": {
            "buys": 449,
            "sells": 231,
            "buyers": 159,
            "sellers": 125
          },
          "h6": {
            "buys": 2299,
            "sells": 2529,
            "buyers": 469,
            "sellers": 449
          },
          "h24": {
            "buys": 7842,
            "sells": 7143,
            "buyers": 1080,
            "sellers": 1023
          }
        },
        "volume_usd": {
          "m5": "3250.5157208819",
          "m15": "65506.4492355472",
          "m30": "106249.849868742",
          "h1": "288538.993449282",
          "h6": "2024698.519826",
          "h24": "6404403.06010605"
        },
        "reserve_in_usd": "2032171.6664"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0x07b3d902783c3c12b077508c3b5c00113d1291d0",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "aerodrome-slipstream-3",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0x5116773e18a9c7bb03ebb961b38678e45e238923",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.000218532405219571",
        "base_token_price_native_currency": "0.0000000809130534635994",
        "quote_token_price_usd": "2700.83",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.00000008091305346",
        "quote_token_price_base_token": "12358945.2775982",
        "address": "0x5116773e18a9c7bb03ebb961b38678e45e238923",
        "name": "DRB / WETH 1%",
        "pool_created_at": "2025-03-07T09:58:57Z",
        "fdv_usd": "21565806.6256851",
        "market_cap_usd": "21853240.52",
        "price_change_percentage": {
          "m5": "0",
          "m15": "-0.033",
          "m30": "-0.051",
          "h1": "0.059",
          "h6": "3.446",
          "h24": "2.955"
        },
        "transactions": {
          "m5": {
            "buys": 2,
            "sells": 0,
            "buyers": 1,
            "sellers": 0
          },
          "m15": {
            "buys": 5,
            "sells": 1,
            "buyers": 1,
            "sellers": 1
          },
          "m30": {
            "buys": 10,
            "sells": 2,
            "buyers": 1,
            "sellers": 2
          },
          "h1": {
            "buys": 22,
            "sells": 3,
            "buyers": 2,
            "sellers": 3
          },
          "h6": {
            "buys": 361,
            "sells": 30,
            "buyers": 25,
            "sellers": 9
          },
          "h24": {
            "buys": 1018,
            "sells": 1074,
            "buyers": 69,
            "sellers": 117
          }
        },
        "volume_usd": {
          "m5": "0.01756510428",
          "m15": "273.7573798995",
          "m30": "380.6247044953",
          "h1": "1363.744727482",
          "h6": "32039.1867521854",
          "h24": "258963.758930401"
        },
        "reserve_in_usd": "1670377.7387"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0x3ec2156d4c0a9cbdab4a016633b7bcf6a8d68ea2",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x4200000000000000000000000000000000000006",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "uniswap-v3-base",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0xec33256bf1ded407a57fd3c1965e7556e42ac14db09bc4e6fef57d5e2eb0b0b9",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.0000230176173435021",
        "base_token_price_native_currency": "0.0000000101997855762525",
        "quote_token_price_usd": "2701.23",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.00000001019978558",
        "quote_token_price_base_token": "98041276.7037216",
        "address": "0xec33256bf1ded407a57fd3c1965e7556e42ac14db09bc4e6fef57d5e2eb0b0b9",
        "name": "GITLAWB / WETH",
        "pool_created_at": "2026-03-11T02:00:07Z",
        "fdv_usd": "2281043.98611021",
        "market_cap_usd": "2301761.734",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "-0.217",
          "h1": "-2.644",
          "h6": "2.978",
          "h24": "2.559"
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
            "sells": 1,
            "buyers": 0,
            "sellers": 1
          },
          "m30": {
            "buys": 0,
            "sells": 5,
            "buyers": 0,
            "sellers": 5
          },
          "h1": {
            "buys": 2,
            "sells": 9,
            "buyers": 2,
            "sellers": 6
          },
          "h6": {
            "buys": 48,
            "sells": 35,
            "buyers": 32,
            "sellers": 26
          },
          "h24": {
            "buys": 211,
            "sells": 172,
            "buyers": 118,
            "sellers": 93
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "1.0582069971",
          "m30": "311.4784757033",
          "h1": "1413.308455097",
          "h6": "17683.0380406156",
          "h24": "63124.8508569758"
        },
        "reserve_in_usd": "554110.8213"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0x5f980dcfc4c0fa3911554cf5ab288ed0eb13dba3",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x4200000000000000000000000000000000000006",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "uniswap-v4-base",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0x01784ef301d79e4b2df3a21ad9a536d4cf09a5ce",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "28.7676931474457",
        "base_token_price_native_currency": "0.0106513400335559",
        "quote_token_price_usd": "2700.85",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.01065134003",
        "quote_token_price_base_token": "93.884900571",
        "address": "0x01784ef301d79e4b2df3a21ad9a536d4cf09a5ce",
        "name": "VVV / WETH",
        "pool_created_at": "2025-01-27T16:44:59Z",
        "fdv_usd": "2332935606.07538",
        "market_cap_usd": "1390698893.97512",
        "price_change_percentage": {
          "m5": "0.175",
          "m15": "1.196",
          "m30": "1.197",
          "h1": "1.469",
          "h6": "2.295",
          "h24": "2.926"
        },
        "transactions": {
          "m5": {
            "buys": 32,
            "sells": 0,
            "buyers": 10,
            "sellers": 0
          },
          "m15": {
            "buys": 118,
            "sells": 1,
            "buyers": 43,
            "sellers": 1
          },
          "m30": {
            "buys": 162,
            "sells": 1,
            "buyers": 43,
            "sellers": 1
          },
          "h1": {
            "buys": 340,
            "sells": 6,
            "buyers": 64,
            "sellers": 3
          },
          "h6": {
            "buys": 1586,
            "sells": 76,
            "buyers": 131,
            "sellers": 55
          },
          "h24": {
            "buys": 5458,
            "sells": 639,
            "buyers": 218,
            "sellers": 282
          }
        },
        "volume_usd": {
          "m5": "8346.7852671316",
          "m15": "55338.3716573515",
          "m30": "55757.4205996396",
          "h1": "70440.5165882545",
          "h6": "217334.260942616",
          "h24": "849346.330702879"
        },
        "reserve_in_usd": "18903177.5395"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0xacfe6019ed1a7dc6f7b508c02d1b04ec88cc21bf",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x4200000000000000000000000000000000000006",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "aerodrome-base",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0xaec085e5a5ce8d96a7bdd3eb3a62445d4f6ce703",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.000421174999883351",
        "base_token_price_native_currency": "0.000000155942804034794",
        "quote_token_price_usd": "2700.83",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.000000155942804",
        "quote_token_price_base_token": "6412607.53382939",
        "address": "0xaec085e5a5ce8d96a7bdd3eb3a62445d4f6ce703",
        "name": "BNKR / WETH 1%",
        "pool_created_at": "2024-12-03T04:44:53Z",
        "fdv_usd": "40658948.1194831",
        "market_cap_usd": "42117499.99",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0.01",
          "m30": "-0.023",
          "h1": "-0.035",
          "h6": "0.175",
          "h24": "4.677"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 2,
            "buyers": 0,
            "sellers": 1
          },
          "m15": {
            "buys": 0,
            "sells": 5,
            "buyers": 0,
            "sellers": 1
          },
          "m30": {
            "buys": 0,
            "sells": 8,
            "buyers": 0,
            "sellers": 1
          },
          "h1": {
            "buys": 0,
            "sells": 22,
            "buyers": 0,
            "sellers": 3
          },
          "h6": {
            "buys": 1,
            "sells": 93,
            "buyers": 1,
            "sellers": 10
          },
          "h24": {
            "buys": 159,
            "sells": 307,
            "buyers": 44,
            "sellers": 15
          }
        },
        "volume_usd": {
          "m5": "0.01756510428",
          "m15": "0.04578840234",
          "m30": "0.0702598685",
          "h1": "49.7516301341",
          "h6": "680.9162070785",
          "h24": "53542.0679202942"
        },
        "reserve_in_usd": "2624747.889"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0x22af33fe49fd1fa80c7149773dde5890d3c76f3b",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x4200000000000000000000000000000000000006",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "uniswap-v3-base",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0x7c84276e317f128b55bd270dbfba3ef94c84b984c124a1de7c4f72da90bfba45",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.830246435754811",
        "base_token_price_native_currency": "0.000116585922930408",
        "quote_token_price_usd": "2700.46",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0001165859229",
        "quote_token_price_base_token": "8577.364872746",
        "address": "0x7c84276e317f128b55bd270dbfba3ef94c84b984c124a1de7c4f72da90bfba45",
        "name": "POD / ETH 1%",
        "pool_created_at": "2026-03-02T17:54:15Z",
        "fdv_usd": "415123217.813613",
        "market_cap_usd": "69339297.0220686",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0.002",
          "m30": "2.231",
          "h1": "1.925",
          "h6": "-0.617",
          "h24": "12.14"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 0,
            "buyers": 0,
            "sellers": 0
          },
          "m15": {
            "buys": 2,
            "sells": 0,
            "buyers": 2,
            "sellers": 0
          },
          "m30": {
            "buys": 2,
            "sells": 1,
            "buyers": 2,
            "sellers": 1
          },
          "h1": {
            "buys": 5,
            "sells": 6,
            "buyers": 4,
            "sellers": 6
          },
          "h6": {
            "buys": 47,
            "sells": 94,
            "buyers": 20,
            "sellers": 46
          },
          "h24": {
            "buys": 712,
            "sells": 475,
            "buyers": 150,
            "sellers": 156
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "21.3772411378",
          "m30": "25.6460471506",
          "h1": "3792.1460490756",
          "h6": "102575.018354006",
          "h24": "2509020.1257924"
        },
        "reserve_in_usd": "3962667.1337"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0xed664536023d8e4b1640c394777d34abaff1df8f",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x0000000000000000000000000000000000000000",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "uniswap-v4-base",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0xe2b182796518e76845f46ccdc522495d81630d14",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.0486323480944806",
        "base_token_price_native_currency": "0.0000180705652952669",
        "quote_token_price_usd": "1.00357797157287",
        "quote_token_price_native_currency": "0.00037158682147552",
        "base_token_price_quote_token": "0.04863080242",
        "quote_token_price_base_token": "20.5630989072",
        "address": "0xe2b182796518e76845f46ccdc522495d81630d14",
        "name": "EDEL / USDC 0.3%",
        "pool_created_at": "2025-11-17T18:30:14Z",
        "fdv_usd": "48632345.0309274",
        "market_cap_usd": "33177136.7181014",
        "price_change_percentage": {
          "m5": "-0.241",
          "m15": "0.705",
          "m30": "1.333",
          "h1": "1.811",
          "h6": "-1.118",
          "h24": "8.048"
        },
        "transactions": {
          "m5": {
            "buys": 6,
            "sells": 1,
            "buyers": 3,
            "sellers": 1
          },
          "m15": {
            "buys": 17,
            "sells": 8,
            "buyers": 11,
            "sellers": 8
          },
          "m30": {
            "buys": 69,
            "sells": 65,
            "buyers": 28,
            "sellers": 28
          },
          "h1": {
            "buys": 81,
            "sells": 77,
            "buyers": 35,
            "sellers": 36
          },
          "h6": {
            "buys": 451,
            "sells": 542,
            "buyers": 125,
            "sellers": 164
          },
          "h24": {
            "buys": 2301,
            "sells": 2142,
            "buyers": 453,
            "sellers": 459
          }
        },
        "volume_usd": {
          "m5": "311.4169849451",
          "m15": "4035.4987176976",
          "m30": "55531.2666380926",
          "h1": "57293.7606248058",
          "h6": "292297.153415986",
          "h24": "846773.816881203"
        },
        "reserve_in_usd": "505981.9333"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0xfb31f85a8367210b2e4ed2360d2da9dc2d2ccc95",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "aerodrome-slipstream-2",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0x717e174d5dae280802d1a2c15c1c0976561a3f61",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "1.97352718818318",
        "base_token_price_native_currency": "0.000730705958562369",
        "quote_token_price_usd": "2700.85",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.0007307059586",
        "quote_token_price_base_token": "1368.539544918",
        "address": "0x717e174d5dae280802d1a2c15c1c0976561a3f61",
        "name": "ZRO / WETH 0.081%",
        "pool_created_at": "2026-04-16T04:45:17Z",
        "fdv_usd": "11978154.7137983",
        "market_cap_usd": "697273454.597282",
        "price_change_percentage": {
          "m5": "-0.083",
          "m15": "-0.002",
          "m30": "0.483",
          "h1": "0.23",
          "h6": "-1.632",
          "h24": "-4.334"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 5,
            "buyers": 0,
            "sellers": 4
          },
          "m15": {
            "buys": 5,
            "sells": 9,
            "buyers": 5,
            "sellers": 6
          },
          "m30": {
            "buys": 12,
            "sells": 14,
            "buyers": 11,
            "sellers": 8
          },
          "h1": {
            "buys": 27,
            "sells": 40,
            "buyers": 14,
            "sellers": 19
          },
          "h6": {
            "buys": 419,
            "sells": 548,
            "buyers": 117,
            "sellers": 121
          },
          "h24": {
            "buys": 2298,
            "sells": 3629,
            "buyers": 399,
            "sellers": 326
          }
        },
        "volume_usd": {
          "m5": "590.8236343436",
          "m15": "1647.7678769024",
          "m30": "5247.8478486445",
          "h1": "16248.5540802595",
          "h6": "182138.836069334",
          "h24": "1087317.06072834"
        },
        "reserve_in_usd": "182657.6752"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0x6985884c4392d348587b19cb9eaaf157f13271cd",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x4200000000000000000000000000000000000006",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "aerodrome-slipstream-3",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0x4a9b9e13975d26f4e3e17c655593bb82145dd4452aedafb826d856b817c9cfd4",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.0000214043556415258",
        "base_token_price_native_currency": "0.00000000666551089303668",
        "quote_token_price_usd": "2700.85",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.000000006665510893",
        "quote_token_price_base_token": "150026009.415824",
        "address": "0x4a9b9e13975d26f4e3e17c655593bb82145dd4452aedafb826d856b817c9cfd4",
        "name": "aeon / WETH",
        "pool_created_at": "2026-03-10T22:01:31Z",
        "fdv_usd": "2140435.5490244",
        "market_cap_usd": "2140435.564",
        "price_change_percentage": {
          "m5": "0",
          "m15": "-0.016",
          "m30": "3.099",
          "h1": "2.015",
          "h6": "-0.924",
          "h24": "14.209"
        },
        "transactions": {
          "m5": {
            "buys": 0,
            "sells": 1,
            "buyers": 0,
            "sellers": 1
          },
          "m15": {
            "buys": 2,
            "sells": 2,
            "buyers": 2,
            "sellers": 2
          },
          "m30": {
            "buys": 18,
            "sells": 13,
            "buyers": 16,
            "sellers": 4
          },
          "h1": {
            "buys": 24,
            "sells": 15,
            "buyers": 21,
            "sellers": 5
          },
          "h6": {
            "buys": 89,
            "sells": 103,
            "buyers": 67,
            "sellers": 68
          },
          "h24": {
            "buys": 205,
            "sells": 179,
            "buyers": 126,
            "sellers": 118
          }
        },
        "volume_usd": {
          "m5": "873.1668566297",
          "m15": "1593.3890346811",
          "m30": "11269.6301592996",
          "h1": "13896.8245215233",
          "h6": "101970.30987592",
          "h24": "191423.456793214"
        },
        "reserve_in_usd": "425572.9345"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0xbf8e8f0e8866a7052f948c16508644347c57aba3",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x4200000000000000000000000000000000000006",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "uniswap-v4-base",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0xd9edc75a3a797ec92ca370f19051babebfb2edee",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.0688162663290964",
        "base_token_price_native_currency": "0.0000254726063272088",
        "quote_token_price_usd": "2700.84",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.00002547260633",
        "quote_token_price_base_token": "39257.859488522",
        "address": "0xd9edc75a3a797ec92ca370f19051babebfb2edee",
        "name": "KTA / WETH",
        "pool_created_at": "2025-03-05T18:32:49Z",
        "fdv_usd": "68816261.2048578",
        "market_cap_usd": "42255538.922784",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0.02",
          "m30": "0.731",
          "h1": "-1.602",
          "h6": "-2.842",
          "h24": "2.272"
        },
        "transactions": {
          "m5": {
            "buys": 1,
            "sells": 0,
            "buyers": 1,
            "sellers": 0
          },
          "m15": {
            "buys": 3,
            "sells": 0,
            "buyers": 3,
            "sellers": 0
          },
          "m30": {
            "buys": 4,
            "sells": 2,
            "buyers": 4,
            "sellers": 2
          },
          "h1": {
            "buys": 19,
            "sells": 30,
            "buyers": 14,
            "sellers": 7
          },
          "h6": {
            "buys": 79,
            "sells": 89,
            "buyers": 38,
            "sellers": 28
          },
          "h24": {
            "buys": 431,
            "sells": 158,
            "buyers": 91,
            "sellers": 62
          }
        },
        "volume_usd": {
          "m5": "486.1512",
          "m15": "625.5625804096",
          "m30": "3310.9716770648",
          "h1": "31887.5347804036",
          "h6": "93049.4383947185",
          "h24": "252064.090525716"
        },
        "reserve_in_usd": "4192579.4339"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0xc0634090f2fe6c6d75e61be2b949464abb498973",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x4200000000000000000000000000000000000006",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "aerodrome-base",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0x5e9782079683037fc8bb57625683359d9efaef80f2b829c4bb5b1896c6bb40b6",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.0000142786141912813",
        "base_token_price_native_currency": "0.00000000410971476788752",
        "quote_token_price_usd": "2700.65",
        "quote_token_price_native_currency": "1.0",
        "base_token_price_quote_token": "0.000000004109714768",
        "quote_token_price_base_token": "243325889.138049",
        "address": "0x5e9782079683037fc8bb57625683359d9efaef80f2b829c4bb5b1896c6bb40b6",
        "name": "Ratspeak / WETH",
        "pool_created_at": "2026-05-18T20:05:33Z",
        "fdv_usd": "1370746.89424866",
        "market_cap_usd": "1370746.89424866",
        "price_change_percentage": {
          "m5": "0",
          "m15": "0",
          "m30": "0",
          "h1": "0.719",
          "h6": "-5.611",
          "h24": "-1.776"
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
            "buys": 2,
            "sells": 1,
            "buyers": 2,
            "sellers": 1
          },
          "h6": {
            "buys": 6,
            "sells": 24,
            "buyers": 6,
            "sellers": 21
          },
          "h24": {
            "buys": 47,
            "sells": 81,
            "buyers": 43,
            "sellers": 62
          }
        },
        "volume_usd": {
          "m5": "0.0",
          "m15": "0.0",
          "m30": "13.9976466586",
          "h1": "1410.4957359726",
          "h6": "10353.902110577",
          "h24": "69604.6321231093"
        },
        "reserve_in_usd": "318890.7099"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0xf1e9baa65d418a9025e1851dd2d37f1ad208bba3",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x4200000000000000000000000000000000000006",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "bankr",
            "type": "dex"
          }
        }
      }
    },
    {
      "id": "base_0x8a8e4170c09074b109352190d47e54d7c1f61e4e",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "0.796528581014995",
        "base_token_price_native_currency": "0.000294884084591147266021095856426908976354064",
        "quote_token_price_usd": "0.997587383249271",
        "quote_token_price_native_currency": "0.000369360528444479",
        "base_token_price_quote_token": "0.7983638258",
        "quote_token_price_base_token": "1.2525617615",
        "address": "0x8a8e4170c09074b109352190d47e54d7c1f61e4e",
        "name": "PROS / USDC 0.01%",
        "pool_created_at": "2026-05-13T13:17:19Z",
        "fdv_usd": "3239249.33463495",
        "market_cap_usd": "3235177.67615649",
        "price_change_percentage": {
          "m5": "-0.895",
          "m15": "0.041",
          "m30": "0.213",
          "h1": "-0.1",
          "h6": "-2.604",
          "h24": "8.833"
        },
        "transactions": {
          "m5": {
            "buys": 9,
            "sells": 19,
            "buyers": 6,
            "sellers": 12
          },
          "m15": {
            "buys": 54,
            "sells": 67,
            "buyers": 16,
            "sellers": 16
          },
          "m30": {
            "buys": 147,
            "sells": 152,
            "buyers": 24,
            "sellers": 20
          },
          "h1": {
            "buys": 424,
            "sells": 477,
            "buyers": 47,
            "sellers": 35
          },
          "h6": {
            "buys": 6816,
            "sells": 7155,
            "buyers": 239,
            "sellers": 195
          },
          "h24": {
            "buys": 26382,
            "sells": 28060,
            "buyers": 545,
            "sellers": 527
          }
        },
        "volume_usd": {
          "m5": "2667.7013633897",
          "m15": "14440.2691476886",
          "m30": "27249.1879627584",
          "h1": "100208.044830587",
          "h6": "1897015.53572653",
          "h24": "8836784.98199141"
        },
        "reserve_in_usd": "1051828.0936"
      },
      "relationships": {
        "base_token": {
          "data": {
            "id": "base_0x8b7dde054be9d180c1be7fae0874697374a49832",
            "type": "token"
          }
        },
        "quote_token": {
          "data": {
            "id": "base_0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
            "type": "token"
          }
        },
        "dex": {
          "data": {
            "id": "aerodrome-slipstream-3",
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
