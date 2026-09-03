# 🫀 Heart Failure Prediction — From Notebook to Cloud

<p align="center">
  <strong>A machine-learning and MLOps project that transforms clinical-record analysis into a containerized prediction API.</strong>
</p>

<p align="center">
  <a href="#-project-highlights">Highlights</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-results">Results</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-api-usage">API</a> •
  <a href="#-aws-roadmap">AWS Roadmap</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Model-Random%20Forest-2E8B57?style=for-the-badge" alt="Random Forest model">
  <img src="https://img.shields.io/badge/ROC--AUC-0.8909-5B5EA6?style=for-the-badge" alt="ROC AUC 0.8909">
  <img src="https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge" alt="FastAPI">
  <img src="https://img.shields.io/badge/Container-Docker-2496ED?style=for-the-badge" alt="Docker">
  <img src="https://img.shields.io/badge/Cloud-AWS%20in%20progress-FF9900?style=for-the-badge" alt="AWS in progress">
</p>

> **Project status:** ✅ ML analysis complete · ✅ FastAPI API complete · ✅ Docker tested locally · ⏳ AWS deployment in progress

---

## ✨ Why this project stands out

Most machine-learning projects stop at a notebook. This project goes further:

```text
Clinical records
     ↓
Exploratory analysis and model comparison
     ↓
Random Forest selection
     ↓
Reusable Python training workflow
     ↓
FastAPI prediction service
     ↓
Docker container tested locally
     ↓
AWS deployment roadmap: S3 → ECR → ECS Fargate → CloudWatch
```

It demonstrates the full path from **data exploration** to a deployable machine-learning service.

> ⚕️ **Educational use only:** This is a portfolio and research demonstration based on a public dataset. It is not a medical device and must not be used for diagnosis, treatment, or clinical decision-making.

---

## 🎯 Project highlights

| Area | What was built |
|---|---|
| Data | Analyzed 299 UCI Heart Failure Clinical Records with 12 input features and `DEATH_EVENT` target |
| Modeling | Compared Logistic Regression, Decision Tree, Random Forest, KNN, and SVM |
| Final candidate | Selected Random Forest based on the latest evaluation results |
| Evaluation | Reported accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix, and stratified cross-validation |
| Engineering | Refactored notebook workflow into reusable `src/train.py` code |
| API | Built FastAPI `/health` and `/predict` endpoints with input validation |
| Deployment | Containerized the API with Docker and tested it locally |
| Cloud roadmap | Preparing Amazon S3, ECR, ECS Fargate, and CloudWatch integration |

---

## 🧠 The problem

Heart failure is a serious clinical condition, and data-driven risk estimation is an important machine-learning research problem. This project explores whether routinely recorded clinical variables can be used to classify the `DEATH_EVENT` outcome in the **UCI Heart Failure Clinical Records** dataset.

The goals are to:

- Explore clinical-record data and check data quality.
- Compare multiple classification approaches fairly.
- Select a model using more than accuracy alone.
- Package the selected model behind a validated REST API.
- Run the API reliably inside a Docker container.
- Extend the local solution into an AWS-hosted MLOps portfolio project.

---

## 🏗️ Architecture

### Current local architecture

```text
┌──────────────────────────────────────────────────────────────────────┐
│                     Local Development Environment                    │
│                                                                      │
│  heart_failure_prediction.csv                                        │
│                │                                                     │
│                ▼                                                     │
│          src/train.py                                                │
│                │                                                     │
│                ├──► models/heart_failure_pipeline.joblib             │
│                └──► models/model_metrics.json                        │
│                               │                                      │
│                               ▼                                      │
│                     FastAPI — api/main.py                            │
│                  GET /health  •  POST /predict                       │
│                               │                                      │
│                               ▼                                      │
│                  Docker image: heart-failure-api                     │
│                               │                                      │
│                               ▼                                      │
│                     http://localhost:8000/docs                       │
└──────────────────────────────────────────────────────────────────────┘
```

### Planned AWS architecture

```text
GitHub repository
      │
      ▼
Docker image build
      │
      ▼
Amazon ECR ─────────────────────► Stores private Docker image
      │
      ▼
Amazon ECS Fargate ─────────────► Runs FastAPI container without managing EC2
      │
      ├──────────────────────────► Amazon CloudWatch logs
      │
      └──────────────────────────► Amazon S3 model artifacts and metrics
```

> AWS components are planned and must not be interpreted as already deployed. Each will be marked complete only after configuration, testing, and documentation.

