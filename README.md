#  DeepSeek + Flux 一键图像生成工作流
### Custom Image Generation Workflow for Hermes Agent

<p align="center">
  <img src="examples/floating-island.jpg" width="45%" />
  <img src="examples/chinese-ink.jpg" width="45%" />
  <br/>
  <img src="examples/cyberpunk-cat.jpg" width="45%" />
  <img src="examples/geometric-abstract.jpg" width="45%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.8+-blue" alt="Python 3.8+" />
  <img src="https://img.shields.io/github/stars/lamwon/hermes-image-generation-skill?style=flat&color=yellow" alt="Stars" />
  <img src="https://img.shields.io/badge/Hermes%20Agent-ready-orange" alt="Hermes Agent Ready" />
  <img src="https://img.shields.io/badge/DeepSeek-V4%20Flash-brightgreen" alt="DeepSeek V4 Flash" />
  <img src="https://img.shields.io/badge/Flux-Schnell-ff69b4" alt="Flux Schnell" />
</p>

---

##  简介 | Introduction

> 用你已有的 **DeepSeek API** + 免费的 **SiliconFlow Flux**，实现 DeepSeek 做创意策划、Flux 出图的全自动工作流。
>
> 不需要 Midjourney 订阅，不需要 Stable Diffusion 显卡，一行命令出图。

### ✨ 核心亮点

| 特性 | 说明 |
|------|------|
|   **零额外成本** | 利用已有 DeepSeek API + 硅基流动免费 Flux 额度 |
|   **智能提示词** | DeepSeek V4 Flash 自动做 prompt engineering |
|   **一键出图** | 单脚本，`pip install` 都不用 |
|   **中国网络友好** | 全部 API 国内直连，无需代理 |
|   **Hermes 集成** | 安装即用，`/img` 命令随时出图 |

---

##  效果预览 | Examples

所有图片使用本工作流生成，**DeepSeek 策划提示词 + Flux 出图**，未经过任何后期处理。

| 风格 | Prompt (由 DeepSeek 生成) | 预览 |
|------|--------------------------|------|
|   赛博朋克 | "A cyberpunk cat with neon fur and glowing eyes in a rainy futuristic alley" | ![][cyberpunk] |
|   中国水墨 | "Chinese ink landscape with misty mountains and a lone boat on a river" | ![][ink] |
| ️ 奇幻浮岛 | "A floating island with waterfalls cascading into clouds, surrounded by ancient ruins" | ![][island] |
|   几何抽象 | "Geometric abstract with sharp triangles and circles in vibrant contrasting colors" | ![][abstract] |

[cyberpunk]: examples/cyberpunk-cat.jpg
[ink]: examples/chinese-ink.jpg
[island]: examples/floating-island.jpg
[abstract]: examples/geometric-abstract.jpg

---

##   快速开始 | Quick Start

### 前置条件

- DeepSeek API Key（已有）
- SiliconFlow 免费账号 → [注册](https://siliconflow.cn)（注册即送免费额度）
- Python 3.8+

### 1. 克隆仓库

```bash
git clone https://github.com/lamwon/hermes-image-generation-skill.git
cd hermes-image-generation-skill
```

### 2. 配置 API Key

```bash
# 方式一：环境变量
export SILICONFLOW_KEY=sk-你的硅基流动key

# 方式二：交互式配置（推荐）
python image_workflow.py --setup
```

> 你的 DeepSeek API Key 会自动从 `OPENAI_API_KEY` 环境变量读取，无需额外配置。

### 3. 开始生成

```bash
# 仅生成提示词（DeepSeek 策划）
python image_workflow.py "赛博朋克猫，霓虹灯，雨夜"

# 全流程：策划 + 出图
python image_workflow.py "橙猫在草地上晒太阳" --generate

# 指定输出路径
python image_workflow.py "水墨山水画" --generate --output my-art.png
```

---

##   在 Hermes Agent 中使用

### 方式一：安装为 Skill（推荐）

```bash
hermes skills install lamwon/hermes-image-generation-skill
```

安装后直接在对话中使用：

```
/img 赛博朋克猫，霓虹灯，雨夜
```

### 方式二：作为独立 Python 脚本

```bash
python image_workflow.py "水墨山水画，要有孤舟和远山" -g -o my-art.png
```

脚本支持多种参数：

| 参数 | 说明 |
|------|------|
| `<prompt>` | 中文描述需求 |
| `--generate` / `-g` | 生成图片（默认只出提示词） |
| `-o <file>` | 指定输出路径 |
| `--batch <n>` | 批量生成 n 张 |
| `--size <ratio>` | 尺寸比例，如 `16:9` `9:16` `1:1` |
| `--setup` | 配置 SiliconFlow Key |

---

##   与主流方案对比

| 方案 | 成本 | 质量 | 速度 | 国内可用 | 需要显卡 |
|------|------|------|------|---------|---------|
| **本方案** |   **免费/极低** | ⭐⭐⭐½ | ⚡ 10-30s | ✅ | ❌ |
| Midjourney |   $10-60/月 | ⭐⭐⭐⭐⭐ | ⚡ 30-60s | ❌（需代理） | ❌ |
| DALL-E 3 |   $0.04/张 | ⭐⭐⭐⭐ | ⚡ 5-15s | ❌（需代理） | ❌ |
| SD WebUI 本地 |   免费 | ⭐⭐⭐ |  慢 | ✅ | ✅ **需要** |
| ComfyUI 本地 |   免费 | ⭐⭐⭐⭐ |  慢 | ✅ | ✅ **需要** |

---

##   FAQ

**Q: SiliconFlow 免费额度有多少？**
A: 注册送 14 元体验金，Flux 模型约 0.14 元/张，约可生成 100 张。用完可继续充值，价格很低。

**Q: 必须用 SiliconFlow 吗？**
A: 不必须。脚本支持任何 OpenAI-compatible 的图像 API，修改 `SILICONFLOW_URL` 和 `SILICONFLOW_MODEL` 即可切换。

**Q: 提示词质量怎么样？**
A: DeepSeek V4 Flash 的中文理解力很强，你只需要说中文需求（如"一只戴墨镜的猫"），它会自动扩展为高质量的英文 Flux 提示词。

**Q: 在中国网络访问慢吗？**
A: 全部使用国内 API 节点（DeepSeek api.deepseek.com + SiliconFlow api.siliconflow.cn），直连流畅。

---

##   Share

如果你觉得这个项目有用，欢迎 ⭐ **Star** 支持！

[知乎](https://zhihu.com) | [V2EX](https://v2ex.com) | [小红书](https://xiaohongshu.com) | [即刻](https://okjike.com)

---

##   License

MIT
