# component 2: Call the Whisper API to transcribe the audio
# input = audio_file_path

import os
from openai import OpenAI

# Initialise the OpenAI client
with open(os.path.expanduser(os.path.join(os.getcwd(), 'OPENAI_API_KEY.txt')), 'r') as f:
    api_key = f.read().strip()  # read the key
client = OpenAI(api_key=api_key)


def get_transcription(audio_file_path):
    with open(audio_file_path, "rb") as audio:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio,
            response_format="text"
        )
    return transcription


# test
if __name__ == '__main__':
    # Audio file path
    audio_file_path_test = os.path.expanduser(os.path.join(os.getcwd(), 'test_recording.wav'))
    transcript = get_transcription(audio_file_path_test)
    print(f"The transcript is: {transcript}")