---

## 📊 Results

### Final model selection

The latest reproducible notebook run evaluated five models using a stratified 80/20 train-test split (`random_state=42`). **Random Forest** was selected as the current deployment candidate because it performed best overall in the final held-out test comparison.

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 81.67% | 78.57% | 57.89% | 66.67% | 0.8588 |
| Decision Tree | 73.33% | 60.00% | 47.37% | 52.94% | 0.6637 |
| **Random Forest** | **83.33%** | **80.00%** | **63.16%** | **70.59%** | **0.8909** |
| K-Nearest Neighbors | 70.00% | 57.14% | 21.05% | 30.77% | 0.8004 |
| Support Vector Machine | 76.67% | 72.73% | 42.11% | 53.33% | 0.8447 |

### Random Forest cross-validation

Five-fold stratified cross-validation on the training data produced:

```text
Fold scores: 87.50% | 79.17% | 87.50% | 75.00% | 93.62%
Mean CV accuracy: 84.56% ± 6.63%
```

### Held-out test confusion matrix

```text
                         Predicted No Event   Predicted Event
Actual No Event                 38                  3
Actual Event                     7                 12
```

The model correctly classified 38 of 41 no-event records and 12 of 19 event records on this test split. Because 7 event records were missed, recall, threshold selection, calibration, and external validation remain important future improvements.

---

## 🔎 Dataset

| Property | Value |
|---|---|
| Source | UCI Heart Failure Clinical Records dataset |
| Patient records | 299 |
| Input features | 12 |
| Target | `DEATH_EVENT` |
| Missing values | 0 |
| No-event records | 203 (67.89%) |
| Event records | 96 (32.11%) |

### Input features

```text
age
anaemia
creatinine_phosphokinase
diabetes
ejection_fraction
high_blood_pressure
platelets
serum_creatinine
serum_sodium
sex
smoking
time
```

### Important limitation: `time`

The `time` column is the follow-up duration in days and is the highest-ranked Random Forest feature in this experiment. Because follow-up duration may not be known at an initial patient assessment, it can create potential **temporal leakage** for an early/baseline-risk use case.

The current model retains `time` to reproduce the analyzed experiment. A future version will train and compare a leakage-safe model without it:

```python
X = df.drop(columns=["DEATH_EVENT", "time"])
```

---

## 📁 Repository structure

```text
Heart-Failure-Prediction-AWS/
├── api/
│   └── main.py                         # FastAPI inference service
├── src/
│   └── train.py                        # Reusable Random Forest training workflow
├── models/                             # Generated local model artifacts; ignored by Git
│   ├── heart_failure_pipeline.joblib
│   └── model_metrics.json
├── tests/                              # Reserved for future automated tests
├── .github/workflows/                  # Reserved for future CI/CD workflow
├── Heart_Failure_Prediction_Project.ipynb
├── heart_failure_prediction.csv
├── DATA_DOCUMENTATION.md
├── INSIGHTS_AND_FUTURE_SCOPE.md
├── PROJECT_KEY_DESCRIPTION.md
├── PROJECT_STRUCTURE.md
├── PROJECT_SUMMARY.md
├── COMPLETION_STATUS.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── requirements.txt
```

---

## ⚡ Quick start

### 1. Clone repository

```bash
git clone https://github.com/manasiwaghmare18/Heart-Failure-Prediction-AWS.git
cd Heart-Failure-Prediction-AWS
```

### 2. Create Python environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install runtime dependencies

```bash
pip install -r requirements.txt
```

### 4. Train and save the model

```bash
python src/train.py
```

Expected generated artifacts:

```text
models/heart_failure_pipeline.joblib
models/model_metrics.json
```

### 5. Run the API locally

```bash
uvicorn api.main:app --reload
```

Open interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🐳 Run with Docker

Docker packages the API and the local model artifact into a consistent Linux container.

### Build image

```bash
docker build --no-cache -t heart-failure-api:1.0 .
```

### Run locally and privately

```bash
docker run --rm -p 127.0.0.1:8000:8000 heart-failure-api:1.0
```

Open:

```text
http://localhost:8000/health
http://localhost:8000/docs
```

The `127.0.0.1` binding makes this local test accessible only from the same computer. The `--rm` flag removes the temporary container when it stops; it does not remove your image or source files.

---

## 🔌 API usage

### Health check

```bash
curl http://127.0.0.1:8000/health
```

