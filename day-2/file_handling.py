def read_csv(file_path):
    import pandas as pd
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None

def write_csv(data, file_path):
    try:
        data.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Error writing to the CSV file: {e}")

def read_json(file_path):
    import pandas as pd
    try:
        data = pd.read_json(file_path)
        return data
    except Exception as e:
        print(f"Error reading the JSON file: {e}")
        return None

def write_json(data, file_path):
    try:
        data.to_json(file_path, orient='records', lines=True)
    except Exception as e:
        print(f"Error writing to the JSON file: {e}")

# Example usage
if __name__ == "__main__":
    # Read CSV
    csv_data = read_csv('data.csv')
    print(csv_data)

    # Write CSV
    if csv_data is not None:
        write_csv(csv_data, 'output.csv')

    # Read JSON
    json_data = read_json('data.json')
    print(json_data)

    # Write JSON
    if json_data is not None:
        write_json(json_data, 'output.json')