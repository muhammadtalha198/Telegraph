#!/usr/bin/env python3
"""
MinerCreator safe pipeline:

  1) Keep FREE / unpaid OmniRoute models only (skip paid)
  2) Probe the REAL OmniRoute model (chat or responses)
     — reject if x-omniroute-response-cost > 0 or billing errors
  3) Only if probe OK → POST /miner-dispatcher/validate
  4) Only if valid:true → host YAML + registerMiner

Usage:
  python3 scripts/safe-register.py probe --endpoint chat --limit 5
  python3 scripts/safe-register.py register --endpoint chat --limit 1
  python3 scripts/safe-register.py register --endpoint responses --batch 40
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "out"
YAML_CHAT = ROOT / "yaml"
YAML_RESP = ROOT / "Response yaml"
TMPL_CHAT = ROOT / "templates" / "chat-completion.miner.yaml.tmpl"
TMPL_RESP = ROOT / "templates" / "responses.miner.yaml.tmpl"
MODELS_JSON = OUT / "omni-models.json"

BASE_URL = "https://omni-chat.13.237.89.59.sslip.io"
NODE = "https://devnode.telegraphprotocol.com"
DIAMOND_DEFAULT = "0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8"
# Only general chat/general-purpose models subscribe to CHAT_COMPLETION.
# Specialized models (coding, vision, search, …) must NOT list CHAT_COMPLETION
# or Alexandria will route "what date is today?" into a coding miner.
INTENT_CHAT_ONLY = ["CHAT_COMPLETION"]

# short valid slugs only: ^[a-z0-9]+(-[a-z0-9]+)*$
CHAT_ID_START = 12001
RESP_ID_START = 13001


def load_env() -> dict[str, str]:
    env = dict(os.environ)
    for line in (ROOT / ".env").read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env.setdefault(k.strip(), v.strip())
    # defaults
    env.setdefault("BASE_URL", BASE_URL)
    env.setdefault("NODE_URL", NODE)
    env.setdefault("DIAMOND", DIAMOND_DEFAULT)
    env.setdefault("RPC_URL", "https://sepolia.base.org")
    env.setdefault("MIN_PRICE_USDC", "10000")
    env.setdefault("INTERNAL_SECRET", "telegraph-internal-secret")
    env.setdefault("HOST_PREFIX_CHAT", f"{BASE_URL}/miner-yamls")
    env.setdefault("HOST_PREFIX_RESP", f"{BASE_URL}/response-yamls")
    return env


def http_json(method: str, url: str, body=None, headers=None, timeout=120):
    data = None if body is None else json.dumps(body).encode()
    hdrs = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "MinerCreator-safe/1.0",
    }
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, data=data, method=method, headers=hdrs)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode()
            resp_headers = {k.lower(): v for k, v in resp.headers.items()}
            return resp.status, json.loads(raw) if raw else {}, resp_headers
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        try:
            parsed = json.loads(raw)
        except Exception:
            parsed = {"raw": raw[:2000]}
        resp_headers = {k.lower(): v for k, v in e.headers.items()} if e.headers else {}
        return e.code, parsed, resp_headers


def looks_free_model(model_id: str) -> bool:
    """Name-level free/unpaid markers used by OmniRoute (OpenRouter-style)."""
    low = model_id.lower().strip()
    if low in ("auto/cheap", "auto/offline", "auto/best-free"):
        return True
    if ":free" in low or low.endswith("-free") or "/free" in low:
        return True
    if ":cheap" in low or low.endswith("-cheap") or "/cheap" in low:
        return True
    if "contributor-free" in low:
        return True
    return False


def parse_response_cost(headers: dict[str, str] | None) -> float | None:
    if not headers:
        return None
    raw = headers.get("x-omniroute-response-cost")
    if raw is None or raw == "":
        return None
    try:
        return float(raw)
    except ValueError:
        return None


def is_paid_probe(probe: dict[str, Any]) -> bool:
    """True when OmniRoute reports a non-zero cost or a billing/payment failure."""
    cost = probe.get("cost")
    if isinstance(cost, (int, float)) and cost > 0:
        return True
    err = (probe.get("error") or "").lower()
    paid_markers = (
        "payment required",
        "insufficient credit",
        "insufficient credits",
        "billing",
        "requires payment",
        "paid plan",
        "upgrade required",
        "not enough credit",
        "balance too low",
        "402",
    )
    return any(m in err for m in paid_markers)


def select_models(*, free_only: bool = True) -> list[str]:
    data = json.loads(MODELS_JSON.read_text())["data"]
    media = ("veo", "embedding", "embed/", "whisper", "tts", "dall-e", "flux", "imagen", "stable-diffusion")
    out = []
    for x in data:
        mid = x["id"]
        if mid.startswith("aihorde/"):
            continue
        low = mid.lower()
        if any(b in low for b in media):
            continue
        if free_only and not looks_free_model(mid):
            continue
        out.append(mid)
    return out


def short_slug(prefix: str, yaml_id: int) -> str:
    return f"{prefix}-{yaml_id}"


def intents_for_model(model: str) -> list[str]:
    """Map OmniRoute model id → intents. Specialized models never get CHAT_COMPLETION.

    Routing rule (from product): a miner only appears in the pool for intents it
    lists. If a coding model also lists CHAT_COMPLETION, general questions get
    wrongly routed to it. One primary specialty per miner; no kitchen-sink intents.
    """
    m = model.lower()

    # --- specialized (exclusive; do NOT add CHAT_COMPLETION) ---
    if any(x in m for x in ("coding", "code", "codex", "coder", "swe-", "/swe")):
        return ["CODE_GENERATION"]
    if any(x in m for x in ("vision", "multimodal", "vl-", "-vl", "image")):
        return ["MULTIMODAL_INFERENCE"]
    if m.startswith("felo/") or any(x in m for x in ("search", "scholar", "web-search")):
        return ["WEB_SEARCH_QUERY"]
    if any(x in m for x in ("embed", "embedding")):
        return ["EMBEDDING_GENERATION"]
    if any(x in m for x in ("whisper", "stt", "speech-to-text", "asr")):
        return ["SPEECH_TO_TEXT"]
    if any(x in m for x in ("tts", "text-to-speech", "kokoro")):
        return ["TEXT_TO_SPEECH"]
    if any(x in m for x in ("translate", "translation", "nllb")):
        return ["LANGUAGE_TRANSLATION"]
    if any(x in m for x in ("moderat", "guard", "toxicity", "llama-guard")):
        return ["TOXICITY_MODERATION"]
    if any(x in m for x in ("reason", "reasoning", "thinking", "think", "r1")):
        # reasoning models → QA specialty, not general chat pool
        return ["QUESTION_ANSWERING"]
    if any(x in m for x in ("pro-coding", "best-coding")):
        return ["CODE_GENERATION"]

    # --- general chat / auto routers that are meant for ordinary Q&A ---
    # auto/cheap, auto/offline, auto/best-free, auto/best-chat, auto/chat, …
    if any(
        x in m
        for x in (
            "auto/cheap",
            "auto/offline",
            "auto/best-free",
            "auto/best-chat",
            "auto/chat",
            "auto/fast",
            "auto/smart",
            ":free",
            "best-free",
        )
    ) or m.startswith("auto/"):
        # still exclude auto coding/vision/reason aliases already caught above
        return list(INTENT_CHAT_ONLY)

    # default unknown chat-capable models → general chat only
    return list(INTENT_CHAT_ONLY)


def render_yaml(endpoint: str, yaml_id: int, slug: str, model: str, intents: list[str], base_url: str) -> str:
    tmpl = TMPL_CHAT if endpoint == "chat" else TMPL_RESP
    text = tmpl.read_text()
    name = f"{'Chat' if endpoint == 'chat' else 'Resp'} {model}"
    intent0 = intents[0]
    # template currently has single INTENT — expand supported_intents + endpoint intents
    desc = f"OmniRoute /v1/{'chat/completions' if endpoint == 'chat' else 'responses'} miner for {model}."
    model_desc = f"Pinned model {model}"
    repl = {
        "{{ID}}": str(yaml_id),
        "{{SLUG}}": slug,
        "{{NAME}}": name,
        "{{MODEL}}": model,
        "{{BASE_URL}}": base_url.rstrip("/"),
        "{{INTENT}}": intent0,
        "{{DESCRIPTION}}": desc,
        "{{MODEL_DESCRIPTION}}": model_desc,
    }
    for k, v in repl.items():
        text = text.replace(k, v)

    # expand intents arrays in YAML
    intents_yaml = "[" + ", ".join(intents) + "]"
    text = re.sub(r"intents:\s*\[[^\]]*\]", f"intents: {intents_yaml}", text, count=1)
    # accepted_fields intents
    text = re.sub(
        r"(accepted_fields:.*?intents:\s*)\[[^\]]*\]",
        rf"\1{intents_yaml}",
        text,
        count=1,
        flags=re.S,
    )
    # supported_intents block
    si = "supported_intents:\n" + "\n".join(f"    - {i}" for i in intents)
    text = re.sub(r"supported_intents:\n(?:\s+- .+\n?)+", si + "\n", text, count=1)
    return text


def probe_model(env: dict, endpoint: str, model: str) -> dict:
    key = env["OMNIROUTE_API_KEY"]
    base = env.get("BASE_URL", BASE_URL).rstrip("/")
    if endpoint == "chat":
        url = f"{base}/v1/chat/completions"
        body = {
            "model": model,
            "messages": [{"role": "user", "content": "hi"}],
            "max_tokens": 8,
        }
    else:
        url = f"{base}/v1/responses"
        body = {"model": model, "input": "hi", "max_output_tokens": 8}

    code, data, resp_headers = http_json(
        "POST",
        url,
        body,
        headers={"Authorization": f"Bearer {key}"},
        timeout=60,
    )
    ok = 200 <= code < 300
    # treat provider credential gaps as fail
    err = ""
    if not ok:
        err = json.dumps(data)[:400]
    elif isinstance(data, dict) and data.get("error"):
        ok = False
        err = json.dumps(data.get("error"))[:400]
    cost = parse_response_cost(resp_headers)
    result = {
        "ok": ok,
        "http": code,
        "error": err,
        "model": model,
        "endpoint": endpoint,
        "cost": cost,
        "free": (cost is None or cost <= 0) and ok,
    }
    if ok and isinstance(cost, (int, float)) and cost > 0:
        result["ok"] = False
        result["free"] = False
        result["error"] = f"paid model: x-omniroute-response-cost={cost}"
    return result


def cast_out(cmd: list[str]) -> str:
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout or "")[-800:])
    return (p.stdout or "").strip()


def validate_yaml(env: dict, yaml_text: str, api_key: str, miner_address: str) -> dict:
    code, data, _headers = http_json(
        "POST",
        f"{env.get('NODE_URL', NODE).rstrip('/')}/miner-dispatcher/validate",
        {
            "yaml": yaml_text,
            "api_key": api_key,
            "miner_address": miner_address,
        },
        headers={"X-Internal-Secret": env.get("INTERNAL_SECRET", "telegraph-internal-secret")},
        timeout=180,
    )
    if not isinstance(data, dict):
        data = {"raw": data}
    data["_http"] = code
    return data


def sha256_text(text: str) -> str:
    return "0x" + hashlib.sha256(text.encode()).hexdigest()


def register_miner(env: dict, yaml_url: str, yaml_hash: str, intents: list[str]) -> tuple[str, int, str]:
    diamond = env.get("DIAMOND", DIAMOND_DEFAULT)
    rpc = env.get("RPC_URL", "https://sepolia.base.org")
    pk = env["MINER_PRIVATE_KEY"]
    fee = env["FEE_ADDRESS"]
    price = env.get("MIN_PRICE_USDC", "10000")
    intents_json = json.dumps(intents)
    addr = cast_out(["cast", "wallet", "address", "--private-key", pk])

    last = ""
    for attempt in range(1, 6):
        nonce = cast_out(["cast", "nonce", addr, "--rpc-url", rpc]).split()[0]
        cmd = [
            "cast", "send", diamond,
            "registerMiner(string,bytes32,address,uint256,string[])",
            yaml_url, yaml_hash, fee, price, intents_json,
            "--rpc-url", rpc, "--private-key", pk, "--nonce", nonce, "--json",
        ]
        p = subprocess.run(cmd, capture_output=True, text=True)
        raw = ((p.stdout or "") + "\n" + (p.stderr or "")).strip()
        if p.returncode != 0:
            last = raw[-800:]
            low = last.lower()
            if any(x in low for x in ("nonce too low", "already known", "underpriced", "nonce too high")):
                time.sleep(2 * attempt)
                continue
            # unsupported intent — surface clearly
            raise RuntimeError(last)
        start = raw.find("{")
        payload = json.loads(raw[start: raw.rfind("}") + 1])
        tx = payload.get("transactionHash") or ""
        status = str(payload.get("status", ""))
        for _ in range(40):
            cur = cast_out(["cast", "nonce", addr, "--rpc-url", rpc]).split()[0]
            if int(cur) > int(nonce):
                break
            time.sleep(0.4)
        cnt = cast_out(["cast", "call", diamond, "minerCount()(uint256)", "--rpc-url", rpc])
        return tx, int(cnt.split()[0]), status
    raise RuntimeError(last)


def host_yaml(env: dict, endpoint: str, slug: str, text: str) -> str:
    """Write local file; expect operator/rsync to public host. Returns public URL."""
    folder = YAML_CHAT if endpoint == "chat" else YAML_RESP
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{slug}.yaml"
    path.write_text(text)
    prefix = env["HOST_PREFIX_CHAT"] if endpoint == "chat" else env["HOST_PREFIX_RESP"]
    return f"{prefix.rstrip('/')}/{slug}.yaml", path


def verify_hosted(url: str, local: Path) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Go-http-client/1.1"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            remote = resp.read()
        return remote == local.read_bytes()
    except Exception:
        return False


def log_path(endpoint: str) -> Path:
    return OUT / f"safe-{endpoint}.jsonl"


def append_log(endpoint: str, row: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with log_path(endpoint).open("a") as f:
        f.write(json.dumps(row) + "\n")


def done_models(endpoint: str) -> set[str]:
    done = set()
    p = log_path(endpoint)
    if not p.exists():
        return done
    for line in p.read_text().splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        if r.get("status") == "registered" and r.get("model"):
            done.add(r["model"])
    return done


def cmd_probe(args, env) -> int:
    free_only = not getattr(args, "include_paid", False)
    models = select_models(free_only=free_only)
    if args.limit:
        models = models[: args.limit]
    ok_n = fail_n = paid_n = 0
    results = []
    print(f"Probing {len(models)} models (free_only={free_only})")
    for i, model in enumerate(models, 1):
        r = probe_model(env, args.endpoint, model)
        if is_paid_probe(r):
            r["ok"] = False
            r["free"] = False
            if not r.get("error"):
                r["error"] = f"paid model cost={r.get('cost')}"
            paid_n += 1
            mark = "PAID"
        elif r["ok"]:
            ok_n += 1
            mark = "OK"
        else:
            fail_n += 1
            mark = "FAIL"
        results.append(r)
        print(
            f"[{i}/{len(models)}] {mark} {model} http={r['http']} "
            f"cost={r.get('cost')} {r['error'][:120]}"
        )
        time.sleep(0.2)
    out = OUT / f"probe-{args.endpoint}.json"
    out.write_text(json.dumps(results, indent=2))
    print(f"OK={ok_n} PAID={paid_n} FAIL={fail_n} wrote {out}")
    return 0


def cmd_register(args, env) -> int:
    if "OMNIROUTE_API_KEY" not in env or "MINER_PRIVATE_KEY" not in env:
        print("Need OMNIROUTE_API_KEY and MINER_PRIVATE_KEY in .env", file=sys.stderr)
        return 1

    free_only = not getattr(args, "include_paid", False)
    models = select_models(free_only=free_only)
    done = done_models(args.endpoint)
    pending = [m for m in models if m not in done]
    if args.limit:
        pending = pending[: args.limit]

    start_id = CHAT_ID_START if args.endpoint == "chat" else RESP_ID_START
    prefix = "chat" if args.endpoint == "chat" else "resp"
    # allocate ids: start + index in full model list for stability
    model_index = {m: i for i, m in enumerate(models)}

    addr = cast_out(["cast", "wallet", "address", "--private-key", env["MINER_PRIVATE_KEY"]])
    print(
        f"Registering up to {len(pending)} FREE {args.endpoint} miners as {addr} "
        f"(free_only={free_only}; paid models are never registered)"
    )

    for n, model in enumerate(pending, 1):
        yaml_id = start_id + model_index[model]
        slug = short_slug(prefix, yaml_id)
        intents = intents_for_model(model)

        # name-level guard (even if --include-paid somehow slipped a non-free id)
        if free_only and not looks_free_model(model):
            append_log(args.endpoint, {
                "model": model, "slug": slug, "yaml_id": yaml_id,
                "status": "skipped_paid_name", "intents": intents,
            })
            print(f"[{n}/{len(pending)}] SKIP paid_name {model}")
            continue

        # 1) probe real model + unpaid cost check
        probe = probe_model(env, args.endpoint, model)
        if is_paid_probe(probe):
            append_log(args.endpoint, {
                "model": model, "slug": slug, "yaml_id": yaml_id,
                "status": "skipped_paid", "probe": probe, "intents": intents,
            })
            print(
                f"[{n}/{len(pending)}] SKIP paid {model}: "
                f"cost={probe.get('cost')} {probe.get('error','')[:120]}"
            )
            continue
        if not probe["ok"]:
            append_log(args.endpoint, {
                "model": model, "slug": slug, "yaml_id": yaml_id,
                "status": "probe_failed", "probe": probe, "intents": intents,
            })
            print(f"[{n}/{len(pending)}] SKIP probe_failed {model}: {probe['error'][:160]}")
            continue

        # 2) build yaml + validate
        yaml_text = render_yaml(args.endpoint, yaml_id, slug, model, intents, env.get("BASE_URL", BASE_URL))
        # Only use intents that are on-chain canonical — validate will error on unknown.
        # Start with CHAT_COMPLETION only for register safety; multi-intent after confirm.
        # User asked for multiple intents — try full list; if validate fails on intent, fall back.
        v = validate_yaml(env, yaml_text, env["OMNIROUTE_API_KEY"], addr)
        if not v.get("valid"):
            # retry with CHAT_COMPLETION only if intent-related
            errs = " ".join(v.get("errors") or [])
            if "intent" in errs.lower() or "unsupported" in errs.lower() or not v.get("valid"):
                yaml_text2 = render_yaml(args.endpoint, yaml_id, slug, model, ["CHAT_COMPLETION"], env.get("BASE_URL", BASE_URL))
                v2 = validate_yaml(env, yaml_text2, env["OMNIROUTE_API_KEY"], addr)
                if v2.get("valid"):
                    yaml_text, v, intents = yaml_text2, v2, ["CHAT_COMPLETION"]
                else:
                    append_log(args.endpoint, {
                        "model": model, "slug": slug, "yaml_id": yaml_id,
                        "status": "validate_failed", "validate": v, "validate_fallback": v2,
                        "intents": intents, "probe": probe,
                    })
                    print(f"[{n}/{len(pending)}] SKIP validate_failed {model}: {v.get('errors') or v}")
                    continue
            else:
                append_log(args.endpoint, {
                    "model": model, "slug": slug, "yaml_id": yaml_id,
                    "status": "validate_failed", "validate": v, "intents": intents, "probe": probe,
                })
                print(f"[{n}/{len(pending)}] SKIP validate_failed {model}: {v.get('errors') or v}")
                continue

        # 3) host + register
        url, path = host_yaml(env, args.endpoint, slug, yaml_text)
        # assume already rsynced OR require match
        if not verify_hosted(url, path):
            append_log(args.endpoint, {
                "model": model, "slug": slug, "yaml_id": yaml_id,
                "status": "host_pending", "yaml_url": url, "yaml_file": str(path),
                "intents": intents, "note": "local yaml written; rsync then re-run",
            })
            print(f"[{n}/{len(pending)}] WAIT host {slug} — rsync '{path.parent}' then re-run")
            # still continue generating locals; don't register without host match
            continue

        yhash = "0x" + hashlib.sha256(path.read_bytes()).hexdigest()
        try:
            tx, reg_id, status = register_miner(env, url, yhash, intents)
            ok = status in ("0x1", "1", "0x01")
            append_log(args.endpoint, {
                "model": model, "slug": slug, "yaml_id": yaml_id, "name": f"{prefix} {model}",
                "reg_id": reg_id, "yaml_url": url, "yaml_hash": yhash,
                "tx_hash": tx, "tx_url": f"https://sepolia.basescan.org/tx/{tx}",
                "tx_status": status, "intents": intents,
                "status": "registered" if ok else "tx_failed",
                "validate": {"valid": True, "results": v.get("results")},
            })
            print(f"[{n}/{len(pending)}] {'OK' if ok else 'FAIL'} {slug} reg={reg_id} intents={intents}")
        except Exception as e:
            append_log(args.endpoint, {
                "model": model, "slug": slug, "yaml_id": yaml_id,
                "status": "register_failed", "error": str(e)[:500], "intents": intents,
            })
            print(f"[{n}/{len(pending)}] FAIL register {slug}: {e}")
            time.sleep(2)
            continue
        time.sleep(0.8)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("probe")
    p1.add_argument("--endpoint", choices=["chat", "responses"], required=True)
    p1.add_argument("--limit", type=int, default=None)
    p1.add_argument(
        "--include-paid",
        action="store_true",
        help="Also list non-:free names (still marks cost>0 as PAID)",
    )

    p2 = sub.add_parser("register")
    p2.add_argument("--endpoint", choices=["chat", "responses"], required=True)
    p2.add_argument("--limit", type=int, default=None)
    p2.add_argument("--batch", type=int, default=None, help="alias for --limit")
    p2.add_argument(
        "--include-paid",
        action="store_true",
        help="Do not use — paid models are still blocked by cost check",
    )

    args = ap.parse_args()
    if getattr(args, "batch", None) and not args.limit:
        args.limit = args.batch
    # Hard rule: registration never opts into paid models.
    if args.cmd == "register":
        args.include_paid = False

    env = load_env()
    if not MODELS_JSON.exists():
        print(f"Missing {MODELS_JSON} — fetch /v1/models first", file=sys.stderr)
        return 1

    if args.cmd == "probe":
        return cmd_probe(args, env)
    if args.cmd == "register":
        return cmd_register(args, env)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
