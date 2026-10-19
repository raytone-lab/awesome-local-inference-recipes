#!/usr/bin/env python3
import json, re, sys
from pathlib import Path
from dataset_constants import BUDGET_TIER_BOUNDS_USD
ROOT = Path(__file__).resolve().parent.parent
MAX_DEVICES = 4
MAX_COST_USD = BUDGET_TIER_BOUNDS_USD[-1][1]
OVER_BUDGET_MARK = f'⚠️超${MAX_COST_USD // 1000}k'
MANUAL_CHECKS = ('total power about 2 kW with no special wiring', 'at most one desktop-class network switch')
DEVICE = re.compile(
    r'RTX|GTX|Radeon|\bRX ?\d|R9700|Instinct|\bMI\d{2,3}|Tesla|\b[VPAHLB](?:\d{2}|[1-9]00)S?s?(?![A-Za-z0-9])|\bA\d{4}s?(?![A-Za-z0-9])|\b(?:A(?:310|380|580|750|770)|B5[78]0|P10[246])s?(?![A-Za-z0-9])|CMP|DGX|Spark|GB10|Ascent|AI TOP'
    r'|Strix Halo|Ryzen AI Max|Framework Desktop|\bMac\b|MacBook|\bM\d (?:Pro|Max|Ultra)\b|\bArc\b|(?<![A-Za-z])GPU'
    r'|(?<![\d-])[1-9]0[5-9]0(?:S|Ti|D)?s?(?![A-Za-z0-9])|\b7900(?:XTX|XT|GRE)?s?(?![A-Za-z0-9])|\b9070(?:XT|GRE)?s?(?![A-Za-z0-9])')
SERVER_ONLY = re.compile(r'SXM|HGX|\brack|\b[124]U\b|机架|机柜|液冷|水冷|liquid[- ]cool|water[- ]cool', re.I)
PARENS = re.compile(r'（([^）]*)）|\(([^)]*)\)')
ALTERNATIVES = re.compile(r'/|\bvs\.?\b')
PCIE_LANES = re.compile(r'(?:PCIe|Gen\s?\d|@)[\s\d.]*[xX]\d+')
MULTIPLIERS = (re.compile(r'(?<![\w.])(\d{1,2})\s*(?:×|[xX](?=[\sA-Z0-9]))'),
               re.compile(r'(?:×|(?<=\s)[xX])\s*(\d{1,2})(?![\w.])'),
               re.compile(r'(?<![\w.])(\d{1,2})\s*(?:张|卡|台)'),
               re.compile(r'(?<![\w.])(\d{1,2})\s+(?:GPUs?|cards?)\b'))

def part_count(part):
    part = PCIE_LANES.sub('', part)
    if not DEVICE.search(part): return 0
    for m in (p.search(part) for p in MULTIPLIERS):
        if m: return int(m.group(1))
    return 1

def flat_count(text):
    return max(sum(part_count(p) for p in alt.split('+')) for alt in ALTERNATIVES.split(text))

def device_count(hardware):
    inner = [a or b for a, b in PARENS.findall(hardware)]
    return max([flat_count(PARENS.sub('', hardware))] + [flat_count(t) for t in inner])

def violations(r):
    out = []
    usd = r.get('hardware_cost_usd')
    if (usd is not None and usd > MAX_COST_USD) or OVER_BUDGET_MARK in (r.get('hardware_cost_text') or ''):
        out.append(f'cost over ${MAX_COST_USD:,}')
    n = device_count(r['hardware'])
    if n > MAX_DEVICES:
        out.append(f'{n} GPUs or machines (max {MAX_DEVICES})')
    if SERVER_ONLY.search(r['hardware']):
        out.append('server-only hardware (rack, SXM/HGX or liquid cooling)')
    return out

if __name__ == '__main__':
    with open(ROOT/'data/recipes.json', encoding='utf-8') as f: D = json.load(f)
    bad = [(r, violations(r)) for r in D]
    bad = [(r, v) for r, v in bad if v]
    for r, v in bad: print(r['id'], '|', r['hardware'], '|', '; '.join(v))
    print(f'{len(bad)} of {len(D)} recipes fail a mechanical check. Check by hand: ' + '; '.join(MANUAL_CHECKS) + '.')
    sys.exit(1 if bad else 0)
