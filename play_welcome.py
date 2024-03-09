# audio-player
import base64
import os
import streamlit as st


def play_welcome():
    speech_file_path = os.path.join(os.getcwd(), 'welcome.mp3')

    with open(speech_file_path, "rb") as f:
        # Read the audio data
        data = f.read()
        # Encode the audio data to base64
        b64 = base64.b64encode(data).decode()
        # Construct the HTML for the audio player
        md = f"""
                <audio id="myAudio" autoplay playsinline>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>

                <script>
                    var myAudio = document.getElementById('myAudio');
                    myAudio.muted = false; 
                    myAudio.autoplay = true;
                    myAudio.play();
                </script>
                """

        # Render the audio player using Markdown
        st.markdown(md, unsafe_allow_html=True)


if __name__ == "__main__":
    st.write("# Welcome 🐱!")
    if st.button("Click here to start"):
        play_welcome()
