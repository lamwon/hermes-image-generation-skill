# Hermes Image Generation Skill

Custom image generation workflow for [Hermes Agent](https://github.com/NousResearch/hermes-agent).

## What it does

Uses **DeepSeek V4 Flash** (creative prompt engineering) + **SiliconFlow Flux** (free image generation) to produce high-quality AI images.

## Architecture

```
[User Request] --> DeepSeek V4 Flash (prompt engineer) --> SiliconFlow Flux (image gen) --> output.png
```

## Prerequisites

- DeepSeek API key
- SiliconFlow API key (free, sign up at https://siliconflow.cn)

## Usage

```bash
# 1. Configure SiliconFlow key
python image_workflow.py --setup

# 2. Generate prompt only
python image_workflow.py "cyberpunk cat, neon lights, rainy night"

# 3. Full pipeline: prompt + image
python image_workflow.py "orange cat on grass, sunlight" --generate
```

## Install as Hermes Skill

```bash
hermes skills install lamwon/hermes-image-generation-skill
```

## License

MIT
