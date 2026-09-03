# Heart Failure Prediction — AWS Upgrade Summary

## Project Overview

This repository is a machine-learning and MLOps upgrade of a heart-failure outcome prediction project based on the UCI Heart Failure Clinical Records dataset. The latest reproducible notebook run evaluates five classification models on 299 patient records and selects **Random Forest** as the current deployment candidate.

The project has progressed from exploratory notebook analysis to a reusable Python training script, a FastAPI inference service, and a Docker container tested locally. AWS deployment is currently in progress.

> **Educational disclaimer:** This is an educational and research demonstration. It is not a medical device and must not be used for diagnosis, treatment, or clinical decision-making.

---

## Quick Statistics

| Metric | Latest Result |
|---|---|
| **Selected model** | Random Forest Classifier |
| **Test accuracy** | 83.33% |
| **Precision** | 80.00% |
| **Recall** | 63.16% |
| **F1-score** | 70.59% |
| **ROC-AUC** | 0.8909 |
| **Cross-validation** | 84.56% ± 6.63% (5-fold stratified CV on training data) |
| **Dataset size** | 299 patient records |
| **Input features** | 12 clinical and demographic variables |
| **Target** | `DEATH_EVENT` |
| **Total dataset columns** | 13: 12 inputs + 1 target |
| **Missing values** | 0 |
| **Class distribution** | 203 no-event (67.89%), 96 event (32.11%) |
| **Local ML API** | FastAPI `/health` and `/predict` endpoints tested |
| **Containerization** | Docker image built and tested locally |
| **AWS deployment** | In progress |

---

## Model Comparison

The latest notebook run compares five classification models using the same stratified 80/20 train-test split (`random_state=42`).

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 81.67% | 78.57% | 57.89% | 66.67% | 0.8588 |
| Decision Tree | 73.33% | 60.00% | 47.37% | 52.94% | 0.6637 |
| **Random Forest** | **83.33%** | **80.00%** | **63.16%** | **70.59%** | **0.8909** |
| K-Nearest Neighbors | 70.00% | 57.14% | 21.05% | 30.77% | 0.8004 |
| Support Vector Machine | 76.67% | 72.73% | 42.11% | 53.33% | 0.8447 |

Random Forest was selected because it achieved the best overall held-out test performance in this comparison, including the highest accuracy, recall, F1-score, and ROC-AUC.

---

## Cross-Validation Summary

Five-fold stratified cross-validation was performed on the training portion of the data.

| Model | Mean CV Accuracy | Standard Deviation |
|---|---:|---:|
| Logistic Regression | 83.27% | 4.34% |
| Decision Tree | 79.96% | 6.20% |
| **Random Forest** | **84.56%** | **6.63%** |
| K-Nearest Neighbors | 76.18% | 3.96% |
| Support Vector Machine | 80.37% | 7.70% |

Random Forest fold scores were 87.50%, 79.17%, 87.50%, 75.00%, and 93.62%. The variation across folds reinforces the need for further validation on larger, independent datasets.

---

## Current Project Components

### 1. `Heart_Failure_Prediction_Project.ipynb`

The main notebook contains:

- Dataset loading and data-quality checks.
- Exploratory data analysis and visualizations.
- Correlation analysis.
- Stratified train-test splitting.
- Training and evaluation of five classifiers.
- Model-comparison plots.
- Confusion-matrix and ROC-curve analysis.
- Five-fold stratified cross-validation.
- Random Forest feature-importance analysis.

### 2. `src/train.py`

The reusable training workflow:

- Loads the CSV dataset.
- Validates the expected feature columns.
- Creates a stratified 80/20 train-test split.
- Trains the selected Random Forest model.
- Saves a model artifact as `models/heart_failure_pipeline.joblib`.
- Writes metrics to `models/model_metrics.json`.

### 3. `api/main.py`

The FastAPI application provides:

| Endpoint | Purpose |
|---|---|
| `GET /` | Service message and educational disclaimer |
| `GET /health` | Health check and model-load status |
| `POST /predict` | Validated patient input and model prediction/probability |
| `GET /docs` | Interactive Swagger/OpenAPI documentation |

