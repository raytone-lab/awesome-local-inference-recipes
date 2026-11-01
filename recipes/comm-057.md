# DeepSeek-V4.1-Flash · Strata (Strata-DS fork) · RTX 5090 Laptop 24GB + Ryzen 9 9955HX3D + 64GB RAM + 2TB NVMe

**English** | [简体中文](comm-057.zh-CN.md) | [日本語](comm-057.ja.md) · [← All recipes](../README.md)

> Source level: **✅ Measured** · Date: 2026-10-16 · Numbers come from the source. This repo did not measure them again.

## Hardware

- RTX 5090 Laptop 24GB + Ryzen 9 9955HX3D + 64GB RAM + 2TB NVMe (NVIDIA consumer)
- Reference cost: Not published. See the source.

## Model

- DeepSeek-V4.1-Flash · `vcruz305 SAGE EXL3 1.59bpw + Engram read in place from the SSD (route/SSD tail skips)`
- Download: [huggingface.co/vcruz305/DSV4.1-Flash-1017-SAGE-EXL3-1.62bpw](https://huggingface.co/vcruz305/DSV4.1-Flash-1017-SAGE-EXL3-1.62bpw)

## Engine

- Strata (Strata-DS fork) — install: https://github.com/Jackwwg83/Strata-DS
- Note: Strata-DS (Strata fork with its own DeepSeek engine ds41_serve, C++/CUDA; hot experts in VRAM, the next in a 46 GiB locked RAM tier computed in place by the CPU, the rest read from the SSD on demand). setup.sh warns that a PC with less than 120 GiB of RAM is not tested; --yes in the command accepts that

## Launch command

```bash
sudo systemctl enable --now nvidia-powerd && git clone https://github.com/Jackwwg83/Strata-DS.git && cd Strata-DS && ./setup.sh --setup --yes --family deepseek --context 32768 --no-start && ./run-deepseek-sage-1.59bpw.sh
```

## Key parameters

- Context: 32,768 (--context 32768; 256K prompt also measured)
- Concurrency: Single stream
- Tags: `MoE`, `long-context`, `offload`

## Expected speed

- Short prompts from a cold start 30.0–32.0 (median of 5; code prompt 31.2); through the API on a running server 33.2–39.3; 30 minutes non-stop 37.6; with 4K/32K/128K/256K prompts decode 26.1/25.6/25.2/24.4 and prefill 244/844/904/752 tok/s; skips on: HumanEval+ 90.2% (off 91.5%), GSM8K 98.0% (off 97.5%) (✅ Measured)

## Caveats

- Speed changes with drivers, engine version, context length, and prompt length.

## Source & attribution

- [https://github.com/Jackwwg83/Strata-DS/blob/main/docs/DEEPSEEK_LAPTOP.md](https://github.com/Jackwwg83/Strata-DS/blob/main/docs/DEEPSEEK_LAPTOP.md)
- Credit to the original author. This page only summarizes and links. Data under CC BY 4.0.
