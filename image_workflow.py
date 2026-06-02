# -*- coding: utf-8 -*-
# image_workflow.py — DeepSeek + Flux 一键出图
# Usage:
#   python image_workflow.py --setup                  # 配置 SiliconFlow Key
#   python image_workflow.py "赛博朋克猫"               # 只生成提示词
#   python image_workflow.py "橘猫草地" --generate      # 生成提示词+出图
#   python image_workflow.py "山水画" -g -o art.png    # 指定输出路径
#   python image_workflow.py "猫" -g --batch 3         # 批量生成多张

import urllib.request, json, ssl, base64, os, sys, time
from urllib.error import HTTPError, URLError

ctx = ssl._create_unverified_context()

# === 配置 ===
DEEPSEEK_KEY = os.environ.get("OPENAI_API_KEY", "")
DEEPSEEK_URL = "https://api.deepseek.com/v1"
DEEPSEEK_MODEL = "deepseek-v4-flash"
SILICONFLOW_URL = "https://api.siliconflow.cn/v1"
SILICONFLOW_MODEL = "black-forest-labs/FLUX.1-schnell"
CONFIG_FILE = os.path.expanduser("~/.hermes/.image_workflow.json")

# 可用尺寸
SUPPORTED_SIZES = ["1024x1024", "512x512", "768x768", "1024x768", "768x1024", "1280x720", "720x1280"]


def load_sf_key():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            return json.load(f).get("siliconflow_key", "")
    return ""


def save_sf_key(key):
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump({"siliconflow_key": key}, f)
    print(f"[OK] SiliconFlow key saved to {CONFIG_FILE}")


def api_call(url, data, headers, timeout=120, max_retries=3):
    """带重试机制的 API 调用"""
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, data=data, headers=headers, method="POST")
            resp = urllib.request.urlopen(req, context=ctx, timeout=timeout)
            return json.loads(resp.read().decode())
        except HTTPError as e:
            body = e.read().decode(errors="ignore")[:200]
            if e.code == 429 and attempt < max_retries - 1:
                wait = 2 ** (attempt + 1)
                print(f"[WARN] 遇到限流 ({e.code})，{wait}秒后重试...")
                time.sleep(wait)
                continue
            raise Exception(f"HTTP {e.code}: {body}")
        except URLError as e:
            if attempt < max_retries - 1:
                wait = 2 ** (attempt + 1)
                print(f"[WARN] 网络错误 ({e.reason})，{wait}秒后重试...")
                time.sleep(wait)
                continue
            raise Exception(f"网络错误: {e.reason}")
    raise Exception("重试次数已用完")


def call_deepseek(prompt, max_tokens=2000, temp=0.8):
    data = json.dumps({
        "model": DEEPSEEK_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens, "temperature": temp
    }).encode("utf-8")
    result = api_call(
        f"{DEEPSEEK_URL}/chat/completions", data,
        {"Authorization": f"Bearer {DEEPSEEK_KEY}",
         "Content-Type": "application/json; charset=utf-8"},
        timeout=120
    )
    return result["choices"][0]["message"]["content"]


def generate_flux(prompt, sf_key, output="output.png", size="1024x1024"):
    data = json.dumps({
        "model": SILICONFLOW_MODEL, "prompt": prompt,
        "n": 1, "size": size
    }).encode("utf-8")
    result = api_call(
        f"{SILICONFLOW_URL}/images/generations", data,
        {"Authorization": f"Bearer {sf_key}",
         "Content-Type": "application/json"},
        timeout=300
    )
    b64 = result["data"][0].get("b64_json")
    if b64:
        with open(output, "wb") as f:
            f.write(base64.b64decode(b64))
        return f"[OK] Saved: {output}"
    url = result["data"][0].get("url")
    if url:
        img_data = urllib.request.urlopen(url, context=ctx).read()
        with open(output, "wb") as f:
            f.write(img_data)
        return f"[OK] Saved: {output}"
    return f"[ERR] No image data: {result}"


