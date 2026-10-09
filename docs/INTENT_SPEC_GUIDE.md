# Intent specs: adding an intent, a source, or a miner with YAML only

`intents/<INTENT>.yaml` is the single source of truth for **verifying answers**. It covers:
- how an intent is asked
- which free APIs answer it, in priority order
- how to pull the value out of each response
- what a correct answer must look like
- how the plain-English answer is written

These files are **not** miner YAMLs. Hosted miner YAMLs (`intentYamls/`) must stay in node format, because the node rejects unknown keys (`additionalProperties: false`). Intent specs point at miners by slug instead.

Run everything with the venv, because PyYAML is required:

```bash
.venv/bin/python -m minercheck validate-spec
```

| Command | What it does |
|---|---|
| `python -m minercheck validate-spec` | Load and validate every spec. Bad YAML fails loudly with every problem listed. |
| `python -m minercheck ask WEATHER_CHECK location=Lahore unit=F` | One question, plain-English answer (`--json` for details, `-v` per source). |
| `python -m minercheck run-tests [--intent X]` | Run each spec's `tests:` live and record history. |
| `python -m minercheck score [--intent X]` | Rank sources/miners from history. |
| `python -m minercheck gate --file intentYamls/.../x.yaml --intent X` | Verify one miner as the node calls it (also runs inside `register_gates_v2.py`). |
| `.venv/bin/python -m unittest discover -s tests -t .` | All tests, no network. |

---

## 1. Add a new source to an existing intent

Example: add a sixth FX source. Append to `sources:` in `intents/FX_NOW.yaml`. Order matters: sources are tried top to bottom.

```yaml
  - id: hexarate                       # unique inside this spec
    name: Hexarate
    publisher: hexarate.paikama.co     # one vote per publisher; two ECB mirrors = same publisher
    request:
      url: "https://hexarate.paikama.co/api/rates/latest/{base}?target={quote}"
      headers: {}                      # optional
      timeout_s: 15                    # optional
    cache_ttl_s: 3600                  # do not burn the free tier
    rate_limit_per_min: 30             # optional client-side pacing
    free_tier: {requests_per_day: 1000}  # optional; feeds the "headroom" score
    value: [{json: data.mid}]          # where the answer is (rules tried in order)
    timestamp: [{json: data.timestamp}]  # for freshness (E4); optional
    entity:                            # what the answer claims to be about (E5)
      base: [{json: data.base}]
      quote: [{json: data.target}]
```

Then:

```bash
.venv/bin/python -m minercheck validate-spec
.venv/bin/python -m minercheck ask FX_NOW base=USD quote=EUR --all-sources -v
```

The `-v` table shows each source as `ok` (with `agreed` or `disagreed`), `REJ` (with layer and reason), or `ERR` (fetch error).

### Placeholders

URLs, headers, and rules can use `{name}`. The spec loader rejects unknown names.

| Input kind | Placeholders it provides |
|---|---|
| `location` | `{lat}` `{lon}` (4 dp), `{place}`, `{country}`, `{timezone}`, `{bbox}` (±0.3°) |
| `asset` | `{symbol}` `{symbol_lower}` `{asset_name}`, plus every column of `normalize.assets` (e.g. `{coingecko}`, `{kraken}`) |
| `currency` / `enum` / `text` | `{<input name>}` and `{<input name>_lower}` (e.g. `{quote}` and `{quote_lower}`) |
| `timezone` | `{timezone}` `{tz_label}` |

Values are percent-encoded in URLs.

### Extraction rules (any response format)

Each rule has exactly one locator. List several rules and the first that yields a value wins. The format is detected from the body, not the Content-Type header.

