import re, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scripts'))
import tag_recipes as t

def strip(s): return re.sub(t.KV_OR_SOURCE, '', s, flags=re.I)

class KvDtypeIsNotWeightQuant(unittest.TestCase):
    def test_weight_kept_cache_removed(self):
        self.assertEqual(strip('Q4_K_M KV Q8_0').strip(), 'Q4_K_M')
        self.assertNotIn('FP8', strip('Q4_K_M, KV cache FP8'))
        self.assertIn('Q4_K_M', strip('Q4_K_M, KV cache FP8'))
        self.assertNotIn('4-bit', strip('UD-Q4 + 4-bit KV'))
        self.assertIn('UD-Q4', strip('UD-Q4 + 4-bit KV'))
    def test_w3a4_is_3bit(self):
        self.assertTrue(re.search(dict(t.QUANT)['3bit'], 'W3A4', re.I))
