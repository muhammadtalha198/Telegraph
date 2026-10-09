#!/usr/bin/env python3
"""
Auto-review apiOutputSamples/*.md  (MERGED: per-intent heuristics + universal LLM judge + consensus).

Layers, in order, per sample:
  1. hard checks      empty / HTML page / error-or-rate-limit body                -> rejected
  2. heuristics       per-intent structural checks (fast, free, no LLM)           -> a decisive REJECT (>=0.8) stops here
  3. LLM judge        universal "does this answer the intent?" + extracted answer  (auto if a key exists; --no-llm to skip)
  4. combine          approved only if LLM says answers AND heuristic does not reject; disagreement -> needs_human
  5. consensus        numeric answers for the same subject across >=3 APIs; outliers (>tolerance) -> needs_human
  6. spot-check       a fraction of approvals is held back for a human glance

Default is REPORT ONLY. Add --apply to write status into the sample files.
Usage (from MinerCreator/):
  python3 scripts/auto_review_samples.py                       # report only
  python3 scripts/auto_review_samples.py --apply
  python3 scripts/auto_review_samples.py --apply --intent FX_NOW --spot-check-rate 0.1
  python3 scripts/auto_review_samples.py --no-llm              # heuristics only
Does not register miners. Override with scripts/set_sample_status.py.
"""
from __future__ import annotations
import argparse, json, os, random, re, statistics, sys, time, urllib.error, urllib.request
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "apiOutputSamples"
OUT = ROOT / "out"

_env = ROOT / ".env"
if _env.is_file():
    for line in _env.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k, v = k.strip(), v.strip().strip('"').strip("'")
        # Local judge / endpoint prefs must win over stale shell exports
        if k.startswith(("OLLAMA_", "AUTO_REVIEW_", "OMNIROUTE_REVIEW_", "OPENAI_REVIEW_")):
            os.environ[k] = v
        else:
            os.environ.setdefault(k, v)


@dataclass
class Verdict:
    status: str  # approved | rejected | needs_human
    confidence: float
    reason: str
    mode: str


