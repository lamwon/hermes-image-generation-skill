---
name: custom-image-generation-workflow
description: 定制版图像生成工作流 — DeepSeek V4 Flash 做创意策划 + SiliconFlow Flux 免费出图。专为你的 Hermes + DeepSeek 环境优化，单文件脚本，一键运行。
tags: [image-generation, deepseek, flux, siliconflow, custom, workflow, windows]
---

# Custom Image Generation Workflow

你的专属图像生成方案。利用已有的 DeepSeek API，搭配硅基流动免费 Flux 出图。

## 前置条件

- DeepSeek API Key（已有，在 `~/.hermes/.env` 里）
- SiliconFlow 免费账号：[https://siliconflow.cn](https://siliconflow.cn)（注册即送免费额度）
- 不需要其他 API

## 架构

```
[需求] --> DeepSeek V4 Flash (提示词工程师) --> SiliconFlow Flux (出图)
                                                      |
                                                 output.png
```

## 快速使用

```bash
# 1. 配置 SiliconFlow Key
python image_workflow.py --setup

# 2. 只生成提示词
python image_workflow.py "赛博朋克猫，霓虹灯，雨夜"

# 3. 生成提示词 + 出图
python image_workflow.py "橘猫在草地上晒太阳" --generate

# 4. 批量生成 3 张
python image_workflow.py "水墨山水" -g --batch 3

# 5. 指定尺寸和输出
python image_workflow.py "浮空岛" -g -o island.png --size 16:9
```

## 完整脚本

独立文件 `image_workflow.py` 位于仓库根目录，约 180 行。

**与原版相比的改进：**

| 项目 | 原版 | 定制版 |
|------|------|--------|
| 模型数量 | DeepSeek + Qwen + Flux 三个 | DeepSeek + Flux 两个（精简） |
| 依赖 | 需要三个 Key | 仅需 DeepSeek(已有) + 硅基流动 |
| 重试机制 | 无 | 含指数退避重试，应对限流/断网 |
| 参数支持 | 仅基本参数 | --output / --batch / --size 等 |
| 配置存储 | 本地 JSON | `~/.hermes/` 目录下统一管理 |
| 编码处理 | 有 GBK 兼容问题 | 显式 utf-8 编码 |
| 报错提示 | 较简略 | 完整的错误提示 |

## Pitfalls

1. **SiliconFlow 免费额度有限制** — 每月有配额，用完了会返回 402/429 错误
2. **Flux.1-schnell 出图约 5-10 秒** — 比标准 Flux 快很多，但质量略低
3. **DeepSeek API 超时** — 如果 prompt 太长，设大 `timeout` 参数
4. **图片保存路径** — 默认当前目录的 `output.png`，可用 `-o` 指定

## 验证

```bash
python image_workflow.py "a cute orange cat on grass, sunlight, warm colors" --generate
# 应该输出 === FINAL PROMPT === 然后保存 output.png
```
