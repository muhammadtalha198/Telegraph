---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-gemini-book
status: approved
captured_at: 2026-10-05T09:27:34Z
request_url: https://api.gemini.com/v1/book/btcusd
content_type: application/json
inputs: |
  {"cb": "BTC-USD", "kraken": "XBTUSD", "kraken_key": "XXBTZUSD", "bitstamp": "btcusd", "okx": "BTC-USDT", "gemini": "btcusd", "bitfinex": "tBTCUSD", "binance": "BTCUSDT", "bybit": "BTCUSDT", "kucoin": "BTC-USDT", "gate": "BTC_USDT", "mexc": "BTCUSDT", "htx": "btcusdt", "cdc": "BTC_USDT", "bitget": "BTCUSDT"}
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must return the live bid/ask order book (depth levels) for the pair asked.
capture_note: |
  golden-test PASS: Gemini
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains bid prices and amounts but lacks the corresponding ask prices and total ask amounts."
reviewed_at: 2026-10-05T12:41:08Z
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
      "price": "85874.89",
      "amount": "0.02328622",
      "timestamp": "1791192437"
    },
    {
      "price": "85864.47",
      "amount": "0.01231433",
      "timestamp": "1791192437"
    },
    {
      "price": "85864.01",
      "amount": "0.06",
      "timestamp": "1791192437"
    },
    {
      "price": "85864.0",
      "amount": "3.0",
      "timestamp": "1791192437"
    },
    {
      "price": "85859.96",
      "amount": "0.03056315",
      "timestamp": "1791192437"
    },
    {
      "price": "85854.98",
      "amount": "0.12225261",
      "timestamp": "1791192437"
    },
    {
      "price": "85835.6",
      "amount": "0.61126304",
      "timestamp": "1791192437"
    },
    {
      "price": "85832.86",
      "amount": "0.12574555",
      "timestamp": "1791192437"
    },
    {
      "price": "85830.0",
      "amount": "3.0",
      "timestamp": "1791192437"
    },
    {
      "price": "85828.78",
      "amount": "0.905832",
      "timestamp": "1791192437"
    },
    {
      "price": "85816.97",
      "amount": "0.139749",
      "timestamp": "1791192437"
    },
    {
      "price": "85815.34",
      "amount": "0.04612337",
      "timestamp": "1791192437"
    },
    {
      "price": "85814.1",
      "amount": "0.06985864",
      "timestamp": "1791192437"
    },
    {
      "price": "85804.97",
      "amount": "0.06918506",
      "timestamp": "1791192437"
    },
    {
      "price": "85782.76",
      "amount": "0.61126305",
      "timestamp": "1791192437"
    },
    {
      "price": "85779.21",
      "amount": "0.06918506",
      "timestamp": "1791192437"
    },
    {
      "price": "85762.13",
      "amount": "0.06918506",
      "timestamp": "1791192437"
    },
    {
      "price": "85743.13",
      "amount": "0.005589",
      "timestamp": "1791192437"
    },
    {
      "price": "85739.43",
      "amount": "0.558803",
      "timestamp": "1791192437"
    },
    {
      "price": "85733.55",
      "amount": "7.940636",
      "timestamp": "1791192437"
    },
    {
      "price": "85731.13",
      "amount": "0.01814698",
      "timestamp": "1791192437"
    },
    {
      "price": "85728.2",
      "amount": "0.16300348",
      "timestamp": "1791192437"
    },
    {
      "price": "85718.22",
      "amount": "0.12574555",
      "timestamp": "1791192437"
    },
    {
      "price": "85716.99",
      "amount": "0.00001746",
      "timestamp": "1791192437"
    },
    {
      "price": "85708.7",
      "amount": "0.48",
      "timestamp": "1791192437"
    },
    {
      "price": "85698.64",
      "amount": "0.46123379",
      "timestamp": "1791192437"
    },
    {
      "price": "85634.07",
      "amount": "0.005589",
      "timestamp": "1791192437"
    },
    {
      "price": "85632.33",
      "amount": "1.38320095",
      "timestamp": "1791192437"
    },
    {
      "price": "85613.81",
      "amount": "0.46123379",
      "timestamp": "1791192437"
    },
    {
      "price": "85604.92",
      "amount": "0.46123379",
      "timestamp": "1791192437"
    },
    {
      "price": "85599.1",
      "amount": "0.00058295",
      "timestamp": "1791192437"
    },
    {
      "price": "85585.71",
      "amount": "0.68694323",
      "timestamp": "1791192437"
    },
    {
      "price": "85568.28",
      "amount": "0.46123379",
      "timestamp": "1791192437"
    },
    {
      "price": "85555.0",
      "amount": "0.0002922",
      "timestamp": "1791192437"
    },
    {
      "price": "85549.3",
      "amount": "0.49",
      "timestamp": "1791192437"
    },
    {
      "price": "85531.92",
      "amount": "0.09542191",
      "timestamp": "1791192437"
    },
    {
      "price": "85522.03",
      "amount": "0.000465",
      "timestamp": "1791192437"
    },
    {
      "price": "85500.0",
      "amount": "1.0017373",
      "timestamp": "1791192437"
    },
    {
      "price": "85382.4",
      "amount": "3.5153232",
      "timestamp": "1791192437"
    },
    {
      "price": "85382.0",
      "amount": "0.00067989",
      "timestamp": "1791192437"
    },
    {
      "price": "85346.41",
      "amount": "1.22252609",
      "timestamp": "1791192437"
    },
    {
      "price": "85333.0",
      "amount": "0.00029296",
      "timestamp": "1791192437"
    },
    {
      "price": "85330.0",
      "amount": "0.00117192",
      "timestamp": "1791192437"
    },
    {
      "price": "85308.69",
      "amount": "0.00001755",
      "timestamp": "1791192437"
    },
    {
      "price": "85300.0",
      "amount": "0.00023",
      "timestamp": "1791192437"
    },
    {
      "price": "85282.72",
      "amount": "0.00001755",
      "timestamp": "1791192437"
    },
    {
      "price": "85268.64",
      "amount": "0.00025167",
      "timestamp": "1791192437"
    },
    {
      "price": "85222.0",
      "amount": "0.00029335",
      "timestamp": "1791192437"
    },
    {
      "price": "85148.15",
      "amount": "0.00005866",
      "timestamp": "1791192437"
    },
    {
      "price": "85111.0",
      "amount": "0.00029373",
      "timestamp": "1791192437"
    }
  ],
  "asks": [
    {
      "price": "85874.9",
      "amount": "0.04860843",
      "timestamp": "1791192437"
    },
    {
      "price": "85876.15",
      "amount": "0.03493379",
      "timestamp": "1791192437"
    },
    {
      "price": "85876.18",
      "amount": "0.05822586",
      "timestamp": "1791192437"
    },
    {
      "price": "85879.35",
      "amount": "0.12225261",
      "timestamp": "1791192437"
    },
    {
      "price": "85886.0",
      "amount": "3.0",
      "timestamp": "1791192437"
    },
    {
      "price": "85900.67",
      "amount": "0.00032416",
      "timestamp": "1791192437"
    },
    {
      "price": "85900.85",
      "amount": "0.61126304",
      "timestamp": "1791192437"
    },
    {
      "price": "85904.86",
      "amount": "0.12574555",
      "timestamp": "1791192437"
    },
    {
      "price": "85909.68",
      "amount": "0.870478",
      "timestamp": "1791192437"
    },
    {
      "price": "85917.84",
      "amount": "0.00038899",
      "timestamp": "1791192437"
    },
    {
      "price": "85920.0",
      "amount": "3.0",
      "timestamp": "1791192437"
    },
    {
      "price": "85926.5",
      "amount": "0.6",
      "timestamp": "1791192437"
    },
    {
      "price": "85932.44",
      "amount": "0.06918506",
      "timestamp": "1791192437"
    },
    {
      "price": "85935.02",
      "amount": "0.00046679",
      "timestamp": "1791192437"
    },
    {
      "price": "85945.89",
      "amount": "0.61126305",
      "timestamp": "1791192437"
    },
    {
      "price": "85947.87",
      "amount": "0.139696",
      "timestamp": "1791192437"
    },
    {
      "price": "85950.36",
      "amount": "0.06918506",
      "timestamp": "1791192437"
    },
    {
      "price": "85952.19",
      "amount": "0.00056014",
      "timestamp": "1791192437"
    },
    {
      "price": "85958.2",
      "amount": "0.06918506",
      "timestamp": "1791192437"
    },
    {
      "price": "85969.37",
      "amount": "0.00067217",
      "timestamp": "1791192437"
    },
    {
      "price": "85975.89",
      "amount": "0.12574555",
      "timestamp": "1791192437"
    },
    {
      "price": "85991.44",
      "amount": "0.005589",
      "timestamp": "1791192437"
    },
    {
      "price": "85998.19",
      "amount": "5.226988",
      "timestamp": "1791192437"
    },
    {
      "price": "86020.37",
      "amount": "0.46123379",
      "timestamp": "1791192437"
    },
    {
      "price": "86022.3",
      "amount": "0.32",
      "timestamp": "1791192437"
    },
    {
      "price": "86061.78",
      "amount": "1.38320095",
      "timestamp": "1791192437"
    },
    {
      "price": "86093.63",
      "amount": "0.46123379",
      "timestamp": "1791192437"
    },
    {
      "price": "86100.3",
      "amount": "0.005588",
      "timestamp": "1791192437"
    },
    {
      "price": "86100.76",
      "amount": "0.68694323",
      "timestamp": "1791192437"
    },
    {
      "price": "86111.0",
      "amount": "0.46123379",
      "timestamp": "1791192437"
    },
    {
      "price": "86167.98",
      "amount": "0.46123379",
      "timestamp": "1791192437"
    },
    {
      "price": "86223.0",
      "amount": "0.69813733",
      "timestamp": "1791192437"
    },
    {
      "price": "86223.01",
      "amount": "0.55348054",
      "timestamp": "1791192437"
    },
    {
      "price": "86233.09",
      "amount": "0.000465",
      "timestamp": "1791192437"
    },
    {
      "price": "86241.0",
      "amount": "0.04",
      "timestamp": "1791192437"
    },
    {
      "price": "86325.55",
      "amount": "0.04",
      "timestamp": "1791192437"
    },
    {
      "price": "86342.2",
      "amount": "1.22252609",
      "timestamp": "1791192437"
    },
    {
      "price": "86361.33",
      "amount": "3.5153232",
      "timestamp": "1791192437"
    },
    {
      "price": "86362.82",
      "amount": "0.55348054",
      "timestamp": "1791192437"
    },
    {
      "price": "86461.87",
      "amount": "0.00005081",
      "timestamp": "1791192437"
    },
    {
      "price": "86670.58",
      "amount": "0.55348054",
      "timestamp": "1791192437"
    },
    {
      "price": "86739.0",
      "amount": "0.29994293",
      "timestamp": "1791192437"
    },
    {
      "price": "86744.0",
      "amount": "0.3",
      "timestamp": "1791192437"
    },
    {
      "price": "86748.3",
      "amount": "0.2",
      "timestamp": "1791192437"
    },
    {
      "price": "86750.0",
      "amount": "0.1",
      "timestamp": "1791192437"
    },
    {
      "price": "86808.4",
      "amount": "0.55348054",
      "timestamp": "1791192437"
    },
    {
      "price": "86832.85",
      "amount": "0.2",
      "timestamp": "1791192437"
    },
    {
      "price": "86980.0",
      "amount": "0.21896192",
      "timestamp": "1791192437"
    },
    {
      "price": "86997.63",
      "amount": "0.00002347",
      "timestamp": "1791192437"
    },
    {
      "price": "87000.0",
      "amount": "1.61656703",
      "timestamp": "1791192437"
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains bid prices and amounts but lacks the corresponding ask prices and total ask amounts._