def parse_sample(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("missing front matter")
    parts = text.split("---", 2)
    fm_raw, body = parts[1], parts[2]
    meta: dict[str, str] = {}
    key = None
    buf: list[str] = []
    for line in fm_raw.splitlines():
        if re.match(r"^[a-z_]+:", line) and not line.startswith(" "):
            if key is not None:
                meta[key] = "\n".join(buf).strip().strip('"')
            key, _, rest = line.partition(":")
            key = key.strip()
            rest = rest.strip()
            if rest == "|":
                buf = []
            else:
                meta[key] = rest.strip('"')
                key = None
                buf = []
        elif key is not None:
            buf.append(line)
    if key is not None:
        meta[key] = "\n".join(buf).strip().strip('"')
    m = re.search(r"```(?:json|text)?\n(.*?)```", body, re.S)
    raw = m.group(1).strip() if m else ""
    parsed = None
    try:
        parsed = json.loads(raw)
    except Exception:
        pass
    return {"meta": meta, "raw": raw, "json": parsed, "path": path, "full": text}


# ---------------------------------------------------------------- layer 1
BAD = [r"^\s*<!doctype html", r"^\s*<html", r"rate.?limit", r"too many requests", r"\bnot found\b",
       r"access denied", r"forbidden", r"unauthorized", r"invalid api key", r"api key.*(required|missing)",
       r"service unavailable", r"\(empty body\)"]


def hard_check(raw: str) -> str | None:
    t = raw.strip()
    if not t or t in ("{}", "[]", "null"):
        return "empty body"
    head = t[:600].lower()
    for pat in BAD:
        if re.search(pat, head, re.I | re.M):
            return f"error-like body ({pat})"
    try:
        o = json.loads(t)
        if isinstance(o, dict) and o.get("error") and len(o) <= 3:
            return "JSON error object"
    except Exception:
        pass
    return None


# ---------------------------------------------------------------- layer 2
def _has_bids_asks(j) -> bool:
    if not isinstance(j, dict):
        if isinstance(j, list) and j and isinstance(j[0], list) and len(j[0]) >= 2:
            return True
        return False
    if "bids" in j and "asks" in j:
        return True
    # KuCoin / Bitget wrap book under data
    data = j.get("data")
    if isinstance(data, dict) and ("bids" in data or "asks" in data):
        return True
    # Bybit spot: result.a / result.b arrays
    res = j.get("result")
    if isinstance(res, dict):
        if ("a" in res and "b" in res) or ("bids" in res and "asks" in res):
            return True
        for v in res.values():
            if isinstance(v, dict) and "bids" in v and "asks" in v:
                return True
    return False


def heuristic(intent: str, meta: dict, j, raw: str) -> Verdict:
    intent = intent.upper()
    low = raw.lower()
    if not raw or raw == "(empty body)":
        return Verdict("rejected", 0.95, "empty response body", "heuristic")

    if intent == "LIQUIDITY_DEPTH_VERIFY":
        # Huge CEX books are often truncated in samples (bids only before 20k cut).
        has_book = (
            _has_bids_asks(j)
            or ('"bids"' in raw and '"asks"' in raw)
            or ("'bids'" in raw and "'asks'" in raw)
            or ('"bids"' in raw and len(raw) >= 15000)  # truncated mid-book
            or ('"asks"' in raw and len(raw) >= 15000)
            or bool(re.search(r'/(book|depth|orderbook)\b', (meta.get("request_url") or ""), re.I) and ('"bids"' in raw or '"asks"' in raw or '"a"' in raw or '"b"' in raw))
        )
        if has_book:
            reason = "Has bid/ask depth for the pair"
            if "decentralized" in (meta.get("intent_description") or "").lower():
                return Verdict("needs_human", 0.55, reason + " — but catalog says decentralized pools; CEX book is partial fit", "heuristic")
            return Verdict("approved", 0.85, reason, "heuristic")
        # DEX pool liquidity (GeckoTerminal / DexScreener) — catalog prefers this over CEX books
        if isinstance(j, dict):
            if j.get("pair") or j.get("pairs"):
                return Verdict("approved", 0.85, "DEX pair liquidity present", "heuristic")
            data = j.get("data")
            if isinstance(data, dict):
                attrs = data.get("attributes") or {}
                if any(k in attrs for k in ("reserve_in_usd", "base_token_price_usd", "fdv_usd", "market_cap_usd")):
                    return Verdict("approved", 0.85, "DEX pool reserves/liquidity present", "heuristic")
            if isinstance(data, list) and data and "reserve_in_usd" in low:
                return Verdict("approved", 0.8, "DEX pool list with reserve/liquidity fields", "heuristic")
        if "liquidity" in low or "reserve_in_usd" in low:
            return Verdict("approved", 0.75, "liquidity-related fields in body", "heuristic")
        return Verdict("rejected", 0.8, "no bid/ask depth or pool liquidity structure found", "heuristic")

    if intent == "ONCHAIN_METRIC_VERIFY":
        if isinstance(j, dict):
            if (
                j.get("coin_balance") is not None
                or j.get("balance") is not None
                or j.get("final_balance") is not None
                or (isinstance(j.get("ETH"), dict) and j["ETH"].get("balance") is not None)
                or j.get("chain_stats") is not None
            ):
                return Verdict("approved", 0.8, "Returns wallet/token balance (partial vs full logs/gas description)", "heuristic")
            result = j.get("result")
            if isinstance(result, str) and (result.startswith("0x") or result.isdigit()):
                return Verdict("approved", 0.8, "Returns on-chain balance/result value", "heuristic")
        return Verdict("rejected", 0.75, "no balance / on-chain value field found", "heuristic")

    if intent == "EVENT_OUTCOME_RESOLUTION":
        if isinstance(j, dict):
            if '"completed": false' in raw or "STATUS_SCHEDULED" in raw:
                # Past-date ESPN boards can mix; if any completed:true also present, continue
                if '"completed": true' not in raw and "STATUS_FINAL" not in raw:
                    return Verdict("rejected", 0.85, "Event is scheduled/not settled — no settled outcome yet", "heuristic")
            if j.get("results") or '"completed": true' in raw or "STATUS_FINAL" in raw:
                return Verdict("approved", 0.8, "Contains settled results / completed event", "heuristic")
            # Polymarket closed / sports APIs
            if j.get("closed") is True:
                return Verdict("approved", 0.8, "Closed/resolved prediction market outcome present", "heuristic")
            if j.get("MRData") or j.get("dates") or j.get("games") or j.get("MatchResults") or j.get("matchResults"):
                return Verdict("approved", 0.75, "Sports schedule/results payload with outcomes", "heuristic")
            if j.get("events") or j.get("event"):
                ev = j.get("events") or j.get("event")
                if isinstance(ev, list) and ev and isinstance(ev[0], dict) and (
                    ev[0].get("strStatus") or ev[0].get("intHomeScore") is not None or ev[0].get("strResult")
                ):
                    return Verdict("approved", 0.75, "Sports event results present", "heuristic")
                return Verdict("needs_human", 0.5, "Has events list but settlement unclear from heuristics", "heuristic")
        if isinstance(j, list) and j and isinstance(j[0], dict):
            if j[0].get("closed") is True or j[0].get("umaResolutionStatus") or j[0].get("outcome"):
                return Verdict("approved", 0.8, "Closed/resolved prediction market list", "heuristic")
            if any(k in j[0] for k in ("matchResults", "team1", "goals", "finalScore", "MatchIsFinished", "pointsTeam1")):
                return Verdict("approved", 0.75, "List of settled match outcomes", "heuristic")
            return Verdict("needs_human", 0.45, "list payload — check settled outcomes", "heuristic")
        return Verdict("needs_human", 0.4, "could not detect settled outcome", "heuristic")

    if intent == "SECURITY_REVIEW":
        if isinstance(j, dict):
            vulns = j.get("vulnerabilities")
            if isinstance(vulns, list) and len(vulns) > 0:
                return Verdict("approved", 0.9, f"Lists {len(vulns)} package vulnerabilities", "heuristic")
            if j.get("advisoryKeys") or j.get("advisories"):
                return Verdict("approved", 0.85, "Package advisory / security keys present", "heuristic")
            # OSV / GHSA advisory document
            if j.get("id") and (j.get("affected") or j.get("severity") or j.get("aliases")):
                return Verdict("approved", 0.85, "OSV/advisory record with affected packages or severity", "heuristic")
            if vulns == []:
                return Verdict("needs_human", 0.5, "vulnerabilities field empty — may still be valid 'no vulns' answer", "heuristic")
            # bare registry metadata without advisories
            if j.get("name") and not (j.get("vulnerabilities") or j.get("advisoryKeys")):
                return Verdict("needs_human", 0.45, "package metadata only — may lack vulnerability list", "heuristic")
        return Verdict("rejected", 0.7, "no vulnerability/advisory signal found", "heuristic")

    if intent == "VULNERABILITY_TRIAGE":
        if isinstance(j, dict) and str(j.get("title", "")).startswith("CISA Catalog"):
            return Verdict("approved", 0.7, "KEV catalog (exploit-in-wild flag); no CVSS — approve as exploit facet only", "heuristic")
        if isinstance(j, dict) and (
            j.get("cvss") is not None or j.get("cvss_v3") is not None or j.get("cvss3") is not None
            or (isinstance(j.get("data"), list) and j["data"] and isinstance(j["data"][0], dict) and "epss" in j["data"][0])
            or j.get("vulnerabilities")  # NVD 2.0
            or j.get("containers")  # CVE.org
            or (j.get("id") and (j.get("severity") or j.get("affected")))  # OSV
            or j.get("cvss3_scoring_vector") is not None or j.get("threat_severity") is not None  # Red Hat
        ):
            return Verdict("approved", 0.9, "Has CVSS and/or EPSS / severity for CVE", "heuristic")
        if isinstance(j, dict) and "packages" in j and ("pkg" in low or "cve" in low):
            return Verdict("approved", 0.8, "distro security DB with package→CVE map", "heuristic")
        if "cve" in low and ("cvss" in low or "epss" in low or "severity" in low):
            return Verdict("approved", 0.75, "CVE severity / exploit fields present in text/JSON", "heuristic")
        return Verdict("rejected", 0.65, "no CVSS/EPSS/KEV severity signal", "heuristic")

    if intent == "CODE_PATCH_VERIFY":
        if isinstance(j, dict) and j.get("workflow_runs"):
            run = j["workflow_runs"][0]
            name = (run.get("name") or "").lower()
            conclusion = run.get("conclusion")
            if conclusion in ("success", "failure", "cancelled", "timed_out"):
                if "lock" in name or run.get("event") == "schedule":
                    return Verdict("rejected", 0.85, f"CI conclusion={conclusion} but workflow '{run.get('name')}' is not patch compile/test", "heuristic")
                return Verdict("approved", 0.8, f"CI/test run conclusion={conclusion} for workflow '{run.get('name')}'", "heuristic")
        if isinstance(j, dict) and j.get("check_runs"):
            cr = j["check_runs"][0] if j["check_runs"] else {}
            if cr.get("conclusion") in ("success", "failure", "neutral", "cancelled", "timed_out"):
                return Verdict("approved", 0.8, f"Commit check-run conclusion={cr.get('conclusion')}", "heuristic")
        if isinstance(j, list) and j and isinstance(j[0], dict) and j[0].get("status") in ("success", "failed", "canceled", "running"):
            return Verdict("approved", 0.8, f"CI pipeline status={j[0].get('status')}", "heuristic")
        if isinstance(j, list) and j and isinstance(j[0], dict) and "outcome" in j[0] and "vcs_url" in j[0]:
            return Verdict("approved", 0.8, f"CircleCI build outcome={j[0].get('outcome')}", "heuristic")
        if isinstance(j, dict) and j.get("status") == "ahead" and j.get("files") is not None:
            return Verdict("needs_human", 0.45, "git compare/diff only — no compile/test pass-fail", "heuristic")
        if isinstance(j, list) and j and isinstance(j[0], dict) and j[0].get("language"):
            return Verdict("rejected", 0.8, "runtime catalog only — not a patch pass/fail result", "heuristic")
        if re.search(r'"exit_status"|compile|pass|fail', low):
            return Verdict("needs_human", 0.5, "possible pass/fail signal — check manually", "heuristic")
        return Verdict("rejected", 0.7, "no clear build/test pass-fail for a patch", "heuristic")

    if intent == "OPTIMAL_EXECUTION_ROUTE":
        if isinstance(j, dict):
            if j.get("priceRoute") or j.get("route") or (isinstance(j.get("data"), dict) and j["data"].get("routeSummary")):
                return Verdict("approved", 0.85, "Swap route / price route present", "heuristic")
            est = j.get("estimate") or {}
            if (
                j.get("toAmount") or est.get("toAmount") or j.get("buyAmount") or j.get("outAmount")
                or j.get("assumedAmountOut") or j.get("swapPrice") is not None
            ):
                return Verdict("approved", 0.85, "Route quote output amount present", "heuristic")
            if j.get("quoteId") and j.get("status") in ("SIG_SUCCESS", "Success", "success"):
                return Verdict("approved", 0.8, "Aggregator quote success with quoteId", "heuristic")
        if "toamount" in low or "buyamount" in low or "priceroute" in low or "assumedamountout" in low:
            return Verdict("approved", 0.75, "Route quote fields in body", "heuristic")
        return Verdict("rejected", 0.75, "no swap route / output amount found", "heuristic")

    if intent == "CROSS_CHAIN_STATE_VERIFY":
        if isinstance(j, dict):
            if j.get("operations") or j.get("deposits") or j.get("requests") or j.get("data"):
                return Verdict("approved", 0.8, "Cross-chain operations/transfers/status list present", "heuristic")
            if j.get("status") in ("DONE", "SUCCESS", "success", "PENDING", "FAILED") or j.get("bridge"):
                return Verdict("approved", 0.8, "Bridge transfer status present", "heuristic")
            if j.get("estimatedFillTimeSec") is not None or j.get("relayGasFeePct") is not None:
                return Verdict("needs_human", 0.5, "bridge fee/ETA quote only — not fill execution status", "heuristic")
        if isinstance(j, list) and j and isinstance(j[0], dict):
            if any(k in j[0] for k in ("depositId", "relayHash", "originChainId", "destinationChainId", "emitterChain", "status")):
                return Verdict("approved", 0.8, "Cross-chain deposit/transfer records present", "heuristic")
        return Verdict("needs_human", 0.4, "could not detect cross-chain execution status", "heuristic")

    # NOTE: no length-based reject: valid answers can be tiny (e.g. '{"price":"64000"}' or 'Lahore: +30C').
    return Verdict("needs_human", 0.35, "no intent-specific heuristic — LLM judge decides", "heuristic")


# ---------------------------------------------------------------- layer 3
JUDGE_SYS = (
    "You are a strict verifier for an API-miner registry (Telegraph Semantic Register V2). Decide whether an API "
    "response ANSWERS the intent for the input given. Format, unit, currency, language and verbosity do NOT matter; "
    "only whether the response actually contains the requested information. Respond ONLY with JSON: "
    '{"verdict":"answers|partial|no","confidence":0-1,"subject":"short normalized subject e.g. BTC/USD price",'
    '"value":number or null (main numeric answer),"unit":"unit/currency or empty","answer_text":"one-sentence plain answer",'
    '"reason":"<=20 words"}. partial = on-topic but only a facet / needs more data. no = off-topic, error, wrong subject, '
    "or scheduled-not-settled. Do NOT echo or copy the API response JSON."
)


def _extract_judge_json(text: str) -> dict:
    """Parse judge JSON; ignore echoed API payloads that lack a verdict field."""
    text = (text or "").strip()
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S)
    candidates: list[str] = []
    if fenced:
        candidates.append(fenced.group(1))
    # compact objects that already include verdict
    candidates.extend(m.group(0) for m in re.finditer(r"\{[^{}]*\"verdict\"\s*:\s*\"[^\"]+\"[^{}]*\}", text, re.S))
    # brace-balanced object around first "verdict"
    idx = text.find('"verdict"')
    if idx >= 0:
        start = text.rfind("{", 0, idx)
        if start >= 0:
            depth = 0
            for i in range(start, len(text)):
                ch = text[i]
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                    if depth == 0:
                        candidates.append(text[start : i + 1])
                        break
    seen: set[str] = set()
    for c in candidates:
        if c in seen:
            continue
        seen.add(c)
        try:
            j = json.loads(c)
        except Exception:
            continue
        if isinstance(j, dict) and j.get("verdict"):
            v = str(j.get("verdict")).strip().lower()
            # small models sometimes echo the schema enum literally
            if v in ("answers|partial", "answers|partial|no", "answer", "yes", "true"):
                j["verdict"] = "answers"
                v = "answers"
            elif v.startswith("answers"):
                j["verdict"] = "answers"
                v = "answers"
            elif v.startswith("partial"):
                j["verdict"] = "partial"
                v = "partial"
            elif v.startswith("no"):
                j["verdict"] = "no"
                v = "no"
            if v in ("answers", "partial", "no"):
                return j
    raise ValueError(f"no judge verdict JSON in model output: {text[:180]!r}")


