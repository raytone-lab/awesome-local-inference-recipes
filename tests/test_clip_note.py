import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scripts'))
from gen_recipe_pages import clip_note
import tag_recipes


class ClipNote(unittest.TestCase):
    def test_short_note_unchanged(self):
        self.assertEqual(clip_note('abc'), 'abc')

    def test_never_cuts_inside_url(self):
        s = 'x' * 180 + '（https://github.com/Niko1221/Strata/issues/4643）'
        out = clip_note(s)
        self.assertNotIn('https://', out)
        self.assertTrue(out.endswith('…'))

    def test_keeps_whole_url_before_limit(self):
        s = 'see https://a.b/c ' + 'y' * 300
        self.assertIn('https://a.b/c', clip_note(s))


class GptOssMoE(unittest.TestCase):
    def test_gpt_oss_is_moe(self):
        r = {'model': 'gpt-oss-120b', 'quant': 'MXFP4', 'engine': 'llama.cpp', 'category': 'text'}
        self.assertIn('MoE', tag_recipes.tags(r))


if __name__ == '__main__':
    unittest.main()
