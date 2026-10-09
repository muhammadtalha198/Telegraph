---
intent: ONCHAIN_METRIC_VERIFY
slug: ocm-blockscout-eth
status: pending_review
captured_at: 2026-10-05T09:28:17Z
request_url: https://eth.blockscout.com/api/v2/addresses/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
content_type: application/json
inputs: |
  {"eaddr": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"}
intent_description: |
  Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.
answer_requirement: |
  Must return the on-chain value asked (address balance / token balance / tx state).
capture_note: |
  golden-test PASS: Blockscout
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "block_number_balance_updated_at": 26125263,
  "coin_balance": "5749318262866090346",
  "creation_status": "success",
  "creation_transaction_hash": null,
  "creator_address_hash": null,
  "ens_domain_name": "vitalik.eth",
  "exchange_rate": "2718.21",
  "has_beacon_chain_withdrawals": false,
  "has_logs": false,
  "has_token_transfers": true,
  "has_tokens": true,
  "has_validated_blocks": false,
  "hash": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
  "implementations": [
    {
      "address_hash": "0x5A7FC11397E9a8AD41BF10bf13F22B0a63f96f6d",
      "name": "AmbireAccount7702"
    }
  ],
  "is_contract": true,
  "is_scam": false,
  "is_verified": true,
  "metadata": null,
  "name": null,
  "private_tags": [],
  "proxy_type": "eip7702",
  "public_tags": [],
  "reputation": "ok",
  "token": null,
  "watchlist_address_id": null,
  "watchlist_names": []
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
