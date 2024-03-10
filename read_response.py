import json
import os


def process_response(file_path, user_name, prior_exchange_num=3):
    response_string = ""

    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)

            if user_name in data:
                user_conversation = data[user_name]
                prior_messages = user_conversation[-prior_exchange_num*2:]
                for message in prior_messages:
                    response_string += "\n"
                    role = message.get('role')
                    content = message.get('content')
                    if role and content:
                        response_string += f"{role}: {content}\n"
            else:
                response_string = f"User '{user_name}' not found in the conversation data."

    else:
        response_string = "File not found."

    return response_string


# Example usage, with 1 previous exchange:
if __name__ == '__main__':
    test_string = process_response('response.json', 'Liqun', 3)
    print(test_string)
