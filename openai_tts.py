# component 4: Call the OpenAPI TTS api
import os
from openai import OpenAI
from pydub import AudioSegment
from pydub.playback import play

# Initialise the OpenAI client
with open(os.path.expanduser(os.path.join(os.path.dirname(__file__), 'OPENAI_API_KEY.txt')), 'r') as f:
    api_key = f.read().strip()  # read the key
client = OpenAI(api_key=api_key)


def tts(text, mute=False):
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )

    speech_file_path = os.path.expanduser(os.path.join(os.getcwd(), 'temp.wav'))

    response.stream_to_file(speech_file_path)

    # play it
    if not mute:
        voice_response = AudioSegment.from_file(speech_file_path)
        play(voice_response)


# test
if __name__ == '__main__':
    # run the defined function
    tts('this is a test')
