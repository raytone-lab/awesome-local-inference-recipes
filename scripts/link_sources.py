#!/usr/bin/env python3
"""Add derived link fields (idempotent, deterministic, never deletes data).
- source_id: 'src-' + sha1(normalized source_url)[:10]; rows from the same post/page share it.
- engine_fork: fork owner parsed from canonical engine names like 'llama.cpp (PrismML fork)'.
Run: python3 scripts/link_sources.py"""
import hashlib, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
FORK = re.compile(r'^(?P<base>.+?) \((?P<fork>[^)]+?) fork\)$')

def norm_url(u):
    u = u.strip().split('#')[0].rstrip('/')
    u = re.sub(r'^http://', 'https://', u)
    u = re.sub(r'^https://(www\.)?(twitter|x)\.com/', 'https://x.com/', u, flags=re.I)
    return re.sub(r'\?.*$', '', u) if 'x.com/' in u else u

def source_id(u):
    return 'src-' + hashlib.sha1(norm_url(u).encode()).hexdigest()[:10]

def link(recipes):
    for r in recipes:
        r['source_id'] = source_id(r['source_url'])
        m = FORK.match(r['engine'])
        if m: r['engine_fork'] = m.group('fork')
        elif r['engine'] == 'Radiance (fork)': r['engine_fork'] = 'Radiance'
    return recipes

if __name__ == '__main__':
    p = ROOT / 'data/recipes.json'; D = json.load(open(p))
    link(D); Path(p).write_text(json.dumps(D, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    from collections import Counter
    c = Counter(r['source_id'] for r in D)
    print(f"{len(D)} recipes, {len(c)} sources, {sum(1 for v in c.values() if v > 1)} shared by >1 row")