| Format | Rule | Example |
|---|---|---|
| JSON | `json: dot.path` | `{json: "result.*.c.0"}`: `*` = first key/item; `[0]`/`.0` index; `-1` last item |
| XML | `xpath:` | `{xpath: ".//item[targetCurrency='{quote}']/exchangeRate"}`; `/@attr` for attributes |
| HTML | `css:` | `{css: "span.ccOutputRslt"}`; `attr:` for an attribute, `index:` for the nth match |
| CSV | `csv: column` | `{csv: price, where: {symbol: "{symbol}"}}` or `{csv: price, row: -1}` |
| Plain text | `regex:` | `{regex: '(?m)^ts=(\d+(?:\.\d+)?)$'}`: group 1 or named group `value` |
| Header | `header:` | `{header: Date}` (a body-less 204 is fine) |

Modifiers on a rule:

| Modifier | Meaning |
|---|---|
| `unit: C` / `"{quote}"` / `USDT` / `cents` / `km/h` | Unit when the value has none. A unit inside the value text wins ("87.8°F"). |
| `scale: 0.01` | Multiply the number. |
| `invert: true` | Use 1/x (an FX rate quoted the other way round). |
| `regex: "…"` | Next to another locator: post-filter the located text. |
| `epoch: s\|ms` | The value is a Unix timestamp. |
| `format: "%Y%m%d%H"` | strptime format. Checked before epoch auto-detection. |
| `tz: UTC` | Zone of a naive timestamp. Allowed for freshness timestamps only. |
| `time_of_day: true` | "06:18 AM" with today's date (yesterday if it would be in the future). |
| `date_order: MDY\|DMY` | For "10/08/2026". Without it an ambiguous date is rejected, never guessed. |

Never guess:
- Broken or truncated JSON or XML is treated as text, so only a `regex` rule can read it.
- A rule that does not fit the format is skipped, and the reason is logged.

---

## 2. Make a registered miner verifiable

Map the miner's slug to the source that calls the same API. `question` is the miner YAML's default question, expressed as spec inputs.

```yaml
  - id: coinbase
    ...
    miner: {slug: cp-coinbase, question: {asset: BTC}}
```

What happens at register time (`register-miner-v2.sh` → `register_gates_v2.py`):

1. The miner YAML is called exactly as the node calls it. `{param}` path placeholders are filled from defaults, and cross-host redirects are refused.
2. The source's rules extract the answer, which then goes through answer type (E5), sanity (E2), freshness (E4), and entity (E5).
3. The other sources are asked the same `question`, and the miner must be in the agreeing majority (E3).
4. If `out/minercheck/history.jsonl` has enough runs, its score must not be DROP.

What the gate prints in each case:

| Situation | Gate result |
|---|---|
| Intent has no spec | **SKIP**: the old LLM gate decides alone |
| Spec exists, slug not mapped | **FAIL**: add the mapping first |

A miner's endpoint may differ slightly from the source URL (Binance `/ticker/price` vs `/ticker/24hr`). Give the source one rule per shape:

```yaml
    value:
      - {json: lastPrice, unit: USDT}     # /ticker/24hr
      - {json: price, unit: USDT}         # /ticker/price (the miner's endpoint)
```

---

## 3. Add a new intent

Copy the closest spec (`intents/WEATHER_CHECK.yaml` for a measurement, `CRYPTO_PRICE.yaml` for a price, `DATE_TODAY.yaml` for a date) to `intents/<INTENT>.yaml`. The file name must equal `intent:`. Then fill in:

