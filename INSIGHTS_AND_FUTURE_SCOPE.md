# Insights and Future Scope — Heart Failure Prediction Project

## Executive Summary

This document summarizes insights from the latest reproducible analysis of the Heart Failure Clinical Records dataset and outlines the future roadmap for the project.

The latest notebook run evaluates five classification algorithms using a stratified 80/20 train-test split and five-fold stratified cross-validation. **Random Forest** was selected as the current model because it achieved the strongest overall held-out test performance and the highest mean cross-validation accuracy among the evaluated models.

> **Educational disclaimer:** This project is an educational and research machine-learning demonstration. It is not a medical device and must not be used for diagnosis, treatment, or clinical decision-making.

---

## Part 1: Key Insights

## 1. Model Performance

### 1.1 Random Forest Selection

**Finding:** Random Forest was the best-performing model in the final rerun of the analysis.

**Held-out test performance:**

| Metric | Random Forest Result |
|---|---:|
| Accuracy | 83.33% |
| Precision | 80.00% |
| Recall | 63.16% |
| F1-score | 70.59% |
| ROC-AUC | 0.8909 |

The test set contains 60 records: 41 no-event records and 19 event records.

**Confusion matrix:**

| Actual / Predicted | No Event | Event |
|---|---:|---:|
| No Event | 38 | 3 |
| Event | 7 | 12 |

This means the model correctly identified 12 of 19 event records and correctly identified 38 of 41 no-event records. It produced 3 false positives and 7 false negatives.

### 1.2 Why Random Forest Was Selected

Random Forest was selected because it led the latest comparison on multiple metrics:

- Highest held-out test accuracy: 83.33%.
- Highest ROC-AUC: 0.8909.
- Highest recall among the evaluated models: 63.16%.
- Highest F1-score among the evaluated models: 70.59%.
- Highest mean five-fold cross-validation accuracy: 84.56%.

Tree-based ensemble models can capture nonlinear relationships and interactions between clinical variables without requiring feature scaling for the model itself.

### 1.3 Model Comparison

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 81.67% | 78.57% | 57.89% | 66.67% | 0.8588 |
| Decision Tree | 73.33% | 60.00% | 47.37% | 52.94% | 0.6637 |
| **Random Forest** | **83.33%** | **80.00%** | **63.16%** | **70.59%** | **0.8909** |
| K-Nearest Neighbors | 70.00% | 57.14% | 21.05% | 30.77% | 0.8004 |
| Support Vector Machine | 76.67% | 72.73% | 42.11% | 53.33% | 0.8447 |

### 1.4 Cross-Validation Results

Five-fold stratified cross-validation was performed on the training data.

| Model | Mean CV Accuracy | Standard Deviation |
|---|---:|---:|
| Logistic Regression | 83.27% | 4.34% |
| Decision Tree | 79.96% | 6.20% |
| **Random Forest** | **84.56%** | **6.63%** |
| K-Nearest Neighbors | 76.18% | 3.96% |
| Support Vector Machine | 80.37% | 7.70% |

Random Forest showed the highest mean accuracy across the five folds. Its fold scores were 87.50%, 79.17%, 87.50%, 75.00%, and 93.62%. The variation across folds also shows why this small dataset requires careful reporting and external validation.

---

## 2. Data Insights

### 2.1 Dataset Overview

| Characteristic | Value |
|---|---:|
| Dataset | UCI Heart Failure Clinical Records |
| Patient records | 299 |
| Input features | 12 |
| Target variable | `DEATH_EVENT` |
| Missing values | 0 |
| No-event records | 203 (67.89%) |
| Event records | 96 (32.11%) |

The target is moderately imbalanced, so accuracy alone is not sufficient. Precision, recall, F1-score, ROC-AUC, confusion matrices, and stratified validation are important for interpreting model performance.

### 2.2 Correlation Patterns

In the latest analysis, the strongest correlations with `DEATH_EVENT` were:

| Feature | Correlation with `DEATH_EVENT` |
|---|---:|
| `time` | -0.5270 |
| `serum_creatinine` | 0.2943 |
| `ejection_fraction` | -0.2686 |
| `age` | 0.2537 |
| `serum_sodium` | -0.1952 |

These values describe association in this dataset; they do not establish causality.

### 2.3 Random Forest Feature Importance

The latest Random Forest feature-importance results are:

