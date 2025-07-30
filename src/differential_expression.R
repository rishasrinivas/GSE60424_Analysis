# Install packages if not already installed
if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
if (!requireNamespace("DESeq2", quietly = TRUE))
  BiocManager::install("DESeq2")
if (!requireNamespace("ggplot2", quietly = TRUE))
  install.packages("ggplot2")
if (!requireNamespace("dplyr", quietly = TRUE))
  install.packages("dplyr")

# Load libraries
library(DESeq2)
library(ggplot2)
library(dplyr)

# Load data
data_file <- "results/processed_data.xls" # Use non-log data for DESeq2
cts <- as.matrix(read.csv(data_file, row.names = 1))

# Example metadata creation (needs to be adapted based on actual sample names)
sample_info <- data.frame(
  sample = colnames(cts),
  condition = factor(rep(c("Group1", "Group2"), each = ncol(cts) / 2)) # Placeholder
)
rownames(sample_info) <- sample_info$sample

# DESeq2 workflow
dds <- DESeqDataSetFromMatrix(countData = cts,
                              colData = sample_info,
                              design = ~ condition)

# Filter low counts (DESeq2 does this internally, but explicit filtering can be done)
# keep <- rowSums(counts(dds)) >= 10
# dds <- dds[keep,]

# Run DESeq
dds <- DESeq(dds)

# Extract results
res <- results(dds)
res_df <- as.data.frame(res)
res_df$gene <- rownames(res_df)

# Save results
write.csv(res_df, "results/deseq2_results.csv", row.names = FALSE)

# MA Plot
plotMA(res, main="MA Plot")
dev.copy(png, "results/Plots&Figures/ma_plot.png")
dev.off()

# Volcano Plot
res_df$threshold <- ifelse(res_df$padj < 0.05 & abs(res_df$log2FoldChange) > 1, "Significant", "Not Significant")
p_volcano <- ggplot(res_df, aes(x = log2FoldChange, y = -log10(padj), color = threshold)) +
  geom_point(alpha = 0.6, size = 1.2) +
  scale_color_manual(values = c("Significant" = "red", "Not Significant" = "grey")) +
  theme_minimal() +
  geom_hline(yintercept = -log10(0.05), linetype = "dashed") +
  geom_vline(xintercept = c(-1, 1), linetype = "dashed") +
  labs(title = "Volcano Plot", x = "Log2 Fold Change", y = "-Log10 (Adjusted P-value)")

ggsave("results/Plots&Figures/volcano_plot.png", plot = p_volcano, width = 8, height = 6)

print("Differential expression analysis complete.")