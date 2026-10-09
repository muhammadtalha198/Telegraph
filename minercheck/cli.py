"""Command line.

  python3 -m minercheck validate-spec                      # load + validate every intents/*.yaml
  python3 -m minercheck ask WEATHER_CHECK location=Lahore unit=F
  python3 -m minercheck ask CRYPTO_PRICE asset=BTC --json
  python3 -m minercheck run-tests [--intent X]              # spec `tests:` against live APIs
  python3 -m minercheck catalog build|table|audit|show X    # Intent Catalog index + spec alignment
  python3 -m minercheck gate --file intentYamls/.../x.yaml --intent CRYPTO_PRICE
  python3 -m minercheck gate --sample apiOutputSamples/X/slug.md    # miner without a YAML
  python3 -m minercheck batch                               # gate all Wave2 approved, diff with last run
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

from .errors import MinerCheckError, SpecError
from .fetch import Fetcher
from .geocode import open_meteo_geocoder
from .spec import DEFAULT_DIR, ROOT, Registry
from .verify import verify

CACHE = ROOT / "out" / "minercheck" / "cache"


def _kv(pairs: list[str]) -> dict[str, str]:
    out = {}
    for p in pairs:
        if "=" not in p:
            raise SystemExit(f"input must be name=value, got {p!r}")
        k, _, v = p.partition("=")
        out[k.strip()] = v.strip()
    return out


def _print_result(res, as_json: bool, verbose: bool) -> None:
    if as_json:
        print(json.dumps(res.to_dict(), indent=2, default=str))
        return
    print(res.answer_text)
    for n in res.notes:
        print(f"  note: {n}")
    if verbose or not res.verified:
        for c in res.candidates:
            mark = {"valid": "ok ", "rejected": "REJ", "error": "ERR"}.get(c.status, "?  ")
            val = "-" if c.parsed is None else (
                c.parsed.display.isoformat(timespec="seconds") if hasattr(c.parsed.display, "hour")
                else str(c.parsed.display))
            tail = c.consensus if c.status == "valid" else f"{c.layer}: {c.reason}"
            print(f"  [{mark}] {c.source.id:14} {c.doc_format or '-':5} {val:>22}  {tail}"[:220])


def yaml_for(slug: str) -> Path | None:
    hits = sorted((ROOT / "intentYamls").rglob(f"{slug}.yaml"))
    return hits[0] if hits else None


def gate_one(reg, fetcher, geocoder, *, yaml_path: Path | None = None, sample: Path | None = None,
             intent: str = "", slug: str = ""):
    """Gate one miner from a YAML and/or its sample. Intent/slug/URL fall back to the sample."""
    from .gate import gate_miner
    meta = sample_meta(sample) if sample else {}
    slug = slug or meta.get("slug") or (yaml_path.stem if yaml_path else "")
    intent = intent or meta.get("intent") or ""
    if yaml_path is None and slug:
        yaml_path = yaml_for(slug)
    if not intent:
        raise MinerCheckError("intent unknown: pass --intent or --sample")
    return gate_miner(yaml_path, intent, reg, fetcher=fetcher, geocoder=geocoder, slug=slug,
                      url=meta.get("request_url") if yaml_path is None else None)


def _batch(args, reg, fetcher, geocoder) -> int:
    rows = [r for r in json.loads(args.report.read_text())["results"] if r.get("status") == "approved"]
    prev = {}
    if args.previous.is_file():
        prev = {r["slug"]: r.get("verdict") for r in json.loads(args.previous.read_text()).get("results", [])}
    out, counts = [], {}
    for r in rows:
        try:
            g = gate_one(reg, fetcher, geocoder, sample=ROOT / r["path"])
            verdict, reason, lines, cat_intent, cov = g.verdict, g.reason, g.lines, g.catalog_intent, g.coverage
        except MinerCheckError as e:
            verdict, reason, lines, cat_intent, cov = "FAIL", str(e), [str(e)], "", []
        counts[verdict] = counts.get(verdict, 0) + 1
        out.append({"slug": r["slug"], "catalog_intent": cat_intent, "verdict": verdict, "previous": prev.get(r["slug"], ""),
                    "reason": reason, "yaml": str(yaml_for(r["slug"]) or ""), "facets": cov, "log": lines})
        print(f"{verdict:8} (was {prev.get(r['slug'], '-'):7}) {r['slug']:30} {reason[:110]}")
    args.out.with_suffix(".json").write_text(json.dumps({"counts": counts, "results": out}, indent=1, default=str) + "\n")
    md = ["# Wave2 approved miners vs. the Intent Catalog", "",
          f"Counts: {counts}. Previous run: `{args.previous.name}`.", "",
          "| Slug | Catalog intent | Was | Now | Reason (tied to the catalog Description) |", "|---|---|---|---|---|"]
    for o in sorted(out, key=lambda o: (o["verdict"], o["catalog_intent"], o["slug"])):
        md.append(f"| `{o['slug']}` | {o['catalog_intent']} | {o['previous'] or '-'} | **{o['verdict']}** | "
                  f"{(o['reason'] or 'verified').replace('|', '/')} |")
    args.out.with_suffix(".md").write_text("\n".join(md) + "\n")
    print(f"\n{counts}\nWROTE {args.out.with_suffix('.json')} and .md")
    return 0


def sample_meta(path: Path) -> dict[str, str]:
    """Front matter of an apiOutputSamples/*.md file (the one parser lives in scripts/sample_file.py)."""
    if str(ROOT / "scripts") not in sys.path:
        sys.path.insert(0, str(ROOT / "scripts"))
    from sample_file import parse_front_matter
    return parse_front_matter(path.read_text(encoding="utf-8"))


def _wave2_by_intent(path: Path, cat) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    if not path.is_file():
        return out
    for r in json.loads(path.read_text()).get("results", []):
        if r.get("status") != "approved":
            continue
        meta = sample_meta(ROOT / r["path"])
        e = cat.entry(meta.get("intent") or Path(r["path"]).parent.name)
        out.setdefault(e.intent if e else (meta.get("intent") or "?"), []).append(r["slug"])
    return out


def _catalog_cmd(args, reg) -> int:
    from .catalog import Catalog, audit_spec, table
    cat = Catalog(args.specs)
    if args.action == "show":
        e = cat.entry(args.intent)
        if e is None:
            print(f"FAIL  {args.intent!r} is not in the Intent Catalog")
            return 1
        print(json.dumps(e.__dict__, indent=2, default=str))
        return 0
    if args.action == "audit":
        bad = 0
        for name, spec in sorted(reg.specs.items()):
            problems = audit_spec(spec, cat)
            c = spec.catalog or {}
            label = "LOCAL" if c.get("local_only") else ("ALIGNED" if not problems else "DRIFT")
            print(f"{label:8} {name:28} -> catalog {c.get('intent') or '(none)'}")
            for p in problems:
                print(f"         - {p}")
            bad += bool(problems)
        return 1 if bad else 0
    wave2 = _wave2_by_intent(args.wave2, cat)
    rows = table(cat, reg, wave2)
    print("| Intent | Tier | Catalog Description | Spec | Wave2 slugs |")
    print("|---|---|---|---|---|")
    for r in rows:
        if not args.all and not r["wave2"] and not r["spec"]:
            continue
        spec = "-" if not r["spec"] else (f"{r['spec']}" + ("" if r["aligned"] else " (drift)"))
        print(f"| {r['intent']} | {r['tier']} | {r['description']} | {spec} | {', '.join(r['wave2']) or '-'} |")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="minercheck", description="YAML-driven answer verification")
    ap.add_argument("--specs", type=Path, default=DEFAULT_DIR)
    ap.add_argument("-v", "--verbose", action="store_true")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("validate-spec", help="load and validate all intent specs")

    a = sub.add_parser("ask", help="answer one question")
    a.add_argument("intent")
    a.add_argument("inputs", nargs="*", help="name=value")
    a.add_argument("--json", action="store_true")
    a.add_argument("--all-sources", action="store_true", help="query every source (no early stop)")
    a.add_argument("--no-cache", action="store_true")

    t = sub.add_parser("run-tests", help="run each spec's tests: block live")
    t.add_argument("--intent", default="")
    t.add_argument("--no-cache", action="store_true")


    c = sub.add_parser("catalog", help="Intent Catalog index: build | table | audit | show INTENT")
    c.add_argument("action", choices=["build", "table", "audit", "show"])
    c.add_argument("intent", nargs="?", default="")
    c.add_argument("--wave2", type=Path, default=ROOT / "out" / "wave2_auto_review_report.json",
                   help="auto-review report whose approved slugs are listed per intent")
    c.add_argument("--all", action="store_true", help="table: include intents with no Wave2 miners")

    g = sub.add_parser("gate", help="verify a miner's answer against its catalog intent (register gate)")
    g.add_argument("--file", type=Path, help="miner YAML (called exactly as the node calls it)")
    g.add_argument("--sample", type=Path, help="apiOutputSamples/*.md: slug/intent/URL from it when there is no YAML")
    g.add_argument("--intent", default="")
    g.add_argument("--slug", default="")

    b = sub.add_parser("batch", help="gate every approved sample in an auto-review report; diff with a previous run")
    b.add_argument("--report", type=Path, default=ROOT / "out" / "wave2_auto_review_report.json")
    b.add_argument("--previous", type=Path, default=ROOT / "out" / "wave2_minercheck_gate_report.json")
    b.add_argument("--out", type=Path, default=ROOT / "out" / "wave2_catalog_gate_report")

    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(name)s: %(message)s")
    if args.cmd == "catalog" and args.action == "build":
        from .catalog import INDEX, build_index, write_index
        entries = build_index()
        write_index(entries, args.specs / INDEX.name)
        tiers = {}
        for e in entries.values():
            tiers[e.tier] = tiers.get(e.tier, 0) + 1
        drift = [e.intent for e in entries.values() if e.build_sheet_description and e.build_sheet_description != e.description]
        print(f"WROTE {args.specs / INDEX.name}: {len(entries)} intents, tiers {tiers}")
        print(f"build-sheet descriptions checked: {sum(1 for e in entries.values() if e.build_sheet_description)}, "
              f"differ from catalog: {drift or 'none'}")
        return 0
    try:
        reg = Registry(args.specs)
    except SpecError as e:
        print(f"FAIL  {e}", file=sys.stderr)
        return 1

    if args.cmd == "validate-spec":
        for name, spec in sorted(reg.specs.items()):
            pubs = len({x.publisher for x in spec.sources if x.enabled})
            miners = [x.miner_slug for x in spec.sources if x.miner_slug]
            print(f"PASS  {name:14} {spec.answer_type:12} {len(spec.sources)} sources / {pubs} publishers"
                  f"  miners: {', '.join(miners) or '-'}")
        return 0

    fetcher = Fetcher(cache_dir=None if getattr(args, "no_cache", False) else CACHE)
    geocoder = open_meteo_geocoder(fetcher)

    if args.cmd == "ask":
        spec = reg.get(args.intent)
        if spec is None:
            print(f"FAIL  no intent spec for {args.intent!r} (have: {', '.join(sorted(reg.specs))})", file=sys.stderr)
            return 2
        res = verify(spec, _kv(args.inputs), fetcher=fetcher, shared=reg.shared, geocoder=geocoder,
                     stop_early=not args.all_sources)
        _print_result(res, args.json, args.verbose)
        return 0 if res.verified else 3

    if args.cmd == "run-tests":
        bad = 0
        for name, spec in sorted(reg.specs.items()):
            if args.intent and reg.get(args.intent) is not spec:
                continue
            for t in spec.tests:
                res = verify(spec, t["inputs"], fetcher=fetcher, shared=reg.shared, geocoder=geocoder,
                             stop_early=False)
                print(f"{'PASS' if res.verified else 'FAIL'}  {name}/{t['id']}: {res.answer_text}")
                _print_result(res, False, True)
                bad += not res.verified
        return 1 if bad else 0

    if args.cmd == "catalog":
        return _catalog_cmd(args, reg)

    if args.cmd == "gate":
        from .gate import gate_miner
        try:
            r = gate_one(reg, fetcher, geocoder, yaml_path=args.file, sample=args.sample,
                         intent=args.intent, slug=args.slug)
        except MinerCheckError as e:
            print(f"FAIL  {e}")
            return 1
        print("\n".join(r.lines))
        return 0 if r.ok else 1

    if args.cmd == "batch":
        return _batch(args, reg, fetcher, geocoder)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
