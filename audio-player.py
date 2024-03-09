# audio-player
import base64
import streamlit as st


def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/wav;base64,{b64}" type="audio/wav">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)


if __name__ == "__main__":
    # Header for the Streamlit app
    st.write("# Auto-playing Audio 🎵!")

    # Provide the path to the WAV audio file you want to play
    autoplay_audio("test_recording.wav")
