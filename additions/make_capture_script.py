#!/usr/bin/env python3
"""Reads candidates.json, skips slugs that already exist in intentYamls/ and candidates with FILL_ placeholders,
writes capture_all.sh containing capture_api_output.py commands (your existing V2 step 1).
Run from MinerCreator/:  python3 ../MinerCreator_additions/make_capture_script.py  (or copy into MinerCreator/)
"""
import json, re, shlex, subprocess, sys
from pathlib import Path
here = Path(__file__).resolve().parent
root = Path.cwd()
existing = set(re.findall(r"(?m)^slug:\s*(\S+)", "\n".join(p.read_text() for p in (root/"intentYamls").rglob("*.yaml"))))
cands = json.load(open(here/"candidates.json"))
out, skipped = ["#!/usr/bin/env bash", "set -u", "cd \"$(dirname \"$0\")\""], []
for c in cands:
    if c["slug"] in existing: skipped.append((c["slug"], "already exists")); continue
    if "FILL_" in c["url"]: skipped.append((c["slug"], "needs real input: " + c["inputs"])); continue
    out.append("python3 scripts/capture_api_output.py " + " ".join([
        "--intent", shlex.quote(c["intent"]), "--slug", shlex.quote(c["slug"]), "--url", shlex.quote(c["url"]),
        "--inputs", shlex.quote(c["inputs"]), "--description", shlex.quote(c["description"]),
        "--requirement", shlex.quote(c["requirement"]), "--note", shlex.quote(c["note"])]) + " || echo \"CAPTURE FAILED: " + c["slug"] + "\"")
    out.append("sleep 1")
(root/"capture_all.sh").write_text("\n".join(out) + "\n")
print(f"wrote capture_all.sh with {sum(1 for l in out if l.startswith('python3'))} captures")
for s, why in skipped: print("SKIP", s, "-", why)
