import re, unittest
from pathlib import Path
R = Path(__file__).resolve().parent.parent
PAGES = 'https://raytone-lab.github.io/awesome-local-inference-recipes/'
CASES = [('README.md', 'en', '', '.md'), ('README.zh-CN.md', 'zh-CN', 'zh-CN/', '.zh-CN.md'), ('README.ja.md', 'ja', 'ja/', '.ja.md')]

class ReadmeLangLinks(unittest.TestCase):
    def test_site_links_match_readme_language(self):
        for f, code, pre, suf in CASES:
            txt = (R / f).read_text()
            urls = re.findall(re.escape(PAGES) + r'[^\s)"\'<>]+', txt)
            self.assertTrue(urls, f)
            for u in urls:
                path = u[len(PAGES):].split('#')[0]
                if not path.split('?')[0].endswith('.html'): continue
                with self.subTest(readme=f, url=u):
                    if path.startswith('hw/'):
                        rest = path[3:]
                        self.assertTrue(rest.startswith(pre) and (pre or not rest.startswith(('zh-CN/', 'ja/'))))
                        self.assertTrue((R / path).exists(), path)
                    else:
                        self.assertIn('lang=' + code, path.split('?', 1)[1] if '?' in path else '')

    def test_guide_links_match_readme_language(self):
        for f, code, pre, suf in CASES:
            links = re.findall(r'\]\((recipes/[^)]+)\)', (R / f).read_text())
            self.assertTrue(links, f)
            for l in links:
                with self.subTest(readme=f, link=l):
                    if suf == '.md': self.assertFalse(l.endswith(('.zh-CN.md', '.ja.md')))
                    else: self.assertTrue(l.endswith(suf))

if __name__ == '__main__': unittest.main()
