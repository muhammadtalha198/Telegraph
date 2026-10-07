---
intent: ONCHAIN_METRIC_VERIFY
slug: ocm-blockscout-polygon
status: approved
captured_at: 2026-10-02T07:46:08Z
request_url: https://polygon.blockscout.com/api/v2/addresses/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
content_type: application/json
inputs: |
  0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
intent_description: |
  Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.
answer_requirement: |
  Must convey the on-chain value asked (wallet/token balance or tx state) for the address given.
capture_note: |
  balance only; capture is GET-only so RPC POST miners need the /truth proxy
reviewer_note: "auto_review: [0.80] Returns wallet/token balance (partial vs full logs/gas description)"
reviewed_at: 2026-10-02T12:49:15Z
---

## Raw API output

```json
{
  "block_number_balance_updated_at": 94813430,
  "coin_balance": "592719767156691654977",
  "creation_status": null,
  "creation_transaction_hash": null,
  "creator_address_hash": null,
  "ens_domain_name": null,
  "exchange_rate": "0.110291",
  "has_beacon_chain_withdrawals": false,
  "has_logs": false,
  "has_token_transfers": true,
  "has_tokens": true,
  "has_validated_blocks": false,
  "hash": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
  "implementations": [],
  "is_contract": false,
  "is_scam": false,
  "is_verified": false,
  "metadata": null,
  "name": null,
  "private_tags": [],
  "proxy_type": null,
  "public_tags": [],
  "reputation": "ok",
  "token": null,
  "watchlist_address_id": null,
  "watchlist_names": []
}
```

## Why this matches (or not)

_[0.80] Returns wallet/token balance (partial vs full logs/gas description)_
