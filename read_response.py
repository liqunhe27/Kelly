import json
import os


def process_response(file_path):
    response_string = ""

    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)

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


# Example usage:
if __name__ == '__main__':
    test_string = process_response('response.json')
    print(test_string)