```yaml
intent: STOCK_PRICE
aliases: [STOCK_PRICE_QUOTE]          # catalog names that mean the same intent
description: Last trade price of a listed equity.
answer_type: price                    # MANDATORY: temperature | price | fx_rate | number | percent | date | datetime_tz
scope: current

inputs:
  symbol: {kind: text, required: true, description: "Ticker, e.g. AAPL"}
  quote: {kind: currency, required: false, default: USD}

validation:
  sanity: {min: 0.01, max: 1000000}               # canonical unit
  freshness: {max_age_s: 86400, max_future_s: 600}
  entity: {max_km: 60}                            # location intents only
  cross_check:
    tolerance: {rel: 0.01}                        # and/or abs: 0.5
    min_sources: 2                                # >= 2: one source cannot verify itself
    target_sources: 3                             # stop after this many agree (saves free calls)

extras:                                           # optional extra facts
  change_pct: {quantity: percent, signed: true, sanity: {min: -100, max: 1000}}

sources: [ ... at least min_sources publishers ... ]

template:
  answer: "{symbol} last traded at {value}."
  extras: ["Change today: {change_pct}."]         # dropped when no source has the fact
  footer: "Median of {agreeing_count} agreeing independent sources ({agreeing_sources}) at {as_of}. Confidence {confidence}."
  unverified: "I could not verify the price of {symbol}. Reason: {reason}."

tests:
  - {id: aapl, inputs: {symbol: AAPL}}
```

### What each answer_type rejects (E5)

| answer_type | Accepts | Rejects (true but wrong type) |
|---|---|---|
| `temperature` | number + unit (in the text or from `unit:`) | "hot", "56%", "4 km/h", a number with no unit |
| `price` | number + currency; cents scaled; USDT/USDC count as USD | "-2.5%", "up 2.5 percent", a price in another currency |
| `fx_rate` | positive number; `invert` supported | percentages, words |
| `date` | day + month + year; ISO, RFC 2822, "8 October 2026", epoch | "Wednesday", "2026-W41", "this week", "October 8", ambiguous "10/08/2026" |
| `datetime_tz` | time of day + zone from the response (offset, Z, GMT, epoch, or a timezone field) | a date alone; a time with no zone |

Template placeholders: `{value}` (rendered in the user's unit), input placeholders, extras, and:

| Placeholder | Meaning |
|---|---|
| `{agreeing_count}`, `{answered_count}`, `{queried_count}` | Source counts |
| `{agreeing_sources}` | Names of the sources that agreed |
| `{confidence}` | Confidence score |
| `{as_of}` | Time of the check |
| `{primary_source}` | Highest-priority agreeing source |
| `{reason}` | Why the answer is unverified |
| `{weekday}`, `{iso_date}` | `date` answers only |
| `{time}`, `{date}`, `{weekday}`, `{tz_abbr}`, `{utc_offset}`, `{iso}` | `datetime_tz` answers only |

Units for the user's choice (weather example):

```yaml
units:
  canonical: C
  render_input: unit          # the enum input that picks the display unit
  render:
    F: {temperature: F, speed: mph}
```

Shared tables (cities including lookalikes, currencies) live in `intents/_shared.yaml`. Add a city there if the Open-Meteo geocoder picks the wrong one.

After adding the intent:

```bash
.venv/bin/python -m minercheck validate-spec
.venv/bin/python -m minercheck run-tests --intent STOCK_PRICE
.venv/bin/python tests/record_live.py STOCK_PRICE     # freeze real responses as replay fixtures
.venv/bin/python -m unittest discover -s tests -t .
```

For the format matrix, add the intent to `tests/fixtures/formats.py` (one mock source and body per format).

---

## 4. Miner scoring rules: `intents/_scoring.yaml`

Weights, latency bounds, `window_runs`, `min_runs`, `register_at`, `drop_below`, and copy detection are all configured here. Decisions:

| Decision | When |
|---|---|
| REGISTER | score ≥ `register_at` and ≥ `min_runs` judged runs |
| WATCH | score between `drop_below` and `register_at` |
| DROP | score < `drop_below`, a suspected copy, or down in most of ≥ `min_runs` calls |
| INSUFFICIENT_DATA | fewer than `min_runs` judged runs |

The register gate blocks a miner whose history says DROP.

---

## 5. The Intent Catalog is the authority

`Intent Catalog v2 25-Sept (1).xlsx` defines what every intent means. `minercheck catalog build`
parses it into `intents/_catalog.json` (119 intents, all columns). Rebuild it whenever the
workbook changes. Each intent gets a **tier** (rules in `intents/_catalog_policy.yaml`):

| Tier | From the catalog | Gate behaviour |
|---|---|---|
| `required` | DETERMINISTIC or HYBRID (comparator path) | a spec is **required**; no spec ⇒ `FAIL` "no spec for catalog intent X" |
| `judgment` | NON-DETERMINISTIC (adapter only) | `SKIP` — no deterministic truth; the LLM judge decides against the catalog Description |
| `unverifiable` | `Verifiable = No` | `BLOCKED`, quoting the catalog's Verifiability Reason |

```bash
.venv/bin/python -m minercheck catalog build        # xlsx -> intents/_catalog.json
.venv/bin/python -m minercheck catalog table        # intent | tier | description | spec? | Wave2 slugs
.venv/bin/python -m minercheck catalog audit         # every spec vs its catalog row (ALIGNED / DRIFT)
.venv/bin/python -m minercheck catalog show FX_NOW   # full catalog row
.venv/bin/python -m minercheck batch                 # gate every approved Wave2 sample, diff vs last run
```

### Binding a spec to its catalog row (`catalog:` block, required)

Every `intents/<INTENT>.yaml` must carry a `catalog:` block. `catalog audit` fails the spec unless:
- `catalog.intent` is a real catalog intent (or an alias in `_catalog_policy.yaml`);
- `catalog.description` is the row's Description **verbatim** (copy it, don't paraphrase);
- the catalog tier is `required` (a deterministic spec for a judgment/unverifiable intent is a contradiction);
- every clause of the Description is accounted for by a **facet**;
- exactly one facet is `covered_by: value` (the verified answer).

