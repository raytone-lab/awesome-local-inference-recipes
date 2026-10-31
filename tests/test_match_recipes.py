import filecmp, importlib.util, json, sys, unittest
from pathlib import Path

R = Path(__file__).resolve().parent.parent
SKILL = R / '.agents/skills/local-inference-recipe-finder'
sys.path.insert(0, str(R / 'scripts'))
import gen_hw_index  # noqa: E402


def load_matcher():
    spec = importlib.util.spec_from_file_location('match_recipes', SKILL / 'scripts/match_recipes.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


M = load_matcher()
IDX = json.loads((R / 'data/hw_index.json').read_text(encoding='utf-8'))
PROFILES = {
    '4090_linux': {'os': 'linux', 'ram_gb': 64, 'cpu': 'AMD Ryzen 9 7950X', 'gpus': [{'name': 'NVIDIA GeForce RTX 4090', 'vram_gb': 24}]},
    'm5max_128': {'os': 'macos', 'ram_gb': 128, 'cpu': 'Apple M5 Max', 'gpus': [{'name': 'Apple M5 Max'}]},
    '3090_win_192': {'os': 'windows', 'ram_gb': 192, 'cpu': 'Intel Core i5-13600K', 'gpus': [{'name': 'NVIDIA GeForce RTX 3090', 'vram_gb': 24}]},
    'm2_24': {'os': 'macos', 'ram_gb': 24, 'cpu': 'Apple M2', 'gpus': [{'name': 'Apple M2'}]},
    'cpu_32': {'os': 'linux', 'ram_gb': 32, 'cpu': 'AMD Ryzen 7 7700', 'gpus': []},
}
EXPECT_CHIP = {'4090_linux': 'RTX 4090', 'm5max_128': 'M5 Max', '3090_win_192': 'RTX 3090', 'm2_24': 'M2', 'cpu_32': None}
OUT_KEYS = {'id', 'score', 'fit', 'model', 'quant', 'engine', 'hardware', 'tok_s_single_stream', 'context', 'source_level', 'date', 'engine_repo',
            'weights_url', 'weights_url_from', 'launch_cmd', 'launch_cmd_warning', 'recipe_page', 'recipe_md', 'source_url', 'source_trust', 'notes'}


def run(profile, *extra):
    a = M.argparse.Namespace(model=None, min_tok=None, top=5, include_relayed=False, lang='en')
    for k, v in extra: setattr(a, k, v)
    mach = M.machine(profile, IDX['chip_patterns'])
    return mach, M.rank(IDX, mach, a)[0]


class IndexInSync(unittest.TestCase):
    def test_index_matches_generator(self):
        self.assertEqual(gen_hw_index.render(gen_hw_index.build()), (R / 'data/hw_index.json').read_text(encoding='utf-8'))

    def test_every_row_has_a_chip(self):
        missing = [x['id'] for x in IDX['recipes'] if not x['chip']]
        self.assertEqual(missing, [], 'add a pattern to CHIPS in scripts/gen_hw_index.py')

    def test_schema(self):
        self.assertEqual(IDX['schema_version'], 1)
        self.assertEqual(IDX['count'], len(json.loads((R / 'data/recipes.json').read_text(encoding='utf-8'))))
        self.assertEqual(M.check(IDX), IDX)
        for x in IDX['recipes']:
            self.assertTrue(M.REQUIRED <= set(x), x['id'])
            self.assertIn(x['kind'], ('gpu', 'unified', 'cpu', 'phone', 'console'))
            self.assertTrue(x['recipe_page'].endswith('?id=' + x['id']))

    def test_parse_examples(self):
        p = gen_hw_index.parse_hw
        self.assertEqual(p('2× RTX 3090 24GB + 128GB DDR4')['vram_gb'], 48)
        self.assertEqual(p('2× RTX 3090 24GB + 128GB DDR4')['sys_ram_gb'], 128)
        self.assertEqual(p('4× ASUS Ascent GX10（GB10，100 Gb 交换机）')['unified_mem_gb'], 512)
        self.assertTrue(p('RTX 4090 Laptop 16GB')['laptop'])
        self.assertEqual(p('RTX 4090 Laptop 16GB')['vram_gb'], 16)
        self.assertEqual(p('Core i5-12600K（仅 CPU）')['kind'], 'cpu')
        self.assertEqual(p('Mac Studio M5 Ultra 256GB')['unified_mem_gb'], 256)


class MirrorInSync(unittest.TestCase):
    def test_claude_mirror_equals_agents(self):
        a, b = SKILL, R / '.claude/skills/local-inference-recipe-finder'
        fa = sorted(str(p.relative_to(a)) for p in a.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
        fb = sorted(str(p.relative_to(b)) for p in b.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
        self.assertEqual(fa, fb)
        for f in fa: self.assertTrue(filecmp.cmp(a / f, b / f, shallow=False), f)

    def test_skill_frontmatter(self):
        t = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        self.assertTrue(t.startswith('---\nname: local-inference-recipe-finder\ndescription: '))
        self.assertLessEqual(len(t.split('\n')[2]), 1024 + 13)


class Profiles(unittest.TestCase):
    def test_profiles(self):
        for name, prof in PROFILES.items():
            with self.subTest(profile=name):
                mach, out = run(prof)
                self.assertEqual(mach['chip'], EXPECT_CHIP[name])
                self.assertGreaterEqual(len(out), 3)
                self.assertEqual(out, run(prof)[1])  # stable
                ids = [r['id'] for r in out]; self.assertEqual(len(ids), len(set(ids)))
                rows = {x['id']: x for x in IDX['recipes']}
                for r in out:
                    self.assertEqual(set(r), OUT_KEYS)
                    self.assertNotEqual(r['source_level'], '转述')
                    x = rows[r['id']]
                    self.assertTrue(x['single_stream'])
                    for f in ('engine_repo', 'weights_url'):
                        if r[f]: self.assertEqual(x[f]['trust'], 'allowlisted')
                    if mach['os'] != 'macos': self.assertFalse(x['mac_only_engine'])
                    if r['fit'] == 'exact' and mach['kind'] != 'cpu':
                        self.assertEqual(x['chip'], mach['chip']); self.assertLessEqual(x['gpu_count'], mach['gpu_count'])
                    if mach['kind'] == 'cpu' and r['fit'] == 'exact': self.assertEqual(x['kind'], 'cpu')
                levels = [r['source_level'] for r in out]
                if '宣称' in levels: self.assertTrue(all(l == '宣称' for l in levels[levels.index('宣称'):]))

    def test_gpu_profiles_lead_with_exact(self):
        for name in ('4090_linux', 'm5max_128', '3090_win_192'):
            self.assertEqual(run(PROFILES[name])[1][0]['fit'], 'exact', name)

    def test_relayed_option(self):
        _, out = run(PROFILES['4090_linux'], ('include_relayed', True), ('top', 200))
        self.assertTrue(out)

    def test_table_languages(self):
        mach, out = run(PROFILES['4090_linux'])
        for lang in ('en', 'zh', 'ja'):
            a = M.argparse.Namespace(lang=lang)
            t = M.table({'machine': mach, 'data_asof': IDX['data_asof'], 'recipes': out}, a)
            self.assertIn(IDX['data_asof'], t)
            if lang == 'en': self.assertNotRegex(t.split('\n', 2)[0], r'[\u4e00-\u9fff]')

    def test_intel_mac_gets_no_apple_silicon_rows(self):
        mach, out = run({'os': 'macos', 'ram_gb': 32, 'cpu': 'Intel(R) Core(TM) i9-9980HK', 'unified_memory': False, 'gpus': [{'name': 'AMD Radeon Pro 5500M'}]})
        self.assertFalse(mach['apple_silicon'])
        rows = {x['id']: x for x in IDX['recipes']}
        for r in out: self.assertNotEqual(rows[r['id']]['kind'], 'unified'); self.assertFalse(rows[r['id']]['mac_only_engine'])

    def test_unknown_gpu_is_not_cpu_only(self):
        mach, _ = run({'os': 'windows', 'ram_gb': 32, 'gpus': [{'name': 'AMD Radeon RX 9070 XT', 'vram_gb': 16}]})
        self.assertEqual((mach['kind'], mach['chip']), ('gpu', 'RX 9070 XT'))
        mach, _ = run({'os': 'linux', 'ram_gb': 32, 'gpus': [{'name': 'Some Future GPU X1', 'vram_gb': 16}]})
        self.assertEqual(mach['kind'], 'gpu')

    def test_lspci_gpu_without_vram(self):
        mach, out = run({'os': 'linux', 'ram_gb': 64, 'gpus': [{'name': 'NVIDIA Corporation AD102 [GeForce RTX 4090]', 'vram_gb': None}]})
        self.assertEqual((mach['kind'], mach['chip']), ('gpu', 'RTX 4090'))
        self.assertTrue(out)

    def test_intel_arc_names(self):
        for n in ('Intel Corporation Arc B580', 'Intel(R) Arc(TM) B580 Graphics'):
            mach, _ = run({'os': 'linux', 'ram_gb': 32, 'gpus': [{'name': n, 'vram_gb': None}]})
            self.assertEqual(mach['kind'], 'gpu', n)

    def test_utf16_hw_file(self):
        import tempfile, os
        fd, name = tempfile.mkstemp(suffix='.json')
        with os.fdopen(fd, 'wb') as f: f.write(json.dumps(PROFILES['4090_linux']).encode('utf-16'))
        try: self.assertEqual(M.read_json(name)['os'], 'linux')
        finally: os.unlink(name)

    def test_bad_index_rejected(self):
        bad = json.loads(json.dumps(IDX)); bad['recipes'][0]['engine_repo'] = {'url': 'http://x.example', 'trust': 'allowlisted'}
        with self.assertRaises(SystemExit): M.check(bad)
        with self.assertRaises(SystemExit): M.check({'schema_version': 2, 'recipes': [], 'chip_patterns': []})


if __name__ == '__main__':
    unittest.main()
