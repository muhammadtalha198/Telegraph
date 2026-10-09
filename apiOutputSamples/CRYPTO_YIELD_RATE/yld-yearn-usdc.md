---
intent: CRYPTO_YIELD_RATE
slug: yld-yearn-usdc
status: pending_review
captured_at: 2026-10-08T04:42:17Z
request_url: https://ydaemon.yearn.fi/1/vaults/0xBe53A109B494E5c9f97b9Cd39Fe969BE68BF6204
content_type: application/json
inputs: |
  {}
intent_description: |
  Tracks annualized percentage yields (APY), staking reward rates, and lending pool yields across DeFi protocols.
answer_requirement: |
  Must return the current annualized yield, as a percent number, for the protocol-specific pool/asset named by the test (ETH liquid-staking rate for cbETH; USDC lending/vault net APY on Ethereum).
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "address": "0xBe53A109B494E5c9f97b9Cd39Fe969BE68BF6204",
  "type": "Yearn Vault",
  "kind": "Multi Strategy",
  "symbol": "yvUSDC-1",
  "name": "USDC",
  "category": "Stablecoin",
  "version": "3.0.2",
  "description": "Multi strategy USDC vault. <br/><br/>Multi strategy vaults are (wait for it) vaults that contain multiple strategies. Multi strategy vaults give the vault creator flexibility to balance risk and opportunity across multiple different strategies.",
  "decimals": 6,
  "chainID": 1,
  "token": {
    "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "name": "USD Coin",
    "symbol": "USDC",
    "description": "",
    "decimals": 6
  },
  "tvl": {
    "totalAssets": "19317621117727",
    "tvl": 19311057.05568189,
    "price": 0.9996448926047525
  },
  "apr": {
    "type": "v2:averaged",
    "netAPR": 0.03651896409915212,
    "fees": {
      "performance": 0.1,
      "management": 0
    },
    "points": {
      "weekAgo": 0.031927981646912906,
      "monthAgo": 0.03651896409915212,
      "inception": 0.046194604300149544
    },
    "pricePerShare": {
      "today": 1.12089,
      "weekAgo": 1.120215,
      "monthAgo": 1.117595
    },
    "extra": {
      "stakingRewardsAPR": 0,
      "gammaRewardAPR": null
    },
    "forwardAPR": {
      "type": "",
      "netAPR": null,
      "composite": {
        "boost": null,
        "poolAPY": null,
        "boostedAPR": null,
        "baseAPR": null,
        "cvxAPR": null,
        "rewardsAPR": null
      }
    }
  },
  "strategies": [
    {
      "address": "0x7130570BCEfCedBe9d15B5b11A33006156460f8f",
      "name": "USDC to sUSDS Lender",
      "status": "active",
      "netAPR": 0.03550149703760713,
      "details": {
        "totalDebt": "2096866303509",
        "totalLoss": "0",
        "totalGain": "0",
        "performanceFee": 0,
        "lastReport": 1790749559,
        "debtRatio": 1085
      }
    },
    {
      "address": "0x68Aea7b82Df6CcdF76235D46445Ed83f85F845A3",
      "name": "Yearn USDC",
      "status": "active",
      "details": {
        "totalDebt": "5916708364607",
        "totalLoss": "0",
        "totalGain": "0",
        "performanceFee": 0,
        "lastReport": 1791004967,
        "debtRatio": 3063
      }
    },
    {
      "address": "0xe63A2aBC24cD9538398d825a4bFe5778D25687dF",
      "name": "stcUSD/USDC Pawn Broker Market",
      "status": "active",
      "details": {
        "totalDebt": "6038311770369",
        "totalLoss": "0",
        "totalGain": "0",
        "performanceFee": 0,
        "lastReport": 1791177911,
        "debtRatio": 3126
      }
    },
    {
      "address": "0x39c0aEc5738ED939876245224aFc7E09C8480a52",
      "name": "USDC to USDS Depositor",
      "status": "active",
      "netAPR": 0.014266450093616061,
      "details": {
        "totalDebt": "5265734676526",
        "totalLoss": "0",
        "totalGain": "0",
        "performanceFee": 0,
        "lastReport": 1790998295,
        "debtRatio": 2726
      }
    }
  ],
  "staking": {
    "address": "0x622fA41799406B120f9a40dA843D358b7b2CFEE3",
    "available": true,
    "source": "VeYFI",
    "rewards": [
      {
        "address": "0x41252E8691e964f7DE35156B68493bAb6797a275",
        "name": "Discount YFI",
        "symbol": "dYFI",
        "decimals": 18,
        "price": 2025.722099,
        "isFinished": false,
        "finishedAt": 1792022400,
        "apr": 0,
        "perWeek": 0
      }
    ]
  },
  "migration": {
    "available": false,
    "address": "0xBe53A109B494E5c9f97b9Cd39Fe969BE68BF6204",
    "contract": "0x0000000000000000000000000000000000000000"
  },
  "featuringScore": 7.052197993331253e+23,
  "pricePerShare": "1120892",
  "info": {
    "riskLevel": 1,
    "isRetired": false,
    "isHidden": false,
    "isBoosted": false,
    "isHighlighted": true,
    "riskScore": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ]
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
