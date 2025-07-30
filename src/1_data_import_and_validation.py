import pandas as pd
import os

def load_data(filepath):
    # The file is tab-separated with gene IDs in the first column
    df = pd.read_csv(filepath, sep='\t', index_col=0)
    print(f"Data loaded. Shape: {df.shape}")
    print(df.head())
    return df

def validate_data(df):
    # Check for missing values
    if df.isnull().any().any():
        print("Warning: Missing values found.")
    else:
        print("No missing values detected.")
    
    # Check for negative values (shouldn't be in normalized counts)
    if (df < 0).any().any():
        print("Warning: Negative values found.")
    else:
        print("All values are non-negative.")
    
    # Summary statistics
    print("\nData Summary:")
    print(df.describe())

if __name__ == "__main__":
    data_path = "GSE60424_GEOSubmit_FC1to11_normalized_counts.txt"
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found at {data_path}")
    
    data = load_data(data_path)
    validate_data(data)
    data.to_csv("results/processed_data.csv") 