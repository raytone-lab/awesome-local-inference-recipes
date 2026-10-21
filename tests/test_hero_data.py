import sys, unittest
from pathlib import Path
R = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(R / 'scripts'))
import hero_data as H


def row(**k):
    r = dict(id='t-1', category='text', model='Qwen3.8-27B', hardware='RTX 3090 24GB', tok_s=10, hardware_cost_usd=1000, source_level='实测')
    r.update(k); return r


class Clean(unittest.TestCase):
    def test_removed_aside_keeps_word_gap(self):
        self.assertEqual(H.clean('RTX 3090 24GB（300W）+ 41GiB RAM', 80), 'RTX 3090 24GB + 41GiB RAM')
        self.assertEqual(H.clean('oQ4e（x）vs', 80), 'oQ4e vs')

    def test_truncation_drops_trailing_joiner(self):
        self.assertEqual(H.clean('ACEMAGIC Strix Halo 128GB + Mini PC', 28), 'ACEMAGIC Strix Halo 128GB…')


class Hwkey(unittest.TestCase):
    def test_drops_parenthesized_notes(self):
        self.assertEqual(H.hwkey('单 RTX 3090 24GB（2026-10 实测）'), 'rtx 3090 24gb')

    def test_keeps_asides_that_add_memory(self):
        self.assertEqual(H.hwkey('RTX 3090 (+64GB RAM)'), 'rtx 3090 +64gb ram')
        self.assertNotEqual(H.hwkey('RTX 3090 (+64GB RAM)'), H.hwkey('RTX 3090'))


class Dedupe(unittest.TestCase):
    def test_measured_beats_faster_claim_on_same_setup(self):
        claim = row(id='a', tok_s=99, source_level='宣称'); meas = row(id='b', tok_s=50, hardware='单 RTX 3090 24GB（note）')
        self.assertEqual(H.dedupe_setups([claim, meas]), [meas])

    def test_faster_wins_among_measured_then_id(self):
        a, b, c = row(id='a', tok_s=40), row(id='b', tok_s=50), row(id='c', tok_s=50)
        self.assertEqual(H.dedupe_setups([a, b, c]), [c])

    def test_different_setups_never_merge(self):
        a, b = row(id='a'), row(id='b', hardware='RTX 3090 24GB (+64GB RAM)')
        self.assertEqual(H.dedupe_setups([a, b]), [a, b])


class Rtx3090Baseline(unittest.TestCase):
    def test_bare_single_3090_strings(self):
        for hw in ('RTX 3090', '单 RTX 3090', 'RTX 3090 24GB', ' RTX 3090 24GB '):
            self.assertTrue(H.is_bare_single_3090(row(hardware=hw)), hw)
        for hw in ('2× RTX 3090', 'RTX 3090 24GB + 64GB RAM', 'RTX 3090 Ti', 'RTX 3090 24GB（+128GB RAM）'):
            self.assertFalse(H.is_bare_single_3090(row(hardware=hw)), hw)

    def test_baseline_uses_only_big_moe_rows(self):
        big = next(m for m in H.PARAMS if dict(H.GROUPS)['big'](m))
        dense = next(m for m in H.PARAMS if dict(H.GROUPS)['dense'](m))
        rows = H.annotate([row(id='big', model=big['label'], tok_s=20), row(id='dense', model=dense['label'], tok_s=40)])
        rows = [r for r in rows if H.params(r)]
        self.assertEqual(H.rtx3090_baseline(rows), 20.0)
        self.assertIsNone(H.rtx3090_baseline([r for r in rows if r['id'] == 'dense']))


class Tiers(unittest.TestCase):
    def test_tier_bounds_are_exclusive_low_inclusive_high(self):
        rows = H.annotate([row(id='a', hardware_cost_usd=2500), row(id='b', hardware_cost_usd=2501, source_level='宣称')])
        self.assertEqual([r['id'] for r in H.tier_rows(rows, 0, 2500)], ['a'])
        self.assertEqual([r['id'] for r in H.tier_rows(rows, 2500, 7000)], ['b'])

    def test_bounds_are_contiguous(self):
        b = H.BUDGET_TIER_BOUNDS_USD
        for (_, hi), (lo, _) in zip(b, b[1:]):
            self.assertEqual(hi, lo)

    def test_chart_tier_labels_follow_bounds(self):
        self.assertEqual(H.TIER_LABELS, ['≤ $2.5k', '$2.5k–7k', '$7k–14k', '$14k–30k'])
        self.assertEqual(H.tier_label(0, 1000), '≤ $1k')


class NoMatplotlib(unittest.TestCase):
    def test_hero_data_does_not_import_matplotlib(self):
        self.assertNotIn('matplotlib', H.__dict__)
        self.assertNotIn('import matplotlib', (R / 'scripts/hero_data.py').read_text())


if __name__ == '__main__': unittest.main()
