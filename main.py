import os
import time
import torch
import whisper
import pandas as pd
from opencc import OpenCC

# ==========================
# 配置
# ==========================

AUDIO_DIR = "audio"
OUTPUT_FILE = "output/标注结果.xlsx"

cc = OpenCC('t2s')

# ==========================
# GPU检测
# ==========================

device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"运行设备: {device}")

# ==========================
# 加载模型
# ==========================

print("正在加载 large-v3 模型...")

model = whisper.load_model(
    "large-v3",
    device=device
)

results = []

start_time = time.time()

# ==========================
# 遍历音频
# ==========================

for file in os.listdir(AUDIO_DIR):

    if not file.lower().endswith(".wav"):
        continue

    path = os.path.join(AUDIO_DIR, file)

    print(f"识别中: {file}")

    try:

        result = model.transcribe(
            path,
            language="zh",
            fp16=torch.cuda.is_available()
        )

        text = result["text"].strip()

        text = cc.convert(text)

        results.append({
            "文件名": file,
            "打开音频": f'=HYPERLINK("{os.path.abspath(path)}","播放")',
            "AI识别结果": text,
            "人工修正结果": "",
            "备注": ""
        })

    except Exception as e:

        print(f"识别失败: {file}")
        print(e)

# ==========================
# 导出Excel
# ==========================

os.makedirs("output", exist_ok=True)

df = pd.DataFrame(results)

with pd.ExcelWriter(
        OUTPUT_FILE,
        engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        index=False
    )

total_time = round(time.time() - start_time, 2)

print("=" * 50)
print("识别完成")
print(f"文件数量: {len(results)}")
print(f"总耗时: {total_time} 秒")
print(f"结果保存至: {OUTPUT_FILE}")
print("=" * 50)