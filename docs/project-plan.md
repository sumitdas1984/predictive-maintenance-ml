# Project Plan

## Objective

Build a complete, reproducible ML lifecycle for machine-failure risk prediction, then exercise the deployed model through a controlled production simulation. The project emphasizes ML engineering practices while keeping the scope feasible for one developer.

## Business problem

Unexpected machine failures can cause unplanned downtime, maintenance expense and production disruption. The proposed model estimates failure risk from operating measurements to help maintenance teams prioritize inspection.

## Scope

### In scope

- AI4I dataset acquisition, validation and documentation.
- Data preprocessing, feature engineering and feature selection.
- Baseline model training, evaluation, tuning and final selection.
- Reproducible experiments and model versioning/registry.
- Batch-based production-data simulation.
- FastAPI inference service.
- Prediction logging and configurable delayed-label simulation.
- Data drift and labelled model-performance monitoring.
- Controlled retraining, candidate evaluation and model-promotion checks.
- Tests, Docker packaging and concise technical documentation.

### Out of scope

- Real-time industrial sensor streaming or Kafka.
- PLC/SCADA integration.
- Kubernetes or distributed training.
- Genuine temporal degradation forecasting.
- Claims of measured factory savings or proven real-world performance from synthetic data.

## Dataset and simulation constraints

- Source: UCI AI4I 2020 Predictive Maintenance Dataset (10,000 synthetic observations).
- Target: `Machine failure`.
- The dataset is static; it does not contain genuine chronological machine histories.
- Failure-mode indicator columns (`TWF`, `HDF`, `PWF`, `OSF`, `RNF`) must be excluded from predictors for `Machine failure`.
- A held-out portion of the dataset will be reserved for production simulation after a defensible split strategy is established.
- The simulator will send observations in batches. Ground-truth labels will be revealed after a configurable delay to emulate label latency.
- Controlled feature perturbations may be introduced in a separate simulation scenario to test drift detection. Such drift is synthetic and must be identified as such.
- Retraining will use eligible labelled simulation observations plus an explicitly defined historical training set. A separate evaluation set will remain untouched for promotion checks.

## Milestones

| # | Lifecycle stage | Exit deliverable | Status |
|---|---|---|---|
| 1 | Business understanding | Decision statement, target, costs, KPIs, assumptions and limitations | In progress |
| 2 | Data collection | Reproducible acquisition and source record | Not started |
| 3 | Data preprocessing | Validated, leakage-safe preprocessing pipeline and split strategy | Not started |
| 4 | Feature engineering | Documented and tested feature transformations | Not started |
| 5 | Feature selection | Comparison of selection methods and rationale | Not started |
| 6 | Model training | Reproducible baseline models and experiment records | Not started |
| 7 | Model evaluation | Evaluation report with class-imbalance and business interpretation | Not started |
| 8 | Hyperparameter tuning | Tuned candidate and recorded search procedure | Not started |
| 9 | Final model selection | Selected model, operating threshold and acceptance criteria | Not started |
| 10 | Model deployment | Versioned model served through a tested, containerized FastAPI service | Not started |
| 11 | Monitoring & maintenance | Prediction/input logging, drift checks and delayed-label performance monitoring | Not started |
| 12 | Model retraining | Retraining workflow, candidate-vs-current comparison and guarded promotion | Not started |

## Production simulation design

The production simulation is a supporting engineering layer for deployment, monitoring and retraining:

1. Partition data so that training, model-selection/evaluation and simulation observations are kept separate.
2. Feed simulation observations to the inference API in configurable batches.
3. Persist input metadata, prediction probability, predicted class, timestamp and model version.
4. Reveal the known dataset label after a configurable simulated delay; keep prediction and label records logically separate.
5. Monitor input distributions even before labels arrive.
6. Calculate model-performance metrics only when corresponding labels become available.
7. Trigger investigation/retraining based on configured conditions and sufficient labelled data—not on drift alone.
8. Evaluate a retrained candidate against a fixed, untouched evaluation set and promotion criteria before changing the production model version.

## Timebox

Target: four weeks, approximately 30–35 focused hours. The timebox is a guide; milestone exit criteria take priority over rushing.

| Week | Focus | Expected deliverable |
|---|---|---|
| 1 | Business understanding, data collection and preprocessing | Business definition and validated data pipeline |
| 2 | Feature engineering, feature selection and model training | Feature pipeline and baseline models |
| 3 | Evaluation, tuning and final model selection | Selected model and evaluation record |
| 4 | Deployment, production simulation, monitoring and retraining | Containerized API and demonstrable simulation workflow |

## Definition of done

A milestone is complete when its deliverable exists, important decisions are recorded, and relevant code/tests run successfully. Do not implement future milestones prematurely.

## Working rules

- One milestone at a time.
- Notebooks are for exploration; reusable logic belongs in `src/`.
- Keep `docs/ml-lifecycle-notes.md` concise: concepts, methods considered, decision/rationale, result, engineering lesson and interview takeaway.
- Do not add infrastructure or tools without a clear milestone-level need.
- Drift is evidence to investigate, not proof that model performance has degraded.
- Retraining does not imply promotion; a candidate must pass acceptance checks.
- Clearly distinguish measured results from assumptions and simulated outcomes.
