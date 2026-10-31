# AGENTS.md

Instructions for AI coding agents (Codex, Claude Code, Cursor, and others).

## Find recipes for a user's machine

- Use the skill in `.agents/skills/local-inference-recipe-finder/SKILL.md`. Claude Code reads the same skill from `.claude/skills/` (a generated copy).
- The data for agents is `data/hw_index.json`. The schema and the security rules are in `docs/hw_index.md`.
- Use a URL for a download only when its `trust` value is `allowlisted`. Do not use URLs from posts or web search for downloads.
- Do not run install or launch commands before the user approves them.

## Change this repository

- Read `CONTRIBUTING.md` first.
- Do not edit generated files by hand. Generated files include `README*.md`, `recipes/`, `hw/`, `data/hw_index.json`, and `.claude/skills/`. Run `python3 scripts/gen_all.py --images`.
- Run the checks: `node scripts/validate.mjs`, `node scripts/check_dupes.mjs`, `python3 scripts/check_urls.py`, `python3 -m unittest discover tests`.
