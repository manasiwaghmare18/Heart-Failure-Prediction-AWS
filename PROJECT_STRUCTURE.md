# Project Structure Documentation — Heart Failure Prediction AWS Upgrade

## Project Purpose

This repository is the cloud and ML-engineering upgrade of a notebook-based heart-failure prediction analysis. It contains the original exploratory analysis, a reusable Random Forest training workflow, a FastAPI prediction service, Docker configuration, and the foundation for AWS deployment.

> **Status:** Local ML API and Docker validation complete. AWS deployment is in progress.

---

## Current Directory Structure

```text
Heart-Failure-Prediction-AWS/
│
├── README.md
│   └── Main project overview, setup instructions, model results, and AWS status
│
├── PROJECT_KEY_DESCRIPTION.md
│   └── Resume-ready, academic, and concise project descriptions
│
├── PROJECT_STRUCTURE.md
│   └── This guide to the repository organization
│
├── PROJECT_SUMMARY.md
│   └── High-level project summary and latest validated results
│
├── COMPLETION_STATUS.txt
│   └── Project completion checklist, current model metrics, and AWS roadmap
│
├── DATA_DOCUMENTATION.md
│   └── Dataset dictionary, variable definitions, quality notes, and limitations
│
├── INSIGHTS_AND_FUTURE_SCOPE.md
│   └── Model findings, limitations, deployment roadmap, and future improvements
│
├── Heart_Failure_Prediction_Project.ipynb
│   └── Main notebook: EDA, preprocessing, five-model comparison, evaluation,
│       feature importance, and Random Forest selection
│
├── heart_failure_prediction.csv
│   └── UCI Heart Failure Clinical Records dataset:
│       299 rows, 12 input features, and DEATH_EVENT target
│
├── requirements.txt
│   └── Minimal Python runtime dependencies for FastAPI and Docker deployment
│
├── package.json
│   └── Existing Next.js/React dependency configuration; frontend source code is
│       not currently part of this repository structure
│
├── .gitignore
│   └── Prevents secrets, virtual environment files, and generated artifacts
│       from being committed to GitHub
│
├── .dockerignore
│   └── Excludes unnecessary local files from the Docker build context
│
├── Dockerfile
│   └── Builds the Linux Docker image for the FastAPI inference service
│
├── api/
│   └── main.py
│       └── FastAPI service exposing:
│           -  GET /
│           -  GET /health
│           -  POST /predict
│
├── src/
│   └── train.py
│       └── Reusable training script that:
│           -  reads the CSV dataset
│           -  performs a stratified train-test split
│           -  trains the selected Random Forest model
│           -  saves the serialized model artifact
│           -  writes model evaluation metrics
│
├── models/
│   ├── heart_failure_pipeline.joblib
│   │   └── Generated serialized Random Forest pipeline used by the API locally
│   └── model_metrics.json
│       └── Generated model metadata and evaluation metrics
│
├── tests/
│   └── Reserved for future automated unit and API tests
│
└── .github/
    └── workflows/
        └── Reserved for future GitHub Actions CI/CD workflows
```

---

## Important Git Tracking Note

The `models/` directory is generated locally after running:

```powershell
python src\train.py
```

The generated files are normally excluded by `.gitignore`:

```text
models/*.joblib
models/*.pkl
models/*.json
```

This protects generated model artifacts from being accidentally committed. During the first Docker deployment stage, the Dockerfile copies the local `models/` folder into the container image.

In the future AWS version, the model artifact can be stored in a private Amazon S3 bucket and loaded securely by the ECS task at startup.

---

## Core Files

### 1. `README.md`

**Purpose:** Primary repository entry point.

**Should contain:**

- Problem statement and educational disclaimer.
- Dataset overview.
- Final Random Forest model results.
- Local installation instructions.
- FastAPI/Docker usage instructions.
- AWS deployment status.
- Architecture overview.
- Project limitations.

**Read first:** Yes.

---

### 2. `Heart_Failure_Prediction_Project.ipynb`

**Purpose:** Main data-analysis notebook.

**Key sections:**

1. Library imports and visualization setup.
2. Dataset loading and data-quality checks.
3. Exploratory data analysis.
4. Correlation and feature-vs-target analysis.
5. Stratified train-test split.
6. Scaling for models that require it.
7. Training and evaluation of five classifiers:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - K-Nearest Neighbors
   - Support Vector Machine
8. Model comparison using accuracy, precision, recall, F1-score, and ROC-AUC.
9. Five-fold stratified cross-validation.
10. Decision Tree and Random Forest feature-importance analysis.
11. Final Random Forest findings and limitations.

**Latest selected model:** Random Forest.

**Latest held-out test metrics:**

| Metric | Result |
|---|---:|
| Accuracy | 83.33% |
| Precision | 80.00% |
| Recall | 63.16% |
| F1-score | 70.59% |
| ROC-AUC | 0.8909 |

**How to run:**

```powershell
jupyter notebook Heart_Failure_Prediction_Project.ipynb
```

**Important limitation:** The `time` column represents follow-up duration. It is retained to reproduce the current experiment but may cause temporal leakage for an initial-risk prediction use case.

---

### 3. `heart_failure_prediction.csv`

**Purpose:** Source dataset for notebook analysis and training script.

**Dataset summary:**

| Property | Value |
|---|---|
| Records | 299 |
| Input columns | 12 |
| Target | `DEATH_EVENT` |
| Total columns | 13 |
| Missing values | 0 |
| No-event class | 203 records, 67.89% |
| Event class | 96 records, 32.11% |

