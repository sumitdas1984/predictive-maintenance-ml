# Lightweight System Architecture

## 1. Purpose

Describe the two workflows in this project: offline model development and a controlled production simulation. This is a learning/portfolio system, not a live industrial deployment.

## 2. High-level architecture

```text
                    OFFLINE ML WORKFLOW
  UCI AI4I data
       |
       v
  Validate / preprocess
       |
       v
  Feature engineering / selection
       |
       v
  Train / evaluate / tune
       |
       v
  Select and version model
       |
       +------------------------------+
                                      |
                                      v
                           Model artifact / registry
                                      |
                                      v
                    PRODUCTION SIMULATION WORKFLOW
  Held-out simulation observations
       |
       v
  Batch production simulator
       |
       v
  FastAPI inference service <--- deployed model version
       |
       +----------------------+
       |                      |
       v                      v
  Prediction records     Simulated delayed labels
       |                      |
       v                      v
  Input/drift checks      Join eligible labels
       |                      |
       |                      v
       |                 Performance metrics
       |                      |
       +----------+-----------+
                  |
                  v
          Monitoring / trigger
                  |
          sufficient evidence
                  |
                  v
          Retraining workflow
                  |
                  v
        Candidate model evaluation
                  |
          acceptance checks pass?
             /          \
           yes           no
            |             |
            v             v
       Promote new     Keep current
       model version   model version
```

## 3. Workflow responsibilities

| Component | Responsibility |
|---|---|
| Offline data pipeline | Load, validate and prepare the source data without modifying the raw file |
| Training pipeline | Fit preprocessing and model steps using training data only |
| Evaluation | Compare candidates and select a threshold using validation data; preserve a final holdout |
| Model registry/versioning | Track model artifact, version and evaluation metadata |
| Production simulator | Send held-out observations in repeatable batches; optionally apply a documented drift scenario |
| FastAPI serving | Validate requests, load a specific model version and return prediction/probability |
| Prediction store | Persist observation reference, input values or approved feature payload, prediction, timestamp and model version |
| Label simulator | Reveal known labels after a configurable delay; labels are stored separately from predictions |
| Monitoring | Check feature distributions and calculate performance only for records with available labels |
| Retraining | Build a candidate using eligible labelled data and the defined historical training data |
| Promotion gate | Compare candidate against current model on a fixed evaluation set and promote only if predefined criteria pass |

## 4. Data and label flow

- **Training data:** used to fit preprocessing and candidate models.
- **Validation data:** used for model selection, tuning and threshold decisions.
- **Final holdout:** reserved for final unbiased evaluation; never used for fitting or retraining.
- **Simulation data:** held-out observations replayed in batches through the API.
- **Prediction record:** created at inference time and includes the model version.
- **Ground-truth record:** created later by the label simulator, after the configured delay.
- **Monitoring join:** joins predictions to labels only after labels become available.

The exact split strategy and whether records can be treated as independent must be examined during preprocessing. The dataset does not provide genuine machine time-series histories.

## 5. Monitoring and retraining policy

Monitor two different things:

1. **Input/data drift:** compare incoming feature distributions with a defined reference dataset. This can run before labels arrive.
2. **Model performance:** calculate precision, recall, F1 and other selected metrics only after ground-truth labels are available.

Drift alone does not automatically trigger model replacement. It can raise an alert or prompt investigation. Retraining requires sufficient eligible labelled observations and a configured trigger/approval policy.

A candidate model is promoted only after it passes predefined checks on data not used to train or tune that candidate. If it fails, retain the current model.

## 6. Simulation limitations

- AI4I is synthetic and static; it is not a chronological stream of real machine telemetry.
- Batch replay simulates arrival, not actual sensor connectivity or production throughput.
- Delayed labels are simulated from labels already present in the dataset; this demonstrates label-latency handling, not a real operational feedback process.
- Drift injection is a controlled test scenario, not observed real-world drift.
- Results demonstrate the implementation of engineering workflows, not proven factory savings or real-world generalization.

## 7. Implementation guardrails

- Keep raw data immutable.
- Keep train/validation/holdout/simulation partitions separate.
- Exclude failure-mode indicators (`TWF`, `HDF`, `PWF`, `OSF`, `RNF`) from predictors of `Machine failure`.
- Record model version with every prediction.
- Make simulation batch size, label delay and drift scenario configurable.
- Make retraining and promotion reproducible and testable.
- Add infrastructure only when a milestone requires it.
