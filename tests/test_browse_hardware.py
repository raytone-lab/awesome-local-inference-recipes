import json, re, sys, unittest
from pathlib import Path
from urllib.parse import unquote
R = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(R/'scripts'))
import hardware_index as hi
PAGES = 'https://raytone-lab.github.io/awesome-local-inference-recipes/'
EXPLORER_DEFAULT_BUDGET = int(re.search(r'id="budget"[^>]*value="(\d+)"', (R/'explore.html').read_text(encoding='utf-8')).group(1))
README = {'en': 'README.md', 'zh': 'README.zh-CN.md', 'ja': 'README.ja.md'}

def explorer_count(D, link):
    q = re.search(r'[?&]q=([^&]+)', link); t = re.search(r'[?&]tag=([^&]+)', link)
    D = [r for r in D if r['hardware_cost_usd'] is None or r['hardware_cost_usd'] <= EXPLORER_DEFAULT_BUDGET]
    if t: return sum(unquote(t.group(1)) in r['tags'] for r in D)
    return sum(unquote(q.group(1)).lower() in hi.explorer_text(r) for r in D)

class BrowseByHardware(unittest.TestCase):
    def setUp(self):
        self.D = json.loads((R/'data/recipes.json').read_text(encoding='utf-8'))

    def section(self, lang):
        s = (R/README[lang]).read_text(encoding='utf-8')
        heads = re.findall(r'^## (.+)$', s, re.M)
        i = heads.index({'en': 'Browse by Hardware', 'zh': '按硬件浏览', 'ja': 'ハードウェア別'}[lang])
        self.assertEqual(heads[i+1], {'en': 'Browse by Model Family', 'zh': '按模型系列浏览', 'ja': 'モデルファミリー別'}[lang])
        a = s.index('## ' + heads[i]); return s[a:s.index('## ' + heads[i+1])]

    def test_every_link_count_matches_its_target(self):
        for lang in README:
            chips = re.findall(r'\[([^\]]+)\]\(([^)]+)\) \((\d+)', self.section(lang))
            self.assertEqual(len(chips), sum(len(c) for _, c in hi.grid(self.D)), lang)
            for label, link, n in chips:
                self.assertTrue(link.startswith(PAGES), link)
                rel = link[len(PAGES):]
                if rel.startswith('hw/'):
                    page = (R/rel).read_text(encoding='utf-8')
                    self.assertNotIn('noindex', page, rel)
                    self.assertEqual(page.count('<tr>') - 1, int(n), rel)
                else:
                    self.assertTrue(rel.startswith('explore.html?'), rel)
                    self.assertEqual(explorer_count(self.D, link), int(n), f'{lang} {label}')

    def test_explorer_text_uses_the_same_fields_as_app_js_search(self):
        js = (R/'app.js').read_text(encoding='utf-8')
        fields = re.search(r'const match=q=>r=>!q\|\|\[(.*?)\]\.join', js).group(1)
        self.assertEqual(fields, 'r.model,r.quant,r.engine,r.engine_note,r.hardware,r.metric,r.metric_en,r.model_family,...r.tags')

    def test_fastest_is_measured_and_shown(self):
        for g, chips in hi.grid(self.D):
            for c, n, b in chips:
                if b: self.assertTrue(hi.meas_text(b), c.label)
        s = self.section('en')
        x = next(b for g, ch in hi.grid(self.D) for c, n, b in ch if c.page == 'rtx-5090')
        self.assertIn(f"⚡**{x['tok_s']:g}**", s)

    def test_chips_ordered_by_count_within_group(self):
        for g, chips in hi.grid(self.D):
            ns = [n for _, n, _ in chips]; self.assertEqual(ns, sorted(ns, reverse=True), g)

class SparkHeadline(unittest.TestCase):
    def test_readme_headline_matches_the_dgx_spark_chip(self):
        D = json.loads((R/'data/recipes.json').read_text(encoding='utf-8'))
        b = hi.fastest_on_page(D, 'dgx-spark')
        for lang, label in [('en', 'Fastest on one DGX Spark'), ('zh', '单台 DGX Spark 最快'), ('ja', 'DGX Spark 1 台で最速')]:
            s = (R/README[lang]).read_text(encoding='utf-8')
            row = next(l for l in s.splitlines() if l.startswith('| ' + label))
            self.assertIn(f"**{b['tok_s']:g} tok/s**", row, lang); self.assertIn(b['source_url'], row, lang)
            self.assertRegex(s, re.escape('[DGX Spark](' + PAGES + 'hw/' + {'en': '', 'zh': 'zh-CN/', 'ja': 'ja/'}[lang] + 'dgx-spark.html) (') + r'\d+ · ⚡\*\*' + re.escape(f"{b['tok_s']:g}") + r'\*\*', lang)

if __name__ == '__main__': unittest.main()
