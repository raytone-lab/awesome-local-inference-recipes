#!/usr/bin/env python3
import argparse, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
TEXT = ('gen_watchlist.py', 'gen_readme.py', 'gen_recipe_pages.py', 'gen_site.py')
IMAGES = ('gen_hero.py', 'gen_screenshot.py')
OPTIONAL = {'gen_screenshot.py'}  # a failed screenshot keeps the old PNGs and does not stop the run


def main(argv):
    ap = argparse.ArgumentParser(description='Run every text generator. CI runs this and fails on any diff.')
    ap.add_argument('--images', action='store_true', help='also render the README charts and the site screenshots')
    a = ap.parse_args(argv)
    for s in TEXT + (IMAGES if a.images else ()):
        print(f'== {s}', flush=True)
        rc = subprocess.run([sys.executable, str(HERE / s)]).returncode
        if rc and s in OPTIONAL:
            print(f'WARNING: {s} failed (exit {rc}); the old files are kept', file=sys.stderr, flush=True)
        elif rc:
            sys.exit(rc)


if __name__ == '__main__':
    main(sys.argv[1:])
