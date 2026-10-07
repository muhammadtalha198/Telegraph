#!/usr/bin/env python3
"""Generate + register one miner per OmniRoute model (excluding aihorde + already done).

Hosts YAMLs at:
  https://omni-chat.13.237.89.59.sslip.io/miner-yamls/<slug>.yaml

Writes:
  out/registry.jsonl   — one JSON object per miner (append)
  out/registry.json    — full array snapshot
  MINERS.md            — table for humans
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "out"
YAML_DIR = ROOT / "yaml"
TMPL = ROOT / "templates" / "chat-completion.miner.yaml.tmpl"
MODELS_JSON = OUT / "omni-models.json"
REGISTRY_JSONL = OUT / "registry.jsonl"
REGISTRY_JSON = OUT / "registry.json"
MINERS_MD = ROOT / "MINERS.md"

BASE_URL = "https://omni-chat.13.237.89.59.sslip.io"
HOST_PREFIX = f"{BASE_URL}/miner-yamls"
INTENT = "CHAT_COMPLETION"
START_YAML_ID = 9202  # 9201 = auto/cheap already registered
SKIP_PREFIXES = ("aihorde/",)
SKIP_MODELS = {"auto/cheap"}  # already registered as omni-cheap-chat / 9201 / reg 421

# Seed row for the first miner (not re-registered by this script)
SEED = {
    "index": 0,
    "name": "OmniRoute Cheap Chat",
    "slug": "omni-cheap-chat",
    "yaml_id": 9201,
    "model": "auto/cheap",
    "reg_id": 421,
    "yaml_url": "https://paste.rs/LMzCt",
    "yaml_hash": "0x0d49fbaefccb1d384d3dfe7318752c61ed4a4d3c9e7879570f1b879a951d1397",
    "tx_hash": "0xc425775c3fe9df05d95df7dbfdfec12903e4ce00c301ce379eefb47929df8e99",
    "tx_url": "https://sepolia.basescan.org/tx/0xc425775c3fe9df05d95df7dbfdfec12903e4ce00c301ce379eefb47929df8e99",
    "status": "registered",
}


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


def slugify(model: str) -> str:
    s = model.lower().strip()
    s = s.replace("/", "-").replace(":", "-").replace(" ", "-")
    s = re.sub(r"[^a-z0-9._-]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    if not s:
        s = "model"
    slug = f"omni-{s}"
    # keep slug reasonably short for URLs / catalog
    if len(slug) > 64:
        digest = hashlib.sha1(model.encode()).hexdigest()[:8]
        slug = f"{slug[:55]}-{digest}"
    return slug


def display_name(model: str) -> str:
    return f"OmniRoute {model}"


def render_yaml(yaml_id: int, slug: str, name: str, model: str) -> str:
    text = TMPL.read_text()
    desc = f"Single-model OmniRoute chat miner pinned to {model} (CHAT_COMPLETION)."
    model_desc = f"Pinned chat model {model}"
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
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    return f"0x{h}"


def select_models() -> list[str]:
    """Non-aihorde models minus auto/cheap (~310), dropping obvious non-chat media ids."""
    data = json.loads(MODELS_JSON.read_text())["data"]
    ids = [x["id"] for x in data]
    media_bits = (
        "veo", "embedding", "embed/", "whisper", "tts", "dall-e",
        "flux", "imagen", "stable-diffusion",
    )
    out = []
    for mid in ids:
        if mid in SKIP_MODELS:
            continue
        if any(mid.startswith(p) for p in SKIP_PREFIXES):
            continue
        low = mid.lower()
        if any(b in low for b in media_bits):
            continue
        out.append(mid)
    return out


def ensure_unique_slugs(models: list[str]) -> list[tuple[str, str, int]]:
    """Return list of (model, slug, yaml_id)."""
    used = {"omni-cheap-chat", "omniroute-chat"}
    rows = []
    yaml_id = START_YAML_ID
    for model in models:
        base = slugify(model)
        slug = base
        n = 2
        while slug in used:
            slug = f"{base}-{n}"
            n += 1
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
            "cast",
            "send",
            diamond,
            "registerMiner(string,bytes32,address,uint256,string[])",
            yaml_url,
            yaml_hash,
            fee,
            price,
            intents,
            "--rpc-url",
            rpc,
            "--private-key",
            pk,
            "--nonce",
            nonce,
            "--json",
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        raw = ((proc.stdout or "") + "\n" + (proc.stderr or "")).strip()
        if proc.returncode != 0:
            last_err = raw[-800:]
            low = last_err.lower()
            if any(
                x in low
                for x in (
                    "nonce too low",
                    "already known",
                    "replacement transaction underpriced",
                    "nonce too high",
                )
            ):
                time.sleep(2 * attempt)
                continue
            raise RuntimeError(f"cast send failed: {last_err}")
        start = raw.find("{")
        if start < 0:
            last_err = raw[:500]
            time.sleep(2)
            continue
        payload = json.loads(raw[start : raw.rfind("}") + 1])
        tx = payload.get("transactionHash") or payload.get("transaction_hash") or ""
        status = str(payload.get("status", ""))
        if not tx:
            raise RuntimeError(f"no tx hash in cast output: {raw[:400]}")

        # Wait until nonce advances past this tx (confirms inclusion)
        for _ in range(40):
            cur = _cast_out(["cast", "nonce", addr, "--rpc-url", rpc]).split()[0]
            if int(cur) > int(nonce):
                break
            time.sleep(0.5)

        cnt = _cast_out(
            ["cast", "call", diamond, "minerCount()(uint256)", "--rpc-url", rpc]
        )
        reg_id = int(cnt.split()[0])
        return tx, reg_id, status

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
    done.add(SEED["slug"])
    return done


def write_miners_md(rows: list[dict]) -> None:
    lines = [
        "# OmniRoute Telegraph Miners",
        "",
        f"Base URL: `{BASE_URL}`  ",
        f"Intent: `{INTENT}`  ",
        f"Diamond: `0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8` (Base Sepolia)  ",
        f"Total listed: **{len(rows)}**",
        "",
        "| # | Name | Slug | YAML id | Model | Reg ID | YAML | Hash | Tx |",
        "|---|------|------|---------|-------|--------|------|------|-----|",
    ]
    for i, r in enumerate(rows, start=1):
        h = r.get("yaml_hash") or ""
        hshort = f"`{h[:10]}…{h[-4:]}`" if len(h) > 16 else f"`{h}`"
        tx = r.get("tx_url") or ""
        yurl = r.get("yaml_url") or ""
        lines.append(
            "| {i} | {name} | `{slug}` | {yid} | `{model}` | {reg} | [yaml]({yurl}) | {h} | [tx]({tx}) |".format(
                i=i,
                name=r.get("name", ""),
                slug=r.get("slug", ""),
                yid=r.get("yaml_id", ""),
                model=r.get("model", ""),
                reg=r.get("reg_id", ""),
                yurl=yurl,
                h=hshort,
                tx=tx,
            )
        )
    lines.append("")
    MINERS_MD.write_text("\n".join(lines))


def snapshot_registry() -> list[dict]:
    rows: list[dict] = []
    seen = set()
    # seed first
    rows.append(dict(SEED))
    seen.add(SEED["slug"])
    if REGISTRY_JSONL.exists():
        for line in REGISTRY_JSONL.read_text().splitlines():
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("slug") in seen:
                continue
            if row.get("status") != "registered":
                continue
            rows.append(row)
            seen.add(row["slug"])
    REGISTRY_JSON.write_text(json.dumps(rows, indent=2))
    write_miners_md(rows)
    return rows


def phase_generate(rows: list[tuple[str, str, int]]) -> None:
    YAML_DIR.mkdir(parents=True, exist_ok=True)
    # keep seed yaml
    for model, slug, yaml_id in rows:
        path = YAML_DIR / f"{slug}.yaml"
        path.write_text(render_yaml(yaml_id, slug, display_name(model), model))
    print(f"Generated {len(rows)} YAML files in {YAML_DIR}")


def phase_register(rows: list[tuple[str, str, int]], env: dict, limit: int | None = None) -> None:
    done = load_done_slugs()
    # ensure seed is in jsonl once
    if not REGISTRY_JSONL.exists() or SEED["slug"] not in {
        json.loads(l).get("slug")
        for l in REGISTRY_JSONL.read_text().splitlines()
        if l.strip()
    }:
        append_registry(dict(SEED))

    pending = [(m, s, i) for m, s, i in rows if s not in done]
    if limit is not None:
        pending = pending[:limit]
    total = len(pending)
    print(f"Registering {total} miners (skipping {len(done)} already done)...")

    for n, (model, slug, yaml_id) in enumerate(pending, start=1):
        path = YAML_DIR / f"{slug}.yaml"
        yaml_url = f"{HOST_PREFIX}/{slug}.yaml"
        yaml_hash = sha256_file(path)

        # verify remote bytes match before gas
        import urllib.request

        try:
            with urllib.request.urlopen(yaml_url, timeout=30) as resp:
                remote = resp.read()
        except Exception as e:
            row = {
                "index": n,
                "name": display_name(model),
                "slug": slug,
                "yaml_id": yaml_id,
                "model": model,
                "yaml_url": yaml_url,
                "yaml_hash": yaml_hash,
                "status": "host_fetch_failed",
                "error": str(e),
            }
            append_registry(row)
            print(f"[{n}/{total}] FAIL host {slug}: {e}")
            continue
        if remote != path.read_bytes():
            row = {
                "index": n,
                "name": display_name(model),
                "slug": slug,
                "yaml_id": yaml_id,
                "model": model,
                "yaml_url": yaml_url,
                "yaml_hash": yaml_hash,
                "status": "hash_mismatch",
                "error": "remote != local",
            }
            append_registry(row)
            print(f"[{n}/{total}] FAIL mismatch {slug}")
            continue

        try:
            tx, reg_id, status = cast_send_register(env, yaml_url, yaml_hash)
            row = {
                "index": n,
                "name": display_name(model),
                "slug": slug,
                "yaml_id": yaml_id,
                "model": model,
                "reg_id": reg_id,
                "yaml_url": yaml_url,
                "yaml_hash": yaml_hash,
                "tx_hash": tx,
                "tx_url": f"https://sepolia.basescan.org/tx/{tx}",
                "tx_status": status,
                "status": "registered" if status in ("0x1", "1", "0x01") else "tx_failed",
            }
            append_registry(row)
            print(f"[{n}/{total}] OK {slug} reg={reg_id} tx={tx[:12]}…")
        except Exception as e:
            row = {
                "index": n,
                "name": display_name(model),
                "slug": slug,
                "yaml_id": yaml_id,
                "model": model,
                "yaml_url": yaml_url,
                "yaml_hash": yaml_hash,
                "status": "register_failed",
                "error": str(e)[:500],
            }
            append_registry(row)
            print(f"[{n}/{total}] FAIL register {slug}: {e}")
            # brief pause on failure (nonce / rate)
            time.sleep(2)
            continue

        # pacing between confirmed txs
        time.sleep(1.0)
        if n % 10 == 0:
            snapshot_registry()

    snapshot_registry()


def main() -> int:
    if not MODELS_JSON.exists():
        print(f"Missing {MODELS_JSON} — fetch /v1/models first", file=sys.stderr)
        return 1
    env = load_env()
    if "MINER_PRIVATE_KEY" not in env or "FEE_ADDRESS" not in env:
        print("Need MINER_PRIVATE_KEY and FEE_ADDRESS in .env", file=sys.stderr)
        return 1

    models = select_models()
    rows = ensure_unique_slugs(models)
    print(f"Selected {len(models)} models → {len(rows)} miners")

    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else None

    if cmd in ("generate", "all"):
        phase_generate(rows)
        # manifest for rsync
        (OUT / "batch-manifest.json").write_text(
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
        print(f"Wrote {OUT / 'batch-manifest.json'}")

    if cmd in ("register", "all"):
        phase_register(rows, env, limit=limit)

    if cmd == "readme":
        snapshot_registry()
        print(f"Wrote {MINERS_MD} and {REGISTRY_JSON}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
