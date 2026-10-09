#!/usr/bin/env python3
"""Wave2 step 1 ONLY: capture samples. No review / YAML / host / register.
Run from MinerCreator/ in a terminal with internet:  python3 scripts/wave2_capture.py [--limit N] [--dry]
"""
import json, re, subprocess, sys, argparse
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser(); ap.add_argument('--limit', type=int, default=0); ap.add_argument('--dry', action='store_true'); a = ap.parse_args()
queue = [json.loads(l) for l in open(ROOT / 'out/wave2_queue.jsonl') if l.strip()]
cands = {}
for f in [ROOT.parent / 'miner_pack/candidates_wave2.json']:
    for b in json.load(open(f)):
        for c in b['candidates']: cands[c['slug']] = (c, b)
rank = {'READY': 0, 'KEYLESS_LOW_CONF': 1, 'pack': 1, 'TIE_ONLY': 2}
queue.sort(key=lambda x: (rank.get(x['bucket'], 3), 0 if x['intent'].startswith('CRYPTO') else 1, x['intent'], x['slug']))
captured, skipped, failed = [], [], []
n = 0
for x in queue:
    s = x['slug']; c, b = cands.get(s, (None, None))
    if x.get('skip'): skipped.append((s, x['skip'])); continue
    if not c: skipped.append((s, 'not in candidates_wave2.json')); continue
    if 'application/dns-message' in json.dumps(c): skipped.append((s, 'DoH binary')); continue
    if c.get('needs_key'): skipped.append((s, 'needs key')); continue
    if (c.get('method') or 'GET').upper() != 'GET' or c.get('body') is not None: skipped.append((s, 'POST/JSON-RPC: capture is GET-only')); continue
    if c.get('headers'): skipped.append((s, 'needs custom headers: capture sends none')); continue
    if a.limit and n >= a.limit: break
    t = next((t for t in b['tests'] if (not c.get('tests') or t['id'] in c['tests'])), b['tests'][0])
    vals = dict(t['inputs']); vals.update({k + '_lower': str(v).lower() for k, v in t['inputs'].items()})
    import datetime; vals.setdefault('today', datetime.date.today().isoformat()); vals.setdefault('tomorrow', (datetime.date.today() + datetime.timedelta(days=1)).isoformat())
    url = re.sub(r'\{(\w+)\}', lambda m: str(vals.get(m.group(1), m.group(0))), c['url'])
    if re.search(r'\{\w+\}', url): failed.append((s, 'unfilled placeholder in ' + url)); continue
    cmd = [sys.executable, str(ROOT / 'scripts/capture_api_output.py'), '--intent', x['intent'], '--slug', s, '--url', url,
           '--inputs', json.dumps(t['inputs']), '--description', x.get('description') or b['description'], '--requirement', x.get('requirement') or b['requirement']]
    n += 1
    print(f"[{n}] {x['bucket']:9} {x['intent']} {s}")
    if a.dry: print('   ', ' '.join(cmd[:8]), '...'); continue
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    p = ROOT / 'apiOutputSamples' / x['intent'] / f'{s}.md'
    if r.returncode == 0 and p.exists(): captured.append((s, str(p.relative_to(ROOT))))
    else: failed.append((s, (r.stderr or r.stdout).strip()[-200:]))
print(f"\nCAPTURED {len(captured)}  SKIPPED {len(skipped)}  FAILED {len(failed)}")
for s, p in captured: print('  ok  ', p)
for s, w in skipped: print('  skip', s, '-', w)
for s, w in failed: print('  FAIL', s, '-', w)
json.dump(dict(captured=captured, skipped=skipped, failed=failed), open(ROOT / 'out/wave2_capture_report.json', 'w'), indent=1)
