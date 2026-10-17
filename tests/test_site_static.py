import json, re, sys, unittest
from pathlib import Path
R = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(R/'scripts'))
class SiteStatic(unittest.TestCase):
    def setUp(self):
        self.D = json.loads((R/'data/recipes.json').read_text(encoding='utf-8'))
        self.sm = (R/'sitemap.xml').read_text(encoding='utf-8')
    def test_explore_fallback_has_every_row(self):
        s = (R/'explore.html').read_text(encoding='utf-8')
        import gen_site
        block = s[s.index(gen_site.STATIC_ROWS_START):s.index(gen_site.STATIC_ROWS_END)]
        self.assertEqual(len(re.findall(r'<tr data-id=', block)), len(self.D))
    def test_sitemap_lists_only_indexable_existing_pages(self):
        base = 'https://raytone-lab.github.io/awesome-local-inference-recipes/'
        for u in re.findall(r'<loc>([^<]+)</loc>', self.sm):
            self.assertTrue(u.startswith(base), u)
            rel = u[len(base):] or 'index.html'
            p = R/rel; self.assertTrue(p.exists(), rel)
            self.assertNotIn('noindex', p.read_text(encoding='utf-8'), rel)
        for p in list((R/'hw').glob('*.html')) + list((R/'model').glob('*.html')):
            s = p.read_text(encoding='utf-8'); n = s.count('<tr>') - 1
            import gen_site
            self.assertEqual('noindex' in s, n < gen_site.MIN_ROWS, p.name)
    def test_guides_hreflang_reciprocal_and_self_canonical(self):
        for p in (R/'guides').rglob('*.html'):
            if p.name == 'index.html': continue
            s = p.read_text(encoding='utf-8')
            canon = re.search(r'rel="canonical" href="([^"]+)"', s).group(1)
            alts = dict(re.findall(r'hreflang="([^"]+)" href="([^"]+)"', s))
            self.assertIn(canon, alts.values(), p)
            self.assertIn('x-default', alts)
            self.assertNotIn('HowTo', s); self.assertNotIn('FAQPage', s)


class LandingWording(unittest.TestCase):
    def test_summary_matches_data(self):
        import importlib.util, re, sys
        sys.path.insert(0, str(R/'scripts'))
        spec = importlib.util.spec_from_file_location('gs', R/'scripts/gen_site.py'); gs = importlib.util.module_from_spec(spec); spec.loader.exec_module(gs)
        from hardware_index import HW
        checks = []
        for key, name, rx, qt in HW:
            rows = [r for r in gs.D if re.search(rx, r['hardware'])]
            if rows: checks.append(('hw', key, rows))
        for f in sorted({r['model_family'] for r in gs.D if r['model_family'] != 'Other'}):
            rows = [r for r in gs.D if r['model_family'] == f]
            checks.append(('model', gs.slug(f), rows))
        for kind, file, rows in checks:
            nmeas = sum(1 for r in rows if r['source_level'] == '实测' and not gs.selfrep(r))
            for lang, none_s, has_s in [
                ('', 'None is first-hand yet', '1 was measured by the poster' if nmeas == 1 else f'{nmeas} were measured by the poster'),
                ('zh-CN', '尚无一手实测', f'实测 {nmeas} 条'),
                ('ja', '投稿者自身の実測はまだありません', f'投稿者実測は {nmeas} 件'),
            ]:
                path = R / kind / ((lang + '/') if lang else '') / f'{file}.html'
                s = path.read_text(encoding='utf-8')
                if nmeas == 0:
                    self.assertIn(none_s, s, str(path.relative_to(R)))
                else:
                    self.assertNotIn(none_s, s, str(path.relative_to(R)))
                    self.assertIn(has_s, s, str(path.relative_to(R)))
                if lang == 'ja':
                    self.assertIn(f'のレシピが <b>{len(rows)} 件</b>あります', s, str(path.relative_to(R)))
        for r in gs.D:
            if 'multi-GPU' in r['tags'] or gs.selfrep(r) or gs.COMPARE.search(r['hardware']):
                self.assertFalse(gs.meas_text(r) and gs.single(r), f"{r['id']}: headline must not cite multi-device, comparison or self-reported rows")

class GuidesIndexI18n(unittest.TestCase):
    def test_localized_indexes_exist_with_hreflang(self):
        for rel, brand in [('guides/index.html', 'Local Inference Recipes'),
                           ('guides/zh-CN/index.html', '本地推理配方'),
                           ('guides/ja/index.html', 'ローカル推論レシピ')]:
            s = (R/rel).read_text(encoding='utf-8')
            self.assertIn(brand, s, rel)
            for hl in ('en', 'zh-CN', 'ja', 'x-default'):
                self.assertIn(f'hreflang="{hl}"', s, rel)

    def test_english_index_links_translations_in_parens(self):
        s = (R/'guides/index.html').read_text(encoding='utf-8')
        self.assertRegex(s, r'<a href="[^"]+\.html">[^<]+</a> \(<a href="zh-CN/[^"]+">中文</a> · <a href="ja/[^"]+">日本語</a>\)')
        self.assertNotIn('(English', s)

    def test_zh_ja_guide_back_and_nav_stay_in_language(self):
        for lang, back, nav in [('zh-CN', '返回列表', '指南'), ('ja', '一覧に戻る', 'ガイド')]:
            for g in (R/'guides'/lang).glob('*.html'):
                if g.name == 'index.html': continue
                s = g.read_text(encoding='utf-8')
                self.assertIn(f'href="../../guides/{lang}/index.html">← {back}</a>', s, g.name)
                self.assertIn(f'href="../../guides/{lang}/index.html">{nav}</a>', s, g.name)

    def test_index_relative_hrefs_resolve(self):
        for page in (R/'guides').rglob('*.html'):
            for href in re.findall(r'href="([^"]+)"', page.read_text(encoding='utf-8')):
                if href.startswith(('http', '#', 'mailto')): continue
                path = href.split('#', 1)[0].split('?', 1)[0]
                if not path: continue
                self.assertTrue((page.parent / path).resolve().exists(), f'{page.relative_to(R)} -> {href}')


    def test_landing_relative_hrefs_resolve(self):
        for page in list((R/'hw').rglob('*.html')) + list((R/'model').rglob('*.html')):
            for href in re.findall(r'href="([^"]+)"', page.read_text(encoding='utf-8')):
                if href.startswith(('http', '#', 'mailto')): continue
                path = href.split('#', 1)[0].split('?', 1)[0]
                if not path: continue
                self.assertTrue((page.parent / path).resolve().exists(), f'{page.relative_to(R)} -> {href}')

    def test_landing_pages_exist_in_three_langs(self):
        for kind in ('hw', 'model'):
            en = {p.name for p in (R/kind).glob('*.html')}
            for lang in ('zh-CN', 'ja'):
                got = {p.name for p in (R/kind/lang).glob('*.html')}
                self.assertEqual(en, got, f'{kind}/{lang}')

if __name__ == '__main__':
    unittest.main()
