---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-dydx-orderbook
status: approved
captured_at: 2026-10-08T04:42:00Z
request_url: https://indexer.dydx.trade/v4/orderbooks/perpetualMarket/BTC-USD
content_type: application/json
inputs: |
  {"upbit": "USDT-BTC", "poloniex": "BTC_USDT", "lbank": "btc_usdt", "bingx": "BTC-USDT", "whitebit": "BTC_USDT", "deribit": "BTC_USDC", "ir": "xbt", "hl": "BTC", "dydx": "BTC-USD", "binance": "BTCUSDT"}
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must return the live bid/ask order book (depth levels) for the pair asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the bid price for the BTC-USD pair, which directly answers the intent to measure the live bid/ask order book."
reviewed_at: 2026-10-08T04:56:29Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "bids": [
    {
      "price": "82502",
      "size": "0.0002"
    },
    {
      "price": "82500",
      "size": "0.07"
    },
    {
      "price": "82473",
      "size": "0.0606"
    },
    {
      "price": "82451",
      "size": "0.1212"
    },
    {
      "price": "82449",
      "size": "0.1802"
    },
    {
      "price": "82445",
      "size": "4.8068"
    },
    {
      "price": "82431",
      "size": "0.1213"
    },
    {
      "price": "82421",
      "size": "2.4034"
    },
    {
      "price": "82420",
      "size": "2.4034"
    },
    {
      "price": "82362",
      "size": "4.8068"
    },
    {
      "price": "82353",
      "size": "0.4217"
    },
    {
      "price": "82351",
      "size": "0.0304"
    },
    {
      "price": "82338",
      "size": "2.4034"
    },
    {
      "price": "82337",
      "size": "2.4034"
    },
    {
      "price": "82280",
      "size": "4.8068"
    },
    {
      "price": "82256",
      "size": "2.4034"
    },
    {
      "price": "82255",
      "size": "2.4034"
    },
    {
      "price": "82252",
      "size": "0.8486"
    },
    {
      "price": "82247",
      "size": "0.8486"
    },
    {
      "price": "82205",
      "size": "3.0423"
    },
    {
      "price": "82198",
      "size": "4.8068"
    },
    {
      "price": "82174",
      "size": "2.4034"
    },
    {
      "price": "82173",
      "size": "2.4034"
    },
    {
      "price": "82157",
      "size": "0.05"
    },
    {
      "price": "82116",
      "size": "4.8068"
    },
    {
      "price": "82092",
      "size": "2.4034"
    },
    {
      "price": "82091",
      "size": "2.4034"
    },
    {
      "price": "82006",
      "size": "0.002"
    },
    {
      "price": "82000",
      "size": "5.15"
    },
    {
      "price": "81977",
      "size": "0.0619"
    },
    {
      "price": "81923",
      "size": "0.4481"
    },
    {
      "price": "81922",
      "size": "2.5457"
    },
    {
      "price": "81921",
      "size": "2.4425"
    },
    {
      "price": "81917",
      "size": "2.5459"
    },
    {
      "price": "81903",
      "size": "0.5872"
    },
    {
      "price": "81844",
      "size": "5"
    },
    {
      "price": "81841",
      "size": "0.02"
    },
    {
      "price": "81840",
      "size": "0.4797"
    },
    {
      "price": "81831",
      "size": "3.2731"
    },
    {
      "price": "81817",
      "size": "3.2736"
    },
    {
      "price": "81800",
      "size": "0.003"
    },
    {
      "price": "81798",
      "size": "5.0915"
    },
    {
      "price": "81784",
      "size": "5.0923"
    },
    {
      "price": "81758",
      "size": "0.172"
    },
    {
      "price": "81675",
      "size": "0.1891"
    },
    {
      "price": "81600",
      "size": "12.8689"
    },
    {
      "price": "81593",
      "size": "0.2382"
    },
    {
      "price": "81586",
      "size": "12.7308"
    },
    {
      "price": "81510",
      "size": "0.2401"
    },
    {
      "price": "81501",
      "size": "0.1"
    },
    {
      "price": "81500",
      "size": "0.0061"
    },
    {
      "price": "81465",
      "size": "0.0001"
    },
    {
      "price": "81444",
      "size": "0.0073"
    },
    {
      "price": "81428",
      "size": "0.1582"
    },
    {
      "price": "81419",
      "size": "1.875"
    },
    {
      "price": "81418",
      "size": "3.675"
    },
    {
      "price": "81405",
      "size": "1.8"
    },
    {
      "price": "81345",
      "size": "0.1918"
    },
    {
      "price": "81341",
      "size": "3"
    },
    {
      "price": "81324",
      "size": "8.3334"
    },
    {
      "price": "81263",
      "size": "0.2209"
    },
    {
      "price": "81229",
      "size": "12.9166"
    },
    {
      "price": "81209",
      "size": "0.0059"
    },
    {
      "price": "81204",
      "size": "8.4"
    },
    {
      "price": "81190",
      "size": "8.4"
    },
    {
      "price": "81180",
      "size": "0.28"
    },
    {
      "price": "81134",
      "size": "17.5"
    },
    {
      "price": "81099",
      "size": "0.0001"
    },
    {
      "price": "81098",
      "size": "0.3668"
    },
    {
      "price": "81040",
      "size": "0.0098"
    },
    {
      "price": "81039",
      "size": "22.0834"
    },
    {
      "price": "81036",
      "size": "0.1177"
    },
    {
      "price": "81015",
      "size": "0.2065"
    },
    {
      "price": "81000",
      "size": "0.0158"
    },
    {
      "price": "80989",
      "size": "15"
    },
    {
      "price": "80976",
      "size": "15"
    },
    {
      "price": "80964",
      "size": "12.5"
    },
    {
      "price": "80957",
      "size": "0.0098"
    },
    {
      "price": "80953",
      "size": "0.1177"
    },
    {
      "price": "80944",
      "size": "26.6666"
    },
    {
      "price": "80933",
      "size": "0.5087"
    },
    {
      "price": "80931",
      "size": "0.0012"
    },
    {
      "price": "80906",
      "size": "71.875"
    },
    {
      "price": "80882",
      "size": "9.6"
    },
    {
      "price": "80869",
      "size": "9.6"
    },
    {
      "price": "80850",
      "size": "3.6741"
    },
    {
      "price": "80849",
      "size": "96.875"
    },
    {
      "price": "80848",
      "size": "65.625"
    },
    {
      "price": "80812",
      "size": "0.02"
    },
    {
      "price": "80808",
      "size": "70.4"
    },
    {
      "price": "80800",
      "size": "333.3705"
    },
    {
      "price": "80797",
      "size": "123.7658"
    },
    {
      "price": "80795",
      "size": "70.4"
    },
    {
      "price": "80791",
      "size": "190.625"
    },
    {
      "price": "80789",
      "size": "123.7784"
    },
    {
      "price": "80788",
      "size": "333.4186"
    },
    {
      "price": "80781",
      "size": "123.791"
    },
    {
      "price": "80775",
      "size": "21.6"
    },
    {
      "price": "80773",
      "size": "123.8037"
    },
    {
      "price": "80764",
      "size": "123.8163"
    }
  ],
  "asks": [
    {
      "price": "82503",
      "size": "0.0605"
    },
    {
      "price": "82506",
      "size": "0.0606"
    },
    {
      "price": "82517",
      "size": "0.1211"
    },
    {
      "price": "82522",
      "size": "0.1802"
    },
    {
      "price": "82533",
      "size": "0.1211"
    },
    {
      "price": "82547",
      "size": "0.2422"
    },
    {
      "price": "82559",
      "size": "4.8068"
    },
    {
      "price": "82560",
      "size": "2.4034"
    },
    {
      "price": "82577",
      "size": "2.4034"
    },
    {
      "price": "82642",
      "size": "4.8068"
    },
    {
      "price": "82644",
      "size": "2.4034"
    },
    {
      "price": "82648",
      "size": "0.0303"
    },
    {
      "price": "82650",
      "size": "0.4202"
    },
    {
      "price": "82660",
      "size": "2.4034"
    },
    {
      "price": "82724",
      "size": "4.8068"
    },
    {
      "price": "82725",
      "size": "3.252"
    },
    {
      "price": "82730",
      "size": "0.8486"
    },
    {
      "price": "82742",
      "size": "2.4034"
    },
    {
      "price": "82783",
      "size": "3.0211"
    },
    {
      "price": "82806",
      "size": "4.8068"
    },
    {
      "price": "82820",
      "size": "4.8068"
    },
    {
      "price": "82871",
      "size": "2.4034"
    },
    {
      "price": "82885",
      "size": "2.4034"
    },
    {
      "price": "82890",
      "size": "2.4034"
    },
    {
      "price": "82902",
      "size": "2.4034"
    },
    {
      "price": "82978",
      "size": "0.0003"
    },
    {
      "price": "83031",
      "size": "0.0774"
    },
    {
      "price": "83055",
      "size": "2.5459"
    },
    {
      "price": "83060",
      "size": "2.5457"
    },
    {
      "price": "83071",
      "size": "2.4087"
    },
    {
      "price": "83078",
      "size": "0.4419"
    },
    {
      "price": "83120",
      "size": "10"
    },
    {
      "price": "83127",
      "size": "0.0243"
    },
    {
      "price": "83137",
      "size": "3.2736"
    },
    {
      "price": "83151",
      "size": "3.2731"
    },
    {
      "price": "83161",
      "size": "0.4721"
    },
    {
      "price": "83168",
      "size": "0.6425"
    },
    {
      "price": "83170",
      "size": "5.0923"
    },
    {
      "price": "83182",
      "size": "0.0001"
    },
    {
      "price": "83184",
      "size": "5.0915"
    },
    {
      "price": "83243",
      "size": "0.1689"
    },
    {
      "price": "83326",
      "size": "0.1853"
    },
    {
      "price": "83353",
      "size": "0.0001"
    },
    {
      "price": "83368",
      "size": "12.7308"
    },
    {
      "price": "83382",
      "size": "12.7287"
    },
    {
      "price": "83408",
      "size": "0.2331"
    },
    {
      "price": "83491",
      "size": "0.2344"
    },
    {
      "price": "83549",
      "size": "1.8"
    },
    {
      "price": "83563",
      "size": "5.55"
    },
    {
      "price": "83573",
      "size": "0.1542"
    },
    {
      "price": "83656",
      "size": "0.1865"
    },
    {
      "price": "83658",
      "size": "8.3334"
    },
    {
      "price": "83732",
      "size": "0.0166"
    },
    {
      "price": "83738",
      "size": "0.2144"
    },
    {
      "price": "83753",
      "size": "12.9166"
    },
    {
      "price": "83764",
      "size": "8.4"
    },
    {
      "price": "83778",
      "size": "8.4"
    },
    {
      "price": "83821",
      "size": "0.2712"
    },
    {
      "price": "83848",
      "size": "17.5"
    },
    {
      "price": "83850",
      "size": "1.2769"
    },
    {
      "price": "83903",
      "size": "0.3546"
    },
    {
      "price": "83931",
      "size": "0.015"
    },
    {
      "price": "83943",
      "size": "22.0834"
    },
    {
      "price": "83978",
      "size": "15"
    },
    {
      "price": "83986",
      "size": "0.1991"
    },
    {
      "price": "83992",
      "size": "15"
    },
    {
      "price": "83999",
      "size": "0.0026"
    },
    {
      "price": "84006",
      "size": "0.1177"
    },
    {
      "price": "84011",
      "size": "0.0098"
    },
    {
      "price": "84014",
      "size": "0.0001"
    },
    {
      "price": "84018",
      "size": "12.5"
    },
    {
      "price": "84038",
      "size": "26.6666"
    },
    {
      "price": "84040",
      "size": "0.0002"
    },
    {
      "price": "84068",
      "size": "0.4897"
    },
    {
      "price": "84075",
      "size": "35.9375"
    },
    {
      "price": "84076",
      "size": "35.9375"
    },
    {
      "price": "84085",
      "size": "9.6"
    },
    {
      "price": "84089",
      "size": "0.1177"
    },
    {
      "price": "84093",
      "size": "0.0098"
    },
    {
      "price": "84099",
      "size": "9.6"
    },
    {
      "price": "84102",
      "size": "3"
    },
    {
      "price": "84113",
      "size": "118.8884"
    },
    {
      "price": "84121",
      "size": "118.8768"
    },
    {
      "price": "84122",
      "size": "0.0003"
    },
    {
      "price": "84129",
      "size": "118.8651"
    },
    {
      "price": "84132",
      "size": "31.25"
    },
    {
      "price": "84133",
      "size": "131.25"
    },
    {
      "price": "84138",
      "size": "118.8535"
    },
    {
      "price": "84146",
      "size": "118.8418"
    },
    {
      "price": "84151",
      "size": "3.5301"
    },
    {
      "price": "84154",
      "size": "118.8302"
    },
    {
      "price": "84160",
      "size": "70.4"
    },
    {
      "price": "84170",
      "size": "333.4186"
    },
    {
      "price": "84174",
      "size": "70.4"
    },
    {
      "price": "84182",
      "size": "333.3705"
    },
    {
      "price": "84191",
      "size": "190.625"
    },
    {
      "price": "84193",
      "size": "21.6"
    },
    {
      "price": "84200",
      "size": "3"
    },
    {
      "price": "84207",
      "size": "21.6"
    },
    {
      "price": "84227",
      "size": "35.8334"
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the bid price for the BTC-USD pair, which directly answers the intent to measure the live bid/ask order book._