_ollama_ok: bool | None = None


def ollama_root() -> str:
    """Ollama server root (no /v1). Default localhost."""
    raw = (
        os.environ.get("OLLAMA_BASE_URL")
        or os.environ.get("OLLAMA_HOST")
        or "http://127.0.0.1:11434"
    ).strip().rstrip("/")
    if raw.endswith("/v1"):
        raw = raw[:-3].rstrip("/")
    return raw


def ollama_available() -> bool:
    """True if local Ollama is configured/reachable."""
    global _ollama_ok
    if os.environ.get("AUTO_REVIEW_DISABLE_OLLAMA", "").strip().lower() in ("1", "true", "yes"):
        return False
    # Explicit config = available (probe can fail under sandbox; chat call is the real check)
    if os.environ.get("OLLAMA_BASE_URL", "").strip() or os.environ.get("OLLAMA_HOST", "").strip():
        return True
    if _ollama_ok is not None:
        return _ollama_ok
    try:
        req = urllib.request.Request(f"{ollama_root()}/api/tags", method="GET")
        with urllib.request.urlopen(req, timeout=2) as r:
            _ollama_ok = 200 <= getattr(r, "status", 200) < 300
    except Exception:
        _ollama_ok = False
    return _ollama_ok


def llm_judge(intent: str, meta: dict, raw: str) -> dict | None:
    omni, oai = os.environ.get("OMNIROUTE_API_KEY", "").strip(), os.environ.get("OPENAI_API_KEY", "").strip()
    base = os.environ.get("BASE_URL", "https://omni-chat.13.237.89.59.sslip.io").rstrip("/")
    use_ollama = ollama_available()
    if not (omni or oai or use_ollama):
        return None
    prompt = (f"INTENT: {intent}\nDESCRIPTION: {meta.get('intent_description','')}\n"
              f"A CORRECT ANSWER MUST CONVEY: {meta.get('answer_requirement','')}\nINPUT USED: {meta.get('inputs','')}\n"
              f"REQUEST URL: {meta.get('request_url','')}\n\nAPI RESPONSE (may be truncated):\n{raw[:3500]}")
    # Prefer local Ollama, then OmniRoute, then OpenAI (override with AUTO_REVIEW_PREFER_*).
    endpoints: list[tuple[str, str, str]] = []
    prefer_oai = os.environ.get("AUTO_REVIEW_PREFER_OPENAI", "").strip().lower() in ("1", "true", "yes")
    prefer_omni = os.environ.get("AUTO_REVIEW_PREFER_OMNI", "").strip().lower() in ("1", "true", "yes")
    prefer_ollama = os.environ.get("AUTO_REVIEW_PREFER_OLLAMA", "1").strip().lower() in ("1", "true", "yes")
    cloud_fallback = os.environ.get("AUTO_REVIEW_ALLOW_CLOUD_FALLBACK", "").strip().lower() in ("1", "true", "yes")
    ollama_model = os.environ.get("OLLAMA_REVIEW_MODEL") or "qwen2.5:3b"
    oai_model = os.environ.get("OPENAI_REVIEW_MODEL", "gpt-4o-mini")
    omni_model = os.environ.get("OMNIROUTE_REVIEW_MODEL") or os.environ.get("AUTO_REVIEW_MODEL", "auto/cheap")

    def add_ollama() -> None:
        if use_ollama:
            endpoints.append(
                (f"{ollama_root()}/v1/chat/completions", "ollama", ollama_model)
            )

    def add_omni() -> None:
        if omni:
            endpoints.append((f"{base}/v1/chat/completions", omni, omni_model))

    def add_oai() -> None:
        if oai:
            endpoints.append(("https://api.openai.com/v1/chat/completions", oai, oai_model))

    if prefer_ollama and use_ollama and not prefer_oai and not prefer_omni:
        add_ollama()
        if cloud_fallback:
            add_omni(); add_oai()
    elif prefer_oai:
        add_oai()
        if cloud_fallback or not use_ollama:
            add_ollama(); add_omni()
        elif use_ollama:
            add_ollama()
    elif prefer_omni:
        add_omni()
        if cloud_fallback or not use_ollama:
            add_ollama(); add_oai()
        elif use_ollama:
            add_ollama()
    else:
        add_ollama(); add_omni(); add_oai()

    last_err = None
    for url, key, model in endpoints:
        body = {"model": model, "temperature": 0, "messages": [{"role": "system", "content": JUDGE_SYS}, {"role": "user", "content": prompt}]}
        # Local 3B can be slower than cloud; give Ollama more time.
        timeout = 180 if "11434" in url or "ollama" in url.lower() else 90
        if "11434" in url:
            body["response_format"] = {"type": "json_object"}
        for attempt in range(1, 4):
            req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST", headers={
                "Authorization": f"Bearer {key}", "Content-Type": "application/json", "User-Agent": "telegraph-auto-review/2"})
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    text = json.loads(r.read().decode())["choices"][0]["message"]["content"]
                j = _extract_judge_json(text)
                j["_model"] = model
                j["_endpoint"] = url.split("/")[2]
                return j
            except urllib.error.HTTPError as e:
                last_err = e
                body_txt = ""
                try:
                    body_txt = e.read().decode("utf-8", "replace")[:200]
                except Exception:
                    pass
                print(f"WARN  LLM judge via {url.split('/')[2]} attempt {attempt}: HTTP {e.code} {body_txt}", file=sys.stderr)
                if e.code in (429, 502, 503, 529) and attempt < 3:
                    time.sleep(2 ** attempt * 2)
                    continue
                break
            except Exception as e:
                last_err = e
                print(f"WARN  LLM judge via {url.split('/')[2]} failed: {type(e).__name__}: {e}", file=sys.stderr)
                break
    if last_err:
        print(f"WARN  LLM judge all endpoints failed: {type(last_err).__name__}: {last_err}", file=sys.stderr)
    return None


