import streamlit as st
from streamlit_mic_recorder import mic_recorder

# Name of the output file
RECORDING_FILENAME = 'recording.wav'


def record(filename=RECORDING_FILENAME, audio_play=False):
    """
    Function to record audio using the Streamlit Mic Recorder component.

    Parameters:
    - filename (str): Name of the output file to save the recorded audio.

    Returns:
    - None
    """
    # Record audio using the Mic Recorder component
    st.write("Record your voice, and play the recorded audio:")
    audio = mic_recorder(start_prompt="Start Recording 🎤", stop_prompt="️Stop", key='recorder', format='wav', use_container_width=True)

    # If audio is recorded, save it to the specified file and play it
    if audio_play and audio:
        # Write the recorded audio to the file
        with open(filename, 'wb') as f:
            f.write(audio['bytes'])

        # Play the recorded audio
        st.audio(audio['bytes'])


if __name__ == "__main__":
    record()
