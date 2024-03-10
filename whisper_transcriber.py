# component 2: Call the Whisper API to transcribe the audio
# input = audio_file_path

import os
from openai import OpenAI

# Initialise the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_transcription(audio_file_path):
    with open(audio_file_path, "rb") as audio:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio,
            response_format="text",
            prompt="Umm, let me think like, hmm... Okay, here's what I'm, like, hello, hi"
        )
    return transcription


# test
if __name__ == '__main__':
    # Audio file path
    audio_file_path_test = os.path.expanduser(os.path.join(os.getcwd(), 'test_recording.wav'))
    transcript = get_transcription(audio_file_path_test)
    print(f"The transcript is: {transcript}")
