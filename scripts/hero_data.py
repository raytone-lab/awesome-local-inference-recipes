import json, re
from pathlib import Path
from dataset_constants import BUDGET_TIER_BOUNDS_USD, DATA_ASOF

R = Path(__file__).resolve().parent.parent
PER = 5
PARENTHESIZED = re.compile(r'[（(]([^）)]*)[）)]')
ADDED_MEMORY = re.compile(r'\+\s*\d+\s*GB')
BARE_SINGLE_3090 = re.compile(r'(单 )?RTX 3090( 24GB)?')


def clean(s, n):
    s = re.sub(r'[（(][^）)]*[）)]', ' ', s); s = re.sub(r'[\u3000-\u30ff\u4e00-\u9fff，、；：]+', ' ', s); s = re.sub(r'\s+', ' ', s).strip(' +/·')
    return s if len(s) <= n else s[:n-1] + '…'


def hwkey(s):
    s = PARENTHESIZED.sub(lambda m: ' ' + m.group(1) if ADDED_MEMORY.search(m.group(1)) else '', s)
    return re.sub(r'\s+', ' ', re.sub(r'^单\s*', '', s)).strip().lower()


def money(x): return f'${x/1000:.1f}k' if x >= 1000 else f'${x:.0f}'


def is_measured(r): return r['source_level'] == '实测'


def dedupe_key(r): return (hwkey(r['hardware']), clean(r['model'], 80).lower())


def preference(r): return (is_measured(r), r['tok_s'], r['id'])


def dedupe_setups(rows):
    best = {}
    for r in rows:
        k = dedupe_key(r); cur = best.get(k)
        if cur is None or preference(r) > preference(cur): best[k] = r
    return sorted(best.values(), key=lambda r: r['id'])


def priced_text_rows(recipes):
    return [r for r in recipes if r['category'] == 'text' and r['tok_s'] and r['hardware_cost_usd']]


def annotate(rows):
    for r in rows: r['_v'] = r['tok_s'] / r['hardware_cost_usd'] * 1000; r['_m'] = is_measured(r)
    return rows


def load_setups():
    return annotate(dedupe_setups(priced_text_rows(json.load(open(R/'data/recipes.json')))))


PARAMS = json.load(open(R/'data/model-params.json'))['models']


def params(r):
    for m in PARAMS:
        if re.search(m['match'], r['model']):
            return None if m.get('exclude') and re.search(m['exclude'], r['model']) else m
    return None


def fmtb(x): return f"{x:g}B"


GROUPS = [('dense', lambda m: m['arch'] == 'dense' and m['total_b'] >= 27),
          ('big', lambda m: m['arch'] == 'moe' and m['total_b'] >= 100),
          ('mid', lambda m: m['arch'] == 'moe' and m['total_b'] < 100 and m['active_b'] >= 5),
          ('small', lambda m: m['arch'] == 'moe' and m['total_b'] < 100 and m['active_b'] < 5)]


def in_group(key, r): return dict(GROUPS)[key](params(r))


def by_value(r): return (-r['_v'], r['id'])


def measured_with_card(setups): return [r for r in setups if r['_m'] and params(r)]


def title_row(setups):
    meas = measured_with_card(setups)
    dense = [r for r in meas if in_group('dense', r)]
    return min(dense or meas, key=by_value)


def grouped_rows(meas):
    rows = []; big_span = None
    for key, ok in GROUPS:
        rs = sorted([r for r in meas if ok(params(r))], key=by_value)[:PER]
        if rs: rows.append(('h', key)); rows += [('r', r) for r in rs]
        if rs and key == 'big': big_span = (len(rows) - len(rs) - 1, len(rows) - 1)
    return rows, big_span


def is_bare_single_3090(r): return bool(BARE_SINGLE_3090.fullmatch(r['hardware'].strip()))


def rtx3090_baseline(meas):
    b = [r for r in meas if is_bare_single_3090(r) and in_group('big', r)]
    return max(r['_v'] for r in b) if b else None


def tier_rows(setups, lo, hi):
    rs = [r for r in setups if lo < r['hardware_cost_usd'] <= hi]; rows = []
    for m in (True, False):
        pool = [r for r in rs if r['_m'] == m]
        if pool: rows.append(max(pool, key=lambda r: (r['tok_s'], r['id'])))
    return rows


def thousands(x): return f'{x/1000:g}k'


def tier_label(lo, hi):
    return f'≤ ${thousands(hi)}' if lo == 0 else f'${thousands(lo)}–{thousands(hi)}'


TIER_LABELS = [tier_label(lo, hi) for lo, hi in BUDGET_TIER_BOUNDS_USD]


def is_used(r): return '二手' in (r.get('hardware_cost_text') or '') or '二手' in r['hardware']