# ---------------------------------------------------------------- layer 4
def decide(intent: str, meta: dict, s: dict, use_llm: bool, min_conf: float):
    bad = hard_check(s["raw"])
    if bad:
        return Verdict("rejected", 0.95, bad, "hard-check"), None
    h = heuristic(intent, meta, s["json"], s["raw"])
    if h.status == "rejected" and h.confidence >= 0.8:
        return h, None
    j = llm_judge(intent, meta, s["raw"]) if use_llm else None
    if j is None:
        return h, None  # heuristics only
    v, c, why = j.get("verdict"), float(j.get("confidence", 0) or 0), j.get("reason", "")
    if v == "answers" and c >= min_conf:
        if h.status == "rejected":
            return Verdict("needs_human", 0.5, f"LLM says answers, heuristic rejects: {h.reason}", "heuristic+llm"), j
        return Verdict("approved", c, why + (f" | heuristic: {h.reason}" if h.status == "approved" else ""), "heuristic+llm"), j
    if v == "no" and c >= min_conf:
        if h.status == "approved":
            return Verdict("needs_human", 0.5, f"LLM says no ({why}), heuristic approves: {h.reason}", "heuristic+llm"), j
        return Verdict("rejected", c, why, "heuristic+llm"), j
    return Verdict("needs_human", c, f"LLM verdict={v} conf={c}: {why}", "heuristic+llm"), j


