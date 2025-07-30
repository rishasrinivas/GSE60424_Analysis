
import pandas as pd
import numpy as np

def filter_low_expression(df, min_counts=1, min_samples=3):
    # A gene is considered expressed if it has at least `min_counts` in at least `min_samples`
    mask = (df >= min_counts).sum(axis=1) >= min_samples
    df_filtered = df[mask]
    print(f"Genes before filtering: {df.shape[0]}")
    print(f"Genes after filtering: {df_filtered.shape[0]}")
    return df_filtered

def log_transform(df, pseudocount=1):
    """Apply log2 transformation."""
    df_log = np.log2(df + pseudocount)
    print("Log2 transformation applied.")
    return df_log

if __name__ == "__main__":
    data = pd.read_csv("results/processed_data.csv", index_col=0)
    data_filtered = filter_low_expression(data)
    data_log = log_transform(data_filtered)
    data_log.to_csv("results/processed_log_data.csv")