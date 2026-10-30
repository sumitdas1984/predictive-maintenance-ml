# Business Understanding

> Status: Working document — complete this during Milestone 1. Do not start modelling until the decision and evaluation approach are clear.

## 1. Business problem
Unexpected machine failures can cause unplanned downtime, maintenance expense and production disruption. The proposed system estimates failure risk from operating measurements to help maintenance teams prioritize inspection.

## 2. Intended user and decision
- **Proposed user:** maintenance planner or operations engineer.
- **Decision to support:** which machine should be inspected or scheduled for preventive maintenance?
- **Action after prediction:** review high-risk machines; the model does not autonomously shut down equipment or schedule maintenance.

## 3. ML formulation
- **Task:** supervised binary classification.
- **Prediction unit:** one machine observation/operating snapshot in the dataset.
- **Target:** `Machine failure` (0 = no failure, 1 = failure).
- **Inputs:** available operating measurements and eligible machine attributes.
- **Prediction output:** failure probability plus a decision at a selected threshold.

## 4. Business costs and trade-offs
- False negative: a failure is missed, potentially leading to unplanned downtime.
- False positive: maintenance attention is spent on a machine that would not fail in the relevant prediction window.
- True positive: a risky machine is correctly flagged.
- True negative: a non-failing machine is correctly not flagged.

The relative costs are not provided by the dataset. They must be treated as assumptions until validated with an operations stakeholder. Do not invent financial savings.

## 5. Success measures

### Business measures (to define)
- Cost of missed failures.
- Cost of unnecessary inspections/interventions.
- Downtime avoided (not measurable from this synthetic dataset alone).
- Maintenance-team alert capacity per shift/day.

### ML measures (candidate set)
- Recall for the failure class.
- Precision for the failure class.
- F1 score.
- Precision-recall AUC (especially relevant if failures are rare).
- Confusion matrix at the chosen operating threshold.
- ROC-AUC as a secondary ranking metric.

Accuracy alone is insufficient when the positive class is rare.

## 6. Data and modelling assumptions to validate
- Dataset is synthetic; results may not generalize to real equipment.
- Each row represents an observation, not necessarily an independent machine/time sequence.
- The dataset does not establish a reliable real-world prediction horizon or maintenance intervention window.
- Failure-mode indicator columns are labels derived from failure information and must not be used as predictors for `Machine failure`.
- Any split strategy must reflect the intended deployment setting and available identifiers/time structure.

## 7. Open decisions
- What lead time should a prediction provide in a real deployment?
- What is the acceptable number of false alerts for the maintenance team?
- What are the relative costs of false negatives and false positives?
- Is the objective to maximize recall subject to an alert-capacity/precision constraint?

## 8. Milestone 1 exit checklist
- [ ] State the business decision in one sentence.
- [ ] Confirm prediction unit and target.
- [ ] Explain false-positive and false-negative consequences.
- [ ] Select primary and supporting ML metrics with rationale.
- [ ] List assumptions and dataset limitations.
- [ ] Define what this project can and cannot claim.
