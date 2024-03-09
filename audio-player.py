# audio-player
import base64
import streamlit as st
import time


def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        placeholder = st.empty()
        md = f"""
            <audio autoplay class="stAudio">
            <source src="data:audio/wav;base64,{b64}" type="audio/wav">
            Your browser does not support the audio element.
            </audio>
            """
        time.sleep(1)
        placeholder.markdown(md, unsafe_allow_html=True)


if __name__ == "__main__":
    # Header for the Streamlit ap
    # p
    st.write("# Auto-playing Audio 🎵!")

    # Provide the path to the WAV audio file you want to play
    autoplay_audio("test_recording.wav")
