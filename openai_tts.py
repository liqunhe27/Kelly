# component 4: Call the OpenAPI TTS api
import os
from openai import OpenAI
from audio_player import play
from pydub import AudioSegment

# Initialise the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def tts(text, mute=False):
    response = client.audio.speech.create(
        model="tts-1",
        voice="echo",
        input=text
    )

    speech_file_name = 'temp.mp3'
    speech_file_path = os.path.join(os.getcwd(), speech_file_name)

    if not os.path.exists(speech_file_path):
        os.makedirs(os.path.dirname(speech_file_path), exist_ok=True)

    response.stream_to_file(speech_file_path)

    # change speed
    audio = AudioSegment.from_file(speech_file_path)
    adjusted_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * 0.8)
    }) + 2
    adjusted_audio.export(speech_file_path, format="mp3")

    # play it
    if not mute:
        play(speech_file_path)


# test
if __name__ == '__main__':
    # run the defined function
    tts('this is a test')
