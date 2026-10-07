---
intent: CRYPTO_TRANSFER_VERIFY
slug: xfer-blockcypher
status: approved
captured_at: 2026-10-05T09:28:05Z
request_url: https://api.blockcypher.com/v1/btc/main/txs/a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d
content_type: application/json
inputs: |
  {"txid": "a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"}
intent_description: |
  Verifies on-chain transaction status, gas fee burn, sender/recipient addresses, and block confirmations.
answer_requirement: |
  Must return the on-chain status of the transaction (confirmed, block, parties/amounts).
capture_note: |
  golden-test PASS: BlockCypher
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the block height where the transaction was confirmed, which is relevant to the intent of verifying the on-chain status of the transaction."
reviewed_at: 2026-10-05T12:18:05Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "block_hash": "00000000152340ca42227603908689183edc47355204e7aca59383b0aaac1fd8",
  "block_height": 57043,
  "block_index": 1,
  "hash": "a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d",
  "addresses": [
    "17SkEw2md5avVNyYgj6RiXuQKNwkXaxFyQ",
    "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
  ],
  "total": 1000000000000,
  "fees": 99000000,
  "size": 23620,
  "vsize": 23620,
  "preference": "high",
  "confirmed": "2010-05-22T18:16:31Z",
  "received": "2010-05-22T18:16:31Z",
  "ver": 1,
  "double_spend": false,
  "vin_sz": 131,
  "vout_sz": 1,
  "confirmations": 912946,
  "confidence": 1,
  "inputs": [
    {
      "prev_hash": "867da54b0fd0a9429d30471af3fcf069e069141fcc544583f3103ac3948f2e0d",
      "output_index": 0,
      "script": "493046022100bc57dc26f46fecc1da03272cb2298d8a08b22d865541f5b3a3e862cc87da4b47022100ce1fc72771d164d608b15065832542a0e9040cfdf28862c5175c81fcb0e0b65501410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 15000000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 53305
    },
    {
      "prev_hash": "a1b2926e0b0e2d032d24a7bc38700cde95b7db754962c8d2add113178ad0df1b",
      "output_index": 0,
      "script": "49304602210097f8cd3973e5d4c7a2556c82539a710345f82f089398649684a12b3026ae9de5022100d3e46fa2e95988e132f609d267fb403c679a60c3d9d3f936e54f8b4f76d4e4a301410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 25000000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 54599
    },
    {
      "prev_hash": "d9be96849d639cf6194d333015943824800302a0263854bac0b9d3cfb7c7c381",
      "output_index": 0,
      "script": "493046022100b91ba45dd7ea4418b38a02174095d8299cfbc4b316bcdff12783d887a7d419ef022100f4d0b730542a057980078b9136444683453bc5cb52d6e03272c0ac69fd98f39001410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 15000000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 55599
    },
    {
      "prev_hash": "9d62e6dadaafde34c0eff8f9f85829f2451dd8379e0ccdd364114f8722100090",
      "output_index": 0,
      "script": "493046022100e14dc4a03700239b7b6751e1aa82adf1b04eebcc6967601cfbec6d33702f01df022100c993a735ee72435c2bfdf3b76ce7d1a99e36cab62341a5b62db706f366f0098001410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 8000000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 52538
    },
    {
      "prev_hash": "29ca7dc4433e506aeedd0213c8b5715d887414093aa7d100661863814f472776",
      "output_index": 0,
      "script": "483045022062652b961c85b70c668ca49f39145c2bc43ac4de043146814c8990732696d90602210087dc7bdc505bce623769b5f8c46bbc85d48c461347b8a48a7430d55accb9bf0101410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51729
    },
    {
      "prev_hash": "1498ba4baa3e211e498ff290d80cee5a378419faeaf0bfad4d5cab4a85c21377",
      "output_index": 0,
      "script": "47304402205fab9b514bfcb7935306e174e295b237f834d1ed175865f67642f8bc8ad15bbb022017ebaa8d64eaeb32a93f362e6169d7c7840126e6a3983c9a6a352f2b663eabed01410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51734
    },
    {
      "prev_hash": "42605a288f6b7afd229050ea3a5ca402d11d0d840ca83140eeb6da51290d2c77",
      "output_index": 1,
      "script": "493046022100c2d3a8a53518f0c6ce6f3bcd2afb71d3924d2b611792b4b102756aed3dc9b56e022100d1ecd72272e988ac6b4f979645dab9dbabd83214509de8dae4579a82841f7a9a01410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51729
    },
    {
      "prev_hash": "dffa83544fb441f040f335f840e218fedf5b1e8329ba05a927f317357fa66478",
      "output_index": 1,
      "script": "4830450220160effb2dd634f9104d7fa0992f3597c0cf031d0bb1bf1bdc97a6f002d085efb022100b123d29fd6164f48cf06d30b2a43671f2b1cb652f293e6e67000ba019ca97e1b01410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51741
    },
    {
      "prev_hash": "88ecb21af0fdff135cd72557f797f46c501e7fb06f0bb85e6797689c200b7b78",
      "output_index": 0,
      "script": "483045022100db02cc7cd191f601b49abef2b5311ea3743a127f536694a7dd9dcdbb503275020220311fde40d96c41d20bd8a5a7f89d0a2003bdc1e6c070641065eb8d5e84da885e01410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51729
    },
    {
      "prev_hash": "411d7cc303e6344f238d2e61d0ccfc95e18b4a5b41acfab7313cf90f2fa99278",
      "output_index": 1,
      "script": "4830450221008d0bb3cee4eadf618a8973b9b46619e7a25868be3517ac56fabca58ca788dad00220428e1e3e4bc97ea6c3c368b8456532cbaf17b5bcb0aececabea04efa0232d61401410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51737
    },
    {
      "prev_hash": "f6858b5c10f9e8025c4a1ebf09e348ce78944739703a8a61a5588cc493d19a78",
      "output_index": 1,
      "script": "4730440220204d9178c0b60849e25629c450ba62053518acecfcbe8d7ce8fc3fc8cf82b31802204cd85ca7a61365c766ef29f31dab6809a4fd33860838c6c10f2e947261e782e101410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51741
    },
    {
      "prev_hash": "3d2ccc12be57cd26fca1a280a321de9559a8dcf86ae46852665ade09e149ab78",
      "output_index": 0,
      "script": "493046022100db1dedb67fcf855e7d54ee88f69a530e4d97a44b96c7948d95402b2129eba6b80221009d4755490f971f6b2044ed7ad0dbee7ddc62a27ef6d9e68a9d087a42ac00724301410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51729
    },
    {
      "prev_hash": "63ff45247f43d354a678835fc2602bc907bdc06249ffe8242f08ccfb4ae16779",
      "output_index": 1,
      "script": "493046022100d2ae25304242fa336e67caf2efc29d91c3b867fe5b2d994c59bf95ffe8bfce28022100deaacda3b40b53f30ed11c28a753bd5a6878980b064c68036ba0a6f3dd1868d701410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51734
    },
    {
      "prev_hash": "ba6bc364c183002d04ae11528ee8543dee9b5e17af147fe9245b705f94df7179",
      "output_index": 0,
      "script": "493046022100c2a7e0f649f75094eaf38c569b0dbacb090572851262cf44b05f9c91d2808caa022100888e68ffa5a4c571c77e3728c44d492ee3357a08a836d1aa0b2f498e8a76266501410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51737
    },
    {
      "prev_hash": "eec82457cbc83612495843f85ba22caa9492978840048944c93294ce3e815f7a",
      "output_index": 1,
      "script": "47304402201d03cadfe3b680a89735181bbd40baf9335cf88d4a6c377e2a423e3fe29bedc902206daa6faa2e8508e78a900349f4179b354f39173e400d7b3c81b1eb7531e731f501410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51728
    },
    {
      "prev_hash": "39fa5eeec4ea7ffc8c4089590bb96b6c09280684bd0f083cacf5b4a70b136f7a",
      "output_index": 0,
      "script": "473044022064f23eecb24da86be58529abb216800de1bd13d1ed086e65cbd7b1d4a62a1f14022060b976e9f01dc0013dfe37447def0adc1090725664338174abaa6dd34a2334f201410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51734
    },
    {
      "prev_hash": "3808ce98d033fd3765c042e1a3ea7a86095bc4d81419281346bb912101c45b7b",
      "output_index": 1,
      "script": "483045022100e2e2e7db2702ce25cd5ba5ca18518d6d547c30dff253eaf6dc0fb01843e549f6022009cfdf2a55364eef0aa5986aba3afb9a986319b6948fef0512340df6e00caeec01410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51741
    },
    {
      "prev_hash": "2ca0decccec19f4e86021dfc56ae2c7581b3f8c16d4c42e252f35e7234de7b7b",
      "output_index": 0,
      "script": "48304502207341e21bc643e7b1696464a08bb9281b8a2816d023433f1abbf178abf1eec4690221008047d9f6bfc1ca916996349d955046718f7ad094d89ca775dfc14fb54daeeaf401410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51734
    },
    {
      "prev_hash": "ce806910ce4804de564a9b2a3704b57b0c87c7517ca2a5012e3b6aa9563dcc7b",
      "output_index": 0,
      "script": "493046022100c3338289a69b0bb5a048fe0a5cac7715938387b5c9945f8a127582b9c3d303c4022100c718de105552436d6a2ca491aa66fdc55fad01cea9405e5dbea2e33348cd908901410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51728
    },
    {
      "prev_hash": "3d2ccf1f47baa32d3866de6096311e3fd2d59c17d92e2c3e014726f788472f7c",
      "output_index": 0,
      "script": "483045022100800a1313efdd57ea35521d546be6e412bfb67acef779813ef238d614fc185e0602204c597f16a9e169660620558aeb68d017baa9a2e5278504cd8b2ebcade6d1dcaa01410434417dd8d89deaf0f6481c2c160d6de0921624ef7b956f38eef9ed4a64e36877be84b77cdee5a8d92b7d93694f89c3011bf1cbdf4fd7d8ca13b58a7bb4ab0804",
      "output_value": 1000000,
      "sequence": 4294967295,
      "addresses": [
        "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
      ],
      "script_type": "pay-to-pubkey-hash",
      "age": 51741
    }
  ],
  "outputs": [
    {
      "value": 1000000000000,
      "script": "76a91446af3fb481837fadbb421727f9959c2d32a3682988ac",
      "spent_by": "cca7507897abc89628f450e8b1e0c6fca4ec3f7b34cccf55f3f531c659ff4d79",
      "addresses": [
        "17SkEw2md5avVNyYgj6RiXuQKNwkXaxFyQ"
      ],
      "script_type": "pay-to-pubkey-hash"
    }
  ],
  "next_inputs": "https://api.blockcypher.com/v1/btc/main/txs/a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d?instart=20&outstart=0&limit=20"
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the block height where the transaction was confirmed, which is relevant to the intent of verifying the on-chain status of the transaction._
