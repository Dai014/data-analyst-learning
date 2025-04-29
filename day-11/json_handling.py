import json

def read_json_file(file_path):
    """Read a JSON file and return its content."""
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json_file(file_path, data):
    """Write data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    # Example usage
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    write_json_file('output.json', data)
    
    read_data = read_json_file('output.json')
    print(read_data)

if __name__ == "__main__":
    main()