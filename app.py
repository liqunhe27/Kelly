# Build the app interface using Streamlit
import os
from openai import OpenAI
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json

# Import local libraries
from audio_recorder import record
from whisper_transcriber import get_transcription
from openai_chatbot import get_response
from openai_tts import tts
from read_response import process_response

# Initialise the OpenAI client
with open(os.path.expanduser(os.path.join(os.path.dirname(__file__), 'OPENAI_API_KEY.txt')), 'r') as f:
    api_key = f.read().strip()  # read the key

# client = OpenAI(api_key=api_key)
client = OpenAI(api_key=api_key)

# Load animation URL
LOTTIE_URL = 'https://assets6.lottiefiles.com/packages/lf20_6e0qqtpa.json'
INPUT_WAVFILE = 'prompt.wav'


# Function to load Lottie animation from URL
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return
    return r.json()


# Load Lottie animation
lottie_anim = load_lottie(LOTTIE_URL)

# Set page configuration and initialize session state variables
st.set_page_config(page_title="Test_version_Kelly", page_icon='', layout='centered')

if "is_recording" not in st.session_state:
    st.session_state.is_recording = False
if "prompt_text" not in st.session_state:
    st.session_state.prompt_text = None
if "chat_text" not in st.session_state:
    st.session_state.chat_text = None


# Define button callback function for recording
#  A callback is a function triggered by an event, enabling dynamic and responsive behaviours.
# @st.cache(allow_output_mutation=True)
@st.cache_data
def create_chat():
    return []


def callback_record():
    st.session_state.is_recording = True
    prompt_box.write("I'm listening ...")

    # Record the prompt
    record(filename=INPUT_WAVFILE)
    # prompt_box.write("Processing the prompt ...")

    st.session_state.is_recording = False

    # Process recording
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

    response = get_response(conversation, 3)  # Through OpenAI API, with 3 preceding exchanges
    conversation.append({"role": "assistant", "content": response})

    json.dump(conversation, open('response.json', 'wt'))

    st.session_state.chat_text = conversation


# Set up the interface layout including Lottie animation, title, and record button
with st.container():
    left, right = st.columns([2, 3])
    with left:
        st_lottie(lottie_anim, height=300, key='coding')

    with right:
        st.subheader('Hi, I\'d love to chat with you ❤️')
        st.write('V0.2 _ 24Feb')
        st.write('Press Record to say something')

        rec_button = st.button(
            label="Record :microphone:", type='primary',
            on_click=callback_record,
            disabled=st.session_state.is_recording)

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


# Display the response_string in Streamlit
response_string = process_response('response.json')

if response_string:
    st.write('---')
    st.subheader('Conversation History')
    st.write(response_string)
