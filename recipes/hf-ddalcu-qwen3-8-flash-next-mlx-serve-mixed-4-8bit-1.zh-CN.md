# Qwen3.8-Flash-Next-MLX-Serve-mixed-4 · mlx-serve · Mac Studio/MBP M4 Max 128GB

[English](hf-ddalcu-qwen3-8-flash-next-mlx-serve-mixed-4-8bit-1.md) | **简体中文** | [日本語](hf-ddalcu-qwen3-8-flash-next-mlx-serve-mixed-4-8bit-1.ja.md) · [← 返回列表](../README.zh-CN.md)

> 来源等级: **📣 宣称** · 日期: 2026-08-27 · 数字来自来源。本仓库未复测。

## 硬件

- Mac Studio/MBP M4 Max 128GB (Mac)
- 参考价格: 未公开。见来源

## 模型

- Qwen3.8-Flash-Next-MLX-Serve-mixed-4 · `mixed 4/8-bit（约 75 GB 驻留）`
- 下载: [huggingface.co/ddalcu/Qwen3.8-Flash-Next-MLX-Serve-mixed-4-8bit](https://huggingface.co/ddalcu/Qwen3.8-Flash-Next-MLX-Serve-mixed-4-8bit)

## 引擎

- mlx-serve
- 备注: mlx-serve 26.8.11

## 启动命令

```bash
mlx-serve --model ddalcu/Qwen3.8-Flash-Next-MLX-Serve-mixed-4-8bit --serve
```

## 关键参数

- 上下文: 268,288
- 并发: 串行单请求
- 标签: `4bit`, `8bit`, `MoE`, `long-context`

## 预期速度

- 60.0 tok/s 生成；730.0 tok/s 读入 (📣 宣称)

## 注意事项

- 非一手实测（宣称或转述）。实际速度可能不同。
- HF 模型卡（作者自报）; 开 --mtp 78 tok/s（code +41%，prose 略慢）；数值为约值
- 速度随驱动、引擎版本、上下文长度和提示长度变化。

## 来源与致谢

- [https://huggingface.co/ddalcu/Qwen3.8-Flash-Next-MLX-Serve-mixed-4-8bit](https://huggingface.co/ddalcu/Qwen3.8-Flash-Next-MLX-Serve-mixed-4-8bit)
- 版权归原作者。本页仅摘要并链接。数据以 CC BY 4.0 发布。
