---
intent: CROSS_CHAIN_STATE_VERIFY
slug: xchain-axelar-transfers
status: approved
captured_at: 2026-10-04T18:41:04Z
request_url: https://api.axelarscan.io/token/searchTransfers?size=5
content_type: application/json
inputs: |
  recent axelar transfers
intent_description: |
  Proves cryptographic Merkle-Patricia state roots and cross-chain message execution headers between distinct blockchain networks.
answer_requirement: |
  Must convey whether the cross-chain message/transfer executed and its status.
capture_note: |
  NEW
reviewer_note: "auto_review: [0.75|heuristic] Cross-chain operations/transfers/status list present"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "data": [
    {
      "link": {
        "txhash": "0x56a9f4db5f6b35639f3cef4fbd374071989523c3537a27d8489e1a81aef704b0",
        "height": 123550033,
        "type": "gateway",
        "created_at": {
          "ms": 1791114977000,
          "hour": 1791111600000,
          "day": 1791072000000,
          "week": 1791072000000,
          "month": 1790812800000,
          "quarter": 1790812800000,
          "year": 1767225600000
        },
        "source_chain": "fantom",
        "destination_chain": "base",
        "sender_address": "0xAaa63DE0d76E3E4942B078196DA1Ff029E7e9f35",
        "recipient_address": "0xAaa63DE0d76E3E4942B078196DA1Ff029E7e9f35",
        "denom": "uusdc",
        "asset": "uusdc",
        "price": 0.999945
      },
      "send": {
        "txhash": "0x56a9f4db5f6b35639f3cef4fbd374071989523c3537a27d8489e1a81aef704b0",
        "height": 123550033,
        "status": "success",
        "type": "evm",
        "created_at": {
          "ms": 1791114977000,
          "hour": 1791111600000,
          "day": 1791072000000,
          "week": 1791072000000,
          "month": 1790812800000,
          "quarter": 1790812800000,
          "year": 1767225600000
        },
        "source_chain": "fantom",
        "destination_chain": "base",
        "sender_address": "0xAaa63DE0d76E3E4942B078196DA1Ff029E7e9f35",
        "recipient_address": "0x304acf330bbE08d1e512eefaa92F6a57871fD895",
        "denom": "uusdc",
        "amount": 30,
        "value": 29.99835,
        "fee": 11.5,
        "insufficient_fee": false,
        "amount_received": 18.5,
        "fee_value": 11.4993675
      },
      "type": "send_token",
      "time_spent": {
        "total": 24287
      },
      "id": "0x56a9f4db5f6b35639f3cef4fbd374071989523c3537a27d8489e1a81aef704b0_fantom",
      "status": "asset_sent",
      "simplified_status": "sent"
    },
    {
      "link": {
        "txhash": "0x3fc2ca9f80b938da838ea99bf339e067cc745c4230237c0df35ee3975029d025",
        "height": 52076981,
        "type": "gateway",
        "created_at": {
          "ms": 1790943309000,
          "hour": 1790942400000,
          "day": 1790899200000,
          "week": 1790467200000,
          "month": 1790812800000,
          "quarter": 1790812800000,
          "year": 1767225600000
        },
        "source_chain": "base",
        "destination_chain": "fantom",
        "sender_address": "0xfa506A1A0e92C6f3712aEe242eB554e881fD21B9",
        "recipient_address": "0xfa506a1a0e92c6f3712aee242eb554e881fd21b9",
        "denom": "uusdc",
        "asset": "uusdc",
        "price": 0.999928
      },
      "send": {
        "txhash": "0x3fc2ca9f80b938da838ea99bf339e067cc745c4230237c0df35ee3975029d025",
        "height": 52076981,
        "status": "success",
        "type": "evm",
        "created_at": {
          "ms": 1790943309000,
          "hour": 1790942400000,
          "day": 1790899200000,
          "week": 1790467200000,
          "month": 1790812800000,
          "quarter": 1790812800000,
          "year": 1767225600000
        },
        "source_chain": "base",
        "destination_chain": "fantom",
        "sender_address": "0xfa506A1A0e92C6f3712aEe242eB554e881fD21B9",
        "recipient_address": "0xe432150cce91c13a887f7D836923d5597adD8E31",
        "denom": "uusdc",
        "amount": 0.274434,
        "value": 0.27441424075200005,
        "fee": 11.5,
        "insufficient_fee": true,
        "amount_received": 0,
        "fee_value": 11.499172
      },
      "type": "send_token",
      "time_spent": {
        "total": 195955
      },
      "id": "0x3fc2ca9f80b938da838ea99bf339e067cc745c4230237c0df35ee3975029d025_base",
      "status": "asset_sent",
      "simplified_status": "sent"
    },
    {
      "link": {
        "txhash": "0xa18fe2f05149108b42c420a9d9f75220723ccb17b1aa3ea5061b1542e1a7f41c",
        "height": 50334619,
        "type": "gateway",
        "created_at": {
          "ms": 1787458585000,
          "hour": 1787457600000,
          "day": 1787443200000,
          "week": 1787443200000,
          "month": 1785542400000,
          "quarter": 1782864000000,
          "year": 1767225600000
        },
        "source_chain": "base",
        "destination_chain": "arbitrum",
        "sender_address": "0x51A6D6Fd3c9dc64ad81Bb002Db8910e62db59558",
        "recipient_address": "0x51A6D6Fd3c9dc64ad81Bb002Db8910e62db59558",
        "denom": "uregen",
        "asset": "uregen",
        "price": 0.00120665
      },
      "send": {
        "txhash": "0xa18fe2f05149108b42c420a9d9f75220723ccb17b1aa3ea5061b1542e1a7f41c",
        "height": 50334619,
        "status": "success",
        "type": "evm",
        "created_at": {
          "ms": 1787458585000,
          "hour": 1787457600000,
          "day": 1787443200000,
          "week": 1787443200000,
          "month": 1785542400000,
          "quarter": 1782864000000,
          "year": 1767225600000
        },
        "source_chain": "base",
        "destination_chain": "arbitrum",
        "sender_address": "0x51A6D6Fd3c9dc64ad81Bb002Db8910e62db59558",
        "recipient_address": "0xe432150cce91c13a887f7D836923d5597adD8E31",
        "denom": "uregen",
        "amount": 80,
        "value": 0.096532,
        "fee": 660,
        "insufficient_fee": true,
        "amount_received": 0,
        "fee_value": 0.796389
      },
      "type": "send_token",
      "time_spent": {
        "total": 3680679
      },
      "id": "0xa18fe2f05149108b42c420a9d9f75220723ccb17b1aa3ea5061b1542e1a7f41c_base",
      "status": "asset_sent",
      "simplified_status": "sent"
    },
    {
      "link": {
        "txhash": "0xb93d42b698eaac1eadd0878e14508666977c740c3839ee0fb885e84e8f5ff6dc",
        "height": 50320880,
        "type": "gateway",
        "created_at": {
          "ms": 1787431107000,
          "hour": 1787428800000,
          "day": 1787356800000,
          "week": 1786838400000,
          "month": 1785542400000,
          "quarter": 1782864000000,
          "year": 1767225600000
        },
        "source_chain": "base",
        "destination_chain": "polygon",
        "sender_address": "0x51A6D6Fd3c9dc64ad81Bb002Db8910e62db59558",
        "recipient_address": "0x51A6D6Fd3c9dc64ad81Bb002Db8910e62db59558",
        "denom": "uregen",
        "asset": "uregen",
        "price": 0.00124912
      },
      "send": {
        "txhash": "0xb93d42b698eaac1eadd0878e14508666977c740c3839ee0fb885e84e8f5ff6dc",
        "height": 50320880,
        "status": "success",
        "type": "evm",
        "created_at": {
          "ms": 1787431107000,
          "hour": 1787428800000,
          "day": 1787356800000,
          "week": 1786838400000,
          "month": 1785542400000,
          "quarter": 1782864000000,
          "year": 1767225600000
        },
        "source_chain": "base",
        "destination_chain": "polygon",
        "sender_address": "0x51A6D6Fd3c9dc64ad81Bb002Db8910e62db59558",
        "recipient_address": "0xe432150cce91c13a887f7D836923d5597adD8E31",
        "denom": "uregen",
        "amount": 2,
        "value": 0.00249824,
        "fee": 380,
        "insufficient_fee": true,
        "amount_received": 0,
        "fee_value": 0.4746656
      },
      "type": "send_token",
      "time_spent": {
        "total": 3708157
      },
      "id": "0xb93d42b698eaac1eadd0878e14508666977c740c3839ee0fb885e84e8f5ff6dc_base",
      "status": "asset_sent",
      "simplified_status": "sent"
    },
    {
      "link": {
        "txhash": "0x46291ab1f108a9d77e1926f13fcb9f1573f374774e5c82684a63f95cafe178f9",
        "height": 50320873,
        "type": "gateway",
        "created_at": {
          "ms": 1787431093000,
          "hour": 1787428800000,
          "day": 1787356800000,
          "week": 1786838400000,
          "month": 1785542400000,
          "quarter": 1782864000000,
          "year": 1767225600000
        },
        "source_chain": "base",
        "destination_chain": "celo",
        "sender_address": "0x51A6D6Fd3c9dc64ad81Bb002Db8910e62db59558",
        "recipient_address": "0x51A6D6Fd3c9dc64ad81Bb002Db8910e62db59558",
        "denom": "uregen",
        "asset": "uregen",
        "price": 0.00124912
      },
      "send": {
        "txhash": "0x46291ab1f108a9d77e1926f13fcb9f1573f374774e5c82684a63f95cafe178f9",
        "height": 50320873,
        "status": "success",
        "type": "evm",
        "created_at": {
          "ms": 1787431093000,
          "hour": 1787428800000,
          "day": 1787356800000,
          "week": 1786838400000,
          "month": 1785542400000,
          "quarter": 1782864000000,
          "year": 1767225600000
        },
        "source_chain": "base",
        "destination_chain": "celo",
        "sender_address": "0x51A6D6Fd3c9dc64ad81Bb002Db8910e62db59558",
        "recipient_address": "0xe432150cce91c13a887f7D836923d5597adD8E31",
        "denom": "uregen",
        "amount": 2,
        "value": 0.00249824,
        "fee": 380,
        "insufficient_fee": true,
        "amount_received": 0,
        "fee_value": 0.4746656
      },
      "type": "send_token",
      "time_spent": {
        "total": 3708171
      },
      "id": "0x46291ab1f108a9d77e1926f13fcb9f1573f374774e5c82684a63f95cafe178f9_base",
      "status": "asset_sent",
      "simplified_status": "sent"
    }
  ],
  "total": 660540,
  "time_spent": 149
}
```

## Why this matches (or not)

_[0.75|heuristic] Cross-chain operations/transfers/status list present_
