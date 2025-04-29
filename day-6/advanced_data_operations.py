import pandas as pd

def clean_data(df):
    # Remove rows with missing values
    df_cleaned = df.dropna()
    return df_cleaned

def calculate_statistics(df):
    # Calculate mean, median, and standard deviation for numerical columns
    stats = {
        'mean': df.mean(),
        'median': df.median(),
        'std_dev': df.std()
    }
    return stats

def group_data(df, group_by_column):
    # Group data by a specified column and calculate the mean
    grouped_data = df.groupby(group_by_column).mean()
    return grouped_data

def merge_dataframes(df1, df2, on_column):
    # Merge two dataframes on a specified column
    merged_df = pd.merge(df1, df2, on=on_column)
    return merged_df

# Example usage
if __name__ == "__main__":
    # Load sample data
    df1 = pd.DataFrame({
        'A': [1, 2, 3, None],
        'B': [4, 5, None, 7]
    })
    
    df2 = pd.DataFrame({
        'A': [1, 2, 3],
        'C': [8, 9, 10]
    })
    
    cleaned_df = clean_data(df1)
    stats = calculate_statistics(cleaned_df)
    grouped = group_data(cleaned_df, 'A')
    merged = merge_dataframes(cleaned_df, df2, 'A')
    
    print("Cleaned DataFrame:\n", cleaned_df)
    print("Statistics:\n", stats)
    print("Grouped Data:\n", grouped)
    print("Merged DataFrame:\n", merged)