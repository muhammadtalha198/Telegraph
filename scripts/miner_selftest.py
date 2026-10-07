#!/usr/bin/env python3
"""
Telegraph miner self-test. Checks a candidate against MINER_SCORING_CONTRACT
rules BEFORE on-chain registration. Stdlib only.

Source: Usman, MINER_SCORING_CONTRACT.md §6 (2026-09-23). Keep in sync with it.

  python3 miner_selftest.py --intent GRID_POWER_PRICE \
      --url "https://example/lmp?node=TH_NP15_GEN-APND&market=DAM&interval_start_utc=2026-09-13T14:00:00Z" \
      --truth 38095

  # distinct-source check against an already-registered peer:
  python3 miner_selftest.py --intent FX_NOW --url "<A>" --peer-url "<B>"
"""
import argparse, json, sys, urllib.request, urllib.error

# NON-DETERMINISTIC / adapter: label is text (LLM-judge), not RelTol scalar.
# (label_field, min_len, max_len)
TEXT_INTENTS = {
    "LANGUAGE_TRANSLATION":  ("translated_text", 2, 50_000),
    "TEXT_SUMMARIZATION":    ("summary_text", 8, 50_000),
    "CHATBOT_CONVERSATION":  ("reply_text", 1, 50_000),
    "TEXT_TO_SPEECH":        ("audio_b64", 100, 500_000),
}

# (label_field, scale_note, tolerance_bps, lo, hi) — from MINER_SCORING_CONTRACT §3
INTENTS = {
    "FX_NOW":                   ("rate",                        "x10000",      50, 5e3,  2e4),
    "ROUTE_ETA":                ("eta_seconds",                 "x1",         800, 60,   2e5),
    "MACRO_ECONOMIC_INDICATOR": ("rate_pct",                    "x1000",      150, 1e3,  3e4),
    "LIQUIDITY_DEPTH_VERIFY":   ("liquidity_usd_cents",         "x100",       300, 1e8,  1e13),
    "MINING_HASHPRICE_VERIFY":  ("hashprice_sats_per_ph_s_day", "x1",         400, 2e4,  2e6),
    "GRID_POWER_PRICE":         ("lmp_usd_per_mwh_milli",       "x1000",       30, 5e3,  5e5),
    "LIVE_SHELF_PRICE":         ("price_cents",                 "x100",       300, 20,   2e4),
    "ONCHAIN_METRIC_VERIFY":    ("value_gwei",                  "x1 (Gwei)",    5, 1e6,  1e17),
    "ASSET_RESERVE_ATTESTATION":("attested_reserve",            "x1 (micro)",  150, 1e10, 1e12),
    # Batch 5–6. Tolerance matches local_validate_keepers. Ranges are scale guards.
    "CRYPTO_YIELD_RATE":             ("apy_bps",                 "x100 (bps)", 500, 1,    5e5),
    "EVENT_OUTCOME_RESOLUTION":      ("resolved_yes",            "0/1",          0, 0,    1),
    "THREAT_IP_REPUTATION":          ("listed",                  "0/1",          0, 0,    1),
    "WEATHER_CHECK":                 ("temp_k_x100",             "x100 K",      50, 2e4, 3.5e4),
    "STOCK_PRICE":                   ("last_cents",              "x100",        50, 50,  1e8),
    "TRAVEL_DISRUPTION":             ("disruption_active",       "0/1",          0, 0,    1),
    "DNS_RECORD_LOOKUP":             ("has_record",              "0/1",          0, 0,    1),
    "SSL_VERIFICATION":              ("not_after_epoch",         "unix s",       1, 1.5e9, 2.5e9),
    "PORT_SCAN_AUDIT":               ("port_open",               "0/1",          0, 0,    1),
    "THREAT_INTELLIGENCE":           ("ioc_flagged",             "0/1",          0, 0,    1),
    "AIR_QUALITY_INDEX":             ("pm25_ugm3_x10",           "x10",       1000, 0,    1e4),
    "WEATHER_FORECAST_VERIFY":       ("wind_kmh_milli",          "x1000",     1200, 0,    5e5),
    "GAS_PRICE":                     ("base_fee_gwei_micro",     "x1e6",      1500, 1e3,  1e12),
    "TOKEN_TOTAL_SUPPLY_VERIFY":     ("total_supply_raw",        "base units",   1, 1e3,  1e30),
    "VALIDATOR_PERFORMANCE_VERIFY":  ("effective_balance_gwei",  "gwei",         1, 0,    1e12),
    "LOAN_INTEREST_RATE_QUOTE":      ("rate_bps",                "x100",         1, 1,    5e4),
    "API_HEALTH_CHECK":              ("http_status",             "status",       0, 100,  599),
    "SERVER_UPTIME_MONITOR":         ("is_up",                   "0/1",          0, 0,    1),
    "CLOUD_RESOURCE_USAGE":          ("metric_value",            "raw",        100, 0,    1e16),
    "SENSOR_TELEMETRY_VERIFY":       ("heartbeat_fresh",         "0/1",          0, 0,    1),
    "VESSEL_TELEMETRY_VERIFY":       ("sog_milliknots",          "x1000 kn",   100, 0,    1e6),
    "CARRIER_SERVICEABILITY":        ("deliverable",             "0/1",          0, 0,    1),
    "VENDOR_VERIFY":                 ("id_valid",                "0/1",          0, 0,    1),
    "GRAMMAR_SPELL_CHECK":           ("has_error",               "0/1",          0, 0,    1),
    "REGRESSION_VERIFY":             ("exit_status",             "0/1",          0, 0,    1),
    "CONTENT_EXTRACTION":            ("has_phrase",              "0/1",          0, 0,    1),
    "SENTIMENT_ANALYSIS":            ("is_positive",             "0/1",          0, 0,    1),
    "WEB_SEARCH":                    ("top1_domain_match",       "0/1",          0, 0,    1),
    # Batch 7 Round Two
    "CRYPTO_PRICE":                  ("price_usd_cents",         "x100",       100, 1e5,  1e9),
    "VULNERABILITY_TRIAGE":          ("cvss_base_score_milli",   "x1000",      150, 0,    1e5),
    "CORPORATE_REGISTRY_LOOKUP":     ("status_active",           "0/1",          0, 0,    1),
    "SEMANTIC_SIMILARITY":           ("similarity_x10000",       "x10000",     500, 0,    1e4),
    "TEXT_CLASSIFICATION":           ("top_label_match",         "0/1",          0, 0,    1),
}


