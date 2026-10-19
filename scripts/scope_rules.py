#!/usr/bin/env python3
"""Mechanical checks for the scope rule in CONTRIBUTING.md: budget, device count and server-only build features.
Power and switch class need a human reading of the source. Run: python3 scripts/scope_rules.py"""
import json, re
from pathlib import Path
from dataset_constants import BUDGET_TIER_BOUNDS_USD
ROOT = Path(__file__).resolve().parent.parent
MAX_DEVICES = 4
MAX_COST_USD = BUDGET_TIER_BOUNDS_USD[-1][1]
OVER_BUDGET_MARK = '⚠️超$30k'
DEVICE = re.compile(r'RTX|GTX|Radeon|\bRX ?\d|R9700|Instinct|\bMI\d|Tesla|V100|A800|A100|H100|H200|B200|CMP|Spark|Mac|\bArc\b|GPU|\b[1-5]0[5-9]0', re.I)
SERVER_ONLY = re.compile(r'SXM|HGX|\brack\b|机架|机柜|液冷|水冷|liquid[- ]cool', re.I)
PARENS = re.compile(r'（[^）]*）|\([^)]*\)')
ALTERNATIVES = re.compile(r'/|\bvs\.?\b')
MULTIPLIER = re.compile(r'(\d+)\s*(?:×|[xX](?![A-Za-z0-9]))')

def device_count(hardware):
    counts = []
    for alt in ALTERNATIVES.split(PARENS.sub('', hardware)):
        n = 0
        for part in alt.split('+'):
            if DEVICE.search(part):
                m = MULTIPLIER.search(part)
                n += int(m.group(1)) if m else 1
        counts.append(n)
    return max(counts)

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
    D = json.load(open(ROOT/'data/recipes.json', encoding='utf-8'))
    for r in D:
        v = violations(r)
        if v: print(r['id'], '|', r['hardware'], '|', '; '.join(v))
