# Contributing / 贡献指南

Please read the [Code of Conduct](CODE_OF_CONDUCT.md) first. · [中文](#中文) · [日本語](#日本語)

## Scope
Only add setups that one person, a desktop user or a small studio can build. Datacenter setups are out of scope. A setup must meet all of these conditions:
- The hardware costs $30,000 or less.
- It has at most 4 GPUs or 4 machines in total (for example, 4 GPUs in one PC, or 4 DGX Sparks).
- It runs on ordinary home or office power: about 2 kW in total, with no special wiring.
- It uses no rack, no SXM or HGX server board and no liquid cooling.
- It uses at most one desktop-class network switch.

A setup that fails one condition is out of scope, even when it costs less than $30,000. Record the price on the date you add the recipe. When a price goes up later, update the price note only. Do not remove the recipe.

`python3 scripts/scope_rules.py` checks the cost, the GPU or machine count and server-only hardware. Reviewers check power and the switch by reading the source.

## Add a recipe
1. Easiest: open a **[Recipe submission](../../issues/new?template=recipe.yml)** issue. Or fork → branch → append to `data/recipes.json` (fields: `schema/recipe.schema.json`, template: `submit.html`).
2. `node scripts/validate.mjs` must pass (CI runs it on every PR).
3. Regenerate READMEs: `python3 scripts/gen_readme.py`.
4. Link the original source; for your own runs include the command and output.
5. No estimates, no invented values: unknown → `null`. Link and summarize, don't copy posts.
6. Source level: official / measured / relayed / claimed (see [docs/sources.md](docs/sources.md)).

## 中文
### 收录范围
只收个人、桌面用户或小型工作室能搭起来的配置，数据中心配置不收录。配置必须同时满足以下条件：
- 硬件总价不超过 3 万美元。
- GPU 或整机合计不超过 4 个（例如一台 PC 装 4 张卡，或 4 台 DGX Spark）。
- 用普通家用或办公室电源即可运行：总功率约 2 kW 以内，不需要专门布线。
- 不用机架，不用 SXM 或 HGX 服务器主板，不用液冷。
- 最多用一台桌面级网络交换机。

不满足任一条件的配置不收录，即使总价低于 3 万美元。价格按收录当天记录。之后涨价时，只更新价格说明，不删除条目。

`python3 scripts/scope_rules.py` 会检查价格、GPU 或整机数量和服务器专用硬件。功率和交换机由审核人对照来源确认。

### 添加配方
1. 最简单：提一个「Recipe submission」issue；或 Fork 后在 `data/recipes.json` 追加记录。
2. `node scripts/validate.mjs` 必须通过（PR 会自动跑 CI）。
3. 运行 `python3 scripts/gen_readme.py` 重新生成三份 README。
4. 附原始来源链接；自测请附命令与输出。
5. 不估算、不编造，未知写 `null`；只留链接与摘要。
6. 来源等级：官方 / 实测 / 转述 / 宣称，详见 [docs/sources.md](docs/sources.md)。

Maintainers: Hugging Face candidate ingestion is described in [docs/sources.md](docs/sources.md).

## 日本語
### 収録範囲
個人、デスクトップ利用者、小規模スタジオが組める構成だけを追加してください。データセンター構成は対象外です。次の条件をすべて満たす必要があります：
- ハードウェアの合計価格が 3 万ドル以下。
- GPU またはマシンが合計 4 台以下（例：PC 1 台に GPU 4 枚、または DGX Spark 4 台）。
- 一般的な家庭用・オフィス用の電源で動く：合計約 2 kW 以内で、専用の配線工事が不要。
- ラック、SXM / HGX サーバーボード、液冷を使わない。
- ネットワークスイッチはデスクトップ型 1 台まで。

1 つでも満たさない構成は、3 万ドル未満でも対象外です。価格は収録日の価格を記録してください。後で値上がりしても、価格メモだけを更新し、レシピは削除しません。

`python3 scripts/scope_rules.py` は価格、GPU またはマシンの台数、サーバー専用ハードウェアを確認します。電力とスイッチは、レビュー担当者が出典を読んで確認します。

### レシピの追加
1. いちばん簡単なのは「Recipe submission」の issue を立てることです。または Fork して `data/recipes.json` に追記してください。
2. `node scripts/validate.mjs` が通ること（PR では CI が自動で実行します）。
3. `python3 scripts/gen_readme.py` で README を再生成してください。
4. 元の出典へのリンクを付けてください。自分で計測した場合はコマンドと出力も。
5. 推定や創作はしないでください。不明な値は `null` に。投稿の全文転載はせず、リンクと要約だけにします。
6. 出典レベル：公式 / 実測 / 伝聞 / 主張（[docs/sources.md](docs/sources.md) を参照）。
