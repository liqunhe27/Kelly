from openai_chatbot import get_response


# Define a function to get completions for a given input
def get_completions(test_input, num_completions=5):
    given_message = [{"role": "user", "content": test_input}]
    for prompt in ['basic', 'advanced']:
        print(f"Prompt: {prompt}")
        for i in range(num_completions):
            response = get_response(conversational_messages=given_message, prior_exchange_num=0, prompt=prompt)
            print(f"Completion {i + 1}: {response}")
        print()


# Get completions for the test question
test_question = "Any suggestions for visiting Chengdu?"
get_completions(test_question, num_completions=5)