| Rank | Feature | Importance |
|---:|---|---:|
| 1 | `time` | 0.3614 |
| 2 | `serum_creatinine` | 0.1541 |
| 3 | `ejection_fraction` | 0.1291 |
| 4 | `platelets` | 0.0768 |
| 5 | `age` | 0.0768 |
| 6 | `creatinine_phosphokinase` | 0.0745 |
| 7 | `serum_sodium` | 0.0662 |

Feature importance is specific to this trained model and dataset. It indicates how useful each feature was for splits in the forest; it does not imply that a feature is a direct medical cause of the outcome.

### 2.4 Clinical Interpretation

The analysis suggests that serum creatinine, ejection fraction, age, serum sodium, and platelets contribute to prediction in this dataset.

- **Serum creatinine** is associated with kidney function and appears as an important model feature.
- **Ejection fraction** reflects cardiac pumping performance and shows an inverse association with the outcome.
- **Age** is associated with increased risk in the observed data.
- **Serum sodium** may provide additional prognostic information.
- **Platelet count** contributes to the Random Forest model but must be interpreted cautiously.

These observations are exploratory and should not be interpreted as clinical recommendations.

---

## 3. Critical Limitation: Follow-Up Time

The feature `time` is the most influential variable in the current Random Forest model. However, it represents the number of follow-up days for a patient.

This is important because follow-up duration may not be known at the time an initial risk prediction is required. Therefore, using `time` in a baseline or early-risk prediction model may introduce **temporal data leakage**.

### Recommended Next Experiment

Train and compare a second Random Forest model without the `time` feature:

```python
X = df.drop(columns=["DEATH_EVENT", "time"])
```

Then compare:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Calibration
- Cross-validation performance

The model without `time` may have lower apparent performance, but it may better represent the information available at an initial clinical assessment.

---

## 4. Model Limitations

- The dataset contains only 299 records, which limits statistical confidence.
- The evaluation uses one held-out 80/20 test split; performance can vary by split.
- The dataset is moderately imbalanced: 67.89% no-event records and 32.11% event records.
- Random Forest recall is 63.16%, meaning 7 of 19 event records were missed in the held-out test set.
- The data represents one public dataset and requires external validation on independent populations.
- The dataset may not represent all demographic groups, institutions, clinical settings, or disease subtypes.
- Feature importance does not establish clinical causality.
- This project is not clinically validated and must not be used for medical decisions.

---

## Part 2: Future Enhancement Roadmap

## 1. Data Improvements

### 1.1 External Validation

Evaluate the approach on an independent dataset before making stronger generalization claims.

Potential validation goals:

- Use data from different healthcare settings.
- Assess performance across geographic and demographic groups.
- Compare outcomes on external cohorts.
- Evaluate robustness to missing values and measurement variation.

### 1.2 Dataset Expansion

A larger dataset would improve statistical power and enable more reliable subgroup analysis.

| Stage | Target Records | Goal |
|---|---:|---|
| Initial expansion | 500–1,000 | More stable model comparison |
| Intermediate expansion | 2,000+ | Subgroup and fairness analysis |
| Advanced expansion | 5,000+ | More robust external validation and temporal analysis |

### 1.3 Additional Features

Potential future features include:

- BNP or NT-proBNP.
- Troponin.
- Hemoglobin and renal function trends.
- Body mass index.
- Medication history and adherence.
- NYHA functional class.
- Longitudinal ejection-fraction measurements.
- Additional echocardiography and imaging features.

---

## 2. Modeling Improvements

### 2.1 Hyperparameter Tuning

Perform systematic tuning using `RandomizedSearchCV` or `GridSearchCV` with stratified cross-validation.

Possible Random Forest parameters:

```text
n_estimators
max_depth
min_samples_split
min_samples_leaf
max_features
class_weight
```

Selection should use a clearly defined metric. Because missed positive cases can matter in this type of task, compare ROC-AUC, recall, F1-score, PR-AUC, and calibration—not accuracy alone.

### 2.2 Leakage-Safe Baseline Model

Create a second model excluding `time`.

This should become the preferred model if the intended use case is risk estimation at the initial patient assessment.

### 2.3 Class-Imbalance Methods

Evaluate:

- `class_weight="balanced"` for tree-based models.
- Threshold adjustment based on desired recall/precision trade-offs.
- SMOTE only within training folds to prevent evaluation leakage.
- Precision-recall curves and PR-AUC.
- Cost-sensitive evaluation, where false negatives may have a higher cost than false positives.

### 2.4 Calibration

Prediction probabilities should be checked before they are presented as risk estimates.

Potential methods:

- Calibration curves.
- Brier score.
- `CalibratedClassifierCV`.
- Platt scaling or isotonic calibration when appropriate.

