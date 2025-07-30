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


# Technical Brief: Hybrid Analysis of GSE60424


## Problem Statement


The goal is to analyze the GSE60424 RNA-seq dataset profiling CD8+ T-cell subsets to identify differentially expressed genes (DEGs) and understand the transcriptomic landscape. The challenge is to create a workflow that is reproducible, modular, and utilizes the strengths of both Python and R.


## Programming Design


We adopted a **Hybrid Python/R** strategy.


- **Python** (`pandas`, `scikit-learn`, `matplotlib`, `seaborn`): Used for data import, initial validation, preprocessing (filtering, log transformation), and general-purpose exploratory data analysis (PCA, heatmaps, boxplots).
- **R** (`DESeq2`, `ggplot2`, `dplyr`): Used for the core differential expression analysis, leveraging its specialized statistical frameworks for count data.


This approach combines Python's data manipulation flexibility and scalability with R's statistical rigor and bioinformatics-specific packages.


## Workflow Snapshot


1.  **Data Import & Validation (Python):** Load data, check for missing/negative values.
2.  **Preprocessing (Python):** Filter low-expression genes, apply log2 transformation.
3.  **Exploratory Analysis (Python):** Generate PCA, boxplots, correlation heatmaps, and expression heatmaps.
4.  **Differential Expression (R):** Use DESeq2 for statistical testing and generate MA/Volcano plots.


## Documentation & Reusability


- Modular scripts with clear input/output.
- Comments and docstrings explain each step.
- `README.md` provides setup and run instructions.
- File paths are relative, ensuring portability.


## Scalability Note


The modular structure allows easy adaptation:
- New datasets can be processed by changing the input file path in `01_data_import_and_validation.py`.
- Preprocessing parameters (e.g., `min_counts`) are configurable.
- The DESeq2 script can be modified to accommodate different experimental designs by updating the `design` formula and `sample_info`.


## Anticipated Questions & Rebuttal


- **Q:** Why not use a single language?
- **A:** A hybrid approach maximizes tool suitability. Python excels at data munging and general visualization, while R/DESeq2 provides the most robust and widely accepted methods for RNA-seq DE analysis. This ensures the highest quality scientific results while maintaining a flexible and maintainable codebase.