def fail(code, msg):
    print(f"FAIL  [{code}] {msg}")
    sys.exit(1)


def get(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "telegraph-selftest/1"})
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        fail("NOT_ASKABLE", f"HTTP {e.code} for {url}")
    except Exception as e:
        fail("NOT_ASKABLE", f"{type(e).__name__}: {e}")


def dig(doc, path):
    """Dotted path, as semantics.signal_mapping.label_field is interpreted."""
    cur = doc
    for part in path.split("."):
        if isinstance(cur, list):
            try:
                cur = cur[int(part)]
            except Exception:
                return None
        elif isinstance(cur, dict):
            if part not in cur:
                return None
            cur = cur[part]
        else:
            return None
    return cur


def as_num(v):
    # Integers/strings are carried exactly; floats above 2^53 are NOT safe
    # (ONCHAIN_METRIC_VERIFY BEACON key) — flagged rather than silently accepted.
    if isinstance(v, bool):
        return None
    if isinstance(v, int):
        return v
    if isinstance(v, float):
        return v
    if isinstance(v, str):
        try:
            return float(v) if ("." in v or "e" in v.lower()) else int(v)
        except ValueError:
            return None
    return None


def bps(miner, truth):
    if truth == 0:
        return None
    return abs(miner - truth) / abs(truth) * 10000.0


def score_bps(e, tol):
    """RelTol curve: 10000 at 0, 5000 at tol, 0 at 2*tol (linear). tol 0 is PassFail."""
    if tol <= 0:
        return 10000.0 if e < 0.5 else 0.0
    if e >= 2 * tol:
        return 0.0
    return 10000.0 * (1.0 - e / (2.0 * tol))


def run_text(a) -> None:
    field, min_len, max_len = TEXT_INTENTS[a.intent]
    field = a.field or field
    print(f"intent={a.intent}  label_field={field}  class=NON-DET/adapter  min_len={min_len}")

    doc = get(a.url)
    raw = dig(doc, field)
    if raw is None:
        keys = list(doc)[:12] if isinstance(doc, dict) else type(doc).__name__
        fail("WRONG_QUANTITY", f"field '{field}' absent. Top-level: {keys}")
    if isinstance(raw, (dict, list)):
        fail("WRONG_QUANTITY", f"field '{field}' is {type(raw).__name__} — need plain text "
                               f"for adapter / LLM-judge (not a nested map)")
    s = str(raw).strip()
    if len(s) < min_len:
        fail("NOT_ASKABLE", f"field '{field}' too short ({len(s)} < {min_len}): {s[:80]!r}")
    if len(s) > max_len:
        fail("WRONG_QUANTITY", f"field '{field}' absurdly long ({len(s)} > {max_len})")
    print(f"value = {s[:160]!r}{'…' if len(s) > 160 else ''}  ({len(s)} chars)")

    if a.peer_url:
        pdoc = get(a.peer_url)
        peer = dig(pdoc, field)
        if peer is None:
            fail("NOT_ASKABLE", f"peer missing field '{field}'")
        ps = str(peer).strip()
        print(f"peer  = {ps[:120]!r}{'…' if len(ps) > 120 else ''}  ({len(ps)} chars)")
        if ps == s and a.intent != "TEXT_TO_SPEECH":
            # Identical free-text across distinct venues is usually the same upstream.
            fail("DUPLICATE", "peer reply identical to candidate — same upstream?")
        if a.intent == "TEXT_TO_SPEECH" and ps == s:
            fail("DUPLICATE", "peer audio_b64 identical — same TTS upstream?")

    print("PASS  (NON-DET text shape + askability; adapter/LLM-judge scores quality)")


