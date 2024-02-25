import json
import os


def process_response(file_path, prior_exchange_num=3):
    response_string = ""

    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)[-prior_exchange_num*2:]

        if isinstance(data, list):
            for message in data:
                response_string += "\n"
                if isinstance(message, dict):
                    role = message.get('role')
                    content = message.get('content')
                    if role and content:
                        response_string += f"{role}: {content}\n"
    else:
        response_string = "File not found."

    return response_string


# Example usage, with 1 previous exchange:
if __name__ == '__main__':
    test_string = process_response('response.json', 1)
    print(test_string)