**Input columns:**

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

**Target column:**

```text
DEATH_EVENT
```

---

### 4. `src/train.py`

**Purpose:** Reusable, non-notebook training workflow.

**Responsibilities:**

- Loads `heart_failure_prediction.csv`.
- Validates required input and target columns.
- Creates a stratified 80/20 train-test split.
- Trains the selected Random Forest model.
- Evaluates accuracy, precision, recall, F1-score, and ROC-AUC.
- Saves the trained model as `models/heart_failure_pipeline.joblib`.
- Saves metrics as `models/model_metrics.json`.

**Run command:**

```powershell
python src\train.py
```

**Run this before:**

- Starting the FastAPI application.
- Building Docker after a training/model change.
- Uploading a refreshed model artifact to S3 later.

---

### 5. `api/main.py`

**Purpose:** FastAPI inference service.

**Endpoints:**

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Confirms the API is running and shows a disclaimer |
| GET | `/health` | Verifies application health and model loading |
| POST | `/predict` | Validates patient inputs and returns prediction/probability output |
| GET | `/docs` | Automatically generated Swagger/OpenAPI documentation |

**Run locally without Docker:**

```powershell
uvicorn api.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

---

### 6. `Dockerfile`

**Purpose:** Defines how Docker builds the Linux image for the FastAPI service.

**Build command:**

```powershell
docker build --no-cache -t heart-failure-api:1.0 .
```

**Run locally with private localhost binding:**

```powershell
docker run --rm -p 127.0.0.1:8000:8000 heart-failure-api:1.0
```

**Test endpoints:**

```text
http://localhost:8000/health
http://localhost:8000/docs
```

The `--rm` flag deletes the temporary container after it is stopped. It does not delete the Docker image, source code, or saved model artifact.

---

### 7. `requirements.txt`

**Purpose:** Contains minimal packages needed by the deployed API container.

**Expected runtime dependencies:**

```text
fastapi
uvicorn[standard]
pydantic
pandas
scikit-learn
joblib
```

This is intentionally different from notebook/development dependencies. Jupyter, visualization libraries, test tools, and Windows-specific packages should not be included in the API Docker image unless required.

---

### 8. `.gitignore`

**Purpose:** Prevents local-only and sensitive files from being pushed to GitHub.

**Examples of excluded files:**

```text
.venv/
.env
__pycache__/
models/*.joblib
models/*.pkl
models/*.json
```

Never commit AWS access keys, secret keys, `.env` files, or model artifacts containing sensitive information.

---

### 9. `.dockerignore`

**Purpose:** Keeps unnecessary local files out of the Docker build context.

**Examples:**

```text
.venv/
.git/
.github/
.ipynb_checkpoints/
node_modules/
tests/
.env
```

This makes image builds faster and keeps images smaller.

---

## Generated Local Artifacts

The following files are produced after the training script runs:

```text
models/
├── heart_failure_pipeline.joblib
└── model_metrics.json
```

They may exist on your local computer but are intentionally ignored by Git.

| Artifact | Purpose |
|---|---|
| `heart_failure_pipeline.joblib` | Serialized selected Random Forest model/pipeline for inference |
| `model_metrics.json` | Saved model name, input columns, data split size, and evaluation metrics |

---

## Dependency Relationships

```text
heart_failure_prediction.csv
        │
        ├──> Heart_Failure_Prediction_Project.ipynb
        │       └──> EDA, visualizations, comparative results
        │
        └──> src/train.py
                │
                ├──> models/heart_failure_pipeline.joblib
                └──> models/model_metrics.json
                         │
                         v
                    api/main.py
                         │
                         v
                    Dockerfile
                         │
                         v
               heart-failure-api:1.0 Docker image
                         │
                         v
            Future: Amazon ECR → ECS Fargate → CloudWatch
```

---

## Current and Planned AWS Architecture

```text
Current Local Workflow
----------------------
CSV dataset → train.py → model artifact → FastAPI → Docker → localhost test

Planned AWS Workflow
--------------------
GitHub source code
        │
        v
Docker image build
        │
        v
Amazon ECR
        │
        v
Amazon ECS Fargate
        │
        v
FastAPI prediction service
        │
        ├──> Amazon CloudWatch logs
        └──> Amazon S3 model artifacts and metrics
```

AWS deployment is currently in progress. Do not state that S3, ECR, ECS Fargate, CloudWatch, or GitHub Actions are completed until each has been configured, tested, and documented.

---

## Quick Start

### Run the notebook

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
jupyter notebook Heart_Failure_Prediction_Project.ipynb
```

### Train the API model

```powershell
.venv\Scripts\activate
python src\train.py
```

### Run FastAPI locally

```powershell
.venv\Scripts\activate
uvicorn api.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

### Build and run Docker locally

```powershell
docker build --no-cache -t heart-failure-api:1.0 .
docker run --rm -p 127.0.0.1:8000:8000 heart-failure-api:1.0
```

Open:

```text
http://localhost:8000/health
```

---

## Version History

| Version | Date | Description |
|---|---|---|

| 1.0 | September 2026 | Latest reproducible analysis selects Random Forest; added reusable training script, FastAPI API, and locally tested Docker container |
| 1.1 | Planned | AWS S3, ECR, ECS Fargate, and CloudWatch deployment |
| 1.2 | Planned | GitHub Actions CI/CD and expanded model validation |

---

**Last updated:** September 03, 2026  
**Current status:** Random Forest analysis, FastAPI API, and local Docker validation complete; AWS deployment in progress.
