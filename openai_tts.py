# component 4: Call the OpenAPI TTS api
import os
import openai
from openai import OpenAI
from pydub import AudioSegment
from pydub.playback import play

# Initialise the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def tts(text, mute=False):
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )

    speech_file_path = 'temp.wav'
    if not os.path.exists(speech_file_path):
        os.makedirs(os.path.dirname(speech_file_path), exist_ok=True)

    speech_file_path = os.path.expanduser(os.path.join(os.getcwd(), speech_file_path))

    response.stream_to_file(speech_file_path)

    # play it
    if not mute:
        voice_response = AudioSegment.from_file(speech_file_path)
        play(voice_response)


# test
if __name__ == '__main__':
    # run the defined function
    tts('this is a test')
