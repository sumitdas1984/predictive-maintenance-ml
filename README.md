# Predictive Maintenance ML

An end-to-end, engineering-focused machine learning project to predict machine failures from operating-condition data and demonstrate the ML lifecycle through a controlled production simulation.

## Business problem

Manufacturing equipment failures can result in unplanned downtime, increased maintenance costs and production disruptions. This project aims to develop a machine learning system that analyzes machine sensor measurements and identifies operating conditions associated with failures. The system helps maintenance teams flag potentially problematic conditions and prioritize machines for further inspection.

## Dataset

**AI4I 2020 Predictive Maintenance Dataset** — UCI Machine Learning Repository.

- Dataset page: https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset
- 10,000 synthetic observations.
- Target: `Machine failure`.
- The five failure-mode indicator columns (`TWF`, `HDF`, `PWF`, `OSF`, `RNF`) must not be used as predictors for `Machine failure`; they leak failure information.

The dataset is static and synthetic. It does not provide genuine chronological machine histories or prove real-world predictive maintenance savings. We will use it for offline model development and as the source for a controlled production simulation.

## Project approach

The project has two connected workflows:

1. **Offline ML workflow:** acquire and validate data, preprocess, engineer/select features, train and evaluate models, tune hyperparameters, select a model and register/version it.
2. **Production simulation workflow:** feed observations in batches to an inference API, store predictions, reveal labels after a configurable delay, monitor input drift and labelled model performance, and run controlled retraining/model-promotion checks.

The simulation demonstrates engineering patterns; it is not a claim of a real industrial deployment.

## Quick start

Python 3.10–3.12 recommended.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

Download the CSV from the UCI dataset page and place it under `data/raw/`. See `data/README.md`.

Validate the downloaded file (replace the example filename with the actual filename):

```bash
python -m src.data.validate_data --input data/raw/ai4i2020.csv
```

## Repository map

- `docs/`: project plan, business understanding, concise lifecycle notes and architecture.
- `data/`: dataset instructions; raw and processed datasets are excluded from Git.
- `notebooks/`: exploratory analysis and experiments.
- `src/data/`: data validation and ingestion logic.
- `src/features/`: reusable feature transformations.
- `src/models/`: training and model loading logic.
- `src/evaluation/`: evaluation and model comparison.
- `src/simulation/`: batch production-data simulator and delayed-label simulation.
- `src/serving/`: inference API.
- `src/monitoring/`: input drift and labelled performance monitoring.
- `src/retraining/`: retraining orchestration and candidate-model promotion checks.
- `tests/`: automated tests.
- `configs/`: configuration added when needed.
- `artifacts/`: generated local outputs; not committed by default.

Directories for later milestones may initially contain only placeholders. Implement components when their milestone is reached.

## Working principles

1. Complete one lifecycle milestone at a time.
2. Use notebooks for exploration; move reusable logic into `src/`.
3. Record decisions and lessons, not textbook-length theory.
4. Prevent data leakage; never use failure-mode labels as model inputs.
5. Evaluate using business-relevant metrics, not accuracy alone.
6. Drift detection is a signal for investigation, not an automatic instruction to replace a model.
7. Promote a retrained model only after it passes predefined evaluation checks.
8. Keep the production simulation clearly labelled as simulated.

## Current milestone

**Milestone 1 — Business Understanding.** Define the operational decision, prediction target, costs of false positives/false negatives, success measures and dataset limitations before modelling.