def main():
    p = argparse.ArgumentParser()
    choices = sorted(set(INTENTS) | set(TEXT_INTENTS))
    p.add_argument("--intent", required=True, choices=choices)
    p.add_argument("--url", required=True, help="candidate miner URL, pins filled in")
    p.add_argument("--field", help="override label_field (dotted path)")
    p.add_argument("--truth", type=float, help="Usman's truth value, already scaled")
    p.add_argument("--peer-url", help="an already-registered miner, for the DUPLICATE check")
    p.add_argument("--scale", type=float, default=1.0, help="per-miner rescale (YAML signal_mapping.scale)")
    a = p.parse_args()

    if a.intent in TEXT_INTENTS:
        run_text(a)
        return

    field, scale_note, tol, lo, hi = INTENTS[a.intent]
    field = a.field or field
    print(f"intent={a.intent}  label_field={field}  scale={scale_note}  rel_tol={tol}bps")

    doc = get(a.url)
    raw = dig(doc, field)
    # VULNERABILITY_TRIAGE: accept cvss_base_score (0–10) or milli (Group D keepers).
    if raw is None and a.intent == "VULNERABILITY_TRIAGE" and not a.field:
        for alt in ("cvss_base_score_milli", "cvss_base_score"):
            if alt == field:
                continue
            raw = dig(doc, alt)
            if raw is not None:
                field = alt
                print(f"note  using alias label_field={field}")
                break
    if raw is None:
        keys = list(doc)[:12] if isinstance(doc, dict) else type(doc).__name__
        fail("WRONG_QUANTITY", f"field '{field}' absent. Top-level: {keys}")

    # Group D: maps/lists must fail before as_num (Usman toNumber behaviour).
    if isinstance(raw, (dict, list)):
        fail("WRONG_QUANTITY", f"field '{field}' is {type(raw).__name__}, not a number "
                               f"(browse/list response — re-spec to cvss_base_score)")

    val = as_num(raw)
    if val is None:
        fail("WRONG_QUANTITY", f"field '{field}' is not numeric: {raw!r}")
    # Normalize CVSS 0–10 → milli so range/truth checks stay consistent.
    if a.intent == "VULNERABILITY_TRIAGE" and field == "cvss_base_score":
        val = float(val) * 1000.0
        scale_note = "x1000 (from cvss_base_score)"
    val *= a.scale

    if isinstance(val, float) and abs(val) > 2**53:
        print(f"WARN  value {val} exceeds 2^53 as a float — carry it as an integer "
              f"or string end to end, or ONCHAIN_METRIC_VERIFY will fail silently.")

    print(f"value = {val}")
    if not (lo <= abs(val) <= hi):
        fail("WRONG_QUANTITY", f"{val} outside plausible range [{lo:g},{hi:g}] "
                               f"— likely a scale error ({scale_note}) or the wrong quantity")

    if a.peer_url:
        pdoc = get(a.peer_url)
        pval = as_num(dig(pdoc, field))
        if pval is not None:
            pval *= a.scale
            d = bps(val, pval)
            print(f"peer  = {pval}   divergence = {d:.2f} bps" if d is not None else "peer = 0")
            if d is not None and d < tol / 10.0:
                fail("DUPLICATE", f"divergence {d:.2f} bps < {tol/10:.2f} bps (tol/10) — "
                                  f"same upstream. Re-check across 3 pins before accepting.")

    if a.truth is not None:
        e = bps(val, a.truth)
        if e is None:
            fail("NOT_ASKABLE", "truth is zero — ground truth did not resolve")
        s = score_bps(e, tol)
        print(f"truth = {a.truth}   error = {e:.2f} bps   score = {s:.0f}/10000 ({s/10000:.4f})")
        if e < 0.5:
            print("WARN  near-zero divergence from truth — check §2.4: this may be an ORACLE "
                  "(redistributing Usman's truth source), which does not count as a distinct source.")
        if s <= 0:
            fail("WRONG_QUANTITY", f"error {e:.2f} bps >= 2x tolerance ({2*tol} bps) — scores 0")
        print(f"PASS  scores {s/10000:.4f}")
    else:
        print("PASS  (shape + range only; rerun with --truth for an accuracy score)")


if __name__ == "__main__":
    main()
