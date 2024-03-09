# audio-player
import base64
import streamlit as st


def play(file_path: str):
    # Open the WAV audio file
    with open(file_path, "rb") as f:
        # Read the audio data
        data = f.read()
        # Encode the audio data to base64
        b64 = base64.b64encode(data).decode()
        # Construct the HTML for the audio player
        md = f"""
        <script>
            Vue.prototype.innerAudioContext = uni.createInnerAudioContext();

            Vue.prototype.playAudio = function(base64Audio) {{
                console.log('Playing');
                var innerAudioContext = Vue.prototype.innerAudioContext;
                innerAudioContext.autoplay = true;
                innerAudioContext.src = 'data:audio/wav;base64,' + base64Audio;
                innerAudioContext.play();
            }}

            Vue.prototype.playStop = function() {{
                console.log('Stopping');
                var innerAudioContext = Vue.prototype.innerAudioContext;
                innerAudioContext.stop();
            }}
        </script>
        """

        # Render the audio player using Markdown
        st.markdown(md, unsafe_allow_html=True)


if __name__ == "__main__":
    st.write("# Auto-playing Audio 🎵!")
    play_audio("test_recording.wav")
