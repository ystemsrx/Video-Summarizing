from moviepy.editor import VideoFileClip
from openai import OpenAI

def extract_audio(video_file, audio_file, callback):
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file)
    return callback(audio_file)

def transcribe_audio(audio_file):
    client = OpenAI()
    print('Starting to convert audio to transcript...')
    audio_file= open(audio_file, "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
        response_format="srt"
    )
    return transcript

def save_transcript_as_srt(transcript, srt_file_name):
    with open(srt_file_name, 'w') as file:
        file.write(transcript)

def read_srt(srt_file_name):
    with open(srt_file_name, 'r') as file:
        return file.read()

def generate_summary(temperature, srt_content):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": f"You are a proficient assistant tasked with summarizing SRT files of videos in {language}. Initially, you need to understand the meaning of the content. Instead of adhering strictly to the segments in the SRT file, you are required to independently reorganize the material into new sections based on content, be as meticulous as possible, if transition words or phrases appear in the content, you should devide it based on them. For each section, first state the corresponding time period, then provide a detailed summary of its contents. Finally, compose an overarching summary of the entire file, encapsulating the key themes and messages. Besides, when generating, you must correct any spelling discrepancies in the transcribed text. Make sure that the names of the following products are spelled correctlly: DALL-E, {careful_words}. The output format are as follows: \nTime: ...\nSummary: ...\n\nFull text summary: ..."
            },
            {
                "role": "user",
                "content": srt_content
            }
        ]
    )
    return response.choices[0].message.content

video_filename = 'test.mp4'
base_filename = video_filename.rsplit('.', 1)[0]
audio_filename = base_filename + '_audio.mp3'
srt_filename = base_filename + '_transcript.srt'

language = input('Enter the language of summary you want to generate: ')
careful_words = input('Enter the words you want AI to be careful with (If there are multiple, separate them with commas. If not, press Enter): ')

print('Starting to extract audio from video...')
transcript = extract_audio(video_filename, audio_filename, transcribe_audio)
save_transcript_as_srt(transcript, srt_filename)
print('Successfully saved transcript as srt file.')

srt_content = read_srt(srt_filename)
print('Starting to generate summary...')
summary = generate_summary(0.5, srt_content)

summary_filename = base_filename + '_summary.txt'
with open(summary_filename, 'w') as file:
    file.write(summary)
print('Successfully saved summary as txt file.')
