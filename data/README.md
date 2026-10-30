# Data

## Source
AI4I 2020 Predictive Maintenance Dataset — UCI Machine Learning Repository:
https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

Download the dataset from the official page. Place the CSV in `data/raw/` (for example, `data/raw/ai4i2020.csv`).

## Data handling
- Raw and processed datasets are excluded from Git by `.gitignore`.
- Keep source, retrieval date, filename and any transformation details in your project notes.
- Do not modify the raw source file.
- Do not use failure-mode indicator columns as predictors for the `Machine failure` target.

## Expected target and leakage warning
Target: `Machine failure`.

Failure-mode indicator columns commonly include:
- `TWF`
- `HDF`
- `PWF`
- `OSF`
- `RNF`

These indicate failure modes and should be excluded from model input features when predicting machine failure.

## Folder convention
- `raw/`: downloaded source data, unchanged.
- `processed/`: derived datasets; regenerate from code where possible.
