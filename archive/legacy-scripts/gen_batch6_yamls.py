"""Write Batch 6 miner YAMLs from batch6_manifest (refuses to overwrite)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from batch6_manifest import M, ROUTES, query  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://omni-chat.13.237.89.59.sslip.io"


def q(s: str) -> str:
    return json.dumps(str(s))


def render(m: dict) -> str:
    pdesc, label, ldesc = ROUTES[m["route"]]
    defaults = query(m)
    names = list(pdesc)
    params = "\n".join(
        f"          - name: {n}\n            type: string\n            intents: [\"*\"]\n"
        f"            description: {pdesc[n]}" for n in names)
    props = "\n".join(
        f"    {n}: {{type: string, description: {q(pdesc[n])}, default: {q(defaults[n])}}}" for n in names)
    return f"""version: "1"
kind: miner
id: {m['id']}
slug: {m['slug']}
protocol: generic
name: {m['name']}
description: >
  {m['name']} -> {label} ({ldesc}).
  Intent {m['intent']} - one publisher per miner.

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
    for m in M:
        assert set(query(m)) == set(ROUTES[m["route"]][0]), m["slug"]
        path = ROOT / "intentYamls" / m["folder"] / f"{m['slug']}.yaml"
        if path.exists() and "--force" not in sys.argv:
            sys.exit(f"exists: {path}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(m), encoding="utf-8")
        m["file"] = str(path.relative_to(ROOT))
    print(f"wrote {len(M)} yamls, ids {M[0]['id']}-{M[-1]['id']}")


if __name__ == "__main__":
    main()
