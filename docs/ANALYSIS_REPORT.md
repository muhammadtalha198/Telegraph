# Step 1 report: how MinerCreator decides "correct" today

Date: 2026-10-08. Read-only pass over every script, YAML, sample, doc, and the node's YAML loader in `../Telegraph`.

## 1. What this repo actually is

The brief describes a question-answering engine (intent → API → extract → validate → plain-English answer). This repo is not that. It is a **miner registration pipeline**:

```
capture_api_output.py      call ONE URL once, save body to apiOutputSamples/<INTENT>/<slug>.md
auto_review_samples.py     heuristics (9 of 56 intents) + LLM judge reads the body -> approved/rejected/needs_human
generate_yamls_...py       turn the sample's URL into a node-format miner YAML
upload-host.sh             host the YAML on Omni
register_gates_v2.py       re-run auto_review + golden-if-any + YAML lint + pin check + live probe
register-miner-v2.sh       byte-match hosted YAML, then cast send registerMiner
```

Answering real users happens elsewhere: the Telegraph Go node calls the API, Usman's LLM normalizes the output, and Alexandria shows it. The only code here that calls APIs at answer time is `scripts/semantic-truth-proxy.py`: 3,464 lines, about 60 hand-coded adapters, deployed on Omni, and serving about 141 registered miners.

**So there was no extraction, validation, verification, or answer-formatting layer in this repo.** I am building one, not repairing one.

## 2. How "really correct" is decided today

| Check the brief asks for | Today |
|---|---|
| E1 extraction | **None.** No code pulls a value out of a response on the V2 path. The LLM is asked to report a `value`, and that is the only "extraction". |
| E2 sanity range | **None on V2.** Ranges exist only in the legacy RelTol path (`miner_selftest.INTENTS`). |
| E3 cross-check | Batch mode only. Groups samples by the LLM's free-text `subject` string, needs 3 or more in one group, 5% tolerance. **In `--gate` mode (the mode that unlocks gas) one file is reviewed, so cross-check never runs.** |
| E4 freshness | **None anywhere.** `wx_temp` returns `obs_time` and nothing reads it. 7timer's "current" value is a forecast slot. |
| E5 answer type / entity / scope | **None in code.** "Wednesday" for a date, or Paris, Texas data for Paris, France, passes if the LLM likes it. |
| Confidence + "could not verify" | LLM self-reported confidence only. |

The deciding vote is a **3B local model (qwen2.5:3b)**. It reads the first 3,500 characters of **one** captured response and says "answers / partial / no". The live probe at gas time checks HTTP 200, a non-empty body, and the JSON-vs-HTML family. It does not check the value.

## 3. Broken (verified)

1. **Two Active on-chain miners serve broken answers.**
   - `cp-kraken` (reg 4683): the YAML default is `pair: "{kraken_pair}"`, an unfilled template. Its "approved" sample body is `{"error":["EQuery:Unknown asset pair"]}`, and the sample's own review line says `[0.95|hard-check] JSON error object`. Its status is still `approved`.
   - `cp-redstone` (reg 4670): the approved sample body is `[]`.
   - Both came from an old "pack V2 smoke pass + pipeline approve" path that skipped review. That path is now archived.
2. **85 of 168 approved samples have no auto_review+LLM record** (manual or pipeline approvals). Gates re-review at gas time, so this only affects miners that are already registered.
3. **The live probe does not call the miner the way the node does.** The node replaces `{address}` in `external_path` with the param value and drops it from the query string (`Telegraph/.../generic/generic.go:171`). `register_gates_v2.yaml_request` leaves `{address}` literally in the path and appends `?address=…`. Every path-param miner is probed with a wrong URL.
4. **The approved sample is not always the miner's question, and no gate compares the two.**
   - On a raw string comparison, 40 approved samples requested a different URL than their YAML's default request. Most of that is bug 3 plus trailing-slash noise.
   - After fixing bug 3 and normalising slashes and blank parameters, one approved sample really asks a different question: `vuln-nvd-cve` was captured from NVD directly, but its YAML calls the `/truth/nvd-cvss` proxy.
   - Pending samples drift too. `CRYPTO_PRICE_LOOKUP/cp-coingecko` asked about bitcoin, while `cp-coingecko.yaml` defaults to ethereum.
5. `generate_yamls_from_approved_samples.py:353` prints `slug` before it is assigned. On the first manual-approved sample this raises NameError. After that it prints the wrong slug.
6. `generate_yamls` copies URL template placeholders into YAML defaults (this is how `cp-kraken` happened). `capture_api_output.py` accepts URLs that still contain `{…}`.
7. `register_gates_v2.py --skip-live` works without `ALLOW_UNSAFE_REGISTER=1`. Every other skip flag requires it.
8. `pin_consistency_check.py --file` (a gas gate) crashes with a traceback, not a reason, if any YAML under `intentYamls/` fails to parse.
9. `set_sample_status.py` passes the note as a regex replacement string, so a `\1` or `\g` in a note raises an error.
10. **Duplicate miner id 31004** in `fx-awesomeapi.yaml` and `fx-hnb.yaml`. The node requires unique ids. `fx-hnb` is deregistered, so there is no live clash right now.
11. **Garbage intent descriptions.** 33 samples and 41 YAMLs say "PACK READY - meets 10 candidates; 22 keyless…" where the catalog description should be. That text is what the LLM judge is told the intent means.
12. `ACTIVE_MINERS.xlsx`: the fx-awesomeapi row's "question asked" column holds a translation prompt ("q=The quick brown fox…").
13. Latent: the auto_review body parser only recognises ```` ```json ```` and ```` ```text ```` fences. Any other fence language would be read from the wrong block. Capture only writes those two today.

