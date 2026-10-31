#!/usr/bin/env python3
"""Copy .agents/skills/<name>/ to .claude/skills/<name>/ (a generated mirror for Claude Code; no symlinks, so Windows clones work).
Edit only the .agents copy. gen_all.py runs this."""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, DST = ROOT / '.agents/skills', ROOT / '.claude/skills'


def files(base):
    return sorted(p.relative_to(base) for p in base.rglob('*') if p.is_file() and '__pycache__' not in p.parts)


def main():
    for skill in sorted(p for p in SRC.iterdir() if p.is_dir()):
        out = DST / skill.name
        if out.exists(): shutil.rmtree(out)
        for rel in files(skill):
            (out / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(skill / rel, out / rel)
        print(f'mirrored {skill.name}: {len(files(skill))} files')


if __name__ == '__main__': main()
