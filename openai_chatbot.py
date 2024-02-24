# component 3: Call the ChatGPT API to get a ChatGPT’s response
# input = transcribed_text_input
import os
from openai import OpenAI

# Initialise the OpenAI client
with open(os.path.expanduser(os.path.join(os.path.dirname(__file__), 'OPENAI_API_KEY.txt')), 'r') as f:
    api_key = f.read().strip()  # read the key
client = OpenAI(api_key=api_key)


# Call the ChatGPT API to get a ChatGPT’s response
def get_response(conversational_messages):
    topic = 'daily life'
    sys_message = f"""
        Your role is to assist non-native L2 learners in improving their oral language proficiency 
        by discussing {topic}"""

    conversation = [{"role": "system", "content": sys_message}] + conversational_messages

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return response.choices[0].message.content


# test
if __name__ == '__main__':
    # open the test file
    text_response = get_response([{"role": "user", "content": "Hi, who are you?!"}])
    print(text_response)
