# Qwen3.8-Flash-Next · ExLlama · 1× DGX Spark

**English** | [简体中文](text-022.zh-CN.md) | [日本語](text-022.ja.md) · [← All recipes](../README.md)

> Source level: **✅ Measured** · Date: — · Numbers come from the source. This repo did not measure them again.

## Hardware

- 1× DGX Spark (DGX Spark)
- Reference cost: ≈ $6,950

## Model

- Qwen3.8-Flash-Next · `Cruz exllamav3 fork · EXL3 3.05bpw · draft depth 5 · 8-bit KV`
- Download: Not published. See the source.

## Engine

- ExLlama — install: https://github.com/turboderp-org/exllamav3

## Launch command

Command not published. See the source.

## Key parameters

- Context: 262K (243K needle test 15/15)
- Concurrency: native engine only 1 stream (separate vLLM concurrent lane also exists)
- Tags: `3bit`, `MoE`, `long-context`, `speculative`

## Expected speed

- code 102.6; prose 71.7; JSON 66.2 tok/s (✅ Measured)

## Caveats

- Speed changes with drivers, engine version, context length, and prompt length.

## Source & attribution

- [https://x.com/yume_arasaki/status/2101741448811229219](https://x.com/yume_arasaki/status/2101741448811229219)
- Credit to the original author. This page only summarizes and links. Data under CC BY 4.0.
