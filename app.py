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
from data_to_excel import data_to_excel

# Initialise the OpenAI client
os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]

# Log version information
version_info = 'Kelly V0.7 _ 10Mar_🐱'

# Initialise voice recording
INPUT_WAVFILE = 'prompt.wav'
if os.path.exists(INPUT_WAVFILE):
    os.remove(INPUT_WAVFILE)

# Set whether to display conversation text
_show_history = False

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
    st.session_state.chat_text = {}
if "username" not in st.session_state:
    st.session_state.username = None


# Set up the interface layout including Lottie animation, title, and record button
with st.container():
    left, right = st.columns([2, 3])
    with left:
        st_lottie(lottie_anim, height=300, key='coding')

    with right:
        st.subheader('Hi, I\'d love to chat with you ❤️')
        st.write(version_info)
        st.write('Press Record to say something')

        # Add username input
        st.session_state.username = st.text_input('Enter your username')

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
            if st.session_state.username in st.session_state.chat_text:
                conversation = st.session_state.chat_text[st.session_state.username]
            else:
                conversation = []

            # Add user message to the conversation history with username
            conversation.append({"role": "user", "content": single_turn})

            response = get_response(conversation, 3, 'advanced')  # Through OpenAI API, with 3 preceding exchanges

            conversation.append({"role": "assistant", "content": response})

            # Update the chat_text dictionary with the conversation for the current user
            st.session_state.chat_text[st.session_state.username] = conversation

            json.dump(st.session_state.chat_text, open('response.json', 'wt'))

            prompt_box = st.empty()
            if st.session_state.prompt_text:
                prompt_box.write(f'I heard you saying: {st.session_state.prompt_text}')


# Add a download button for the conversation history
if st.button('Get Conversation History'):
    with open('response.json', 'r') as file:
        json_data = file.read()

        if st.session_state.username in json_data:
            data_to_excel(json_data, st.session_state.username)

            # Provide download button for the Excel file
            excel_file_path = f'conversation_history_{st.session_state.username}.xlsx'
            with open(excel_file_path, 'rb') as excel_file:
                excel_data = excel_file.read()
                st.download_button(label=f"Download {st.session_state.username}'s Conversation History",
                                   data=excel_data, file_name=excel_file_path,
                                   mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        else:
            st.write(f"User '{st.session_state.username}' not found in the conversation data.")


#  Output responses
if st.session_state.chat_text:
    # Extract 'assistant' replies for the current user
    assistant_replies = [message['content'] for message in st.session_state.chat_text.get(st.session_state.username, [])
                         if message.get('role') == 'assistant']

    # Perform text-to-speech conversion only for the last 'assistant' reply for the current user
    if assistant_replies:
        last_assistant_reply = assistant_replies[-1]
        tts(last_assistant_reply)

        # Display recording result
        if _show_history:
            st.write('---')
            st.subheader('Last Assistant Reply')
            st.write(last_assistant_reply)

# Display the Conversation History in Streamlit
if _show_history:
    response_string = process_response('response.json', st.session_state.username, 3)

    if response_string:
        st.write('---')
        st.subheader('Conversation History for ' + st.session_state.username)  # Display history for the current user
        st.write(response_string)
