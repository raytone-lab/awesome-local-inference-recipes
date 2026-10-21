# DeepSeek-V4.1-Flash-1017 · Strata (Strata-DS fork) · 1× DGX Spark (GB10, 128GB unified memory, 4TB NVMe)

**English** | [简体中文](comm-056.zh-CN.md) | [日本語](comm-056.ja.md) · [← All recipes](../README.md)

> Source level: **✅ Measured** · Date: 2026-10-18 · Numbers come from the source. This repo did not measure them again.

## Hardware

- 1× DGX Spark (GB10, 128GB unified memory, 4TB NVMe) (DGX Spark)
- Reference cost: ≈ $6,950

## Model

- DeepSeek-V4.1-Flash-1017 · `LibertAIDAI EXL3 2.9bpw (experts; dense 5 / head 6) + the official 1017 checkpoint's other tensors and Engram (single machine, DSpark drafting every step, SSD tail skip)`
- Download: [huggingface.co/LibertAIDAI/DeepSeek-V4.1-Flash-1017-EXL3-2.9bpw](https://huggingface.co/LibertAIDAI/DeepSeek-V4.1-Flash-1017-EXL3-2.9bpw) · [huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

## Engine

- Strata (Strata-DS fork) — install: https://github.com/Jackwwg83/Strata-DS
- Note: Strata-DS (Strata fork with its own DeepSeek engine ds41_serve, C++/CUDA; hot experts in a unified-memory RAM tier computed in place by the GPU, cold experts read from the SSD on demand; sudoingX's exl3_smoe and exl3_mrow EXL3 kernels)

## Launch command

```bash
git clone https://github.com/Jackwwg83/Strata-DS.git && cd Strata-DS && ./setup.sh --setup --yes --family deepseek --no-start && ./run-deepseek-1017-exl3-2.9bpw.sh
```

## Key parameters

- Context: 262,144 (setup default 256K)
- Concurrency: Single stream
- Tags: `2bit`, `MoE`, `long-context`, `speculative`, `offload`

## Expected speed

- Real coding-agent session, 48 turns (context 10K–91K), 70,211 tokens at 30.8 tok/s average (per turn 23.6–36.4, median 28.6); single runs: decode at 8K/32K/64K/128K/250K context 24.2/27.4/27.4/27.3/22.9; time to first token for an agent turn adding ≤50 tokens median 0.57 s, a new conversation with the same 10K system prompt 0.25 s; cold prefill about 500 tok/s (250K in 8.3 min); vs official MXFP4 KL 0.074 / top-1 88.6% (✅ Measured)

## Caveats

- Speed changes with drivers, engine version, context length, and prompt length.

## Source & attribution

- [https://github.com/Jackwwg83/Strata-DS/blob/main/docs/DEEPSEEK_SPARK.md](https://github.com/Jackwwg83/Strata-DS/blob/main/docs/DEEPSEEK_SPARK.md)
- Credit to the original author. This page only summarizes and links. Data under CC BY 4.0.
