#!/usr/bin/env python3
"""Needs Google Chrome or Chromium on PATH. PNG bytes vary by browser and font version."""
import functools, http.server, os, shutil, subprocess, sys, tempfile, threading
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
LANGS = {'en': '', 'zh-CN': '.zh-CN', 'ja': '.ja'}
PAGE = 'index.html'
WINDOW = (1024, 720)
LIGHT_SCHEME = 'preferredColorScheme=1'
BROWSERS = ('google-chrome', 'chromium', 'chromium-browser')


def browser():
    for b in BROWSERS:
        if shutil.which(b): return b
    sys.exit('Chrome or Chromium not found')


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def main():
    handler = functools.partial(QuietHandler, directory=str(ROOT))
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    exe = browser()
    try:
        for lang, suf in LANGS.items():
            out = ROOT / 'docs' / f'screenshot{suf}.png'
            prof = tempfile.mkdtemp(prefix='shot-')
            cmd = [exe, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--user-data-dir={prof}',
                   '--force-prefers-reduced-motion', f'--blink-settings={LIGHT_SCHEME}', f'--lang={lang}',
                   f'--window-size={WINDOW[0]},{WINDOW[1]}', '--virtual-time-budget=8000', f'--screenshot={out}',
                   f'http://127.0.0.1:{srv.server_port}/{PAGE}?lang={lang}']
            if os.geteuid() == 0: cmd.insert(2, '--no-sandbox')
            try:
                subprocess.run(cmd, check=True, timeout=120, capture_output=True, text=True)
            except subprocess.CalledProcessError as e:
                sys.exit(e.stderr or str(e))
            finally:
                shutil.rmtree(prof, ignore_errors=True)
            print(out.relative_to(ROOT))
    finally:
        srv.shutdown()


if __name__ == '__main__':
    main()
