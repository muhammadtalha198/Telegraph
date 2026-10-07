# MinerCreator scripts — what to use

**Default path = Semantic V2.** See [`../SEMANTIC_REGISTER_V2.md`](../SEMANTIC_REGISTER_V2.md).

Old one-off / bypass scripts were moved to [`../archive/legacy-scripts/`](../archive/legacy-scripts/) — do not run those for new work.

---

## V2 (use these)

| Script | Role |
|--------|------|
| `capture_api_output.py` | Capture live API → `apiOutputSamples/<INTENT>/<slug>.md` |
| `auto_review_samples.py` | Heuristic/LLM review → approve / reject / needs_human |
| `set_sample_status.py` | Manual override of sample status |
| `generate_yamls_from_approved_samples.py` | Build YAML from **approved** samples only |
| `create_miner_v2.sh` | Thin wrapper: capture / review / gen-yamls |
| `smoke_v2_endpoints.py` | Quick GET smoke on research endpoints |
| `upload-host.sh` | Host YAML (paste.rs / Dropbox / omni-chat) |
| `register_gates_v2.py` | Fail-closed V2 gates (approved sample + YAML + probe) |
| `register-miner-v2.sh` | **Only** gas path for V2 |
| `register_approved_v2_batch.py` | Batch: host + `register-miner-v2.sh` for approved set |
| `validate_miner_yaml.py` | YAML schema check (used by V2 + legacy) |

Typical flow:

```bash
python3 scripts/capture_api_output.py --intent … --slug … --url …
python3 scripts/auto_review_samples.py --apply
python3 scripts/generate_yamls_from_approved_samples.py
./scripts/upload-host.sh intentYamls/…/slug.yaml
./scripts/register-miner-v2.sh --file … --url … --sample apiOutputSamples/…/slug.md
```

---

## Legacy RelTol (only if Usman wants numeric comparator)

| Script | Role |
|--------|------|
| `register-miner.sh` | Gas after RelTol gates |
| `register_gates.py` | validate → preflight → selftest → keepers |
| `preflight_miner.py` | Groups A–D |
| `miner_selftest.py` | Numeric RelTol / NON-DET text |
| `local_validate_keepers.py` | Keeper suite |
| `batch6_manifest.py` / `batch7_manifest.py` | Data for keepers (imported) |
| `generate-yaml.sh` / `create-miner.sh` | Old YAML helpers |
| `semantic-truth-proxy.py` | Omni `/truth` proxy (deployed host) |

---

## Do not use

Anything under `archive/legacy-scripts/` or `archive/legacy-batch-register/` — old batch / Omni free-model / probe generators that bypass V2 gates.
