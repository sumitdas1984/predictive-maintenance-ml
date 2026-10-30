# Business Understanding

> Status: Completed — Milestone

## 1. Business Problem
Unexpected machine failures can cause unplanned downtime, increased maintenance expenses, and production disruptions.
The proposed system analyzes machine operating measurements and classifies each observation as normal or failure-associated. It also generates a probability score indicating the likelihood that the observation belongs to the failure-associated class.
This helps maintenance teams flag potentially problematic conditions and prioritize inspections.

## 2. Stakeholders and Business Decisions
- **Primary stakeholder:** Maintenance team.
- **Supporting stakeholder:** Manufacturing operations manager.
- **Model output:** Classification and probability score.
- **Business decision:** Which machine conditions should be investigated first?
- **Action after prediction:** Review observations with higher failure-classification scores.

## 3. ML Problem Formulation
- **Task:** supervised binary classification.
- **Prediction unit:** one machine observation/operating snapshot in the dataset.
- **Target:** `Machine failure` (0 = no failure, 1 = failure).
- **Inputs:** available operating measurements and eligible machine attributes.
- **Prediction output:** predicted class and Estimated probability of belonging to the failure-associated class.

## 4. Features and Target Variable
- Input features (X): Type, Air temperature, Process temperature, Rotational speed, Torque, Tool wear
- Target (y): Machine failure
- Exclude: TWF, HDF, PWF, OSF, RNF

- UDI and Product ID (not useful as predictive measurements for this formulation).

## 5. Business Success Criteria
- Failure detection: How many failure-associated observations are identified?
- False alarms: How many non-failure observations are incorrectly flagged?
- Inspection efficiency: Whether the maintenance team can prioritize the most concerning observations.
- Mention that measurable targets are still to be established.

## 6. ML Evaluation Metrics
- Recall for the failure class.
- Precision for the failure class.
- F1 score.
- Precision-recall AUC (especially relevant if failures are rare).
- Confusion matrix at the chosen operating threshold.
- Accuracy: Will be reported, but as the secondary metric.
- Select the classification threshold based on the precision-recall trade-off and the relative business costs of false positives and false negatives.

## 7. Assumptions and Limitations
| Assumption               | Explanation                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- |
| Data quality             | Sensor measurements are sufficiently accurate and reliable.                            |
| Representative data      | Training data represents the operating conditions where the model will be used.        |
| Label correctness        | `Machine failure` labels are correctly recorded.                                       |
| Feature availability     | All six selected input features are available when making predictions.                 |
| Consistent relationships | Relationships between sensor measurements and failure labels remain reasonably stable. |

### Dataset limitations
Our AI4I dataset has some important limitations:
- Synthetic data: It does not represent actual industrial operating conditions perfectly.
- No timestamps: We cannot establish chronological machine behaviour.
- No future failure labels: We cannot predict whether a machine will fail within the next 24 hours or another future horizon.
- Limited observations: It contains 10,000 records, which may not capture all failure scenarios.
- Class imbalance: Failure observations are much less frequent than normal observations.

### Business implications
Our model can demonstrate:
- Binary failure classification.
- Failure detection and inspection prioritization.
- ML model evaluation and deployment.
- Production simulation, monitoring and retraining workflows.

It cannot establish:
- Actual future failure prediction.
- Real-world maintenance cost savings.
- Production-grade industrial performance.
