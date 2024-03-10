import json
import pandas as pd


def data_to_excel(json_data, username):
    # Parse JSON
    data = json.loads(json_data)

    # Initialize lists to store role and content
    roles = []
    contents = []

    # Extract role and content from the data
    for message in data[username]:
        roles.append(message['role'])
        contents.append(message['content'])

    # Create DataFrame
    df = pd.DataFrame({
        'Role': roles,
        'Content': contents
    })

    # Write to Excel
    excel_file = f'conversation_history_{username}.xlsx'
    df.to_excel(excel_file, index=True)

    print(f"Excel file '{excel_file}' has been created.")


if __name__ == "__main__":
    # Specify the file path to your JSON file
    file_path = 'response.json'
    with open(file_path, 'r') as file:
        _data = file.read()
    data_to_excel(_data,'Liqun')
