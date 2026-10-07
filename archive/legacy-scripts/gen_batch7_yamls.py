"""Write Batch 7 miner YAMLs from batch7_manifest (refuses overwrite unless --force)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from batch7_manifest import M  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://omni-chat.13.237.89.59.sslip.io"

# Shared venue routes already on the proxy (external_path).
SHARED = {
    "crypto-spot",
    "ip-rep",
    "wx-temp",
    "aq-pm25",
    "dns-has",
    "stock-last",
    "vendor-id",
}


def q(s: str) -> str:
    return json.dumps(str(s))


def render(m: dict) -> str:
    defaults = dict(m["defaults"])
    names = list(defaults)
    label = m["label"]
    params = "\n".join(
        f"          - name: {n}\n            type: string\n            intents: [\"*\"]\n"
        f"            description: {n}"
        for n in names
    )
    props = "\n".join(
        f"    {n}: {{type: string, description: {q(n)}, default: {q(defaults[n])}}}" for n in names
    )
    return f"""version: "1"
kind: miner
id: {m['id']}
slug: {m['slug']}
protocol: generic
name: {m['name']}
description: >
  {m['name']} -> {label}.
  Intent {m['intent']} - Round Two Batch 7.

base_url: {BASE}

auth:
  type: none

rate_limit_per_sec: 1
cache_ttl_sec: 60
circuit_threshold: 5
circuit_cooldown_seconds: 30

docs:
  documentation: {m['docs']}
  website: {BASE}

endpoints:
  - path: /query
    external_path: /truth/{m['route']}
    method: GET
    description: Query for intent {m['intent']} via {m['name']}.
    intents: [{m['intent']}]
    params:
      query:
        required:
{params}

input_schema:
  type: object
  required: [{', '.join(names)}]
  properties:
{props}

semantics:
  signal_mapping:
    label_field: {label}
  supported_intents:
    - {m['intent']}

on_chain:
  description: Stores signal for {m['intent']}.
  transform: direct
  min_price_usdc: 0.01
  fields:
    strings:
      - index: 0
        name: result
        description: Primary result
        source_path: result
      - index: 1
        name: intent
        description: Intent name
        source_path: intent
    integers:
      - index: 0
        name: ok
        description: Success flag
        source_path: ok
"""


def main() -> None:
    force = "--force" in sys.argv
    for m in M:
        path = ROOT / "intentYamls" / m["folder"] / f"{m['slug']}.yaml"
        if path.exists() and not force:
            print(f"exists (skip): {path}")
            m["file"] = str(path.relative_to(ROOT))
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(m), encoding="utf-8")
        m["file"] = str(path.relative_to(ROOT))
        print("wrote", path.relative_to(ROOT))
    print(f"batch7 {len(M)} miners, ids {M[0]['id']}-{M[-1]['id']}")


if __name__ == "__main__":
    main()
