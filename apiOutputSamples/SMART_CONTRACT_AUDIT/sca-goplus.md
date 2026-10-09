---
intent: SMART_CONTRACT_AUDIT
slug: sca-goplus
status: pending_review
captured_at: 2026-10-08T04:43:47Z
request_url: https://api.gopluslabs.io/api/v1/token_security/1?contract_addresses=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
content_type: application/json
inputs: |
  {"addr": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "addr_lc": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", "chain": "1"}
intent_description: |
  Inspects bytecode and smart contract source code for reentrancy, access control, and integer overflows.
answer_requirement: |
  Must return security-relevant static facts for the pinned contract: source verified, proxy/upgradeable, owner/mint/self-destruct privileges, honeypot flags.
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "code": 1,
  "message": "OK",
  "result": {
    "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2": {
      "anti_whale_modifiable": "0",
      "buy_tax": "0",
      "can_take_back_ownership": "0",
      "creator_address": "0x4f26ffbe5f04ed43630fdc30a87638d53d0b0876",
      "creator_balance": "0.0042501181000001",
      "creator_percent": "0.000000",
      "external_call": "0",
      "hidden_owner": "0",
      "holder_count": "3679802",
      "holders": [
        {
          "address": "0x4d5f47fa6a74757f35c14fd3a6ef8e3c9bc514e8",
          "tag": "",
          "is_contract": 1,
          "balance": "378753.254317567474874331",
          "percent": "0.173900025617813421",
          "is_locked": 0
        },
        {
          "address": "0xf04a5cc80b1e94c69b48f5ee68a08cd2f09a7c3e",
          "tag": "",
          "is_contract": 1,
          "balance": "294403.380870999434566809",
          "percent": "0.135171790319487312",
          "is_locked": 0
        },
        {
          "address": "0x2f0b23f53734252bda2277357e97e1517d6b042a",
          "tag": "",
          "is_contract": 1,
          "balance": "268515.108466044016366952",
          "percent": "0.123285499751412139",
          "is_locked": 0
        },
        {
          "address": "0x59cd1c87501baa753d0b5b5ab5d8416a45cd71db",
          "tag": "",
          "is_contract": 1,
          "balance": "145391.480267144186810004",
          "percent": "0.066754758816855071",
          "is_locked": 0
        },
        {
          "address": "0x94335f3f93e90e4f49c61ef32dfdbb037aba5873",
          "tag": "",
          "is_contract": 0,
          "balance": "60367.5582",
          "percent": "0.027717042158171957",
          "is_locked": 0
        },
        {
          "address": "0xc3d688b66703497daa19211eedff47f25384cdc3",
          "tag": "",
          "is_contract": 1,
          "balance": "59158.184787842526264953",
          "percent": "0.027161772823959579",
          "is_locked": 0
        },
        {
          "address": "0x3ee18b2214aff97000d974cf647e7c347e8fa585",
          "tag": "",
          "is_contract": 1,
          "balance": "46879.16550886",
          "percent": "0.021524008018415980",
          "is_locked": 0
        },
        {
          "address": "0x3afdc9bca9213a35503b077a6072f3d0d5ab0840",
          "tag": "",
          "is_contract": 1,
          "balance": "37725.965646551897754761",
          "percent": "0.017321425803225977",
          "is_locked": 0
        },
        {
          "address": "0x21b8065d10f73ee2e260e5b47d3344d3ced7596e",
          "tag": "",
          "is_contract": 1,
          "balance": "28353.994527677124007347",
          "percent": "0.013018397382788357",
          "is_locked": 0
        },
        {
          "address": "0x4553e3bc6327006a63c5aa4cdac887f66b6a433e",
          "tag": "",
          "is_contract": 0,
          "balance": "26924.269621698788841623",
          "percent": "0.012361956296297799",
          "is_locked": 0
        }
      ],
      "honeypot_with_same_creator": "0",
      "is_anti_whale": "0",
      "is_blacklisted": "0",
      "is_honeypot": "0",
      "is_in_dex": "1",
      "is_mintable": "0",
      "is_open_source": "1",
      "is_proxy": "0",
      "is_whitelisted": "0",
      "owner_balance": "0",
      "owner_change_balance": "0",
      "owner_percent": "0",
      "personal_slippage_modifiable": "0",
      "selfdestruct": "0",
      "sell_tax": "0",
      "slippage_modifiable": "0",
      "token_name": "Wrapped Ether",
      "token_symbol": "WETH",
      "total_supply": "2177994.241070255173739383",
      "trading_cooldown": "0",
      "transfer_pausable": "0",
      "transfer_tax": "",
      "cannot_buy": "0",
      "trust_list": "1"
    }
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
