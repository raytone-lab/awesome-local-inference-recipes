# DeepSeek-V4.1-Flash · Strata (Strata-DS fork) · RTX 5090 Laptop 24GB + Ryzen 9 9955HX3D + 64GB DDR5 + 2TB NVMe

[English](comm-057.md) | **简体中文** | [日本語](comm-057.ja.md) · [← 返回列表](../README.zh-CN.md)

> 来源等级: **✅ 实测** · 日期: 2026-10-16 · 数字来自来源。本仓库未复测。

## 硬件

- RTX 5090 Laptop 24GB + Ryzen 9 9955HX3D + 64GB DDR5 + 2TB NVMe (NVIDIA 消费级)
- 参考价格: 未公开。见来源

## 模型

- DeepSeek-V4.1-Flash · `vcruz305 SAGE EXL3 1.59bpw + Engram 原地读 SSD（route/SSD 尾部跳过）`
- 下载: [huggingface.co/vcruz305/DSV4.1-Flash-SAGE-EXL3-1.59bpw](https://huggingface.co/vcruz305/DSV4.1-Flash-SAGE-EXL3-1.59bpw)

## 引擎

- Strata (Strata-DS fork) — 安装见 https://github.com/Jackwwg83/Strata-DS

## 启动命令

```bash
sudo systemctl enable --now nvidia-powerd && git clone https://github.com/Jackwwg83/Strata-DS.git && cd Strata-DS && ./setup.sh --setup --yes --family deepseek --context 32768 --no-start && ./run-deepseek-sage-1.59bpw.sh
```

## 关键参数

- 上下文: 32,768（--context 32768；另测 256K 提示）
- 并发: 单路
- 标签: `long-context`, `offload`

## 预期速度

- 冷启动短提示 30.0–32.0（5 次中位；代码提示 31.2）；服务运行后 API 33.2–39.3；连续 30 分钟 37.6；4K/32K/128K/256K 提示解码 26.1/25.6/25.2/24.4，读入 244/844/904/752 tok/s；跳过开 HumanEval+ 90.2%（关 91.5%），GSM8K 98.0%（关 97.5%） (✅ 实测)

## 注意事项

- Strata-DS 笔记本配方页，作者实测（每条件 5 次中位；原始数据 ds41/bench/results/2026-10-16-laptop-5090；setup 下载 vcruz305/DSV4.1-Flash-SAGE-EXL3-1.59bpw 并打包）
- 速度随驱动、引擎版本、上下文长度和提示长度变化。

## 来源与致谢

- [https://github.com/Jackwwg83/Strata-DS/blob/main/docs/DEEPSEEK_LAPTOP.md](https://github.com/Jackwwg83/Strata-DS/blob/main/docs/DEEPSEEK_LAPTOP.md)
- 版权归原作者。本页仅摘要并链接。数据以 CC BY 4.0 发布。
