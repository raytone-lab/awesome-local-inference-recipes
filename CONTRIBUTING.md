# Contributing / 贡献指南

Please read the [Code of Conduct](CODE_OF_CONDUCT.md) first. · [中文](#中文) · [日本語](#日本語)

## Scope

This list is for setups that one person, a home or office desktop user, or a small studio can build. Datacenter setups are out of scope. Used datacenter cards in a desktop PC are in scope. A setup is in scope only when it meets all of these conditions:

- The hardware costs $30,000 or less.
- It has at most 4 GPUs or 4 machines. Count each GPU, and each machine without a separate GPU. For example: 4 GPUs in one PC count as 4, 4 DGX Sparks count as 4, and 4 DGX Sparks plus 1 PC with an RTX 5090 count as 5.
- It runs on ordinary home or office power: about 2 kW in total, from one or two ordinary outlets, with no special wiring. One US 120 V / 15 A circuit gives about 1.44 kW continuous, and one Japanese outlet gives about 1.5 kW.
- It uses no rack, no SXM or HGX server board, no custom liquid-cooling loop and no server liquid cooling. A DIY SXM2-to-PCIe adapter build that fits in a desktop is in scope. A consumer GPU with a factory all-in-one (AIO) liquid cooler is in scope.
- It uses at most one desktop-class network switch.

A setup that fails one condition is out of scope, even when it costs less than $30,000. We record the price on the date that we add the recipe. When the price goes up later, we update only the price note (`hardware_cost_text`). We do not remove the recipe.

`python3 scripts/scope_rules.py` lists the recipes that fail the cost, count or server-hardware check. Add `⚠️超$30k` to `hardware_cost_text` when the price on the date of inclusion is over $30,000. This includes a lower bound computed from prices published on that date. Do not add the mark for a later price rise. Reviewers check power and the network switch by reading the source.

## Add a recipe
1. Easiest: open a **[Recipe submission](../../issues/new?template=recipe.yml)** issue. Or fork → branch → append to `data/recipes.json` (fields: `schema/recipe.schema.json`, template: `submit.html`).
2. `node scripts/validate.mjs` must pass (CI runs it on every PR).
3. Regenerate READMEs: `python3 scripts/gen_readme.py`.
4. Link the original source; for your own runs include the command and output.
5. No estimates, no invented values: unknown → `null`. Link and summarize, don't copy posts.
6. Source level: official / measured / relayed / claimed (see [docs/sources.md](docs/sources.md)).

## 中文
### 收录范围

本清单只收个人、家用或办公桌面用户、小型工作室能搭起来的配置。数据中心配置不收录。装在桌面 PC 里的二手数据中心卡可以收录。配置必须同时满足以下条件：

- 硬件总价不超过 3 万美元。
- GPU 或整机合计不超过 4 个。每张 GPU 算 1 个；没有独立 GPU 的整机每台算 1 个。例如：一台 PC 装 4 张卡算 4 个，4 台 DGX Spark 算 4 个，4 台 DGX Spark 加一台装 RTX 5090 的 PC 算 5 个。
- 用普通家用或办公室电源即可运行：总功率约 2 kW 以内，最多分接两个普通插座，不需要专门布线。美国一路 120 V / 15 A 电路持续供电约 1.44 kW，日本一个插座约 1.5 kW。
- 不用机架，不用 SXM 或 HGX 服务器主板，不用分体式水冷或服务器液冷。装得进桌面机箱的 DIY SXM2 转 PCIe 转接方案可以收录。出厂自带一体式水冷（AIO）的消费级显卡可以收录。
- 最多用一台桌面级网络交换机。

不满足任一条件的配置不收录，即使总价低于 3 万美元。价格按收录当天记录。之后涨价时，只更新价格说明（`hardware_cost_text`），不删除条目。

`python3 scripts/scope_rules.py` 会列出未通过价格、数量或服务器硬件检查的条目。收录当天的价格超过 3 万美元时，在 `hardware_cost_text` 里加 `⚠️超$30k`。用当天公开价格算出的下限超过 3 万美元时也加。之后涨价不加这个标记。功率和网络交换机由审核人对照来源确认。

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

このリストは、個人、家庭やオフィスのデスクトップ利用者、小規模スタジオが組める構成だけを収録します。データセンター構成は対象外です。デスクトップ PC に載せた中古データセンター GPU は対象です。次の条件をすべて満たす構成だけを収録します：

- ハードウェアの合計価格が 3 万ドル以下。
- GPU 4 枚またはマシン 4 台まで。GPU は 1 枚ずつ、独立 GPU のないマシンは 1 台ずつ数えます。例：PC 1 台に GPU 4 枚は 4、DGX Spark 4 台は 4、DGX Spark 4 台と RTX 5090 搭載 PC 1 台は 5。
- 一般的な家庭用・オフィス用の電源で動く：合計約 2 kW 以内で、ふつうのコンセント 2 口までに分けてよく、専用の配線工事は不要。米国の 120 V / 15 A 回路 1 本は連続で約 1.44 kW、日本のコンセント 1 口は約 1.5 kW。
- ラック、SXM / HGX サーバーボード、カスタムループ水冷、サーバー用液冷を使わない。デスクトップに収まる DIY の SXM2→PCIe 変換構成は対象。メーカー出荷時から簡易水冷（AIO）付きのコンシューマー GPU も対象。
- ネットワークスイッチはデスクトップ型 1 台まで。

1 つでも満たさない構成は、3 万ドル未満でも対象外です。価格は収録日の価格を記録します。後で値上がりしても、価格メモ（`hardware_cost_text`）だけを更新し、レシピは削除しません。

`python3 scripts/scope_rules.py` は、価格・台数・サーバー用ハードウェアのチェックに通らないレシピを一覧表示します。収録日の価格が 3 万ドルを超えるときは、`hardware_cost_text` に `⚠️超$30k` を付けます。収録日の公開価格から計算した下限が 3 万ドルを超えるときも付けます。後の値上がりでは付けません。電力とネットワークスイッチは、レビュー担当者が出典を読んで確認します。

### レシピの追加
1. いちばん簡単なのは「Recipe submission」の issue を立てることです。または Fork して `data/recipes.json` に追記してください。
2. `node scripts/validate.mjs` が通ること（PR では CI が自動で実行します）。
3. `python3 scripts/gen_readme.py` で README を再生成してください。
4. 元の出典へのリンクを付けてください。自分で計測した場合はコマンドと出力も。
5. 推定や創作はしないでください。不明な値は `null` に。投稿の全文転載はせず、リンクと要約だけにします。
6. 出典レベル：公式 / 実測 / 伝聞 / 主張（[docs/sources.md](docs/sources.md) を参照）。
