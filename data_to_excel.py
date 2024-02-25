import json
import pandas as pd


def data_to_excel(file_path):
    # Read JSON file content
    with open(file_path, 'r') as file:
        json_data = file.read()

    # Parse JSON
    data = json.loads(json_data)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Write to Excel
    excel_file = 'conversation.xlsx'
    df.to_excel(excel_file, index=False)

    print(f"Excel file '{excel_file}' has been created.")


if __name__ == "__main__":
    # Specify the file path to your JSON file
    file_path = 'response.json'
    data_to_excel(file_path)