```yaml
catalog:
  intent: CRYPTO_PRICE_LOOKUP
  description: "Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges."
  facets:
    - {text: "real-time spot", covered_by: value, required: true, note: "..."}   # the checked answer
    - {text: "volume-weighted average prices", covered_by: "extra:vwap"}         # a declared extra
    - {text: "across major exchanges", covered_by: none, note: "the cross-check enforces this"}
  allowed_kinds: [cex, dex, dex_indexer, price_aggregator, index]
```

`covered_by`: `value` | `extra:<name>` | `entity:<key>` | `input:<name>` | `none` (with a `note`).
A facet marked `required: true` must be present in the miner's answer or the gate FAILs with the
catalog reason (e.g. COLLATERAL requires a `risk haircut`; a price-only feed fails).

A local verifier that is **not** a catalog intent uses `catalog: {local_only: true, notes: "..."}`
(DATE_TODAY, TIME_IN_CITY).

### Source `kind` and `allowed_kinds`

Every source needs a `kind` (see the list in `_catalog_policy.yaml → source_kinds`). The gate
rejects a miner whose `kind` is not in the spec's `allowed_kinds`, with the catalog reason — this
is how CEX order-book miners fail LIQUIDITY_DEPTH_VERIFY ("decentralized pools").

### Authoritative and conditional sources

- `authority: true` — an official record holder (a national register, an exchange's own
  disclosures). A valid answer from it verifies on its own (`min_sources: 1` is then allowed);
  other sources are compared against it.
- `when: {input: value}` — only query this source when the question matches (e.g. a Nasdaq Nordic
  portal only `when: {market: nasdaq-nordic}`).

### More answer types and rules (added for catalog intents)

| Feature | Use |
|---|---|
| `answer_type: boolean` | yes/no (serviceable, active). `template.yes`/`template.no` wording; rule `map:` / `exists:` turn fields into booleans |
| `answer_type: record_set` | an unordered set (DNS records); cross-check matches the whole set |
| `kind: table` (input) + `normalize.<table>` | per-entity ids/scales (token decimals, per-API series ids), exported as placeholders |
| `each:` / `where:` (json list) | pull a field from every list item, optionally filtered |
| `aggregate: notional` (`price`,`size`,`flat`) | sum price×size over an order book |
| `hex: true` / `map: {...}` / `exists: true` | hex integer, value mapping, presence-as-boolean |