## 4. Weak

- Correctness is decided by an LLM with no ground truth.
- The hard-check regexes run on the first 600 characters only. `rate.?limit`, `not found`, and `forbidden` can reject valid bodies (for example a payload with a `rate_limit` key) and miss errors further down.
- Format handling is JSON or "text". Capture pretty-prints JSON and stores everything else as text. Every check is `json.loads`. XML, CSV, and HTML answers fall through to the LLM.
- Sample front matter is parsed by hand, in four slightly different copies.
- The proxy hard-codes extraction per venue in Python. Adding a source means editing a 3.4k-line file and redeploying it.

## 5. Duplicated

- The front-matter parser appears in `auto_review_samples.py`, `register_gates_v2.py`, `generate_yamls_from_approved_samples.py`, and `v2_golden_gate.py` (that last one is a weaker variant).
- `v2_golden_gate.py` re-implements `miner_pack/run_golden_tests.py` (`fill`, `jpath`, `to_num`, `call`, `hard_fail`, `extract`).
- The same slug is sampled under two folders for one intent: CRYPTO_PRICE vs CRYPTO_PRICE_LOOKUP, WEATHER_CHECK vs WEATHER_CURRENT, SSL_*, WEB_SEARCH*, *CONTENT_EXTRACTION. That is 24 slugs, and 21 of them have conflicting statuses (one approved, one pending).

## 6. Fragile

- There are no tests (zero test files).
- The gas path depends on a local LLM being up.
- The proxy is the live answer source for about 141 miners. Changing its output changes live answers without changing any on-chain hash.

## 7. Hard constraint that shapes the fix

The node validates every miner YAML against `integration.schema.json` with **`additionalProperties: false`**, both at the top level and inside `semantics`. If I added `answer_type`, extraction rules, or templates to miner YAMLs, **every miner would be rejected on-chain**.

So the new "single source of truth" is a separate MinerCreator-side **intent spec** (`intents/<INTENT>.yaml`). It references registered miners by slug. Hosted miner YAMLs stay in node format and are untouched.

## 8. Plan

1. New stdlib + PyYAML package `minercheck/` with these modules:
   - `spec`: schema-validated loader that fails loudly
   - `normalize`: city, coordinates, coin, currency, timezone
   - `fetch`: timeouts, retry, 429/Retry-After, TTL cache
   - `reader`: format sniffing; JSON path, XPath, CSS, regex, CSV, headers
   - `units`: Decimal, canonical units
   - `validate`: E1–E5
   - `verify`: leave-one-out consensus by publisher, confidence, "could not verify"
   - `render`: YAML templates
   - `scoring`: YAML-configured miner ranking with copy detection
   - `cli`
2. Intent specs for the brief's five example intents: WEATHER_CHECK, CRYPTO_PRICE, FX_NOW, DATE_TODAY, TIME_IN_CITY. Each source is verified against its live API before I write it down. The other 51 intents keep the current path; the new gate reports SKIP for them, not PASS.
3. Wire the verifier into `register_gates_v2.py` as a fail-closed gate for spec'd intents, and into `auto_review` as a deterministic pre-LLM check.
4. Fix bugs 3–9 and 13 above. Fix the local `cp-kraken.yaml`. I will not touch on-chain state (CLAUDE.md forbids direct `cast`), so that needs your gated update.
5. Tests with stdlib `unittest`, no new dependency. Every intent gets mocks in JSON, XML, text, HTML, and CSV, plus wrong-type, wrong-entity, stale, conflict, and broken cases.

## 9. Found during the build (verified live)

- **`fx-frankfurter` depends on a cross-host redirect.** `api.frankfurter.app` now answers 301 → `api.frankfurter.dev`. The node follows it; the register gate refuses it. Fixed locally (needs an on-chain update).
- **The LLM gate blocks correct answers.** qwen2.5:3b judged a correct USD→EUR rate "partial", because the catalog description also asks for spreads. A correct answer can fail gas for reasons unrelated to correctness.
- **System `python3` has no PyYAML.** Run outside the venv, `register-miner-v2.sh` failed closed on `validate_miner_yaml` / `pin_consistency_check`. The script now prefers `.venv/bin/python`.
- **The sample parser truncated 3 bodies** at a ```` ``` ```` inside a JSON string, so those samples never parsed as JSON in auto_review.
- **The content family was judged from the header** (`"json" in Content-Type` → json). A JSON body served as text/html counted as HTML.
- **Weather sources really disagree.** For Lahore at 06:36 UTC: wttr.in said 35 °C; Open-Meteo, MET Norway and the airport METAR said 31.1 / 30.8 / 32. A single-source check would have accepted 35.
- **STOCK_PRICE miners `stock-cnbc`, `stock-nasdaq`, and `stock-yahoo` all default to ticker `BTC`.** That is a real NYSE Arca ETF (Grayscale Bitcoin Mini Trust), but a confusing default for a stock intent. Not changed.
