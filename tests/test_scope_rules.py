import json, os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
import scope_rules as S
from scope_text import SCOPE
R = os.path.join(os.path.dirname(__file__), '..')

OUT_OF_SCOPE_ROWS = {
    'text-076': '4 DGX Sparks plus an RTX 5090 PC count as 5; cost over $30k',
    'text-082': '4 DGX Sparks plus an RTX 5090 PC count as 5; cost over $30k',
    'comm-006': '6 RTX 3090 cards',
    'comm-043': '2 RTX PRO 6000 Max-Q cards cost about $33k',
    'text-125': '4 Mac Studio M5 Ultra 512GB cost at least $37,996',
    'text-129': '4 Mac Studio M5 Ultra 512GB cost at least $37,996',
    'text-133': '4 Mac Studio M5 Ultra 512GB cost at least $37,996',
}


def row(hardware, usd=None, cost_text=None):
    return {'hardware': hardware, 'hardware_cost_usd': usd, 'hardware_cost_text': cost_text}


def read(path):
    with open(os.path.join(R, path), encoding='utf-8') as f: return f.read()


class DeviceCount(unittest.TestCase):
    def test_counts(self):
        for hw, n in [('RTX 5090 32GB', 1), ('2× RTX 3090 + 64GB DDR5', 2), ('4× DGX Spark + RTX 5090', 5),
                      ('Threadripper PRO 9955WX + 128GB + 4× Radeon AI PRO R9700', 4), ('6× RTX 3090 + 7950X', 6),
                      ('RTX 5090 vs 1× DGX Spark', 1), ('1× / 2× DGX Spark', 2), ('8x H100', 8),
                      ('4× DGX Spark（有/无交换机均可）', 4), ('M4 Mac mini 16GB + RTX 3090 + iGPU', 2),
                      ('5× Strix Halo', 5), ('5× ASUS Ascent GX10', 5), ('8× P40', 8), ('M3 Ultra 512GB', 1)]:
            self.assertEqual(S.device_count(hw), n, hw)

    def test_multiplier_forms(self):
        for hw, n in [('RTX 3090 ×5', 5), ('RTX 3090 x5', 5), ('4x4090', 4), ('4xRTX 3090', 4), ('8 卡 4090', 8),
                      ('HP Z8（6× RTX A6000）', 6), ('1× DGX Spark（对照 4090）', 1)]:
            self.assertEqual(S.device_count(hw), n, hw)

    def test_model_numbers_and_lanes_are_not_multipliers(self):
        for hw in ('AMD RX 7900 XTX 24GB', 'AMD RX 9070 XT 16GB', 'RX 7900 XTX + Ryzen 9 9950X（PCIe 4.0 x16）',
                   'RTX 3090 PCIe 4.0 x16', 'i9-10900K + RTX 3090', 'RTX 5080 16GB（外置 M.2×2 RAID0 SSD）'):
            self.assertEqual(S.device_count(hw), 1, hw)


class Violations(unittest.TestCase):
    def test_each_condition(self):
        self.assertEqual(S.violations(row('RTX 5090', 5400)), [])
        self.assertEqual(S.violations(row('4× DGX Spark', 27800)), [])
        self.assertIn('cost over $30,000', S.violations(row('2× RTX PRO 6000', 32000)))
        self.assertIn('cost over $30,000', S.violations(row('2× RTX PRO 6000', None, '≈$33,000 ⚠️超$30k')))
        self.assertIn('5 GPUs or machines (max 4)', S.violations(row('5× RTX 3090')))
        self.assertTrue(S.violations(row('4× V100 SXM2')))
        self.assertTrue(S.violations(row('RTX 5090（液冷）')))

    def test_out_of_scope_rows_are_known(self):
        D = json.loads(read('data/recipes.json'))
        self.assertEqual({r['id'] for r in D if S.violations(r)}, set(OUT_OF_SCOPE_ROWS))


class RuleText(unittest.TestCase):
    def test_contributing_and_submit_page_carry_the_readme_rule(self):
        contributing, submit = read('CONTRIBUTING.md'), read('submit.html')
        for lang, s in SCOPE.items():
            for sentence in s['intro'] + [s['lead']] + s['items']:
                self.assertIn(sentence, contributing, lang)
                self.assertIn(sentence, submit, lang)


if __name__ == '__main__': unittest.main()
