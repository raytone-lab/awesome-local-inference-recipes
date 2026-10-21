# DeepSeek-V4.1-Flash · Strata (Strata-DS fork) · RTX 5090 Laptop 24GB + Ryzen 9 9955HX3D + 64GB DDR5 + 2TB NVMe

[English](comm-057.md) | [简体中文](comm-057.zh-CN.md) | **日本語** · [← 一覧に戻る](../README.ja.md)

> 出典レベル: **✅ 実測** · 日付: 2026-10-16 · 数値は出典からの引用です。このリポジトリでは再計測していません。

## ハードウェア

- RTX 5090 Laptop 24GB + Ryzen 9 9955HX3D + 64GB DDR5 + 2TB NVMe (NVIDIA コンシューマー)
- 参考価格: 未公開。出典を参照

## モデル

- DeepSeek-V4.1-Flash · `vcruz305 SAGE EXL3 1.59bpw (mixed K1–K6 experts) + Engram read in place from the SSD (route/SSD tail skips)`
- ダウンロード: [huggingface.co/vcruz305/DSV4.1-Flash-SAGE-EXL3-1.59bpw](https://huggingface.co/vcruz305/DSV4.1-Flash-SAGE-EXL3-1.59bpw)

## エンジン

- Strata (Strata-DS fork) — インストール： https://github.com/Jackwwg83/Strata-DS

## 起動コマンド

```bash
git clone https://github.com/Jackwwg83/Strata-DS.git && cd Strata-DS && ./setup.sh --setup --yes --family deepseek --context 32768 --no-start && ./run-deepseek-sage-1.59bpw.sh
```

## 主なパラメータ

- コンテキスト: 262,144 (setup default 32,768)
- 同時実行: Single stream
- タグ: `MoE`, `long-context`, `offload`

## 想定速度

- Short prompts from a cold start 30.0–32.0 (median of 5); through the API on a running server 33.2–39.3; 30 minutes non-stop 37.6; with 4K/32K/128K/256K prompts decode 26.1/25.6/25.2/24.4 and prefill 244/844/904/752 tok/s; skips on: HumanEval+ 90.2% (off 91.5%), GSM8K 98.0% (✅ 実測)

## 注意点

- 速度はドライバー、エンジンのバージョン、コンテキスト長、プロンプト長によって変わります。

## 出典とクレジット

- [https://github.com/Jackwwg83/Strata-DS/blob/main/docs/DEEPSEEK_LAPTOP.md](https://github.com/Jackwwg83/Strata-DS/blob/main/docs/DEEPSEEK_LAPTOP.md)
- 権利は元の投稿者にあります。このページは要約とリンクのみです。データは CC BY 4.0。
