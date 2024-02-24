import json


def process_response(file_path):
    response_string = ""
    with open(file_path, 'r') as f:
        data = json.load(f)

    if isinstance(data, list):
        for message in data:
            if isinstance(message, dict):
                role = message.get('role')
                content = message.get('content')
                if role and content:
                    response_string += f"{role}: {content}\n"
    return response_string


# Example usage:
if __name__ == '__main__':
    test_string = process_response('test_response.json')
    print(test_string)
