---
intent: OPTIMAL_EXECUTION_ROUTE
slug: route-paraswap-usdt
status: approved
captured_at: 2026-10-04T18:41:02Z
request_url: https://apiv5.paraswap.io/prices?srcToken=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&destToken=0xdAC17F958D2ee523a2206206994597C13D831ec7&amount=1000000000000000000&srcDecimals=18&destDecimals=6&side=SELL&network=1
content_type: application/json
inputs: |
  1 ETH->USDT
intent_description: |
  Determines optimal multi-venue order execution routing to minimize slippage, exchange fees, and market impact.
answer_requirement: |
  Must convey the best swap route / output amount for the trade asked.
capture_note: |
  NEW
reviewer_note: "auto_review: [0.85|heuristic] Swap route / price route present"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "priceRoute": {
    "blockNumber": 26120848,
    "network": 1,
    "srcToken": "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
    "srcDecimals": 18,
    "srcAmount": "1000000000000000000",
    "destToken": "0xdac17f958d2ee523a2206206994597c13d831ec7",
    "destDecimals": 6,
    "destAmount": "2701169391",
    "bestRoute": [
      {
        "percent": 100,
        "swaps": [
          {
            "srcToken": "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            "srcDecimals": 18,
            "destToken": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "destDecimals": 6,
            "swapExchanges": [
              {
                "exchange": "uniswapv3",
                "srcAmount": "1000000000000000000",
                "destAmount": "2700873854",
                "percent": 100,
                "poolAddresses": [
                  "0xe0554a476a092703abdb3ef35c80e0d76d32939f"
                ],
                "poolIdentifiers": [
                  "uniswapv3_0xe0554a476a092703abdb3ef35c80e0d76d32939f"
                ],
                "targetExchange": "0xe592427a0aece92de3edee1f18e0157c05861564",
                "data": {
                  "apiGo": true,
                  "blockNumber": 26120848,
                  "source": "L1",
                  "path": [
                    {
                      "tokenIn": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
                      "tokenOut": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                      "fee": "100",
                      "currentFee": "100"
                    }
                  ],
                  "gasUSD": "0.034645"
                }
              }
            ]
          },
          {
            "srcToken": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "srcDecimals": 6,
            "destToken": "0xdac17f958d2ee523a2206206994597c13d831ec7",
            "destDecimals": 6,
            "swapExchanges": [
              {
                "exchange": "curvev1stableng",
                "srcAmount": "2700873854",
                "destAmount": "2701169391",
                "percent": 100,
                "poolAddresses": [
                  "0x4f493b7de8aac7d55f71853688b1f7c8f0243c85"
                ],
                "poolIdentifiers": [
                  "curvev1stableng_0x4f493b7de8aac7d55f71853688b1f7c8f0243c85"
                ],
                "data": {
                  "apiGo": true,
                  "blockNumber": 26120797,
                  "source": "L1",
                  "coins": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48,0xdac17f958d2ee523a2206206994597c13d831ec7",
                  "exchange": "0x4f493b7de8aac7d55f71853688b1f7c8f0243c85",
                  "i": "0",
                  "j": "1",
                  "path": [
                    {
                      "exchange": "0x4f493b7de8aac7d55f71853688b1f7c8f0243c85",
                      "i": 0,
                      "j": 1,
                      "n_coins": 2,
                      "tokenIn": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                      "tokenOut": "0xdac17f958d2ee523a2206206994597c13d831ec7",
                      "underlyingSwap": false
                    }
                  ],
                  "gasUSD": "0.069289"
                }
              }
            ]
          }
        ]
      }
    ],
    "gasCostUSD": "0.137296",
    "gasCost": "396300",
    "side": "SELL",
    "version": "5",
    "contractAddress": "0xDEF171Fe48CF0115B1d80b88dc8eAB59176FEe57",
    "tokenTransferProxy": "0x216b4b4ba9f3e719726886d34a177484278bfcae",
    "contractMethod": "multiSwap",
    "partnerFee": 0.01,
    "srcUSD": "2700.7900000000",
    "destUSD": "2700.8209401486",
    "destAmountAfterFee": "2700899274",
    "partner": "anon",
    "maxImpactReached": false,
    "hmac": "8aab68b44fd78db244031281fb9f60b3a2bfa530"
  }
}
```

## Why this matches (or not)

_[0.85|heuristic] Swap route / price route present_
