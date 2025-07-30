import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os

def plot_expression_boxplot(df, sample_size=20):
    plt.figure(figsize=(15, 6))
    # Sample a subset of samples for clarity
    df_sample = df.iloc[:, :sample_size] if df.shape[1] > sample_size else df
    df_sample.boxplot(rot=45)
    plt.title('Distribution of Gene Expression (Log2)')
    plt.ylabel('Log2(Normalized Counts + 1)')
    plt.tight_layout()
    plt.savefig('results/Plots&Figures/boxplot_expression.png')
    plt.close()
    print("Boxplot saved.")

def plot_sample_correlation_heatmap(df):
    corr_matrix = df.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, cmap='coolwarm', center=0, square=True)
    plt.title('Sample Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('results/ePlots&Figures/correlation_heatmap.png')
    plt.close()
    print("Correlation heatmap saved.")

def plot_pca(df):
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(df.T) # Transpose for samples as rows
    
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(data_scaled)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(pca_result[:, 0], pca_result[:, 1])
    for i, sample in enumerate(df.columns):
        plt.text(pca_result[i, 0], pca_result[i, 1], sample, fontsize=9)
    plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2%} variance)')
    plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2%} variance)')
    plt.title('PCA of Samples')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('results/Plots&Figures/pca_plot.png')
    plt.close()
    print("PCA plot saved.")
    print(f"Explained variance ratio: {pca.explained_variance_ratio_}")

def plot_expression_heatmap(df, top_n=50):
    # Calculate variance for each gene
    gene_var = df.var(axis=1).sort_values(ascending=False)
    top_genes = gene_var.head(top_n).index
    df_top = df.loc[top_genes]

    plt.figure(figsize=(15, 12))
    sns.heatmap(df_top, cmap='viridis', yticklabels=False, xticklabels=True, cbar_kws={'label': 'Log2(Normalized Counts + 1)'})
    plt.title(f'Heatmap of Top {top_n} Most Variable Genes')
    plt.xlabel('Samples')
    plt.ylabel('Genes')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('results/Plots&Figures/heatmap_expression.png')
    plt.close()
    print("Expression heatmap saved.")

if __name__ == "__main__":
    os.makedirs("results/Plots&Figures", exist_ok=True)
    data = pd.read_csv("results/processed_log_data.csv", index_col=0)
    
    plot_expression_boxplot(data)
    plot_sample_correlation_heatmap(data)
    plot_pca(data)
    plot_expression_heatmap(data)