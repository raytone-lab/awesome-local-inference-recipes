"""URL and launch-command hygiene for recipe data and data/hw_index.json.
Used by gen_hw_index.py and tests/test_url_safety.py. Stdlib only."""
import ipaddress, json, re, unicodedata
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / 'data/trusted_domains.json').read_text(encoding='utf-8'))
TRUSTED = CFG['trusted']
URL_RE = re.compile(r'https?://[^\s<>"\'`)\]）】，,;；]+')
GH_PART = re.compile(r'^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$')
REPO_PART = re.compile(r'^[A-Za-z0-9._-]{1,100}$')
# Brand words that a typosquat tries to copy, with the hosts that may use them.
BRANDS = {'github': ('github.com', 'raw.githubusercontent.com', 'github.io'), 'huggingface': ('huggingface.co',), 'modelscope': ('modelscope.cn',),
          'ollama': ('ollama.com',), 'pypi': ('pypi.org',), 'nvidia': ('nvidia.com',), 'apple': ('apple.com',)}


def host_of(url):
    return (urlsplit(url).hostname or '').lower()


def under(host, dom):
    return host == dom or host.endswith('.' + dom)


def trusted(url):
    return any(under(host_of(url), d) for d in TRUSTED)


def _dist(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def problems(url):
    """Return a list of hygiene problems for one URL (empty list = clean)."""
    out = []
    if any(ord(c) > 127 for c in url):
        scripts = {unicodedata.name(c, '?').split()[0] for c in url if c.isalpha()}
        out.append('non-ASCII characters' + (' (mixed scripts)' if len(scripts) > 1 else ''))
    try:
        p = urlsplit(url)
        port = p.port
    except ValueError:
        return out + ['unparseable URL']
    host = (p.hostname or '').lower()
    if p.scheme != 'https': out.append('not https')
    if not host: return out + ['no host']
    if '@' in p.netloc: out.append('userinfo in URL')
    if port not in (None, 443): out.append(f'non-default port {port}')
    try:
        ipaddress.ip_address(host.strip('[]')); out.append('IP-literal host')
    except ValueError:
        pass
    if 'xn--' in host: out.append('punycode host')
    if any(under(host, s) for s in CFG['shorteners']): out.append('URL shortener')
    labels = re.split(r'[.-]', host)
    for brand, okhosts in BRANDS.items():
        if any(under(host, h) for h in okhosts): continue
        for lab in labels:
            if lab != brand and len(lab) >= 4 and _dist(lab, brand) <= 2 and abs(len(lab) - len(brand)) <= 2:
                out.append(f'lookalike of {brand}: {host}')
    parts = [x for x in p.path.split('/') if x]
    if host == 'github.com':
        if len(parts) < 2 and not (parts and parts[0] in CFG['github_non_repo_paths']) and parts:
            pass  # a user or org page is allowed
        if len(parts) >= 2 and parts[0] not in CFG['github_non_repo_paths'] and not (GH_PART.match(parts[0]) and REPO_PART.match(parts[1])):
            out.append('GitHub path is not owner/repo')
    if host in ('huggingface.co', 'hf.co') and parts and parts[0] not in CFG['hf_prefixes']:
        if len(parts) < 2 or not (REPO_PART.match(parts[0]) and REPO_PART.match(parts[1])):
            out.append('Hugging Face path is not owner/repo')
    return out


def repo_key(url):
    """'host/owner/repo' for GitHub, Codeberg, HF and ModelScope URLs, else None."""
    p = urlsplit(url); host = (p.hostname or '').lower(); parts = [x for x in p.path.split('/') if x]
    if host in ('huggingface.co', 'hf.co') and parts and parts[0] in ('models',): parts = parts[1:]
    if host in ('modelscope.cn',) and parts and parts[0] == 'models': parts = parts[1:]
    if host in ('github.com', 'codeberg.org', 'huggingface.co', 'hf.co', 'modelscope.cn') and len(parts) >= 2 \
            and parts[0] not in CFG['github_non_repo_paths'] + CFG['hf_prefixes']:
        return f'{host}/{parts[0]}/{parts[1]}'
    return None


UNSAFE_CMD = [
    (re.compile(r'\b(curl|wget)\b[^|;&]*\|\s*(sudo\s+)?(ba|z|da)?sh\b'), 'pipes a download into a shell'),
    (re.compile(r'\b(ba|z)?sh\s+<\('), 'runs a downloaded script through process substitution'),
    (re.compile(r'(^|[\s;&|(])sudo\b'), 'uses sudo'),
    (re.compile(r'\brm\s+-[a-zA-Z]*r[a-zA-Z]*f|\brm\s+-[a-zA-Z]*f[a-zA-Z]*r'), 'uses rm -rf'),
    (re.compile(r'\bpip3?\s+install\b[^;&|]*\b(git\+\S+|https?://\S+)'), 'pip install from a URL'),
    (re.compile(r'\b(iex|Invoke-Expression)\b.*\b(iwr|Invoke-WebRequest|irm)\b|\b(iwr|irm)\b[^|]*\|\s*iex', re.I), 'PowerShell download-and-run'),
]


def cmd_problems(cmd):
    out = [why for rx, why in UNSAFE_CMD if rx.search(cmd or '')]
    for m in re.finditer(r'(git\+)?(https?://\S+)', cmd or ''):
        if m.group(1) and not trusted(m.group(2)): out.append('git+ URL on an unverified host')
    return out
