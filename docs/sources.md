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

## Original sources only / 只用原始来源 / 元の出典のみ
- **EN:** Use only an original source for a new recipe. The original source comes from the person or team that ran the test, and it gives the measured numbers. A relayed report (a repost, summary or article that quotes the result of a different person) is not a valid source. Find its original source and link that source. If you cannot find an original source with measured numbers, do not add the recipe.
- **中文：** 新收录的配方只用原始来源。原始来源由做测试的人或团队自己发布，并给出实测数字。转述（转发、汇总或引用别人结果的文章）不是有效来源。先找到它的原始来源，再链接原始来源。找不到带实测数字的原始来源时，不收录。
- **日本語：** 新しいレシピには元の出典だけを使います。元の出典は、テストを実行した人またはチームが自分で出したもので、計測した数値を示します。伝聞（他の人の結果を引用した再投稿、まとめ、記事）は有効な出典ではありません。その元の出典を探し、元の出典にリンクしてください。計測した数値のある元の出典が見つからないときは、収録しません。

The 🔁 Relayed level stays in the schema for recipes that were added before this rule.

## Hugging Face ingestion (maintainers)
`python3 scripts/ingest_hf.py --limit 40` (optional `HF_TOKEN`) scans trending GGUF/MLX cards and writes candidates to `data/candidates/` (git-ignored). It never writes `data/recipes.json`. Candidates are reviewed with `python3 scripts/review_candidates.py list | show <id> | approve <id> | reject <id>`; only approved items enter the dataset. Batch approval: `python3 scripts/approve_review.py <review.json>`.

## Rules
No estimates, no invented values — unknown fields are `null`. No full-text copies of posts.
