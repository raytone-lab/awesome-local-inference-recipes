#!/usr/bin/env python3
"""Rank recipes from data/hw_index.json for one machine. Stdlib only. Read-only.

  python3 detect_hw.py > hw.json
  python3 match_recipes.py --hw hw.json [--model qwen3.8] [--min-tok 20] [--top 5] [--lang en|zh|ja] [--json]

Data: --index PATH, else <repo>/data/hw_index.json, else the pinned raw GitHub URL (https, main branch).
Links: only URLs with trust == 'allowlisted' are actionable. Other URLs are 'source for reading' only."""
import argparse, datetime, json, os, re, sys, urllib.request

INDEX_URL = 'https://raw.githubusercontent.com/raytone-lab/awesome-local-inference-recipes/main/data/hw_index.json'
HERE = os.path.dirname(os.path.abspath(__file__))
LOCAL = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'data', 'hw_index.json'))
LEVEL = {'实测': 3, '官方': 2, '宣称': 1, '转述': 0}
LEVEL_NAME = {'en': {'实测': 'measured', '官方': 'official', '宣称': 'claimed (not verified)', '转述': 'relayed'},
              'zh': {'实测': '实测', '官方': '官方', '宣称': '宣称（未核实）', '转述': '转述'},
              'ja': {'実測': '実測', '实测': '実測', '官方': '公式', '宣称': '公称（未検証）', '转述': '伝聞'}}
T = {'en': dict(machine='Machine', none='No recipe fits this machine. See', speed='tok/s (single stream)', level='Source level', engine_repo='Engine repo',
                weights='Weights', cmd='Launch command', page='Recipe page', read='Source (for reading only, not for downloads)', asof='Data as of',
                nolink='not in the data (do not search for a mirror)', unsafe='hidden: unsafe pattern', similar='other hardware, speed will differ', cpu='CPU only'),
     'zh': dict(machine='本机', none='没有适合本机的配方。请看', speed='tok/s（单流）', level='来源级别', engine_repo='引擎仓库',
                weights='权重', cmd='启动命令', page='配方页面', read='来源（只供阅读，不要从这里下载）', asof='数据截至',
                nolink='数据里没有（不要去找镜像）', unsafe='已隐藏：含不安全写法', similar='硬件不同，速度会有差别', cpu='仅 CPU'),
     'ja': dict(machine='このマシン', none='このマシンに合うレシピはありません。次を参照：', speed='tok/s（シングルストリーム）', level='ソースレベル', engine_repo='エンジンのリポジトリ',
                weights='重み', cmd='起動コマンド', page='レシピページ', read='ソース（読むだけ。ダウンロードには使わない）', asof='データ時点',
                nolink='データにない（ミラーを探さない）', unsafe='非表示：危険なパターン', similar='別のハードウェア。速度は異なる', cpu='CPU のみ')}
REQUIRED = {'id', 'model', 'engine', 'chip', 'kind', 'gpu_count', 'vram_gb', 'unified_mem_gb', 'sys_ram_gb', 'tok_s', 'single_stream',
            'source_level', 'source_url', 'engine_repo', 'weights_url', 'launch_cmd', 'recipe_page', 'os_hints', 'date', 'category'}
