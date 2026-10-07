#!/usr/bin/env python3
"""Fix Response miner slugs to short valid names (resp-<yaml_id>) and updateMiner in batches.

Slug pattern required by node: ^[a-z0-9]+(-[a-z0-9]+)*$
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "out"
YAML_DIR = ROOT / "Response yaml"
TMPL = ROOT / "templates" / "responses.miner.yaml.tmpl"
REGISTRY_JSON = OUT / "response-registry.json"
REGISTRY_JSONL = OUT / "response-registry.jsonl"
FIX_JSONL = OUT / "response-slug-fix.jsonl"
MINERS_MD = ROOT / "response Miners.md"

BASE_URL = "https://omni-chat.13.237.89.59.sslip.io"
HOST_PREFIX = f"{BASE_URL}/response-yamls"
INTENT = "CHAT_COMPLETION"


def load_env() -> dict[str, str]:
    env = dict(os.environ)
    for line in (ROOT / ".env").read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env.setdefault(k.strip(), v.strip())
    return env


def short_slug(yaml_id: int) -> str:
    # short + unique + valid: resp-10201
    return f"resp-{yaml_id}"


def short_name(model: str) -> str:
    return f"Resp {model}"


def render_yaml(yaml_id: int, slug: str, name: str, model: str) -> str:
    text = TMPL.read_text()
    desc = f"OmniRoute /v1/responses miner for {model}."
    model_desc = f"Pinned Responses model {model}"
    for k, v in {
        "{{ID}}": str(yaml_id),
        "{{SLUG}}": slug,
        "{{NAME}}": name,
        "{{MODEL}}": model,
        "{{BASE_URL}}": BASE_URL,
        "{{INTENT}}": INTENT,
        "{{DESCRIPTION}}": desc,
        "{{MODEL_DESCRIPTION}}": model_desc,
    }.items():
        text = text.replace(k, v)
    return text


def sha256_file(path: Path) -> str:
    return f"0x{hashlib.sha256(path.read_bytes()).hexdigest()}"


def _cast_out(cmd: list[str]) -> str:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError((proc.stderr or proc.stdout or "").strip()[:800])
    return (proc.stdout or "").strip()


def cast_update(env: dict, old_id: int, yaml_url: str, yaml_hash: str) -> tuple[str, int, str]:
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
            "updateMiner(uint256,string,bytes32,address,uint256,string[])",
            str(old_id), yaml_url, yaml_hash, fee, price, intents,
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
            raise RuntimeError(f"cast update failed: {last_err}")
        start = raw.find("{")
        if start < 0:
            last_err = raw[:500]
            time.sleep(2)
            continue
        payload = json.loads(raw[start: raw.rfind("}") + 1])
        tx = payload.get("transactionHash") or ""
        status = str(payload.get("status", ""))
        if not tx:
            raise RuntimeError(f"no tx: {raw[:400]}")
        for _ in range(40):
            cur = _cast_out(["cast", "nonce", addr, "--rpc-url", rpc]).split()[0]
            if int(cur) > int(nonce):
                break
            time.sleep(0.5)
        cnt = _cast_out(["cast", "call", diamond, "minerCount()(uint256)", "--rpc-url", rpc])
        return tx, int(cnt.split()[0]), status
    raise RuntimeError(f"cast update failed after retries: {last_err}")


def regenerate_yamls(rows: list[dict]) -> list[dict]:
    # wipe and rewrite with short slugs
    YAML_DIR.mkdir(parents=True, exist_ok=True)
    for p in YAML_DIR.glob("*.yaml"):
        p.unlink()

    updated = []
    for r in rows:
        yaml_id = int(r["yaml_id"])
        model = r["model"]
        slug = short_slug(yaml_id)
        name = short_name(model)
        path = YAML_DIR / f"{slug}.yaml"
        path.write_text(render_yaml(yaml_id, slug, name, model))
        updated.append({
            **r,
            "old_slug": r.get("slug"),
            "slug": slug,
            "name": name,
            "yaml_file": str(path),
            "yaml_url": f"{HOST_PREFIX}/{slug}.yaml",
            "yaml_hash": sha256_file(path),
        })
    print(f"Regenerated {len(updated)} YAMLs with short slugs in {YAML_DIR}")
    return updated


def load_done_old_regs() -> set[int]:
    done = set()
    if FIX_JSONL.exists():
        for line in FIX_JSONL.read_text().splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("status") == "updated" and row.get("old_reg_id") is not None:
                done.add(int(row["old_reg_id"]))
    return done


def append_fix(row: dict) -> None:
    with FIX_JSONL.open("a") as f:
        f.write(json.dumps(row) + "\n")


def write_docs(rows: list[dict]) -> None:
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
        lines.append(
            "| {i} | {name} | `{slug}` | {yid} | `{model}` | {reg} | [yaml]({yurl}) | `{h}` | [tx]({tx}) |".format(
                i=i,
                name=r.get("name", ""),
                slug=r.get("slug", ""),
                yid=r.get("yaml_id", ""),
                model=r.get("model", ""),
                reg=r.get("reg_id", ""),
                yurl=r.get("yaml_url", ""),
                h=r.get("yaml_hash", ""),
                tx=r.get("tx_url", ""),
            )
        )
    lines.append("")
    MINERS_MD.write_text("\n".join(lines))
    REGISTRY_JSON.write_text(json.dumps(rows, indent=2))


def phase_update(rows: list[dict], env: dict, limit: int | None = None) -> None:
    done = load_done_old_regs()
    pending = [r for r in rows if int(r["reg_id"]) not in done]
    if limit is not None:
        pending = pending[:limit]
    total = len(pending)
    print(f"Updating {total} miners (skipping {len(done)} already fixed)...")

    for n, r in enumerate(pending, start=1):
        old_id = int(r["reg_id"])
        slug = r["slug"]
        path = Path(r["yaml_file"])
        yaml_url = r["yaml_url"]
        yaml_hash = r["yaml_hash"]

        try:
            with urllib.request.urlopen(yaml_url, timeout=30) as resp:
                remote = resp.read()
        except Exception as e:
            append_fix({**r, "old_reg_id": old_id, "status": "host_fetch_failed", "error": str(e)})
            print(f"[{n}/{total}] FAIL host {slug}: {e}")
            continue
        if remote != path.read_bytes():
            append_fix({**r, "old_reg_id": old_id, "status": "hash_mismatch"})
            print(f"[{n}/{total}] FAIL mismatch {slug}")
            continue

        try:
            tx, new_id, status = cast_update(env, old_id, yaml_url, yaml_hash)
            append_fix({
                **r,
                "old_reg_id": old_id,
                "reg_id": new_id,
                "tx_hash": tx,
                "tx_url": f"https://sepolia.basescan.org/tx/{tx}",
                "tx_status": status,
                "status": "updated" if status in ("0x1", "1", "0x01") else "tx_failed",
            })
            print(f"[{n}/{total}] OK {slug} old={old_id} new={new_id} tx={tx[:12]}…")
        except Exception as e:
            append_fix({**r, "old_reg_id": old_id, "status": "update_failed", "error": str(e)[:500]})
            print(f"[{n}/{total}] FAIL update {slug}: {e}")
            time.sleep(2)
            continue
        time.sleep(0.8)

    # rebuild registry from latest successful updates + leftover originals
    latest: dict[int, dict] = {}
    # start from regenerated rows keyed by yaml_id
    by_yaml = {int(r["yaml_id"]): dict(r) for r in rows}
    if FIX_JSONL.exists():
        for line in FIX_JSONL.read_text().splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("status") != "updated":
                continue
            yid = int(row["yaml_id"])
            by_yaml[yid] = {
                "name": row["name"],
                "slug": row["slug"],
                "yaml_id": yid,
                "model": row["model"],
                "reg_id": row["reg_id"],
                "yaml_url": row["yaml_url"],
                "yaml_hash": row["yaml_hash"],
                "tx_hash": row.get("tx_hash"),
                "tx_url": row.get("tx_url"),
                "status": "registered",
                "endpoint": "/v1/responses",
                "old_reg_id": row.get("old_reg_id"),
                "old_slug": row.get("old_slug"),
            }
    final = [by_yaml[k] for k in sorted(by_yaml)]
    write_docs(final)
    print(f"Wrote {MINERS_MD} ({len(final)} rows)")


def main() -> int:
    env = load_env()
    rows = json.loads(REGISTRY_JSON.read_text())
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else None

    if cmd in ("generate", "all"):
        rows = regenerate_yamls(rows)
        (OUT / "response-short-manifest.json").write_text(json.dumps(rows, indent=2))
    else:
        # reload from manifest if present
        man = OUT / "response-short-manifest.json"
        if man.exists():
            rows = json.loads(man.read_text())

    if cmd in ("update", "all"):
        phase_update(rows, env, limit=limit)
    if cmd == "readme":
        # rebuild docs from fix log
        phase_update(rows, env, limit=0)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
