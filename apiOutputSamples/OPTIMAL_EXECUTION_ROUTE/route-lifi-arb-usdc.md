---
intent: OPTIMAL_EXECUTION_ROUTE
slug: route-lifi-arb-usdc
status: approved
captured_at: 2026-10-04T18:41:04Z
request_url: https://li.quest/v1/quote?fromChain=1&toChain=42161&fromToken=ETH&toToken=USDC&fromAmount=1000000000000000000&fromAddress=0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
content_type: application/json
inputs: |
  1 ETH eth->USDC arb
intent_description: |
  Determines optimal multi-venue order execution routing to minimize slippage, exchange fees, and market impact.
answer_requirement: |
  Must convey the best swap route / output amount for the trade asked.
capture_note: |
  cross-chain route quote
reviewer_note: "auto_review: [0.85|heuristic] Route quote output amount present"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "type": "lifi",
  "id": "f5f60983-01f7-43af-a37a-52770fb58f8f:0",
  "tool": "celercircle",
  "toolDetails": {
    "key": "celercircle",
    "name": "CCTP + Celer (Standard)",
    "logoURI": "https://raw.githubusercontent.com/lifinance/types/main/src/assets/icons/bridges/circle.svg"
  },
  "action": {
    "fromToken": {
      "address": "0x0000000000000000000000000000000000000000",
      "chainId": 1,
      "symbol": "ETH",
      "decimals": 18,
      "name": "ETH",
      "coinKey": "ETH",
      "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/logo.png",
      "priceUSD": "2700.87",
      "tags": [
        "major_asset"
      ],
      "verificationStatus": "verified",
      "verificationStatusBreakdown": [
        {
          "provider": "hypernative",
          "result": "verified",
          "providerResult": "accept"
        }
      ]
    },
    "fromAmount": "1000000000000000000",
    "toToken": {
      "address": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
      "chainId": 42161,
      "symbol": "USDC",
      "decimals": 6,
      "name": "USD Coin",
      "coinKey": "USDC",
      "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48/logo.png",
      "priceUSD": "1.0004912682",
      "tags": [
        "stablecoin"
      ],
      "verificationStatus": "verified",
      "verificationStatusBreakdown": [
        {
          "provider": "hypernative",
          "result": "verified",
          "providerResult": "accept"
        }
      ]
    },
    "fromChainId": 1,
    "toChainId": 42161,
    "slippage": 0.005,
    "fromAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "toAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
  },
  "estimate": {
    "tool": "celercircle",
    "approvalAddress": "0x1231DEB6f5749EF6cE6943a275A1D3E7486F4EaE",
    "toAmountMin": "2680551143",
    "toAmount": "2694021249",
    "fromAmount": "1000000000000000000",
    "feeCosts": [
      {
        "name": "LIFI Fixed Fee",
        "description": "Fixed LIFI fee, independent of any other fee",
        "token": {
          "address": "0x0000000000000000000000000000000000000000",
          "chainId": 1,
          "symbol": "ETH",
          "decimals": 18,
          "name": "ETH",
          "coinKey": "ETH",
          "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/logo.png",
          "priceUSD": "2700.87",
          "tags": [
            "major_asset"
          ],
          "verificationStatus": "verified",
          "verificationStatusBreakdown": [
            {
              "provider": "hypernative",
              "result": "verified",
              "providerResult": "accept"
            }
          ]
        },
        "amount": "2500000000000000",
        "amountUSD": "6.7522",
        "percentage": "0.0025",
        "included": true,
        "feeSplit": {
          "lifiFee": "2500000000000000",
          "integratorFee": "0",
          "recipients": [
            {
              "name": "lifi",
              "type": "FIXED",
              "fee": "2500000000000000"
            }
          ]
        }
      },
      {
        "name": "Transaction Fee",
        "description": "Transaction Fee is used to cover the gas cost for sending your transfer on the destination chain.",
        "token": {
          "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
          "chainId": 1,
          "symbol": "USDC",
          "decimals": 6,
          "name": "USD Coin",
          "coinKey": "USDC",
          "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48/logo.png",
          "priceUSD": "1.0001085997",
          "tags": [
            "stablecoin"
          ],
          "verificationStatus": "verified",
          "verificationStatusBreakdown": [
            {
              "provider": "hypernative",
              "result": "verified",
              "providerResult": "accept"
            }
          ]
        },
        "amount": "100000",
        "amountUSD": "0.1000",
        "percentage": "0.0000",
        "included": true
      }
    ],
    "gasCosts": [
      {
        "type": "SEND",
        "price": "140787609",
        "estimate": "569811",
        "limit": "740754",
        "amount": "80222328271899",
        "amountUSD": "0.2167",
        "token": {
          "address": "0x0000000000000000000000000000000000000000",
          "chainId": 1,
          "symbol": "ETH",
          "decimals": 18,
          "name": "ETH",
          "coinKey": "ETH",
          "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/logo.png",
          "priceUSD": "2700.87",
          "tags": [
            "major_asset"
          ],
          "verificationStatus": "verified",
          "verificationStatusBreakdown": [
            {
              "provider": "hypernative",
              "result": "verified",
              "providerResult": "accept"
            }
          ]
        }
      }
    ],
    "executionDuration": 964,
    "fromAmountUSD": "2700.8700",
    "toAmountUSD": "2695.3447",
    "skipApproval": true
  },
  "includedSteps": [
    {
      "id": "6ad364cc-3d40-4a8e-b46a-53e9d711b2d7",
      "type": "protocol",
      "action": {
        "fromChainId": 1,
        "fromAmount": "1000000000000000000",
        "fromToken": {
          "address": "0x0000000000000000000000000000000000000000",
          "chainId": 1,
          "symbol": "ETH",
          "decimals": 18,
          "name": "ETH",
          "coinKey": "ETH",
          "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/logo.png",
          "priceUSD": "2700.87",
          "tags": [
            "major_asset"
          ],
          "verificationStatus": "verified",
          "verificationStatusBreakdown": [
            {
              "provider": "hypernative",
              "result": "verified",
              "providerResult": "accept"
            }
          ]
        },
        "toChainId": 1,
        "toToken": {
          "address": "0x0000000000000000000000000000000000000000",
          "chainId": 1,
          "symbol": "ETH",
          "decimals": 18,
          "name": "ETH",
          "coinKey": "ETH",
          "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/logo.png",
          "priceUSD": "2700.87",
          "tags": [
            "major_asset"
          ],
          "verificationStatus": "verified",
          "verificationStatusBreakdown": [
            {
              "provider": "hypernative",
              "result": "verified",
              "providerResult": "accept"
            }
          ]
        },
        "slippage": 0.005,
        "fromAddress": "0x1231DEB6f5749EF6cE6943a275A1D3E7486F4EaE",
        "toAddress": "0x1231DEB6f5749EF6cE6943a275A1D3E7486F4EaE",
        "jitoBundle": false,
        "integratorFees": {
          "feePercent": 0.0025,
          "sourceAmount": {
            "s": 1,
            "e": 18,
            "c": [
              10000
            ]
          },
          "totalFee": {
            "s": 1,
            "e": 15,
            "c": [
              25
            ]
          },
          "recipients": [
            {
              "name": "lifi",
              "type": "FIXED",
              "fee": {
                "s": 1,
                "e": 15,
                "c": [
                  25
                ]
              }
            }
          ]
        }
      },
      "estimate": {
        "fromAmount": "1000000000000000000",
        "toAmount": "997500000000000000",
        "toAmountMin": "997500000000000000",
        "tool": "feeCollection",
        "approvalAddress": "0xCE40449B773a3E6E5e769ADb4e567179d4828cbd",
        "gasCosts": [
          {
            "type": "SEND",
            "price": "140787609",
            "estimate": "100000",
            "limit": "130000",
            "amount": "14078760900000",
            "amountUSD": "0.0380",
            "token": {
              "address": "0x0000000000000000000000000000000000000000",
              "chainId": 1,
              "symbol": "ETH",
              "decimals": 18,
              "name": "ETH",
              "coinKey": "ETH",
              "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/logo.png",
              "priceUSD": "2700.87",
              "tags": [
                "major_asset"
              ],
              "verificationStatus": "verified",
              "verificationStatusBreakdown": [
                {
                  "provider": "hypernative",
                  "result": "verified",
                  "providerResult": "accept"
                }
              ]
            }
          }
        ],
        "feeCosts": [
          {
            "name": "LIFI Fixed Fee",
            "description": "Fixed LIFI fee, independent of any other fee",
            "token": {
              "address": "0x0000000000000000000000000000000000000000",
              "chainId": 1,
              "symbol": "ETH",
              "decimals": 18,
              "name": "ETH",
              "coinKey": "ETH",
              "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/logo.png",
              "priceUSD": "2700.87",
              "tags": [
                "major_asset"
              ],
              "verificationStatus": "verified",
              "verificationStatusBreakdown": [
                {
                  "provider": "hypernative",
                  "result": "verified",
                  "providerResult": "accept"
                }
              ]
            },
            "amount": "2500000000000000",
            "amountUSD": "6.7522",
            "percentage": "0.0025",
            "included": true,
            "feeSplit": {
              "lifiFee": "2500000000000000",
              "integratorFee": "0",
              "recipients": [
                {
                  "name": "lifi",
                  "type": "FIXED",
                  "fee": "2500000000000000"
                }
              ]
            }
          }
        ],
        "executionDuration": 0
      },
      "tool": "feeCollection",
      "toolDetails": {
        "key": "feeCollection",
        "name": "Integrator Fee",
        "logoURI": "https://raw.githubusercontent.com/lifinance/types/main/src/assets/icons/protocols/feeCollection.svg"
      }
    },
    {
      "id": "0187af65-7b23-41c0-b5a6-31af866ab6bb",
      "type": "swap",
      "action": {
        "fromChainId": 1,
        "fromAmount": "997500000000000000",
        "fromToken": {
          "address": "0x0000000000000000000000000000000000000000",
          "chainId": 1,
          "symbol": "ETH",
          "decimals": 18,
          "name": "ETH",
          "coinKey": "ETH",
          "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/logo.png",
          "priceUSD": "2700.87",
          "tags": [
            "major_asset"
          ],
          "verificationStatus": "verified",
          "verificationStatusBreakdown": [
            {
              "provider": "hypernative",
              "result": "verified",
              "providerResult": "accept"
            }
          ]
        },
        "toChainId": 1,
        "toToken": {
          "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
          "chainId": 1,
          "symbol": "USDC",
          "decimals": 6,
          "name": "USD Coin",
          "coinKey": "USDC",
          "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48/logo.png",
          "priceUSD": "1.0001085997",
          "tags": [
            "stablecoin"
          ],
          "verificationStatus": "verified",
          "verificationStatusBreakdown": [
            {
              "provider": "hypernative",
              "result": "verified",
              "providerResult": "accept"
            }
          ]
        },
        "slippage": 0.005,
        "fromAddress": "0x1231DEB6f5749EF6cE6943a275A1D3E7486F4EaE",
        "toAddress": "0x1231DEB6f5749EF6cE6943a275A1D3E7486F4EaE",
        "jitoBundle": false,
        "integratorFees": {
          "feePercent": 0.0025,
          "sourceAmount": {
            "s": 1,
            "e": 18,
            "c": [
              10000
            ]
          },
          "totalFee": {
            "s": 1,
            "e": 15,
            "c": [
              25
            ]
          },
          "recipients": [
            {
              "name": "lifi",
              "type": "FIXED",
              "fee": {
                "s": 1,
                "e": 15,
                "c": [
                  25
                ]
              }
            }
          ]
        }
      },
      "estimate": {
        "tool": "bitget",
        "fromAmount": "997500000000000000",
        "toAmount": "2694121752",
        "toAmountMin": "2680651143",
        "approvalAddress": "0xbc1d9760bd6ca468ca9fb5ff2cfbeac35d86c973",
        "executionDuration": 0,
        "feeCosts": [],
        "gasCosts": [
          {
            "type": "SEND",
            "price": "140787609",
            "estimate": "1100000",
            "limit": "1430000",
            "amount": "154866369900000",
            "amountUSD": "0.4183",
            "token": {
              "address": "0x0000000000000000000000000000000000000000",
              "chainId": 1,
              "symbol": "ETH",
              "decimals": 18,
              "name": "ETH",
              "coinKey": "ETH",
              "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/logo.png",
              "priceUSD": "2700.87",
              "tags": [
                "major_asset"
              ],
              "verificationStatus": "verified",
              "verificationStatusBreakdown": [
                {
                  "provider": "hypernative",
                  "result": "verified",
                  "providerResult": "accept"
                }
              ]
            }
          }
        ]
      },
      "tool": "bitget",
      "toolDetails": {
        "key": "bitget",
        "name": "Bitget",
        "logoURI": "https://raw.githubusercontent.com/lifinance/types/main/src/assets/icons/exchanges/bitget.svg"
      }
    },
    {
      "id": "7e36715c-7250-4d5d-b25c-bf04b15ac13d",
      "type": "cross",
      "action": {
        "fromChainId": 1,
        "fromAmount": "2694121752",
        "fromToken": {
          "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
          "chainId": 1,
          "symbol": "USDC",
          "decimals": 6,
          "name": "USD Coin",
          "coinKey": "USDC",
          "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48/logo.png",
          "priceUSD": "1.0001085997",
          "tags": [
            "stablecoin"
          ],
          "verificationStatus": "verified",
          "verificationStatusBreakdown": [
            {
              "provider": "hypernative",
              "result": "verified",
              "providerResult": "accept"
            }
          ]
        },
        "toChainId": 42161,
        "toToken": {
          "address": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
          "chainId": 42161,
          "symbol": "USDC",
          "decimals": 6,
          "name": "USD Coin",
          "coinKey": "USDC",
          "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48/logo.png",
          "priceUSD": "1.0004912682",
          "tags": [
            "stablecoin"
          ],
          "verificationStatus": "verified",
          "verificationStatusBreakdown": [
            {
              "provider": "hypernative",
              "result": "verified",
              "providerResult": "accept"
            }
          ]
        },
        "slippage": 0.005,
        "fromAddress": "0x1231DEB6f5749EF6cE6943a275A1D3E7486F4EaE",
        "toAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
        "jitoBundle": false,
        "integratorFees": {
          "feePercent": 0.0025,
          "sourceAmount": {
            "s": 1,
            "e": 18,
            "c": [
              10000
            ]
          },
          "totalFee": {
            "s": 1,
            "e": 15,
            "c": [
              25
            ]
          },
          "recipients": [
            {
              "name": "lifi",
              "type": "FIXED",
              "fee": {
                "s": 1,
                "e": 15,
                "c": [
                  25
                ]
              }
            }
          ]
        },
        "destinationGasConsumption": "0"
      },
      "estimate": {
        "tool": "celercircle",
        "fromAmount": "2680651143",
        "toAmount": "2694021249",
        "toAmountMin": "2680551143",
        "approvalAddress": "0xc75fdd24820ddcdadee9bb653ae6cd73ba8f0e80",
        "executionDuration": 964,
        "feeCosts": [
          {
            "name": "Transaction Fee",
            "description": "Transaction Fee is used to cover the gas cost for sending your transfer on the destination chain.",
            "token": {
              "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
              "chainId": 1,
              "symbol": "USDC",
              "decimals": 6,
              "name": "USD Coin",
              "coinKey": "USDC",
              "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48/logo.png",
              "priceUSD": "1.0001085997",
              "tags": [
                "stablecoin"
              ],
              "verificationStatus": "verified",
              "verificationStatusBreakdown": [
                {
                  "provider": "hypernative",
                  "result": "verified",
                  "providerResult": "accept"
                }
              ]
            },
            "amount": "100000",
            "amountUSD": "0.1000",
            "percentage": "0.0000",
            "included": true
          }
        ],
        "gasCosts": [
          {
            "type": "SEND",
            "price": "140787609",
            "estimate": "163000",
            "limit": "211900",
            "amount": "22948380267000",
            "amountUSD": "0.0620",
            "token": {
              "address": "0x0000000000000000000000000000000000000000",
              "chainId": 1,
              "symbol": "ETH",
              "decimals": 18,
              "name": "ETH",
              "coinKey": "ETH",
              "logoURI": "https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/ethereum/assets/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/logo.png",
              "priceUSD": "2700.87",
              "tags": [
                "major_asset"
              ],
              "verificationStatus": "verified",
              "verificationStatusBreakdown": [
                {
                  "provider": "hypernative",
                  "result": "verified",
                  "providerResult": "accept"
                }
              ]
            }
          }
        ]
      },
      "tool": "celercircle",
      "toolDetails": {
        "key": "celercircle",
        "name": "CCTP + Celer (Standard)",
        "logoURI": "https://raw.githubusercontent.com/lifinance/types/main/src/assets/icons/bridges/circle.svg"
      }
    }
  ],
  "integrator": "lifi-api",
  "stepSimulation": {
    "status": "success",
    "gasSource": "simulation"
  },
  "transactionRequest": {
    "value": "0xde0b6b3a7640000",
    "to": "0x1231DEB6f5749EF6cE6943a275A1D3E7486F4EaE",
    "data": "0x4f3b075900000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000240000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007d0f04d08566eb84a038338a9ab11173a46d05a6136b6fd9fa16420737469ee6b8e000000000000000000000000000000000000000000000000000000000000014000000000000000000000000000000000000000000000000000000000000001800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48000000000000000000000000d8da6bf26964af9d7eed9e03e53415d37aa96045000000000000000000000000000000000000000000000000000000009fc77d87000000000000000000000000000000000000000000000000000000000000a4b100000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000b63656c6572636972636c6500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000086c6966692d6170690000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000001e0000000000000000000000000ce40449b773a3e6e5e769adb4e567179d4828cbd000000000000000000000000ce40449b773a3e6e5e769adb4e567179d4828cbd000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000de0b6b3a764000000000000000000000000000000000000000000000000000000000000000000e0000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000840e8ae67f00000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000001000000000000000000000000c06ebbefd94032b85424d51906e2a335efae264b0000000000000000000000000000000000000000000000000008e1bc9bf0400000000000000000000000000000000000000000000000000000000000000000000000000000000000bc1d9760bd6ca468ca9fb5ff2cfbeac35d86c973000000000000000000000000bc1d9760bd6ca468ca9fb5ff2cfbeac35d86c9730000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a0b86991c6218b36c1d19d4a2e9eb0ce3606eb480000000000000000000000000000000000000000000000000dd7d4f70b73c00000000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000604d984396a000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000002e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a0b86991c6218b36c1d19d4a2e9eb0ce3606eb480000000000000000000000001231deb6f5749ef6ce6943a275a1d3e7486f4eae0000000000000000000000000000000000000000000000000dd7d4f70b73c000000000000000000000000000000000000000000000000000000000009fc77d8700000000000000000000000000000000000000000000000000000000a0950918000000000000000000000000000000000000000000000000000000006ac2a0180000000000000000000000000000000056c7c83f3f774ff3a5279d0adbb019800000000000000000000000000000000000000000000000000000000000000003000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001e019ebcc6fe7d50968a86627bdf19eb3e1a3b657b0842d5abe54c0938b31ba41ba000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000412eb002313796213b08861a59a63c54a23e9d6d2caa0c41c988cc0c008e98b9fc72849cc33c169539be773be749cdd617f39baf388c172f6544b2dfc3e4d574e41b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000180000000000000000000000000000000000000000000000000000000000000271000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000bc1d9760bd6ca468ca9fb5ff2cfbeac35d86c973000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2000000000000000000000000000000000000000000000000000000000000012000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002710000000000000000000000000000000000000000000000000000000000000000300000000000000000000000000000000000000000000000000000000000000010000000000000000000000001231deb6f5749ef6ce6943a275a1d3e7486f4eae0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e0554a476a092703abdb3ef35c80e0d76d32939f000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2000000000000000000000000a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48000000000000000000000000000000000000000000000000000000000000012000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000064000000000000000000000000000000000000730f7c9759dff1f62a74e03ac9b200000000000000000000000000000000000000000000000000000000",
    "from": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "chainId": 1,
    "gasPrice": "0x8643f99",
    "gasLimit": "0xb4d92"
  },
  "transactionId": "0xf04d08566eb84a038338a9ab11173a46d05a6136b6fd9fa16420737469ee6b8e"
}
```

## Why this matches (or not)

_[0.85|heuristic] Route quote output amount present_