EXPLORE = 'https://raytone-lab.github.io/awesome-local-inference-recipes/explore.html'
# Detected GPU name -> chip name in the index. Longer names first.
CHIP_RX = [('RTX PRO 6000', r'RTX PRO 6000'), ('RTX 5090', r'5090'), ('RTX 5080', r'5080'), ('RTX 5070 Ti', r'5070 ?Ti'), ('RTX 5070', r'5070'),
           ('RTX 5060 Ti', r'5060 ?Ti'), ('RTX 5060', r'5060'), ('RTX 4090', r'4090'), ('RTX 4080', r'4080'), ('RTX 4070 Ti SUPER', r'4070 ?Ti ?SUPER'),
           ('RTX 4070 Ti', r'4070 ?Ti'), ('RTX 4070', r'4070'), ('RTX 4060 Ti', r'4060 ?Ti'), ('RTX 4060', r'4060'), ('RTX 3090', r'3090'),
           ('RTX 3080', r'3080'), ('RTX 3070', r'3070'), ('RTX 3060', r'3060'), ('RTX 2080 Ti', r'2080 ?Ti'), ('RTX A6000', r'A6000'),
           ('Tesla P40', r'P40\b'), ('V100', r'V100'), ('A100', r'A100'), ('MI50', r'MI50'), ('RX 7900 XTX', r'7900 ?XTX'), ('RX 7900 XT', r'7900 ?XT'),
           ('R9700', r'R9700'), ('DGX Spark', r'GB10|DGX Spark'), ('Strix Halo', r'Strix Halo|AI Max'),
           ('M5 Ultra', r'M5 Ultra'), ('M5 Max', r'M5 Max'), ('M5 Pro', r'M5 Pro'), ('M5', r'\bM5\b'), ('M4 Max', r'M4 Max'), ('M4 Pro', r'M4 Pro'), ('M4', r'\bM4\b'),
           ('M3 Ultra', r'M3 Ultra'), ('M3 Max', r'M3 Max'), ('M3 Pro', r'M3 Pro'), ('M3', r'\bM3\b'), ('M2 Ultra', r'M2 Ultra'), ('M2 Max', r'M2 Max'),
           ('M2 Pro', r'M2 Pro'), ('M2', r'\bM2\b'), ('M1 Ultra', r'M1 Ultra'), ('M1 Max', r'M1 Max'), ('M1', r'\bM1\b')]
CPU_ENGINES = re.compile(r'llama\.cpp|ollama|lm studio|ik_llama|bitnet|mnn|edge0|strata|cpu', re.I)


def chip_of(name):
    for c, rx in CHIP_RX:
        if re.search(rx, name or '', re.I): return c
    return None


def machine(hw):
    gpus = [g for g in hw.get('gpus') or [] if g.get('name')]
    names = [g['name'] for g in gpus] + [hw.get('cpu') or '']
    chip = next((chip_of(n) for n in names if chip_of(n)), None)
    if hw.get('dgx_spark'): chip = 'DGX Spark'
    osn = hw.get('os')
    unified = osn == 'macos' or chip in ('DGX Spark', 'Strix Halo')
    count = sum(1 for g in gpus if chip_of(g['name']) == chip) or (1 if chip else 0)
    ram = float(hw.get('ram_gb') or 0)
    vram = ram if unified else sum(float(g.get('vram_gb') or 0) for g in gpus if chip_of(g['name']) == chip)
    gname = next((n for n in names if chip and chip_of(n) == chip), '')
    kind = 'unified' if unified else ('gpu' if chip else 'cpu')
    return {'os': osn, 'chip': chip, 'kind': kind, 'gpu_count': count, 'mem_gb': round(vram, 1), 'ram_gb': round(ram, 1),
            'laptop': bool(re.search(r'Laptop|Max-Q|Mobile', gname, re.I)), 'gpu_name': gname}


def load_index(path):
    for p in [path, LOCAL]:
        if p and os.path.exists(p):
            with open(p, encoding='utf-8') as f: return check(json.load(f)), p
    if path: sys.exit(f'index not found: {path}')
    with urllib.request.urlopen(INDEX_URL, timeout=30) as r:  # pinned https URL; no redirects to other hosts are used
        if not r.geturl().startswith('https://raw.githubusercontent.com/raytone-lab/awesome-local-inference-recipes/'): sys.exit('unexpected redirect')
        return check(json.loads(r.read().decode('utf-8'))), INDEX_URL


def check(idx):
    if not isinstance(idx, dict) or idx.get('schema_version') != 1 or not isinstance(idx.get('recipes'), list):
        sys.exit('hw_index.json: unknown schema')
    for x in idx['recipes']:
        miss = REQUIRED - set(x)
        if miss: sys.exit(f'hw_index.json: row {x.get("id")} misses {sorted(miss)}')
        for f in ('engine_repo', 'weights_url', 'source_url'):
            v = x[f]
            if v is not None and not (isinstance(v, dict) and str(v.get('url', '')).startswith('https://') and v.get('trust') in ('allowlisted', 'unverified')):
                sys.exit(f'hw_index.json: row {x["id"]} has a bad {f}')
    return idx


