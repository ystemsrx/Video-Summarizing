[English](README.md)
# 视频总结

## 概述
这个Python脚本自动化了总结视频文件内容的过程。它从视频中提取音频，使用OpenAI的Whisper模型将其转录为SRT文件，然后使用OpenAI的GPT-4 Turbo生成转录文本的摘要。此脚本特别适用于创建冗长视频内容的简明总结。

## 特性
- 从视频文件中提取音频。
- 使用OpenAI的Whisper模型将音频转录为文本。
- 使用OpenAI的GPT模型生成转录文本的摘要。
- 将转录和摘要保存到文件中。

## 要求
- Python 3.8或更高版本。
- `moviepy`库用于处理视频文件。
- `openai` Python客户端，用于与OpenAI的API进行交互。

## 使用方法
1. 安装必要的Python包：
   ```bash
   pip install moviepy openai
   ```
2. 在环境变量中设置您的OpenAI API密钥。
3. 运行脚本并按照屏幕上的提示输入视频文件名称和总结生成的偏好设置。

## 输入
- `video_filename`：需要提取音频的视频文件名称。
- `language`：摘要输出的语言。
- `careful_words`：在转录中需要小心处理的特定词汇。

## 输出
- 音频文件（`MP3`格式）。
- 转录文件（`SRT`格式）。
- 摘要文件（`TXT`格式，如截图所示）。

## 样本摘要截图
所提供的截图是脚本生成的样本输出，展示了代码对一个视频片段的总结效果。

这是从OpenAI开发者日视频的一个简短片段中总结出来的，完整视频可在此处观看：https://www.youtube.com/watch?v=U9mJuUkhUzk。

![image](https://github.com/ystemsrx/Video-Summarizing/assets/140463276/f2e064dc-3fc5-49d5-914b-b3b5e96d3282)

该脚本通过程序化处理音频提取、转录和总结的复杂任务，简化了生成视频摘要的过程。