# ---------------------------------------------------------------- writing
def replace_or_add(fm: str, key: str, value: str) -> str:
    pat = re.compile(rf"(?m)^{re.escape(key)}:\s*.*$")
    safe = value.replace("\\", "\\\\").replace('"', "'")
    line = f'{key}: "{safe}"' if key in ("reviewer_note", "capture_note") else f"{key}: {value}"
    return pat.sub(lambda _m: line, fm, count=1) if pat.search(fm) else fm.rstrip() + "\n" + line + "\n"


def apply_status(path: Path, status: str, note: str, *, mode: str = "auto_review", confidence: float | None = None, llm_used: bool = False) -> None:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    fm, body = parts[1], parts[2]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    fm = replace_or_add(fm, "status", status)
    fm = replace_or_add(fm, "reviewed_at", now if status != "pending_review" else '""')
    fm = replace_or_add(fm, "reviewer_note", f"auto_review: {note}"[:500])
    fm = replace_or_add(fm, "review_source", "auto_review")
    fm = replace_or_add(fm, "review_mode", mode)
    fm = replace_or_add(fm, "llm_used", "true" if llm_used else "false")
    if confidence is not None:
        fm = replace_or_add(fm, "review_confidence", f"{confidence:.3f}")
    if "## Why this matches" in body:
        body = re.sub(r"(## Why this matches \(or not\)\n\n).*", lambda m: m.group(1) + f"_{note}_\n", body, count=1, flags=re.S)
    path.write_text(f"---{fm}---{body}", encoding="utf-8")