def age_days(d, asof):
    try: return (datetime.date.fromisoformat(asof) - datetime.date.fromisoformat(d[:10])).days
    except Exception: return 365


def score(x, M, a, asof):
    """Return (score, fit, notes) or None. Deterministic: uses the index DATA_ASOF, not today."""
    if x['category'] != 'text' or not x['tok_s'] or not x['single_stream'] or x.get('superseded_by'): return None
    if x['source_level'] == '转述' and not a.include_relayed: return None
    if a.model and a.model.lower() not in (x['model'] + ' ' + (x.get('model_family') or '')).lower(): return None
    if a.min_tok and x['tok_s'] < a.min_tok: return None
    if x.get('mac_only_engine') and M['os'] != 'macos': return None
    if M['os'] not in x['os_hints'] and not (M['os'] == 'windows' and 'linux' in x['os_hints']): return None
    notes, s = [], 0.0
    ram_need = x['sys_ram_gb'] if x['kind'] == 'gpu' else None
    if M['kind'] == 'cpu':  # CPU-only fallback: CPU recipes, then small models on CPU-capable engines
        if x['kind'] == 'cpu':
            if x['sys_ram_gb'] and x['sys_ram_gb'] > M['ram_gb'] + 2: return None
            s += 50; fit = 'exact'
        else:
            size = x.get('total_params_b')
            if not size or not CPU_ENGINES.search(x['engine']) or size * 0.6 > M['ram_gb'] * 0.8 or x['kind'] not in ('gpu', 'unified'): return None
            s += 10; fit = 'similar'; notes.append(f'measured on {x["hardware"]}; CPU-only speed is much lower')
    elif x['chip'] == M['chip']:
        if x['gpu_count'] > M['gpu_count']: return None
        mem = x['unified_mem_gb'] if x['kind'] == 'unified' else x['vram_gb']
        per = (mem or 0) / max(x['gpu_count'], 1); have = M['mem_gb'] / max(M['gpu_count'], 1)
        if mem and per > have + 2: return None
        if ram_need and ram_need > M['ram_gb'] + 4: return None
        s += 50; fit = 'exact'
        if x.get('laptop') != M['laptop']: s -= 30; fit = 'similar'; notes.append('laptop vs desktop GPU')
        if mem and per < have - 2 and x['kind'] == 'unified': notes.append(f'recipe used {mem:.0f}GB')
    else:
        mem = x['unified_mem_gb'] if x['kind'] == 'unified' else x['vram_gb']
        if not mem or x['gpu_count'] > 1 or x['kind'] != M['kind'] or mem > M['mem_gb']: return None
        if ram_need and ram_need > M['ram_gb'] + 4: return None
        s += 15; fit = 'similar'; notes.append(f'other hardware ({x["chip"]}); speed will differ')
    if M['os'] == 'windows' and x['os_hints'] == ['linux']: s -= 5; notes.append('tested on Linux; on Windows use WSL2')
    s += LEVEL.get(x['source_level'], 0) * 8
    s += max(0.0, 20 - age_days(x.get('date') or '', asof) / 9)
    s += min(x['tok_s'], 150) / 10
    if x['engine'] == 'Unspecified': s -= 5
    if x['source_level'] == '宣称': notes.append('claimed by the author; no raw data')
    return round(s, 2), fit, notes


def actionable(link):
    return link['url'] if link and link['trust'] == 'allowlisted' else None


