# audio-player
import base64
import streamlit as st
import time


def play(file_path: str):
    # Open the WAV audio file
    with open(file_path, "rb") as f:
        # Read the audio data
        data = f.read()
        # Encode the audio data to base64
        b64 = base64.b64encode(data).decode()
        # Create an empty placeholder
        placeholder = st.empty()
        # Construct the HTML for the audio player
        md = f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                Your browser does not support the audio element.
            </audio>
            """

        time.sleep(1)
        # Render the audio player using Markdown
        placeholder.markdown(md, unsafe_allow_html=True)


if __name__ == "__main__":
    st.write("# Auto-playing Audio 🎵!")
    play("test_recording.wav")
