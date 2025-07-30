# GSE60424 Hybrid Transcriptomic Analysis

This project provides a hybrid Python/R workflow for analyzing the GSE60424 dataset, which profiles human CD8+ T-cell subsets using RNA-seq.

## Project Structure
```bash 
GSE60424_Analysis/
├── README.md
├── requirements.txt
├── data/
│   └── GSE60424_GEOSubmit_FC1to11_normalized_counts.txt
├── src/
│   ├── 01_data_import_and_validation.py
│   ├── 02_data_preprocessing.py
│   ├── 03_exploratory_analysis.py
│   └── 04_differential_expression.R
├── results/
│   ├── Plots&Figures/
│   │   ├── pca_plot.png
│   │   ├── boxplot_expression.png
│   │   ├── heatmap_expression.png
│   │   └── ... (additional plots)
│   └── differential_expression/
│       ├── deseq2_results.csv
│       └── ma_plot.png
└── docx/
    └── report.pdf
```

## Requirements

- Python 3.8+
- R 4.0+
- See `requirements.txt` for Python dependencies.
- R packages: `DESeq2`, `ggplot2`, `dplyr`, `pheatmap`, `RColorBrewer`.

## Running the Analysis

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt` and install R packages.
3. Execute scripts in `src/` in numerical order.
4. Check `results/` for outputs.

## Authors

Risha