def rank(idx, M, a):
    rows = []
    for x in idx['recipes']:
        r = score(x, M, a, idx['data_asof'])
        if r: rows.append((r, x))
    # 实测/官方 always rank above 宣称; then score; then id for a stable order
    rows.sort(key=lambda t: (t[1]['source_level'] == '宣称', -t[0][0], t[1]['id']))
    out, seen = [], set()
    for (s, fit, notes), x in rows:
        k = (x['model'], x['engine'])
        if k in seen: continue
        seen.add(k)
        src = x['source_url']
        out.append({'id': x['id'], 'score': s, 'fit': fit, 'model': x['model'], 'quant': x.get('quant'), 'engine': x['engine'],
                    'hardware': x['hardware'], 'tok_s_single_stream': x['tok_s'], 'context': x.get('context'), 'source_level': x['source_level'],
                    'date': x.get('date'), 'engine_repo': actionable(x['engine_repo']), 'weights_url': actionable(x['weights_url']),
                    'weights_url_from': x.get('weights_url_from'), 'launch_cmd': x['launch_cmd'], 'launch_cmd_warning': x.get('launch_cmd_warning'),
                    'recipe_page': x['recipe_page'] + ('' if a.lang == 'en' else '&lang=' + {'zh': 'zh-CN', 'ja': 'ja'}[a.lang]),
                    'recipe_md': x.get('recipe_md'),
                    'source_url': src['url'], 'source_trust': src['trust'], 'notes': notes})
        if len(out) >= a.top: break
    return out, len(rows)


def table(res, a):
    t = T[a.lang]; L = LEVEL_NAME[a.lang]; M = res['machine']
    lines = [f"{t['machine']}: {M['os']}, {M['gpu_name'] or M['chip'] or t['cpu']}, VRAM/unified {M['mem_gb']} GB, RAM {M['ram_gb']} GB",
             f"{t['asof']}: {res['data_asof']}", '']
    if not res['recipes']: lines.append(f"{t['none']} {EXPLORE}")
    for i, r in enumerate(res['recipes'], 1):
        lines.append(f"{i}. {r['model']} | {r['engine']} | {r['quant']} | {r['hardware']}")
        lines.append(f"   {t['speed']}: {r['tok_s_single_stream']}   {t['level']}: {L.get(r['source_level'], r['source_level'])}   ({r['date']}, {r['id']})")
        if r['fit'] == 'similar': lines.append(f"   ! {t['similar']}")
        lines.append(f"   {t['engine_repo']}: {r['engine_repo'] or t['nolink']}")
        lines.append(f"   {t['weights']}: {r['weights_url'] or t['nolink']}" + (' (base model card)' if r['weights_url_from'] == 'model-params.json' else ''))
        if r['launch_cmd']: lines.append(f"   {t['cmd']}: {r['launch_cmd']}")
        elif r['launch_cmd_warning']: lines.append(f"   {t['cmd']}: {t['unsafe']} ({', '.join(r['launch_cmd_warning'])})")
        lines.append(f"   {t['page']}: {r['recipe_page']}")
        lines.append(f"   {t['read']}: {r['source_url']}" + ('' if r['source_trust'] == 'allowlisted' else ' [unverified host]'))
        for n in r['notes']: lines.append(f"   - {n}")
    return '\n'.join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--hw', help='detect_hw.py JSON file, or - for stdin'); ap.add_argument('--index')
    ap.add_argument('--model'); ap.add_argument('--min-tok', type=float); ap.add_argument('--top', type=int, default=5)
    ap.add_argument('--include-relayed', action='store_true', help='also show 转述 (relayed) rows')
    ap.add_argument('--lang', default='en', choices=['en', 'zh', 'ja']); ap.add_argument('--json', action='store_true', help='JSON only')
    a = ap.parse_args(argv)
    hw = json.load(sys.stdin if a.hw in (None, '-') else open(a.hw, encoding='utf-8'))
    idx, src = load_index(a.index); M = machine(hw)
    recs, n = rank(idx, M, a)
    res = {'machine': M, 'index': src, 'data_asof': idx['data_asof'], 'candidates': n, 'recipes': recs}
    if a.json: print(json.dumps(res, ensure_ascii=False, indent=1))
    else: print(table(res, a)); print('\n---JSON---'); print(json.dumps(res, ensure_ascii=False))
    return res


if __name__ == '__main__': main()
