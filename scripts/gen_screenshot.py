#!/usr/bin/env python3
"""Render docs/screenshot{,.zh-CN,.ja}.png: the landing page (index.html) in each language, 1024x720.
Needs Google Chrome or Chromium on PATH. Not part of the CI up-to-date check (PNG bytes vary across browser and font versions).
Run: python3 scripts/gen_screenshot.py"""
import functools, http.server, shutil, subprocess, sys, tempfile, threading
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
LANGS = {'en': '', 'zh-CN': '.zh-CN', 'ja': '.ja'}
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
            with tempfile.TemporaryDirectory() as prof:
                subprocess.run([exe, '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars', f'--user-data-dir={prof}',
                                '--force-prefers-reduced-motion', '--blink-settings=preferredColorScheme=1', f'--lang={lang}',
                                '--window-size=1024,720', '--virtual-time-budget=8000', f'--screenshot={out}',
                                f'http://127.0.0.1:{srv.server_port}/index.html?lang={lang}'], check=True, capture_output=True, timeout=120)
            print(out.relative_to(ROOT))
    finally:
        srv.shutdown()


if __name__ == '__main__':
    main()
