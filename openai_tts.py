# component 4: Call the OpenAPI TTS api
import os
from openai import OpenAI
from audio_player import play

# Initialise the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def tts(text, mute=False):
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )

    speech_file_name = 'temp.mp3'
    speech_file_path = os.path.join(os.getcwd(), speech_file_name)

    if not os.path.exists(speech_file_path):
        os.makedirs(os.path.dirname(speech_file_path), exist_ok=True)

    response.stream_to_file(speech_file_path)

    # play it
    if not mute:
        play(speech_file_path)


# test
if __name__ == '__main__':
    # run the defined function
    tts('Hello there, I\'m Kelly from London. I\'m happy to meet you.', mute=True)