Example response:

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### Prediction request

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d "{\
    \"age\": 65,\
    \"anaemia\": 0,\
    \"creatinine_phosphokinase\": 320,\
    \"diabetes\": 1,\
    \"ejection_fraction\": 38,\
    \"high_blood_pressure\": 1,\
    \"platelets\": 263000,\
    \"serum_creatinine\": 1.46,\
    \"serum_sodium\": 142,\
    \"sex\": 0,\
    \"smoking\": 0,\
    \"time\": 130\
  }"
```

Example response shape:

```json
{
  "prediction": 0,
  "risk_label": "Lower predicted risk in this model",
  "heart_failure_probability": 0.1234,
  "disclaimer": "Educational ML demonstration only. This is not medical advice, a diagnosis, or a treatment recommendation."
}
```

A prediction represents the behavior of the trained model on this dataset. It is not a medical conclusion.

---

## ☁️ AWS roadmap

| AWS component | Purpose | Status |
|---|---|---|
| IAM | Secure deployment permissions and access control | In progress |
| Billing budget | Cost alert for student/learning usage | In progress |
| Amazon S3 | Private storage for model artifacts, metrics, and project outputs | Planned |
| Amazon ECR | Private registry for Docker image | Planned |
| Amazon ECS Fargate | Serverless hosting for FastAPI Docker container | Planned |
| Amazon CloudWatch | Container logs and troubleshooting | Planned |
| GitHub Actions | Automated testing and deployment | Planned |

### Target resume statement after verified deployment

> Deployed a containerized Random Forest prediction API using FastAPI and Docker on Amazon ECS Fargate; stored images in Amazon ECR, managed model artifacts in private Amazon S3, and monitored runtime logs with Amazon CloudWatch.

Use this statement only after every listed AWS service is configured and tested.

---

## 🧪 Improvement roadmap

### Modeling

- [ ] Retrain without `time` to create a leakage-safe baseline model.
- [ ] Tune Random Forest with stratified cross-validation.
- [ ] Compare ROC-AUC, PR-AUC, recall, F1-score, calibration, and accuracy.
- [ ] Test `class_weight="balanced"` and threshold tuning.
- [ ] Add calibration curve and Brier score.
- [ ] Add SHAP or permutation-importance explainability.

### Data and validation

- [ ] Validate on an independent dataset.
- [ ] Expand the dataset and assess demographic representation.
- [ ] Evaluate subgroup performance and fairness.
- [ ] Investigate data drift and monitoring requirements.

### Engineering and cloud

- [x] Create reusable training code.
- [x] Build FastAPI prediction endpoints.
- [x] Containerize and test locally with Docker.
- [ ] Upload image to Amazon ECR.
- [ ] Deploy service using Amazon ECS Fargate.
- [ ] Store model artifacts/metrics privately in Amazon S3.
- [ ] Add CloudWatch logging and alarms.
- [ ] Add CI/CD with GitHub Actions.

---

## 🛡️ Responsible-use notes

This project has important limitations:

- The dataset includes only 299 records.
- The target classes are imbalanced.
- The model was evaluated on a single held-out split plus cross-validation, not prospective clinical data.
- The follow-up `time` feature can create temporal leakage for early-risk use.
- Feature importance does not establish medical causality.
- The model has not undergone external validation, bias assessment, clinical validation, privacy review, or regulatory review.

**Do not use this project for healthcare decisions.** It is intended for learning data science, machine learning, API development, Docker, and cloud deployment practices.

---

## 📚 Documentation guide

| File | Read it for |
|---|---|
| `PROJECT_SUMMARY.md` | Short current project summary and verified metrics |
| `DATA_DOCUMENTATION.md` | Dataset variables, units, ranges, and quality notes |
| `INSIGHTS_AND_FUTURE_SCOPE.md` | Findings, limitations, MLOps roadmap, and research extensions |
| `PROJECT_STRUCTURE.md` | Repository layout, commands, and component relationships |
| `PROJECT_KEY_DESCRIPTION.md` | Resume-ready and concise project descriptions |
| `COMPLETION_STATUS.txt` | Completion checklist and deployment status |
| `Heart_Failure_Prediction_Project.ipynb` | Full exploratory analysis and model comparison |

---

## 👩‍💻 Author

**Manasi Waghmare**  
Data / Machine Learning Project Portfolio

---

## 📄 License

This project is provided under the repository's included license. Please review the `LICENSE` file before reuse or redistribution.
