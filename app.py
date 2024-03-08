import os
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json

# Import local libraries
from streamlit_mic_recorder import mic_recorder  # Using a new streamlit component
from whisper_transcriber import get_transcription
from openai_chatbot import get_response
from openai_tts import tts
from read_response import process_response

# Initialise the OpenAI client
os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]

# Log version information
version_info = 'Kelly V0.4 _ 08Mar'

# Initialise voice recording
INPUT_WAVFILE = 'prompt.wav'
if os.path.exists(INPUT_WAVFILE):
    os.remove(INPUT_WAVFILE)

# Load animation URL
LOTTIE_URL = 'https://assets6.lottiefiles.com/packages/lf20_6e0qqtpa.json'


# Function to load Lottie animation from URL
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return
    return r.json()


# Load Lottie animation
lottie_anim = load_lottie(LOTTIE_URL)

# Set page configuration and initialize session state variables
st.set_page_config(page_title="Internal_Beta_Kelly", page_icon='', layout='centered')

if "prompt_text" not in st.session_state:
    st.session_state.prompt_text = None
if "chat_text" not in st.session_state:
    st.session_state.chat_text = None


# Set up the interface layout including Lottie animation, title, and record button
with st.container():
    left, right = st.columns([2, 3])
    with left:
        st_lottie(lottie_anim, height=300, key='coding')

    with right:
        st.subheader('Hi, I\'d love to chat with you ❤️')
        st.write(version_info)
        st.write('Press Record to say something')

        audio = mic_recorder(start_prompt="Start Recording 🎤", stop_prompt="️Stop", key='recorder', format='wav',
                             use_container_width=True)  # the new streamlit component

        if audio:
            # Write the recorded audio to the file
            with open(INPUT_WAVFILE, 'wb') as f:
                f.write(audio['bytes'])

        if os.path.exists(INPUT_WAVFILE):
            # transcribe recording
            single_turn = get_transcription(INPUT_WAVFILE)

            # Record conversation
            if 'conversation' not in st.session_state:
                st.session_state.conversation = []

            conversation = st.session_state.conversation

            # Clear conversation history when the user starts a new conversation
            # if st.button("Start New Conversation"):
            #    conversation.clear()

            # Add user message to the conversation history
            conversation.append({"role": "user", "content": single_turn})

            response = get_response(conversation, 3, 'advanced')  # Through OpenAI API, with 3 preceding exchanges
            conversation.append({"role": "assistant", "content": response})

            json.dump(conversation, open('response.json', 'wt'))

            st.session_state.chat_text = conversation

            prompt_box = st.empty()
            if st.session_state.prompt_text:
                prompt_box.write(f'I heard you saying: {st.session_state.prompt_text}')


# Display recording result and chat information
if st.session_state.chat_text:
    # Extract 'assistant' replies
    assistant_replies = [message['content'] for message in st.session_state.chat_text if message.get('role') == 'assistant']

    # Perform text-to-speech conversion only for the last 'assistant' reply
    if assistant_replies:
        last_assistant_reply = assistant_replies[-1]
        st.write('---')
        st.subheader('Last Assistant Reply')
        st.write(last_assistant_reply)
        tts(last_assistant_reply)


# Display the Conversation History in Streamlit
response_string = process_response('response.json', 3)

if response_string:
    st.write('---')
    st.subheader('Conversation History')
    st.write(response_string)
