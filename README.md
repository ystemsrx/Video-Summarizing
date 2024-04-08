# Video Summarizing Script

## Description
This Python script automates the process of summarizing the content of video files. It extracts audio from a video, transcribes it to an SRT file using the OpenAI's Whisper model, and then generates a summary of the transcript using OpenAI's GPT-4 Turbo. This script is particularly useful for creating concise summaries of lengthy video contents.

## Features
- Extracts audio from video files.
- Transcribes audio to text using the OpenAI's Whisper model.
- Generates summaries of the transcribed text using OpenAI's GPT model.
- Saves the transcripts and summaries to files.

## Requirements
- Python 3.8 or later.
- `moviepy` library for handling video files.
- `openai` Python client to interact with OpenAI's API.

## Usage
1. Install the necessary Python packages:
   ```bash
   pip install moviepy openai
   ```
2. Set your OpenAI API key in your environment variables.
3. Run the script and follow the on-screen prompts to input the video file name and preferences for the summary generation.

## Input
- `video_filename`: Name of the video file from which to extract audio.
- `language`: Language for the summary output.
- `careful_words`: Specific words that need to be treated with care in the transcript.

## Output
- Audio file (`MP3` format).
- Transcript file (`SRT` format).
- Summary file (`TXT` format).

This script streamlines the process of generating video summaries by handling the complex tasks of audio extraction, transcription, and summarization programmatically.