### 2.5 Explainability

Use appropriate explainability methods for the final Random Forest model:

- Permutation importance.
- SHAP TreeExplainer.
- Partial dependence plots.
- Individual conditional expectation plots.

Explainability must be presented as model behavior, not clinical causality.

---

## 3. API and Deployment Roadmap

### 3.1 Completed Local Engineering Work

- Random Forest training script created.
- Trained pipeline serialized with `joblib`.
- FastAPI service created.
- `/health` endpoint created for service validation.
- `/predict` endpoint created for structured prediction requests.
- Docker image built and tested locally.
- Local API tested using FastAPI Swagger documentation.

### 3.2 AWS Deployment: In Progress

The intended AWS architecture is:

```text
GitHub repository
      |
      v
Docker build
      |
      v
Amazon ECR
      |
      v
Amazon ECS Fargate
      |
      v
FastAPI prediction API
      |
      +--> Amazon CloudWatch logs
      +--> Amazon S3 model artifacts and evaluation outputs
```

Planned AWS components:

- **Amazon S3:** private storage for model artifacts, metrics, and project outputs.
- **Amazon ECR:** private container-image registry.
- **Amazon ECS Fargate:** serverless runtime for the FastAPI container.
- **Amazon CloudWatch:** application logs and deployment troubleshooting.
- **IAM:** least-privilege permissions for users and ECS tasks.
- **GitHub Actions:** optional CI/CD workflow after manual deployment is validated.

> AWS deployment must not be described as completed until the image has been pushed to ECR, the ECS service is running, the endpoint is tested, and logs are verified.

### 3.3 Production Considerations

Before any real deployment handling sensitive healthcare data, the system would require:

- Strong authentication and authorization.
- HTTPS/TLS.
- Encryption in transit and at rest.
- Audit logging.
- Input validation and rate limiting.
- Data-retention controls.
- Formal privacy, security, and regulatory review.
- Clinical validation and monitoring for model drift and bias.

---

## 4. Evaluation and Fairness

### 4.1 Subgroup Evaluation

Evaluate performance separately by:

- Age groups.
- Sex.
- Smoking status.
- Diabetes status.
- Ejection-fraction categories.
- Serum-creatinine ranges.

Measure accuracy, recall, false-positive rate, false-negative rate, and calibration across each group.

### 4.2 Fairness Assessment

Potential checks include:

- Whether false-negative rates differ across groups.
- Whether false-positive rates differ across groups.
- Whether probability calibration differs by subgroup.
- Whether the training data under-represents meaningful patient populations.

The current dataset is small, so subgroup results may be unstable and should be interpreted cautiously.

---

## 5. Future Research Directions

Potential advanced extensions:

- Survival-analysis methods for time-to-event prediction.
- Longitudinal/time-series models with repeated patient measurements.
- External validation against independent cohorts.
- Comparison with established clinical risk scores.
- Ensemble models after careful validation.
- Uncertainty estimation and calibrated risk scoring.
- Data-drift and model-performance monitoring after deployment.

---

## Part 3: Project Roadmap

| Phase | Status | Deliverables |
|---|---|---|
| Data analysis and EDA | Complete | Notebook, visualizations, feature exploration |
| Model comparison | Complete | Five-model evaluation, Random Forest selection |
| Local ML engineering | Complete | Training script, model serialization, FastAPI API |
| Dockerization | Complete | Dockerfile and successful local API test |
| AWS foundation | In progress | AWS account security, budget, IAM configuration |
| Cloud deployment | Planned | S3, ECR, ECS Fargate, CloudWatch |
| MLOps automation | Planned | GitHub Actions CI/CD |
| Validation and enhancement | Planned | No-time model, calibration, fairness, external validation |

---

## Conclusion

The latest reproducible analysis selected **Random Forest** as the current deployment candidate. On the held-out test split, it achieved 83.33% accuracy, 80.00% precision, 63.16% recall, 70.59% F1-score, and 0.8909 ROC-AUC. Five-fold cross-validation produced a mean accuracy of 84.56% with a 6.63% standard deviation.

The project has progressed from notebook-based analysis to a locally tested FastAPI and Docker implementation. The next technical objective is a documented AWS deployment using S3, ECR, ECS Fargate, and CloudWatch.

The model should be treated as an educational demonstration. Its small dataset, class imbalance, single-source evaluation, and possible temporal leakage from the `time` feature mean it is not appropriate for clinical use without substantial external validation, governance, and regulatory work.
