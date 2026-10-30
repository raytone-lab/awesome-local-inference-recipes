#!/usr/bin/env python3
"""Render docs/screenshot*.png with headless Chrome or Chromium on PATH. PNG bytes vary by browser and font version.

The script drives the browser over the DevTools protocol. It does not use `--screenshot`: on some hosts that
one-shot mode never exits (for example when the browser loads extension background pages), and it only waits
for a fixed virtual-time budget. Here we wait until the page has rendered its data and its fonts, with a timeout."""
import base64, functools, http.server, json, os, re, shutil, socket, struct, subprocess, sys, tempfile, threading, time, urllib.parse, urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
LANGS = {'en': '', 'zh-CN': '.zh-CN', 'ja': '.ja'}
PAGE = 'index.html'
WINDOW = (1024, 720)
BROWSERS = ('google-chrome', 'chromium', 'chromium-browser')
START_TIMEOUT = 30   # seconds for the browser to open its DevTools port
PAGE_TIMEOUT = 45    # seconds for one page to become ready
# Ready when the budget list and key stats have data and the web fonts are loaded.
READY_JS = ("document.readyState==='complete' && document.fonts.status==='loaded' && "
            "!!document.querySelector('#tb li:not(.muted)') && document.querySelector('#ks').childElementCount>0")


def browser():
    for b in BROWSERS:
        if shutil.which(b): return b
    sys.exit('Chrome or Chromium not found')


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class CDP:
    """Minimal DevTools WebSocket client (text frames only), standard library only."""
    def __init__(self, ws_url, timeout):
        u = urllib.parse.urlparse(ws_url)
        self.s = socket.create_connection((u.hostname, u.port), timeout=timeout)
        key = base64.b64encode(os.urandom(16)).decode()
        self.s.sendall((f'GET {u.path} HTTP/1.1\r\nHost: {u.hostname}:{u.port}\r\nUpgrade: websocket\r\n'
                        f'Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n').encode())
        head = b''
        while b'\r\n\r\n' not in head:
            c = self.s.recv(1)
            if not c: raise ConnectionError('DevTools handshake closed')
            head += c
        if b' 101 ' not in head.split(b'\r\n', 1)[0]: raise ConnectionError(head.decode(errors='replace'))
        self.n = 0

    def _recv_exact(self, n):
        b = b''
        while len(b) < n:
            c = self.s.recv(n - len(b))
            if not c: raise ConnectionError('DevTools socket closed')
            b += c
        return b

    def _recv(self):
        data = b''
        while True:
            h = self._recv_exact(2); fin, op, ln = h[0] & 0x80, h[0] & 0x0F, h[1] & 0x7F
            if ln == 126: ln = struct.unpack('>H', self._recv_exact(2))[0]
            elif ln == 127: ln = struct.unpack('>Q', self._recv_exact(8))[0]
            data += self._recv_exact(ln)
            if op == 8: raise ConnectionError('DevTools socket closed')
            if fin: return json.loads(data)

    def call(self, method, **params):
        self.n += 1
        p = json.dumps({'id': self.n, 'method': method, 'params': params}).encode()
        h = bytes([0x81]); ln = len(p)
        h += bytes([0x80 | ln]) if ln < 126 else (bytes([0x80 | 126]) + struct.pack('>H', ln) if ln < 65536 else bytes([0x80 | 127]) + struct.pack('>Q', ln))
        mask = os.urandom(4)
        self.s.sendall(h + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(p)))
        while True:
            m = self._recv()
            if m.get('id') == self.n:
                if 'error' in m: raise RuntimeError(f"{method}: {m['error']}")
                return m.get('result', {})

    def close(self):
        self.s.close()


def start_browser(exe, prof):
    cmd = [exe, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--disable-extensions',
           '--force-prefers-reduced-motion', f'--user-data-dir={prof}', '--remote-debugging-port=0', 'about:blank']
    if os.geteuid() == 0: cmd.insert(2, '--no-sandbox')
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    port_file = Path(prof) / 'DevToolsActivePort'
    end = time.time() + START_TIMEOUT
    while time.time() < end:
        if port_file.exists():
            lines = port_file.read_text().split()
            if lines: return proc, int(lines[0])
        if proc.poll() is not None: break
        time.sleep(0.2)
    proc.kill()
    raise RuntimeError(f'browser did not open a DevTools port in {START_TIMEOUT}s')


def shoot(port, url, out):
    req = urllib.request.Request(f'http://127.0.0.1:{port}/json/new?about:blank', method='PUT')
    tgt = json.load(urllib.request.urlopen(req, timeout=10))
    cdp = CDP(tgt['webSocketDebuggerUrl'], PAGE_TIMEOUT)
    try:
        cdp.call('Emulation.setDeviceMetricsOverride', width=WINDOW[0], height=WINDOW[1], deviceScaleFactor=1, mobile=False)
        cdp.call('Emulation.setEmulatedMedia', features=[{'name': 'prefers-color-scheme', 'value': 'light'},
                                                         {'name': 'prefers-reduced-motion', 'value': 'reduce'}])
        cdp.call('Page.navigate', url=url)
        end = time.time() + PAGE_TIMEOUT
        while True:
            r = cdp.call('Runtime.evaluate', expression=READY_JS, returnByValue=True)
            if r.get('result', {}).get('value') is True: break
            if time.time() > end: raise TimeoutError(f'{url} not ready after {PAGE_TIMEOUT}s')
            time.sleep(0.25)
        time.sleep(0.5)  # let the last layout settle
        png = cdp.call('Page.captureScreenshot', format='png')['data']
        out.write_bytes(base64.b64decode(png))
    finally:
        cdp.close()
        try: urllib.request.urlopen(f"http://127.0.0.1:{port}/json/close/{tgt['id']}", timeout=5).read()
        except Exception: pass


def main():
    handler = functools.partial(QuietHandler, directory=str(ROOT))
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    prof = tempfile.mkdtemp(prefix='shot-')
    proc = None
    try:
        proc, port = start_browser(browser(), prof)
        for lang, suf in LANGS.items():
            out = ROOT / 'docs' / f'screenshot{suf}.png'
            shoot(port, f'http://127.0.0.1:{srv.server_port}/{PAGE}?lang={lang}', out)
            print(out.relative_to(ROOT))
    except Exception as e:
        sys.exit(f'gen_screenshot failed: {e}')
    finally:
        if proc:
            proc.terminate()
            try: proc.wait(timeout=10)
            except subprocess.TimeoutExpired: proc.kill()
        srv.shutdown()
        shutil.rmtree(prof, ignore_errors=True)


if __name__ == '__main__':
    main()
