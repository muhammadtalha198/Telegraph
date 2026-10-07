#!/usr/bin/env python3
"""Batch generate + register OmniRoute /v1/responses miners (311 models).

YAMLs live in:  MinerCreator/Response yaml/
Hosted at:      https://omni-chat.13.237.89.59.sslip.io/response-yamls/<slug>.yaml
Docs:           MinerCreator/response Miners.md  (full hashes)
Registry:       MinerCreator/out/response-registry.jsonl
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "out"
YAML_DIR = ROOT / "Response yaml"
TMPL = ROOT / "templates" / "responses.miner.yaml.tmpl"
MODELS_JSON = OUT / "omni-models.json"
REGISTRY_JSONL = OUT / "response-registry.jsonl"
REGISTRY_JSON = OUT / "response-registry.json"
MINERS_MD = ROOT / "response Miners.md"

BASE_URL = "https://omni-chat.13.237.89.59.sslip.io"
HOST_PREFIX = f"{BASE_URL}/response-yamls"
INTENT = "CHAT_COMPLETION"
START_YAML_ID = 10201  # chat miners used 9201–9511


def load_env() -> dict[str, str]:
    env = dict(os.environ)
    env_path = ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env.setdefault(k.strip(), v.strip())
    return env


def slugify(model: str, yaml_id: int | None = None) -> str:
    """Short valid slug: only a-z0-9 and hyphens (Telegraph schema)."""
    if yaml_id is not None:
        return f"resp-{yaml_id}"
    s = model.lower().strip()
    s = s.replace("/", "-").replace(":", "-").replace(".", "-").replace("_", "-").replace(" ", "-")
    s = re.sub(r"[^a-z0-9-]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-") or "model"
    slug = f"resp-{s}"
    if len(slug) > 40:
        digest = hashlib.sha1(model.encode()).hexdigest()[:8]
        slug = f"resp-{digest}"
    return slug


def display_name(model: str) -> str:
    return f"Resp {model}"


def render_yaml(yaml_id: int, slug: str, name: str, model: str) -> str:
    text = TMPL.read_text()
    desc = f"Single-model OmniRoute Responses API miner pinned to {model} (CHAT_COMPLETION)."
    model_desc = f"Pinned Responses model {model}"
    repl = {
        "{{ID}}": str(yaml_id),
        "{{SLUG}}": slug,
        "{{NAME}}": name,
        "{{MODEL}}": model,
        "{{BASE_URL}}": BASE_URL,
        "{{INTENT}}": INTENT,
        "{{DESCRIPTION}}": desc,
        "{{MODEL_DESCRIPTION}}": model_desc,
    }
    for k, v in repl.items():
        text = text.replace(k, v)
    return text


def sha256_file(path: Path) -> str:
    return f"0x{hashlib.sha256(path.read_bytes()).hexdigest()}"


def select_models() -> list[str]:
    """Same 311 set as chat Responses UI (non-aihorde, drop media/veo)."""
    data = json.loads(MODELS_JSON.read_text())["data"]
    ids = [x["id"] for x in data]
    media_bits = (
        "veo", "embedding", "embed/", "whisper", "tts", "dall-e",
        "flux", "imagen", "stable-diffusion",
    )
    out = []
    for mid in ids:
        if mid.startswith("aihorde/"):
            continue
        low = mid.lower()
        if any(b in low for b in media_bits):
            continue
        out.append(mid)
    return out


def ensure_unique_slugs(models: list[str]) -> list[tuple[str, str, int]]:
    used: set[str] = set()
    rows = []
    yaml_id = START_YAML_ID
    for model in models:
        slug = slugify(model, yaml_id=yaml_id)
        if slug in used:
            raise RuntimeError(f"duplicate slug {slug}")
        used.add(slug)
        rows.append((model, slug, yaml_id))
        yaml_id += 1
    return rows


def _cast_out(cmd: list[str]) -> str:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError((proc.stderr or proc.stdout or "").strip()[:800])
    return (proc.stdout or "").strip()


def cast_send_register(env: dict, yaml_url: str, yaml_hash: str) -> tuple[str, int, str]:
    diamond = env.get("DIAMOND", "0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8")
    rpc = env.get("RPC_URL", "https://sepolia.base.org")
    pk = env["MINER_PRIVATE_KEY"]
    fee = env["FEE_ADDRESS"]
    price = env.get("MIN_PRICE_USDC", "10000")
    intents = json.dumps([INTENT])
    addr = _cast_out(["cast", "wallet", "address", "--private-key", pk])

    last_err = ""
    for attempt in range(1, 6):
        nonce = _cast_out(["cast", "nonce", addr, "--rpc-url", rpc]).split()[0]
        cmd = [
            "cast", "send", diamond,
            "registerMiner(string,bytes32,address,uint256,string[])",
            yaml_url, yaml_hash, fee, price, intents,
            "--rpc-url", rpc, "--private-key", pk, "--nonce", nonce, "--json",
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        raw = ((proc.stdout or "") + "\n" + (proc.stderr or "")).strip()
        if proc.returncode != 0:
            last_err = raw[-800:]
            low = last_err.lower()
            if any(x in low for x in (
                "nonce too low", "already known",
                "replacement transaction underpriced", "nonce too high",
            )):
                time.sleep(2 * attempt)
                continue
            raise RuntimeError(f"cast send failed: {last_err}")
        start = raw.find("{")
        if start < 0:
            last_err = raw[:500]
            time.sleep(2)
            continue
        payload = json.loads(raw[start: raw.rfind("}") + 1])
        tx = payload.get("transactionHash") or ""
        status = str(payload.get("status", ""))
        if not tx:
            raise RuntimeError(f"no tx hash: {raw[:400]}")
        for _ in range(40):
            cur = _cast_out(["cast", "nonce", addr, "--rpc-url", rpc]).split()[0]
            if int(cur) > int(nonce):
                break
            time.sleep(0.5)
        cnt = _cast_out(["cast", "call", diamond, "minerCount()(uint256)", "--rpc-url", rpc])
        return tx, int(cnt.split()[0]), status
    raise RuntimeError(f"cast send failed after retries: {last_err}")


def append_registry(row: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with REGISTRY_JSONL.open("a") as f:
        f.write(json.dumps(row) + "\n")


def load_done_slugs() -> set[str]:
    done = set()
    if REGISTRY_JSONL.exists():
        for line in REGISTRY_JSONL.read_text().splitlines():
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("status") == "registered" and row.get("slug"):
                done.add(row["slug"])
    return done


def write_miners_md(rows: list[dict]) -> None:
    lines = [
        "# OmniRoute Telegraph Response Miners",
        "",
        f"Base URL: `{BASE_URL}`  ",
        f"Endpoint: `/v1/responses`  ",
        f"Intent: `{INTENT}`  ",
        f"Diamond: `0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8` (Base Sepolia)  ",
        f"Total listed: **{len(rows)}**",
        "",
        "| # | Name | Slug | YAML id | Model | Reg ID | YAML | Hash | Tx |",
        "|---|------|------|---------|-------|--------|------|------|-----|",
    ]
    for i, r in enumerate(rows, start=1):
        h = r.get("yaml_hash") or ""
        tx = r.get("tx_url") or ""
        yurl = r.get("yaml_url") or ""
        lines.append(
            "| {i} | {name} | `{slug}` | {yid} | `{model}` | {reg} | [yaml]({yurl}) | `{h}` | [tx]({tx}) |".format(
                i=i,
                name=r.get("name", ""),
                slug=r.get("slug", ""),
                yid=r.get("yaml_id", ""),
                model=r.get("model", ""),
                reg=r.get("reg_id", ""),
                yurl=yurl,
                h=h,
                tx=tx,
            )
        )
    lines.append("")
    MINERS_MD.write_text("\n".join(lines))


def snapshot_registry() -> list[dict]:
    rows: list[dict] = []
    seen = set()
    if REGISTRY_JSONL.exists():
        for line in REGISTRY_JSONL.read_text().splitlines():
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("status") != "registered":
                continue
            if row.get("slug") in seen:
                continue
            rows.append(row)
            seen.add(row["slug"])
    REGISTRY_JSON.write_text(json.dumps(rows, indent=2))
    write_miners_md(rows)
    return rows


def phase_generate(rows: list[tuple[str, str, int]]) -> None:
    YAML_DIR.mkdir(parents=True, exist_ok=True)
    for model, slug, yaml_id in rows:
        path = YAML_DIR / f"{slug}.yaml"
        path.write_text(render_yaml(yaml_id, slug, display_name(model), model))
    print(f"Generated {len(rows)} YAML files in {YAML_DIR}")
    (OUT / "response-batch-manifest.json").write_text(
        json.dumps(
            [
                {
                    "model": m,
                    "slug": s,
                    "yaml_id": i,
                    "file": f"{s}.yaml",
                    "url": f"{HOST_PREFIX}/{s}.yaml",
                }
                for m, s, i in rows
            ],
            indent=2,
        )
    )


def phase_register(rows: list[tuple[str, str, int]], env: dict, limit: int | None = None) -> None:
    done = load_done_slugs()
    pending = [(m, s, i) for m, s, i in rows if s not in done]
    if limit is not None:
        pending = pending[:limit]
    total = len(pending)
    print(f"Registering {total} response miners (skipping {len(done)} already done)...")

    for n, (model, slug, yaml_id) in enumerate(pending, start=1):
        path = YAML_DIR / f"{slug}.yaml"
        yaml_url = f"{HOST_PREFIX}/{slug}.yaml"
        yaml_hash = sha256_file(path)
        try:
            with urllib.request.urlopen(yaml_url, timeout=30) as resp:
                remote = resp.read()
        except Exception as e:
            append_registry({
                "index": n, "name": display_name(model), "slug": slug,
                "yaml_id": yaml_id, "model": model, "yaml_url": yaml_url,
                "yaml_hash": yaml_hash, "status": "host_fetch_failed", "error": str(e),
            })
            print(f"[{n}/{total}] FAIL host {slug}: {e}")
            continue
        if remote != path.read_bytes():
            append_registry({
                "index": n, "name": display_name(model), "slug": slug,
                "yaml_id": yaml_id, "model": model, "yaml_url": yaml_url,
                "yaml_hash": yaml_hash, "status": "hash_mismatch",
            })
            print(f"[{n}/{total}] FAIL mismatch {slug}")
            continue
        try:
            tx, reg_id, status = cast_send_register(env, yaml_url, yaml_hash)
            append_registry({
                "index": n, "name": display_name(model), "slug": slug,
                "yaml_id": yaml_id, "model": model, "reg_id": reg_id,
                "yaml_url": yaml_url, "yaml_hash": yaml_hash, "tx_hash": tx,
                "tx_url": f"https://sepolia.basescan.org/tx/{tx}",
                "tx_status": status,
                "status": "registered" if status in ("0x1", "1", "0x01") else "tx_failed",
                "endpoint": "/v1/responses",
            })
            print(f"[{n}/{total}] OK {slug} reg={reg_id} tx={tx[:12]}…")
        except Exception as e:
            append_registry({
                "index": n, "name": display_name(model), "slug": slug,
                "yaml_id": yaml_id, "model": model, "yaml_url": yaml_url,
                "yaml_hash": yaml_hash, "status": "register_failed",
                "error": str(e)[:500],
            })
            print(f"[{n}/{total}] FAIL register {slug}: {e}")
            time.sleep(2)
            continue
        time.sleep(1.0)
        if n % 10 == 0:
            snapshot_registry()
    snapshot_registry()


def main() -> int:
    if not MODELS_JSON.exists():
        print(f"Missing {MODELS_JSON}", file=sys.stderr)
        return 1
    env = load_env()
    if "MINER_PRIVATE_KEY" not in env or "FEE_ADDRESS" not in env:
        print("Need MINER_PRIVATE_KEY and FEE_ADDRESS in .env", file=sys.stderr)
        return 1

    models = select_models()
    rows = ensure_unique_slugs(models)
    print(f"Selected {len(models)} models → {len(rows)} response miners")

    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else None

    if cmd in ("generate", "all"):
        phase_generate(rows)
    if cmd in ("register", "all"):
        phase_register(rows, env, limit=limit)
    if cmd == "readme":
        snapshot_registry()
        print(f"Wrote {MINERS_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
