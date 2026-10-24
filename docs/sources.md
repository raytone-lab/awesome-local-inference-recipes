# Data sources / 数据来源

Where recipes come from and how they are checked. Every recipe links to its original source; we store only a link, a short summary and the numbers.

| Source | Role | What it gives | Notes |
|---|---|---|---|
| X (Twitter) | Primary | Measured tok/s, hardware, community heat | Many reposts — we trace back to the original post |
| Hugging Face model cards | Primary | Benchmark tables from quant authors (prefill / decode t/s) | Hardware often missing; reviewed by hand |
| r/LocalLLaMA | Primary (manual) | Consumer-hardware reports | Manual review only |
| GitHub (engine repos, llama.cpp discussions) | Primary | Official bench threads, release notes | |
| llamabench.ai / LocalScore / llamaperf | Cross-check | Benchmarks with commands | Linked, not copied |
| Hacker News | Discovery | New engines and projects | |
| arXiv | Discovery (methods) | Speculative decoding, quantization, KV cache | Datacenter numbers are not added as recipes |

## Source levels
- 🏛️ **Official** (官方) — published by the model/engine/hardware vendor.
- ✅ **Measured** (实测) — the poster ran it themselves and shows a screenshot or log of the run.
- 🔁 **Relayed** (转述) — second-hand report of someone else's result.
- 📣 **Claimed** (宣称) — marketing, a prediction, or an unverified claim with no screenshot/log or no way to reproduce it (e.g. an unpublished private build).

## Original sources only
Use only an original source for a new recipe. The original source comes from the person or team that ran the test, and it gives the measured numbers. A relayed report (a repost, summary or article that quotes the result of a different person) is not a valid source. Find the original source of the relayed report and link that source. If you cannot find an original source with measured numbers, do not add the recipe.

The Relayed level is kept only for recipes added before this rule.

## Hugging Face ingestion (maintainers)
`python3 scripts/ingest_hf.py --limit 40` (optional `HF_TOKEN`) scans trending GGUF/MLX cards and writes candidates to `data/candidates/` (git-ignored). It never writes `data/recipes.json`. Candidates are reviewed with `python3 scripts/review_candidates.py list | show <id> | approve <id> | reject <id>`; only approved items enter the dataset. Batch approval: `python3 scripts/approve_review.py <review.json>`.

## Rules
No estimates, no invented values — unknown fields are `null`. No full-text copies of posts.
