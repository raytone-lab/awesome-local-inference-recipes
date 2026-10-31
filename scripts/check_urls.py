#!/usr/bin/env python3
"""URL and launch-command hygiene check. CI runs this. Exit 1 on any violation.
Rules: scripts/url_safety.py and docs/hw_index.md (Security)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import url_safety as us

ROOT = Path(__file__).resolve().parent.parent
# Launch commands that a test already knows about. The index does not emit them (launch_cmd is null, launch_cmd_warning says why).
KNOWN_UNSAFE_CMDS = {'comm-053', 'comm-057', 'x-108'}


def load(p): return json.loads((ROOT / p).read_text(encoding='utf-8'))


def known_owners():
    """HF/ModelScope owners named by the data itself: model cards in model-params.json and recipe sources on the hubs."""
    out = {k for k in us.CFG.get('verified_hub_owners', {}) if not k.startswith('_')}
    for u in [m['source'] for m in load('data/model-params.json')['models']] + [r['source_url'] for r in load('data/recipes.json')]:
        k = us.repo_key(u)
        if k and k.split('/')[0] in ('huggingface.co', 'hf.co', 'modelscope.cn'): out.add(k.split('/')[1])
    return out


def violations():
    bad = []
    R = load('data/recipes.json')
    texts = [(r['id'], json.dumps(r, ensure_ascii=False)) for r in R]
    texts += [('repos.json', json.dumps(load('data/repos.json'), ensure_ascii=False)), ('sources.json', json.dumps(load('data/sources.json'), ensure_ascii=False))]
    for where, t in texts:
        for u in us.URL_RE.findall(t):
            for p in us.problems(u): bad.append(f'{where}: {u}: {p}')
    for r in R:
        cp = us.cmd_problems(r.get('launch_command'))
        if cp and r['id'] not in KNOWN_UNSAFE_CMDS: bad.append(f"{r['id']}: launch_command: {', '.join(cp)}")
    idx = ROOT / 'data/hw_index.json'
    if idx.exists():
        owners = {o.lower() for o in known_owners()}
        for x in load('data/hw_index.json')['recipes']:
            w = x.get('weights_url')
            if w:
                k = us.repo_key(w['url'])
                if not k: bad.append(f"{x['id']}: weights_url is not a hub owner/repo URL: {w['url']}")
                elif k.split('/')[1].lower() not in owners: bad.append(f"{x['id']}: weights_url owner {k.split('/')[1]} is not a known owner")
            for f in ('engine_repo', 'weights_url'):
                if x.get(f) and x[f]['trust'] != 'allowlisted': bad.append(f"{x['id']}: {f} is not on an allowlisted host: {x[f]['url']}")
            if x.get('launch_cmd') and us.cmd_problems(x['launch_cmd']): bad.append(f"{x['id']}: unsafe launch_cmd in index")
    return bad


def main():
    bad = violations()
    for b in bad: print('URL CHECK:', b)
    print(f'check_urls: {len(bad)} violation(s)')
    sys.exit(1 if bad else 0)


if __name__ == '__main__': main()
