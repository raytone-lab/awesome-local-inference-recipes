#!/usr/bin/env python3
"""Run every generator in the order that CI checks them.
--images also renders the README charts (gen_hero.py) and the site screenshots (gen_screenshot.py). CI does not check PNG bytes.
Run: python3 scripts/gen_all.py [--images]"""
import subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
TEXT = ('gen_watchlist.py', 'gen_readme.py', 'gen_recipe_pages.py', 'gen_site.py')
IMAGES = ('gen_hero.py', 'gen_screenshot.py')


def main(argv):
    steps = TEXT + (IMAGES if '--images' in argv else ())
    for s in steps:
        subprocess.run([sys.executable, str(HERE / s)], check=True)


if __name__ == '__main__':
    main(sys.argv[1:])
