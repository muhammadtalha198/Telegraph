#!/usr/bin/env python3
"""
Client-demo re-register of old intent YAMLs in batches of 200.

Gate: POST NODE_URL/miner-dispatcher/validate only.
Host: Omni host if bytes already match; else paste.rs (EC2 SSH:22 unreachable).
Does NOT update INTENT_BUILD_SHEET / newlyRegisteredMiners.
Tracks progress in client-demo-miners/clientDemoMinors.md + out/*.jsonl
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEMO = ROOT / "client-demo-miners"
OUT = DEMO / "out"
HOST_OMNI = "https://omni-chat.13.237.89.59.sslip.io/miner-yamls"
PASTE_HOST = "https://paste.rs/"
BATCH_SIZE = 200
DIAMOND_DEFAULT = "0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8"


def load_env() -> dict[str, str]:
    env = dict(os.environ)
    for line in (ROOT / ".env").read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env.setdefault(k.strip(), v.strip())
    env.setdefault("NODE_URL", "https://devnode.telegraphprotocol.com")
    env.setdefault("DIAMOND", DIAMOND_DEFAULT)
    env.setdefault("RPC_URL", "https://sepolia.base.org")
    env.setdefault("MIN_PRICE_USDC", "10000")
    env.setdefault("INTERNAL_SECRET", "telegraph-internal-secret")
    return env


def http_json(method: str, url: str, body=None, headers=None, timeout=180):
    data = None if body is None else json.dumps(body).encode()
    hdrs = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "client-demo-register/1.0",
    }
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, data=data, method=method, headers=hdrs)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode()
            return resp.status, json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        try:
            parsed = json.loads(raw)
        except Exception:
            parsed = {"raw": raw[:2000]}
        return e.code, parsed


def cast_out(cmd: list[str]) -> str:
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout or "")[-800:])
    return (p.stdout or "").strip()


def validate_yaml(env: dict, yaml_text: str, api_key: str, miner_address: str) -> dict:
    code, data = http_json(
        "POST",
        f"{env['NODE_URL'].rstrip('/')}/miner-dispatcher/validate",
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


def paste_host(local: Path) -> str:
    local_bytes = local.read_bytes()
    req = urllib.request.Request(
        PASTE_HOST,
        data=local_bytes,
        method="POST",
        headers={"Content-Type": "text/yaml", "User-Agent": "client-demo-register/1.0"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        url = resp.read().decode().strip()
    if not url.startswith("http"):
        raise RuntimeError(f"paste.rs bad response: {url[:200]}")
    req2 = urllib.request.Request(url, headers={"User-Agent": "Go-http-client/1.1"})
    with urllib.request.urlopen(req2, timeout=30) as resp2:
        remote = resp2.read()
    if remote != local_bytes:
        raise RuntimeError(f"paste.rs bytes mismatch for {local.name}")
    return url


def ensure_hosted(slug: str, local: Path) -> str:
    """Prefer Omni if already matching; else paste.rs (SSH:22 blocked)."""
    local_bytes = local.read_bytes()
    omni = f"{HOST_OMNI}/{slug}.yaml"
    try:
        req = urllib.request.Request(omni, headers={"User-Agent": "Go-http-client/1.1"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.read() == local_bytes:
                return omni
    except Exception:
        pass
    return paste_host(local)


def register_miner(env: dict, yaml_url: str, yaml_hash: str, intents: list[str]) -> tuple[str, str]:
    diamond = env["DIAMOND"]
    rpc = env["RPC_URL"]
    pk = env["MINER_PRIVATE_KEY"]
    fee = env["FEE_ADDRESS"]
    price = env.get("MIN_PRICE_USDC", "10000")
    intents_json = json.dumps(intents)
    addr = cast_out(["cast", "wallet", "address", "--private-key", pk])

    last = ""
    for attempt in range(1, 8):
        nonce = cast_out(["cast", "nonce", addr, "--rpc-url", rpc]).split()[0]
        cmd = [
            "cast",
            "send",
            diamond,
            "registerMiner(string,bytes32,address,uint256,string[])",
            yaml_url,
            yaml_hash,
            fee,
            price,
            intents_json,
            "--rpc-url",
            rpc,
            "--private-key",
            pk,
            "--nonce",
            nonce,
            "--json",
        ]
        p = subprocess.run(cmd, capture_output=True, text=True)
        raw = ((p.stdout or "") + "\n" + (p.stderr or "")).strip()
        if p.returncode != 0:
            last = raw[-800:]
            low = last.lower()
            if any(
                x in low
                for x in (
                    "nonce too low",
                    "already known",
                    "underpriced",
                    "nonce too high",
                    "replacement transaction underpriced",
                )
            ):
                time.sleep(2 * attempt)
                continue
            raise RuntimeError(last)
        start = raw.find("{")
        payload = json.loads(raw[start : raw.rfind("}") + 1])
        tx = payload.get("transactionHash") or ""
        status = str(payload.get("status", ""))
        for _ in range(40):
            cur = cast_out(["cast", "nonce", addr, "--rpc-url", rpc]).split()[0]
            if int(cur) > int(nonce):
                break
            time.sleep(0.4)
        return tx, status
    raise RuntimeError(last)


def receipt_reg_id(env: dict, tx: str) -> int | None:
    out = cast_out(["cast", "receipt", tx, "--rpc-url", env["RPC_URL"], "--json"])
    rec = json.loads(out)
    reg_id = None
    for log in rec.get("logs") or []:
        topics = log.get("topics") or []
        if len(topics) >= 2:
            try:
                rid = int(topics[1], 16)
                if 1000 < rid < 200000:
                    reg_id = rid
            except Exception:
                pass
    return reg_id


def update_progress_md(stats: list[dict]) -> None:
    path = DEMO / "clientDemoMinors.md"
    lines = [
        "# Client Demo Minors",
        "",
        "Temporary re-registration of the old (~1400) intent YAMLs for client demo.",
        "Not counted as production keepers. Do not merge into INTENT_BUILD_SHEET / newlyRegisteredMiners.",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Updated | {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} |",
        "| Source | `intentYamls/` → `client-demo-miners/yamls/` (excluding current keepers) |",
        f"| Total candidates | {len(json.loads((DEMO / 'manifest.json').read_text()))} |",
        "| Batch size | 200 |",
        "| Gate | Node `/miner-dispatcher/validate` only |",
        "| Host | Omni if present, else paste.rs (SSH:22 blocked) |",
        f"| Diamond | `{DIAMOND_DEFAULT}` |",
        "",
        "## Progress",
        "",
        "| Batch | Attempted | Validate OK | Registered | Failed/Skip |",
        "|------:|----------:|------------:|-----------:|------------:|",
    ]
    total_a = total_v = total_r = total_f = 0
    for s in stats:
        lines.append(
            f"| {s['batch']} | {s['attempted']} | {s['validate_ok']} | {s['registered']} | {s['failed']} |"
        )
        total_a += s["attempted"]
        total_v += s["validate_ok"]
        total_r += s["registered"]
        total_f += s["failed"]
    lines.append(f"| **Total** | **{total_a}** | **{total_v}** | **{total_r}** | **{total_f}** |")
    lines += [
        "",
        "## Notes",
        "",
        "- May be deregistered later after the demo.",
        "- Logs: `client-demo-miners/out/batchN-register.jsonl`",
        "",
    ]
    path.write_text("\n".join(lines) + "\n")


def already_done_slugs() -> set[str]:
    done = set()
    for p in OUT.glob("batch*-register.jsonl"):
        for line in p.read_text().splitlines():
            if not line.strip():
                continue
            try:
                r = json.loads(line)
            except Exception:
                continue
            if r.get("status") == "registered" and r.get("slug"):
                done.add(r["slug"])
    return done


def process_batch(env: dict, batch_num: int, items: list[dict], addr: str, api_key: str) -> dict:
    OUT.mkdir(parents=True, exist_ok=True)
    report = OUT / f"batch{batch_num}-register.jsonl"
    validate_report = OUT / f"batch{batch_num}-validate.jsonl"
    done = already_done_slugs()

    attempted = validate_ok = registered = failed = 0
    print(f"\n===== BATCH {batch_num} ({len(items)} miners) =====", flush=True)

    for i, item in enumerate(items, 1):
        slug = item["slug"]
        intent = item.get("intent") or "UNKNOWN"
        path = DEMO / "yamls" / f"{slug}.yaml"
        if not path.exists():
            path = ROOT / item["path"]
        attempted += 1

        if slug in done:
            print(f"[{batch_num}:{i}/{len(items)}] SKIP already {slug}", flush=True)
            validate_ok += 1
            registered += 1
            continue
        if not path.exists():
            failed += 1
            report.open("a").write(json.dumps({"slug": slug, "status": "missing_yaml"}) + "\n")
            print(f"[{batch_num}:{i}/{len(items)}] MISS {slug}", flush=True)
            continue

        yaml_text = path.read_text(encoding="utf-8")
        if not intent or intent == "UNKNOWN":
            m = re.search(r"supported_intents:\s*\n\s*-\s*(\S+)", yaml_text)
            intent = m.group(1) if m else "UNKNOWN"

        try:
            v = validate_yaml(env, yaml_text, api_key, addr)
        except Exception as e:
            failed += 1
            rec = {"slug": slug, "intent": intent, "status": "validate_error", "error": str(e)[-400:]}
            validate_report.open("a").write(json.dumps(rec) + "\n")
            report.open("a").write(json.dumps(rec) + "\n")
            print(f"[{batch_num}:{i}/{len(items)}] VALERR {slug}: {e}", flush=True)
            continue

        valid = bool(v.get("valid"))
        validate_report.open("a").write(
            json.dumps(
                {
                    "slug": slug,
                    "intent": intent,
                    "valid": valid,
                    "http": v.get("_http"),
                    "errors": v.get("errors"),
                }
            )
            + "\n"
        )
        if not valid:
            failed += 1
            rec = {
                "slug": slug,
                "intent": intent,
                "status": "validate_failed",
                "validate": {"errors": v.get("errors"), "http": v.get("_http")},
            }
            report.open("a").write(json.dumps(rec) + "\n")
            print(f"[{batch_num}:{i}/{len(items)}] FAIL validate {slug}", flush=True)
            continue

        validate_ok += 1
        yhash = sha256_text(yaml_text)
        print(f"[{batch_num}:{i}/{len(items)}] OK validate {slug} → host+register", flush=True)

        try:
            url = ensure_hosted(slug, path)
            tx, status = register_miner(env, url, yhash, [intent])
            time.sleep(1.0)
            try:
                reg_id = receipt_reg_id(env, tx)
            except Exception:
                reg_id = None
            rec = {
                "slug": slug,
                "intent": intent,
                "status": "registered",
                "tx": tx,
                "tx_status": status,
                "reg_id": reg_id,
                "yaml_url": url,
                "yaml_hash": yhash,
                "batch": batch_num,
            }
            report.open("a").write(json.dumps(rec) + "\n")
            registered += 1
            print(
                f"[{batch_num}:{i}/{len(items)}] REGISTERED {slug} id={reg_id} tx={tx[:12]}…",
                flush=True,
            )
        except Exception as e:
            failed += 1
            rec = {
                "slug": slug,
                "intent": intent,
                "status": "register_failed",
                "error": str(e)[-500:],
            }
            report.open("a").write(json.dumps(rec) + "\n")
            print(f"[{batch_num}:{i}/{len(items)}] REGFAIL {slug}: {e}", flush=True)
            time.sleep(2)

        # live progress after each miner
        if i % 5 == 0:
            (OUT / "live-progress.json").write_text(
                json.dumps(
                    {
                        "batch": batch_num,
                        "i": i,
                        "attempted": attempted,
                        "validate_ok": validate_ok,
                        "registered": registered,
                        "failed": failed,
                    },
                    indent=2,
                )
            )

    return {
        "batch": batch_num,
        "attempted": attempted,
        "validate_ok": validate_ok,
        "registered": registered,
        "failed": failed,
    }


def main() -> int:
    for k in (
        "HTTP_PROXY",
        "HTTPS_PROXY",
        "http_proxy",
        "https_proxy",
        "ALL_PROXY",
        "all_proxy",
        "SOCKS_PROXY",
        "SOCKS5_PROXY",
    ):
        os.environ.pop(k, None)

    env = load_env()
    if not env.get("MINER_PRIVATE_KEY") or not env.get("FEE_ADDRESS"):
        print("missing MINER_PRIVATE_KEY or FEE_ADDRESS", file=sys.stderr)
        return 1

    OUT.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((DEMO / "manifest.json").read_text())
    addr = cast_out(["cast", "wallet", "address", "--private-key", env["MINER_PRIVATE_KEY"]])
    api_key = env.get("OMNIROUTE_API_KEY", "")
    n_batches = (len(manifest) + BATCH_SIZE - 1) // BATCH_SIZE
    print(f"signer={addr} total={len(manifest)} batches={n_batches}", flush=True)

    stats_path = OUT / "progress.json"
    stats: list[dict] = []
    if stats_path.exists():
        try:
            stats = json.loads(stats_path.read_text())
        except Exception:
            stats = []

    # Resume: start at first incomplete batch (or next after last complete)
    start_batch = 1
    done = already_done_slugs()
    for b in range(1, n_batches + 1):
        items = manifest[(b - 1) * BATCH_SIZE : b * BATCH_SIZE]
        remaining = [x for x in items if x["slug"] not in done]
        if remaining:
            start_batch = b
            break
    else:
        start_batch = n_batches + 1

    for b in range(start_batch, n_batches + 1):
        items = manifest[(b - 1) * BATCH_SIZE : b * BATCH_SIZE]
        st = process_batch(env, b, items, addr, api_key)
        stats = [s for s in stats if s["batch"] != b] + [st]
        stats.sort(key=lambda x: x["batch"])
        stats_path.write_text(json.dumps(stats, indent=2))
        update_progress_md(stats)
        print(f"===== BATCH {b} DONE {st} =====", flush=True)

    print("ALL BATCHES COMPLETE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