def llm_available() -> bool:
    return bool(
        os.environ.get("OMNIROUTE_API_KEY", "").strip()
        or os.environ.get("OPENAI_API_KEY", "").strip()
        or ollama_available()
    )


def review_sample_path(
    path: Path,
    *,
    use_llm: bool = True,
    apply: bool = False,
    min_confidence: float = 0.75,
    require_llm: bool = False,
) -> tuple[Verdict, dict | None]:
    """Review one sample. Used by register_gates_v2 (fail-closed)."""
    if require_llm and use_llm and not llm_available():
        return Verdict(
            "rejected",
            1.0,
            "LLM required (Ollama local, OMNIROUTE_API_KEY, or OPENAI_API_KEY) — register gate refuses heuristics-only",
            "gate",
        ), None
    s = parse_sample(path)
    meta = s["meta"]
    intent = meta.get("intent") or path.parent.name
    v, j = decide(intent, meta, s, use_llm, min_confidence)
    if use_llm and llm_available() and j is None and v.mode == "heuristic":
        # LLM was requested but failed — do not treat heuristic needs_human as gate-pass
        if v.status != "rejected":
            v = Verdict("needs_human", 0.4, f"LLM judge unavailable/failed; heuristic={v.status}: {v.reason}", "gate")
    if apply and v.status in ("approved", "rejected"):
        llm_used = bool(j) or ("llm" in (v.mode or ""))
        apply_status(
            path,
            v.status,
            f"[{v.confidence:.2f}|{v.mode}] {v.reason}",
            mode=v.mode,
            confidence=v.confidence,
            llm_used=llm_used,
        )
    return v, j


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="review approved/rejected too (default: pending_review only)")
    ap.add_argument("--no-llm", action="store_true", help="heuristics only (NOT allowed for register gates)")
    ap.add_argument("--llm", action="store_true", help="(compat) LLM is on automatically when a key exists")
    ap.add_argument("--require-llm", action="store_true", help="fail samples if no LLM key (batch / gate mode)")
    ap.add_argument("--apply", action="store_true", help="write status into sample files")
    ap.add_argument("--min-confidence", type=float, default=0.75)
    ap.add_argument("--tolerance", type=float, default=0.05, help="numeric consensus tolerance vs median")
    ap.add_argument("--spot-check-rate", type=float, default=0.0, help="fraction of approvals held for human glance (suggest 0.1)")
    ap.add_argument("--intent", default="")
    ap.add_argument("--slug", default="", help="only this slug")
    ap.add_argument("--file", type=Path, default=None, help="review a single sample path (exit 0 only if approved)")
    ap.add_argument("--gate", action="store_true", help="single-file gate mode: require LLM + apply + exit 1 unless approved")
    a = ap.parse_args()

    if a.gate:
        if not a.file:
            print("FAIL  --gate requires --file", file=sys.stderr)
            return 1
        path = a.file if a.file.is_absolute() else ROOT / a.file
        v, _j = review_sample_path(
            path,
            use_llm=not a.no_llm,
            apply=True,
            min_confidence=a.min_confidence,
            require_llm=True,
        )
        print(f"{v.status.upper():12} conf={v.confidence:.2f} {path} {v.reason[:120]}")
        return 0 if v.status == "approved" else 1

    if a.require_llm and not a.no_llm and not llm_available():
        print("FAIL  --require-llm set but no Ollama / OMNIROUTE_API_KEY / OPENAI_API_KEY", file=sys.stderr)
        return 1

    files = sorted(p for p in SAMPLES.rglob("*.md") if p.name not in ("_TEMPLATE.md", "README.md")
                   and (not a.intent or a.intent.upper() in p.parent.name.upper())
                   and (not a.slug or p.stem == a.slug))
    if a.file:
        fp = a.file if a.file.is_absolute() else ROOT / a.file
        files = [fp]

    rows, counts = [], defaultdict(int)
    for path in files:
        try:
            s = parse_sample(path)
        except Exception as e:
            print(f"SKIP  {path}: {e}"); counts["skipped"] += 1; continue
        meta = s["meta"]
        if not a.all and not a.file and (meta.get("status") or "").strip() not in ("pending_review", ""):
            counts["skipped"] += 1; continue
        intent = meta.get("intent") or path.parent.name
        use_llm = not a.no_llm
        if a.require_llm and use_llm and not llm_available():
            v, j = Verdict("rejected", 1.0, "LLM key required", "gate"), None
        else:
            v, j = decide(intent, meta, s, use_llm, a.min_confidence)
            if use_llm and llm_available() and j is None and v.status != "rejected" and "hard" not in v.mode:
                v = Verdict("needs_human", 0.4, f"LLM judge failed; heuristic={v.status}: {v.reason}", "gate")
        rows.append(dict(path=path, intent=intent, slug=meta.get("slug", path.stem), v=v, j=j, applied=False))

    groups = defaultdict(list)  # consensus
    for r in rows:
        j = r["j"]
        if r["v"].status == "approved" and j and isinstance(j.get("value"), (int, float)):
            groups[(r["intent"], str(j.get("subject", "")).lower().strip(), str(j.get("unit", "")).lower().strip())].append(r)
    for g in groups.values():
        if len(g) >= 3:
            med = statistics.median(x["j"]["value"] for x in g)
            for x in g:
                if med and abs(x["j"]["value"] - med) / abs(med) > a.tolerance:
                    x["v"] = Verdict("needs_human", 0.5, f"outlier vs consensus: {x['j']['value']} vs median {med} ({len(g)} APIs)", "consensus")
    random.seed(7)
    for r in rows:
        if r["v"].status == "approved" and random.random() < a.spot_check_rate:
            r["v"] = Verdict("needs_human", r["v"].confidence, "spot-check: auto-approved, held for human glance", "spot-check")

    for r in rows:
        v = r["v"]; counts[v.status] += 1
        if a.apply and v.status in ("approved", "rejected") and (v.status == "rejected" or v.confidence >= a.min_confidence):
            llm_used = bool(r["j"]) or ("llm" in (v.mode or ""))
            apply_status(
                r["path"],
                v.status,
                f"[{v.confidence:.2f}|{v.mode}] {v.reason}",
                mode=v.mode,
                confidence=v.confidence,
                llm_used=llm_used,
            )
            r["applied"] = True
        print(f"{v.status.upper():12} conf={v.confidence:.2f} {r['path'].relative_to(ROOT)} {'(applied) ' if r['applied'] else ''}{v.reason[:100]}")

    OUT.mkdir(exist_ok=True)
    report = OUT / f"AUTO_REVIEW-{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.md"
    L = ["# Auto-review report", "", f"Generated: {datetime.now(timezone.utc).isoformat()}",
         f"Apply={a.apply}  LLM={not a.no_llm}  require_llm={a.require_llm}  min_confidence={a.min_confidence}  spot_check={a.spot_check_rate}", "",
         "| approved | rejected | needs_human | skipped |", "|---:|---:|---:|---:|",
         f"| {counts['approved']} | {counts['rejected']} | {counts['needs_human']} | {counts['skipped']} |", "",
         "| Intent | Slug | Verdict | Conf | Mode | Extracted answer | Reason |", "|---|---|---|---:|---|---|---|"]
    for r in sorted(rows, key=lambda x: (x["v"].status, x["intent"])):
        v, j = r["v"], r["j"] or {}
        L.append(f"| `{r['intent']}` | `{r['slug']}` | **{v.status}** | {v.confidence:.2f} | {v.mode} | "
                 f"{str(j.get('answer_text',''))[:70].replace('|','/')} | {v.reason[:100].replace('|','/')} |")
    L += ["", "## Next",
          "- `needs_human` / `rejected` → fix capture or drop; **do not register**.",
          "- Manual `set_sample_status.py approved` does **not** unlock gas — `register_gates_v2` re-runs auto_review+LLM.",
          "- Register only after auto_review **approved**: `./scripts/register-miner-v2.sh … --sample …`", ""]
    report.write_text("\n".join(L), encoding="utf-8")
    print(f"\nWROTE  {report.relative_to(ROOT)}\nsummary  approved={counts['approved']} rejected={counts['rejected']} "
          f"needs_human={counts['needs_human']} skipped={counts['skipped']}")
    if a.file or a.slug:
        return 0 if counts["approved"] > 0 and counts["rejected"] == 0 and counts["needs_human"] == 0 else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
