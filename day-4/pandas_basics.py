import pandas as pd

# Create a DataFrame from a CSV file
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Save a DataFrame to a CSV file
def save_to_csv(df, file_path):
    df.to_csv(file_path, index=False)

# Example usage
if __name__ == "__main__":
    # Read data from a CSV file
    data = read_csv('example_data.csv')
    print(data)

    # Perform basic operations
    print("DataFrame Info:")
    print(data.info())

    # Save the DataFrame to a new CSV file
    save_to_csv(data, 'processed_data.csv')