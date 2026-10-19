import json, os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
import scope_rules as S
R = os.path.join(os.path.dirname(__file__), '..')

AWAITING_MAINTAINER_DECISION = {'text-076', 'text-082', 'comm-006', 'comm-043'}


def row(hardware, usd=None, cost_text=None):
    return {'hardware': hardware, 'hardware_cost_usd': usd, 'hardware_cost_text': cost_text}


class DeviceCount(unittest.TestCase):
    def test_counts(self):
        for hw, n in [('RTX 5090 32GB', 1), ('2× RTX 3090 + 64GB DDR5', 2), ('4× DGX Spark + RTX 5090', 5),
                      ('Threadripper PRO 9955WX + 128GB + 4× Radeon AI PRO R9700', 4), ('6× RTX 3090 + 7950X', 6),
                      ('RTX 5090 vs 1× DGX Spark', 1), ('1× / 2× DGX Spark', 2), ('8x H100', 8),
                      ('4× DGX Spark（有/无交换机均可）', 4), ('Strix Halo 128GB', 0)]:
            self.assertEqual(S.device_count(hw), n, hw)

    def test_model_numbers_are_not_multipliers(self):
        for hw in ('AMD RX 7900 XTX 24GB', 'AMD RX 9070 XT 16GB', 'RX 7900 XTX + Ryzen 9 9950X（PCIe 4.0 x16）'):
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

    def test_out_of_scope_rows_are_the_ones_awaiting_a_decision(self):
        D = json.load(open(os.path.join(R, 'data/recipes.json'), encoding='utf-8'))
        self.assertEqual({r['id'] for r in D if S.violations(r)}, AWAITING_MAINTAINER_DECISION)


if __name__ == '__main__': unittest.main()