### 4. Docker

The API has been containerized and tested locally.

```powershell
docker build --no-cache -t heart-failure-api:1.0 .
docker run --rm -p 127.0.0.1:8000:8000 heart-failure-api:1.0
```

Local test URLs:

```text
http://localhost:8000/health
http://localhost:8000/docs
```

---

## Feature Insights

The latest Random Forest feature-importance analysis ranks the following variables highest:

| Rank | Feature | Importance |
|---:|---|---:|
| 1 | `time` | 0.3614 |
| 2 | `serum_creatinine` | 0.1541 |
| 3 | `ejection_fraction` | 0.1291 |
| 4 | `platelets` | 0.0768 |
| 5 | `age` | 0.0768 |
| 6 | `creatinine_phosphokinase` | 0.0745 |
| 7 | `serum_sodium` | 0.0662 |

Feature importance describes how the current Random Forest used variables for prediction. It is not evidence of clinical causality.

---

## Important Limitations

- The dataset has only 299 records, so estimates may vary with different splits.
- The positive class is smaller: 96 event records versus 203 no-event records.
- The current evaluation uses a single held-out test split plus five-fold cross-validation; external validation is still required.
- The `time` feature represents follow-up duration and is the highest-ranked Random Forest feature. It may not be known at an initial patient assessment, which can create potential temporal leakage in an early-risk-prediction use case.
- The current held-out test recall is 63.16%, meaning 7 of 19 event records were missed.
- Results may not generalize to other patient populations, hospitals, clinical settings, or data-collection processes.
- This work is not clinically validated and must not be used for diagnosis, treatment, or medical decisions.

---

## Project Status

| Area | Status |
|---|---|
| Dataset loading and EDA | Complete |
| Model comparison | Complete |
| Latest Random Forest selection | Complete |
| Reusable Python training workflow | Complete |
| FastAPI prediction API | Complete |
| Local Docker build and API test | Complete |
| Separate AWS-upgrade GitHub repository | Complete |
| AWS account/IAM setup | In progress |
| Amazon S3 artifact storage | Planned |
| Amazon ECR image registry | Planned |
| Amazon ECS Fargate deployment | Planned |
| CloudWatch logging | Planned |
| GitHub Actions CI/CD | Planned |

---

## Next Steps

### Near-term ML improvements

- Train and evaluate a leakage-safe model that excludes `time`.
- Tune Random Forest hyperparameters with stratified cross-validation.
- Compare ROC-AUC, PR-AUC, recall, F1-score, calibration, and accuracy.
- Evaluate class-weighting and threshold selection.
- Add calibration curves and Brier score.
- Perform subgroup and fairness checks when sufficient data is available.

### AWS/MLOps roadmap

- Create a private Amazon S3 bucket for model artifacts and metrics.
- Push the Docker image to Amazon ECR.
- Deploy the FastAPI service on Amazon ECS Fargate.
- Validate the live API endpoint and CloudWatch logs.
- Add GitHub Actions for automated testing and deployment after manual deployment works.

---

## How to Start

### Run the notebook

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
jupyter notebook Heart_Failure_Prediction_Project.ipynb
```

### Train model artifact

```powershell
.venv\Scripts\activate
python src\train.py
```

### Run FastAPI without Docker

```powershell
.venv\Scripts\activate
uvicorn api.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

### Run Docker container

```powershell
docker build --no-cache -t heart-failure-api:1.0 .
docker run --rm -p 127.0.0.1:8000:8000 heart-failure-api:1.0
```

---

## Version History

| Version | Date | Description |
|---|---|---|
| 1.0 | January 2026 | Original notebook-based project with earlier KNN-focused documentation |
| 2.0 | September 2026 | Latest notebook rerun selects Random Forest; FastAPI API and local Docker validation added |
| 2.1 | Planned | Amazon S3, ECR, ECS Fargate, and CloudWatch deployment |
| 2.2 | Planned | CI/CD automation, leakage-safe model experiment, calibration, and external validation |

---

**Last updated:** September 03, 2026  
**Current status:** Random Forest analysis, FastAPI API, and local Docker validation complete; AWS deployment in progress.
