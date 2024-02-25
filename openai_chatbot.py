# component 3: Call the ChatGPT API to get a ChatGPT’s response
# input = transcribed_text_input
import os
from openai import OpenAI

# Initialise the OpenAI client
with open(os.path.expanduser(os.path.join(os.path.dirname(__file__), 'OPENAI_API_KEY.txt')), 'r') as f:
    api_key = f.read().strip()  # read the key
client = OpenAI(api_key=api_key)


# Call the ChatGPT API to get a ChatGPT’s response
def get_response(conversational_messages, prior_exchange_num=3, prompt='advanced'):
    topic = 'daily life'

    basic_message = f"""
    Your role is to assist non-native L2 learners in improving their oral language proficiency 
    by discussing {topic} in a casual and informal way."""

    advanced_messages = """\n
    Make sure your responses are:
    1. Sensible and logical
    2. Specific to the user's input
    3. Emotionally connected
    4. Mindful of social contexts and situations in the conversation
    5. Interesting and engaging for audiences
    6. Encourage further conversation"""

    if prompt == 'advanced':
        sys_message = basic_message + advanced_messages
    else:
        sys_message = basic_message

    print('prompt_used =', sys_message)

    conversation = [{"role": "system", "content": sys_message}] + conversational_messages[-prior_exchange_num*2:]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return response.choices[0].message.content


# test
if __name__ == '__main__':
    # open the test file
    text_response = get_response([{"role": "user", "content": "Hi, who are you?!"}], prompt='basic')
    print('\n Response is:', text_response)
