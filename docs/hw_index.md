# data/hw_index.json

A compact, machine-readable index of `data/recipes.json` for AI agents. `scripts/gen_hw_index.py` writes it, and `python3 scripts/gen_all.py` runs that script. Do not edit the file by hand. CI fails when the file is not up to date.

The skill `.agents/skills/local-inference-recipe-finder` reads this file.

## Top level

| Field | Meaning |
|---|---|
| `schema_version` | `1`. A change that removes or renames a field increases this number. |
| `chip_patterns` | The chip regexes that the generator uses. The matcher uses the same list for the detected device names. `generic: true` means a family pattern (for example any GeForce), not one model. |
| `data_asof` | The data date (`DATA_ASOF` in `scripts/dataset_constants.py`). |
| `count` | The number of rows. |
| `recipes` | One row per recipe, sorted by `id`. |

## Row fields

| Field | Meaning |
|---|---|
| `id` | Recipe id in `data/recipes.json`. |
| `category` | `text`, `image`, or `video-audio`. |
| `model`, `model_family` | Model name and family. |
| `total_params_b`, `active_params_b` | Parameters in billions, from `data/model-params.json` or from the model name (for example `35B-A3B`). Else `null`. |
| `quant` | Quantization and settings (English). |
| `engine`, `engine_fork` | Engine name. `engine_fork` names the fork owner when the recipe uses a fork. |
| `engine_repo` | Link object (see below) or `null`. |
| `engine_repo_from` | `repos.json` (the engine table) or `source_url` (the recipe source is the engine's own repo). |
| `weights_url` | Link object or `null`. |
| `weights_url_from` | `recipe` (a hub link in the recipe) or `model-params.json` (the base model card; the quantized file can be in a different repo). |
| `launch_cmd` | The launch command from the recipe, or `null`. |
| `launch_cmd_warning` | A list of reasons when the recipe command has an unsafe pattern. Then `launch_cmd` is `null`. |
| `chip` | Parsed chip, for example `RTX 4090`, `M5 Max`, `DGX Spark`, `CPU`. |
| `kind` | `gpu`, `unified`, `cpu`, `phone`, or `console`. |
| `gpu_count` | Number of GPUs or machines. `0` for CPU only. |
| `laptop` | `true` for a laptop GPU. |
| `vram_gb` | Total VRAM of the discrete GPUs, or `null`. |
| `unified_mem_gb` | Total unified memory, or `null`. |
| `sys_ram_gb` | System RAM that the recipe names, or `null`. |
| `hardware` | Hardware text from the recipe (English). |
| `os_hints` | Operating systems that the recipe shows or needs: `linux`, `windows`, `macos`, `ios`. |
| `mac_only_engine` | `true` when the engine runs only on Apple silicon (for example MLX). |
| `tok_s`, `single_stream` | Speed in tokens per second, and `true` when it is one stream (not aggregate). |
| `context` | Context length, if known. |
| `source_level` | `实测` (measured), `官方` (official), `宣称` (claimed), `转述` (relayed). |
| `source_url` | Link object for the original source. |
| `date` | Recipe date. |
| `tags`, `superseded_by` | Tags; the id of a newer row, if any. |
| `recipe_page` | Site link: `explore.html?id=<id>`. |
| `recipe_md` | GitHub link to `recipes/<id>.md`, or `null`. |

A **link object** is `{"url": "https://...", "trust": "allowlisted" | "unverified"}`.

## Security

- `trust` is `allowlisted` only when the host is in `data/trusted_domains.json` and the URL passes the hygiene checks. Agents use only allowlisted links for downloads and installs. An unverified link is a source to read.
- `scripts/check_urls.py` (CI) checks every URL in the data. It fails on: a scheme that is not https; an IP-literal host; a punycode (`xn--`) host; non-ASCII characters; a lookalike of a known brand (for example `githubb`); a URL shortener; userinfo (`user@host`); a port that is not 443; a GitHub or Hugging Face path that is not `owner/repo`.
- The owner of each `weights_url` must be a known hub owner: the owner of a model card in `data/model-params.json`, the owner of a recipe source on the hub, or an entry in `verified_hub_owners` in `data/trusted_domains.json`.
- A launch command is hidden when it contains a URL that is not clean or not on an allowlisted host, when it pipes into a shell, uses `bash <(...)`, `sudo`, `rm -rf`, `pip install` from a URL, `iex` / `Invoke-Expression`, or pipes into an interpreter. Known rows are listed in `KNOWN_UNSAFE_CMDS` in `scripts/check_urls.py`. A new row with such a command fails CI.
- The generator prints hardware text that it cannot parse. The tests fail when a row has no `chip`.
