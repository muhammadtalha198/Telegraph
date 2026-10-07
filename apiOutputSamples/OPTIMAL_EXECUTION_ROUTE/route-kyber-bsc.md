---
intent: OPTIMAL_EXECUTION_ROUTE
slug: route-kyber-bsc
status: approved
captured_at: 2026-10-04T18:41:01Z
request_url: https://aggregator-api.kyberswap.com/bsc/api/v1/routes?tokenIn=0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c&tokenOut=0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d&amountIn=1000000000000000000
content_type: application/json
inputs: |
  1 WBNB->USDC bsc
intent_description: |
  Determines optimal multi-venue order execution routing to minimize slippage, exchange fees, and market impact.
answer_requirement: |
  Must convey the best swap route / output amount for the trade asked.
capture_note: |
  NEW smoke-candidate
reviewer_note: "auto_review: [0.85|heuristic] Swap route / price route present"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "code": 0,
  "message": "successfully",
  "data": {
    "routeSummary": {
      "tokenIn": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
      "amountIn": "1000000000000000000",
      "amountInUsd": "788.7428656802747",
      "tokenOut": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
      "amountOut": "788769935899877798350",
      "amountOutUsd": "788.6537758622045",
      "gas": "642998",
      "gasPrice": "50000000",
      "gasUsd": "0.025358004257334265",
      "l1FeeUsd": "0",
      "extraFee": {
        "feeAmount": "",
        "chargeFeeBy": "",
        "isInBps": false,
        "feeReceiver": ""
      },
      "route": [
        [
          {
            "pool": "0x1166de8bc61fff4ea279d68bcb08293614e4d8fc",
            "tokenIn": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
            "tokenOut": "0x55d398326f99059ff775485246999027b3197955",
            "swapAmount": "1000000000000000000",
            "amountOut": "788878155107312379408",
            "exchange": "metric-propamm/kipseli-prop",
            "poolType": "metric-propamm",
            "poolExtra": {
              "swapDir": true,
              "priceProvider": "",
              "blockNumber": 125725953
            },
            "extra": {
              "_ce": {
                "prCnt": 1,
                "tgtAmtOut": "788878155107312379408",
                "ces": [
                  {
                    "pool": "0x172fcd41e0913e95784454622d1c3724f546f849",
                    "tokenIn": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
                    "tokenOut": "0x55d398326f99059ff775485246999027b3197955",
                    "swapAmount": "1000000000000000000",
                    "amountOut": "788793508559330429187",
                    "exchange": "pancake-v3",
                    "poolType": "pancake-v3",
                    "poolExtra": {
                      "swapFee": 100,
                      "priceLimit": "1461446703485210103287273052203988822378723970341",
                      "blockNumber": 125725970
                    },
                    "extra": {
                      "rAI": "0",
                      "nSqrtRx96": "2820834652236786896338730532",
                      "nT": -66710
                    }
                  },
                  {
                    "pool": "kipseli-prop_0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c_0x55d398326f99059ff775485246999027b3197955",
                    "tokenIn": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
                    "tokenOut": "0x55d398326f99059ff775485246999027b3197955",
                    "swapAmount": "1000000000000000000",
                    "amountOut": "788866126066186452992",
                    "exchange": "kipseli-prop",
                    "poolType": "kipseli-prop",
                    "poolExtra": {
                      "blockNumber": 125725967,
                      "routerAddress": "0x4cb2140c29518db6203f661b9f6dd60b68bb7f0d",
                      "approvalAddress": "0x4cb2140c29518db6203f661b9f6dd60b68bb7f0d"
                    },
                    "extra": null
                  }
                ]
              },
              "_cs": "7534836556863725877",
              "_fr": {
                "amountOut": "788757908607607466167",
                "amountOutUsd": 788.6417503411612
              },
              "_fs": {
                "pool": "kipseli-prop_0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c_0x55d398326f99059ff775485246999027b3197955",
                "tokenIn": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
                "tokenOut": "0x55d398326f99059ff775485246999027b3197955",
                "swapAmount": "1000000000000000000",
                "amountOut": "788866126066186452992",
                "exchange": "kipseli-prop",
                "poolType": "kipseli-prop",
                "poolExtra": {
                  "blockNumber": 125725967,
                  "routerAddress": "0x4cb2140c29518db6203f661b9f6dd60b68bb7f0d",
                  "approvalAddress": "0x4cb2140c29518db6203f661b9f6dd60b68bb7f0d"
                },
                "extra": null
              },
              "_ts": "1791139261",
              "ri": "95dc36a2X85EfoKg"
            }
          },
          {
            "pool": "0x32a805e65a3219a79707ab3e75443d75160d798de46613fc960d39cd4a96bb22",
            "tokenIn": "0x55d398326f99059ff775485246999027b3197955",
            "tokenOut": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
            "swapAmount": "788878155107312379408",
            "amountOut": "788769935899877798350",
            "exchange": "pancake-infinity-cl",
            "poolType": "pancake-infinity-cl",
            "poolExtra": {
              "blockNumber": 125725968,
              "vault": "0x238a358808379702088667322f80ac48bad5e6c4",
              "poolManager": "0xa0ffb9c1ce1fe56963b0321b32e7a0302114058b",
              "permit2Addr": "0x31c2f6fcff4f8759b3bd5bf0e1084a055615c768",
              "tokenIn": "0x55d398326f99059ff775485246999027b3197955",
              "tokenOut": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
              "fee": 1,
              "parameters": "0x0000000000000000000000000000000000000000000000000000000000010000",
              "hookAddress": "0x0000000000000000000000000000000000000000",
              "hookData": "",
              "priceLimit": "4295128740",
              "swapFee": 2
            },
            "extra": {
              "HookSwapInfo": null,
              "_ss": {
                "pool": "0x0b1a513ee24972daef112bc777a5610d4325c9e7",
                "tokenIn": "0x55d398326f99059ff775485246999027b3197955",
                "tokenOut": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
                "swapAmount": "788878155107312379408",
                "amountOut": "788755291258665000000",
                "exchange": "fluid-dex-t1",
                "poolType": "fluid-dex-t1",
                "poolExtra": {
                  "blockNumber": 125725969,
                  "approvalAddress": "0x0b1a513ee24972daef112bc777a5610d4325c9e7"
                },
                "extra": {
                  "hasNative": false
                }
              },
              "nSqrtRx96": "79222482184984782658314503831",
              "nT": -2,
              "rAI": "0"
            }
          }
        ]
      ],
      "routerAddress": "0x6131B5fae19EA4f9D964eAc0408E4408b66337b5",
      "routeID": "95dc36a2X85EfoKg",
      "checksum": "7534836556863725877",
      "timestamp": 1791139261
    },
    "routerAddress": "0x6131B5fae19EA4f9D964eAc0408E4408b66337b5"
  },
  "requestId": "95dc36a2-5fce-447e-82a0-1835b2ac97a6"
}
```

## Why this matches (or not)

_[0.85|heuristic] Swap route / price route present_
