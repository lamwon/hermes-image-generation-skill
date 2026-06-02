# 分享文案 — 各平台可直接发布

---

##  知乎

### 标题：用 DeepSeek + 免费 Flux 实现 AI 图像自由，零成本零显卡

最近发现了一个超实用的组合：DeepSeek V4 Flash（负责策划提示词）+ SiliconFlow 的免费 Flux（负责出图），完全不需要显卡，一行命令出图。

这个工作流的思路是：你只需要用中文说"赛博朋克猫，霓虹灯，雨夜"，DeepSeek 自动把它扩展成高质量的英文 Flux 提示词，然后调用免费 API 出图。整个过程 10-30 秒完成。

最大的优势：
1. **零额外成本** — DeepSeek API 本来就在用，Flux 有免费额度
2. **国内直连** — 全部国内节点，不用代理
3. **单文件脚本** — 连 pip install 都不需要，一个 Python 脚本搞定
4. **Hermes Agent 集成** — 装成 skill 后随时调用

我已经把完整的脚本和工作流开源了，效果图在 README 里有，有兴趣的可以看看：
https://github.com/lamwon/hermes-image-generation-skill

---

##   V2EX

### 标题：分享一个 DeepSeek + Flux 免费 AI 出图方案，零成本零显卡

![](https://img.shields.io/badge/python-3.8+-blue) ![](https://img.shields.io/badge/license-MIT-green)

之前在 V 站看到不少讨论 AI 出图的帖子，要么需要 Midjourney 付费订阅，要么需要本地显卡跑 SD。今天分享一个完全不同的思路。

**核心思路：** DeepSeek V4 Flash（做 prompt engineering）+ SiliconFlow 免费 Flux（出图）

**为什么这个方案不错：**
- DeepSeek 的中文理解力强，你说"一只戴墨镜的橘猫躺在沙滩上"，它自动翻译扩展成高质量英文 prompt
- SiliconFlow 在国内有节点，速度很快，免费额度够用很久
- 整个过程不需要显卡，不需要翻墙

我已经把脚本开源到 GitHub，欢迎 Star ⭐：
https://github.com/lamwon/hermes-image-generation-skill

---

##  小红书

### 标题： 不用显卡也能出图！DeepSeek+免费Flux，真香

家人们谁懂啊！  终于找到一个不需要显卡的AI出图方案！

用 DeepSeek 做创意策划，SiliconFlow 的免费 Flux 出图，全程国内网络直连，一行命令搞定！

  **亮点：**
✅ 零成本 — DeepSeek本来就有，Flux有免费额度
✅ 零显卡 — 纯API调用，网页都能跑
✅ 中文友好 — "我想要一只赛博朋克风格的猫"，自动帮你写好英文提示词
✅ 10-30秒出图

  成品放在前面了，效果还不错吧！
完整教程和脚本在GitHub，链接放评论区

#AI绘画 #Flux #DeepSeek #免费AI工具 #效率工具

---

##   即刻

### 主题：发现一个 DeepSeek + 免费 Flux 的 AI 出图方案

之前一直用 Midjourney，但每个月付费有点心疼。今天折腾了一个方案：DeepSeek V4 Flash 负责写提示词 + SiliconFlow 的免费 Flux 出图。

测试了几张，效果出乎意料的好（看配图）。DeepSeek 的中文理解真的强，你说"水墨山水画，孤舟远山"，它自动优化成英文 prompt，Flux 出图质量也高。

最香的是全部免费，国内网络直连。脚本开源了：https://github.com/lamwon/hermes-image-generation-skill

---

## Twitter/X

🧵 Just set up a zero-cost AI image generation pipeline:
DeepSeek V4 Flash (prompt engineer) + SiliconFlow Flux (image gen)

No GPU needed. No Midjourney subscription. Works in China.
All open source: https://github.com/lamwon/hermes-image-generation-skill

1/ Tell DeepSeek your idea in Chinese
2/ It crafts the perfect FLUX prompt
3/ Flux generates the image in 10-30s
4/ Done. Free. 

---

## Reddit (r/StableDiffusion)

**Zero-cost AI image gen pipeline: DeepSeek V4 Flash + Free Flux API**

I put together a simple workflow that uses DeepSeek V4 Flash for prompt engineering + SiliconFlow's free Flux API for generation. No GPU required, no Midjourney subscription.

The best part: DeepSeek understands Chinese naturally, so you can just say "cyberpunk cat" in Chinese and it auto-expands to a detailed FLUX-optimized English prompt.

All scripts are single-file Python, no dependencies. Works with any OpenAI-compatible API backend.

GitHub: https://github.com/lamwon/hermes-image-generation-skill

Try it out! Feedback welcome ⭐
