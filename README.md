SpeechLabelTool

基于 OpenAI Whisper Large-V3 的中文语音自动标注工具，支持批量语音识别、繁简体转换、Excel 标注文件导出以及 NVIDIA CUDA GPU 加速。

项目简介

SpeechLabelTool 是一个面向语音数据标注场景开发的自动化工具。

工具能够批量读取 WAV 音频文件，调用 Whisper Large-V3 模型完成中文语音识别，并自动生成符合人工标注流程的 Excel 标注表，大幅提高语音数据预标注效率。

功能特点

- 批量读取 WAV 音频文件
- 基于 Whisper Large-V3 中文语音识别
- 自动检测 CUDA GPU
- 支持 RTX4060 等 NVIDIA 显卡加速
- 繁体中文自动转换为简体中文
- 自动生成 Excel 标注文件
- 音频文件超链接回放
- 异常处理与运行统计

技术栈

- Python 3.11
- OpenAI Whisper
- PyTorch CUDA
- Pandas
- OpenCC
- OpenPyXL

项目结构

SpeechLabelTool
│
├── audio/
│   ├── test1.wav
│   ├── test2.wav
│   └── ...
│
├── output/
│   └── 标注结果.xlsx
│
├── main.py
├── test.py
└── 

环境配置

1. 创建虚拟环境

python -m venv .venv

2. 激活环境

Windows：

.venv\Scripts\activate

3. 安装依赖

pip install torch torchvision torchaudio
pip install openai-whisper
pip install pandas
pip install opencc-python-reimplemented
pip install openpyxl

或者：

pip install -r requirements.txt

使用方法

1. 准备音频文件

将待识别音频放入：

audio/

例如：

audio/
├── test1.wav
├── test2.wav
├── test3.wav

2. 运行程序

python main.py

3. 查看结果

程序执行完成后会自动生成：

output/标注结果.xlsx

Excel内容示例：

文件名| 打开音频| AI识别结果| 人工修正结果| 备注
test1.wav| 播放|登录键| | 正确
test2.wav| 播放|砍我有点痛| | 正确
test3.wav| 播放|梁志超| | 正确
test4.wav| 播放|职员底卷还有没有|十元抵卷还有没有| 错误
GPU加速

程序启动时自动检测 CUDA：

device = "cuda" if torch.cuda.is_available() else "cpu"

运行示例：

运行设备: cuda
正在加载 large-v3 模型...
识别中: test1.wav
识别中: test2.wav

测试环境：

- Lenovo 拯救者 R9000P 2023
- NVIDIA GeForce RTX 4060 Laptop GPU
- CUDA 12.7
- Python 3.11.5

核心流程

读取音频
    ↓
Whisper Large-V3识别
    ↓
繁体转简体
    ↓
结果整理
    ↓
导出Excel
    ↓
人工复核

应用场景

- ASR语音数据标注
- 语音识别训练数据预处理
- 数据集构建
- 智能客服语音整理
- 会议录音整理
- 课程录音转写

项目亮点

- 基于 OpenAI Whisper Large-V3 高精度识别模型
- 支持 GPU 加速推理
- 自动生成标准化标注文件
- 提升人工标注效率
- 易于扩展至大规模语音数据处理任务

作者

江浩

2026
