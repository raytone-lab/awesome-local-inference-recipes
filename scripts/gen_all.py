#!/usr/bin/env python3
import argparse, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
TEXT = ('gen_watchlist.py', 'gen_readme.py', 'gen_recipe_pages.py', 'gen_site.py')
IMAGES = ('gen_hero.py', 'gen_screenshot.py')


def main(argv):
    ap = argparse.ArgumentParser(description='Run every text generator. CI runs this and fails on any diff.')
    ap.add_argument('--images', action='store_true', help='also render the README charts and the site screenshots')
    a = ap.parse_args(argv)
    for s in TEXT + (IMAGES if a.images else ()):
        print(f'== {s}', flush=True)
        subprocess.run([sys.executable, str(HERE / s)], check=True)


if __name__ == '__main__':
    main(sys.argv[1:])