def batch_generate(prompt, sf_key, count=3, size="1024x1024"):
    """批量生成多张图片"""
    results = []
    for i in range(count):
        output = f"output_{i+1}.png"
        print(f"  [{i+1}/{count}] 生成中...")
        result = generate_flux(prompt, sf_key, output, size)
        print(f"    {result}")
        results.append(result)
    return results


def main():
    if not DEEPSEEK_KEY:
        print("[ERR] DeepSeek API key not found. Set OPENAI_API_KEY in env or .env")
        return

    args = sys.argv[1:]

    # --help
    if "--help" in args or "-h" in args or not args:
        print("Usage:")
        print("  python image_workflow.py --setup                  配置 SiliconFlow Key")
        print("  python image_workflow.py <prompt>                 只生成提示词")
        print("  python image_workflow.py <prompt> --generate      生成提示词+出图")
        print("  python image_workflow.py <prompt> -g -o out.png   指定输出路径")
        print("  python image_workflow.py <prompt> -g --batch 3    批量生成3张")
        print("  python image_workflow.py <prompt> -g --size 16:9  横版 1280x720")
        print("  python image_workflow.py <prompt> -g --size 9:16  竖版 720x1280")
        return

    # --setup
    if args[0] == "--setup":
        key = input("SiliconFlow API Key: ").strip()
        if key:
            save_sf_key(key)
        else:
            print("[ERR] Key cannot be empty")
        return

    # 解析参数
    do_gen = "--generate" in args or "-g" in args

    # 输出路径
    output = "output.png"
    if "-o" in args:
        oi = args.index("-o")
        if oi + 1 < len(args):
            output = args[oi + 1]
    if "--output" in args:
        oi = args.index("--output")
        if oi + 1 < len(args):
            output = args[oi + 1]

    # 尺寸
    size = "1024x1024"
    if "--size" in args:
        si = args.index("--size")
        if si + 1 < len(args):
            size_str = args[si + 1]
            size_map = {
                "1:1": "1024x1024", "square": "1024x1024",
                "16:9": "1280x720", "landscape": "1280x720",
                "9:16": "720x1280", "portrait": "720x1280",
                "4:3": "1024x768",
                "3:4": "768x1024",
            }
            size = size_map.get(size_str, size_str)
            if size not in SUPPORTED_SIZES:
                print(f"[WARN] 未知尺寸 '{size_str}'，使用默认 1024x1024")
                print(f"       支持的尺寸: {', '.join(SUPPORTED_SIZES)}")
                size = "1024x1024"

    # 批量
    batch_count = 1
    if "--batch" in args:
        bi = args.index("--batch")
        if bi + 1 < len(args):
            try:
                batch_count = int(args[bi + 1])
            except ValueError:
                pass

    # 提取真正的 prompt
    skip_words = {"--generate", "-g", "--output", "-o", "--batch", "--size", "--help", "-h"}
    words = []
    i = 0
    while i < len(args):
        if args[i] in skip_words:
            i += 1
            if args[i-1] in ("-o", "--output", "--batch", "--size"):
                i += 1  # skip the value too
            continue
        words.append(args[i])
        i += 1
    req = " ".join(words)

    if not req:
        print("[ERR] No prompt provided")
        return

    # DeepSeek 生成提示词
    print(f"[DeepSeek] 正在构思...")
    prompt = call_deepseek(
        f"You are an expert AI image prompt engineer. User wants: {req}\n"
        f"Write a detailed English prompt for FLUX.1-schnell model. "
        f"Include: subject, environment, lighting, style, color palette, composition, mood. "
        f"Output ONLY the prompt, no explanation."
    )
    print(f"=== FINAL PROMPT ===\n{prompt}\n====================")

    # 出图
    if do_gen:
        sf_key = load_sf_key()
        if not sf_key:
            print("[ERR] SiliconFlow key not configured. Run: python image_workflow.py --setup")
            return
        print(f"[Flux] 正在生成 {'%d张' % batch_count if batch_count > 1 else '图片'}...")
        if batch_count > 1:
            batch_generate(prompt, sf_key, batch_count, size)
        else:
            result = generate_flux(prompt, sf_key, output, size)
            print(result)


if __name__ == "__main__":
    main()
