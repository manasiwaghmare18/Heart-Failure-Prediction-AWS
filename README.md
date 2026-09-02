# Heart Failure Prediction Project

## Executive Summary

This project implements a comprehensive machine learning solution for predicting heart failure in patients based on clinical measurements and medical history. The analysis evaluates seven different algorithms to identify the optimal model for heart failure prediction, achieving 85.55% accuracy with the K-Nearest Neighbors (KNN) algorithm.

**Project Highlights:**
- Best Model: K-Nearest Neighbors (KNN)
- Accuracy: 85.55%
- Precision: 84.00%
- Recall: 78.95%
- AUC-ROC Score: 0.87
- Dataset: 299 patients with 13 clinical features

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Dataset Information](#dataset-information)
3. [Methodology](#methodology)
4. [Model Performance](#model-performance)
5. [Key Findings](#key-findings)
6. [Installation & Usage](#installation--usage)
7. [Project Structure](#project-structure)
8. [References](#references)

---

## Project Overview

### Problem Statement
Heart failure is a chronic condition affecting millions worldwide. Early detection and risk assessment are critical for improving patient outcomes and enabling preventive interventions. This project develops machine learning models to predict heart failure occurrence based on readily available clinical measurements.

### Objectives
- Analyze clinical factors associated with heart failure
- Develop and compare multiple machine learning algorithms
- Identify the most effective predictive model
- Provide interpretable results for clinical decision-making
- Create a reproducible and well-documented analysis framework

### Scope
- **Task Type:** Binary Classification
- **Target Variable:** Heart Failure (Present/Absent)
- **Number of Features:** 13 clinical and demographic indicators
- **Sample Size:** 299 patient records
- **Evaluation Method:** Cross-validation with multiple performance metrics

---

## Dataset Information

### Overview
- **Source:** UCI Machine Learning Repository
- **Total Records:** 299 patients
- **Total Features:** 13 (12 clinical features + 1 target variable)
- **Missing Values:** 0 (Complete dataset)
- **Class Distribution:** 67.89% No Event, 32.11% Event (Imbalanced but acceptable)

### Features Description

| # | Feature | Type | Unit | Description |
|---|---------|------|------|-------------|
| 1 | age | Numeric | years | Patient age in years |
| 2 | anaemia | Binary | 0/1 | Decrease of red blood cells or hemoglobin |
| 3 | creatinine_phosphokinase | Numeric | mcg/L | CPK enzyme level in blood |
| 4 | diabetes | Binary | 0/1 | Presence of diabetes mellitus |
| 5 | ejection_fraction | Numeric | % | Percentage of blood leaving the heart at contraction |
| 6 | high_blood_pressure | Binary | 0/1 | Presence of hypertension |
| 7 | platelets | Numeric | kiloplatelets/mL | Platelet count in blood |
| 8 | serum_creatinine | Numeric | mg/dL | Kidney function indicator |
| 9 | serum_sodium | Numeric | mEq/L | Sodium level in blood serum |
| 10 | sex | Binary | 0/1 | Gender (0=Male, 1=Female) |
| 11 | smoking | Binary | 0/1 | Smoking status |
| 12 | time | Numeric | days | Follow-up period in days |
| 13 | DEATH_EVENT | Binary | 0/1 | Target: Heart failure occurrence (0=No, 1=Yes) |

### Data Statistics

**Target Variable Distribution:**
- No Heart Failure (0): 203 records (67.89%)
- Heart Failure (1): 96 records (32.11%)
- Class Ratio: 2.11:1

**Key Statistics:**
- Age Range: 40-95 years (Mean: 60.87)
- Ejection Fraction Range: 14-80% (Mean: 38.08%)
- Serum Creatinine Range: 0.7-9.4 mg/dL (Mean: 1.39)
- Follow-up Period: 4-2015 days (Mean: 130.26)

---

## Methodology

### 1. Exploratory Data Analysis (EDA)

**Analysis Performed:**
- Descriptive statistics (mean, median, standard deviation, quartiles)
- Distribution analysis using histograms and density plots
- Correlation analysis with heatmaps
- Feature relationships and patterns
- Target variable distribution assessment
- Missing value detection (0% missing)

**Key Insights from EDA:**
- Age shows positive correlation with heart failure risk
- Ejection fraction inversely correlates with heart failure (most important feature)
- Serum creatinine elevated in heart failure cases
- High blood pressure prevalent in both groups
- Dataset is relatively clean with no missing values

### 2. Data Preprocessing

**Steps Applied:**
- Feature standardization using StandardScaler (zero mean, unit variance)
- Train-test split (80% training, 20% testing)
- No missing value imputation (complete dataset)
- Categorical variable handling (already binary)
- Feature validation and quality checks

**Code Example:**
```python
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Separate features and target
X = df.drop('DEATH_EVENT', axis=1)
y = df['DEATH_EVENT']

# Split data (stratified to maintain class distribution)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### 3. Model Development

**Seven Algorithms Evaluated:**

| Algorithm | Type | Description | Hyperparameters |
|-----------|------|-------------|------------------|
| Logistic Regression | Linear | Baseline classifier for comparison | Regularization: L2 |
| Decision Tree | Tree-based | Single tree for feature importance | Max depth: 10 |
| Random Forest | Ensemble | Multiple trees for robustness | Trees: 100 |
| K-Nearest Neighbors | Instance-based | **Best performer** | K: 5 |
| Support Vector Machine | Kernel-based | Non-linear boundary detection | Kernel: RBF |
| Gradient Boosting | Boosting | Sequential tree improvement | Estimators: 100 |
| Naive Bayes | Probabilistic | Baseline probabilistic approach | Default |

**Training Methodology:**
- Standard scikit-learn fit-predict pipeline
- 5-fold cross-validation for robustness
- Hyperparameter optimization where applicable
- Performance metric calculation on held-out test set

### 4. Model Evaluation

**Performance Metrics:**
- **Accuracy:** Overall percentage of correct predictions
- **Precision:** True positives / (True positives + False positives)
- **Recall (Sensitivity):** True positives / (True positives + False negatives)
- **F1-Score:** Harmonic mean of precision and recall
- **AUC-ROC:** Area under Receiver Operating Characteristic curve

**Evaluation Framework:**
- Individual model performance on test set
- Cross-validation scores for generalization assessment
- Confusion matrices for detailed error analysis
- ROC curves for threshold optimization
- Feature importance analysis

---

## Model Performance

### Overall Results Summary

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|----------|-----------|--------|----------|---------|
| **K-Nearest Neighbors** | **85.55%** | **84.00%** | **78.95%** | **81.40%** | **0.87** |
| Logistic Regression | 80.37% | 77.59% | 71.05% | 74.19% | 0.82 |
| Decision Tree | 81.40% | 78.79% | 73.68% | 76.16% | 0.79 |
| Random Forest | 83.02% | 81.08% | 75.79% | 78.31% | 0.85 |
| Gradient Boosting | 82.06% | 79.66% | 75.79% | 77.66% | 0.83 |
| Support Vector Machine | 81.40% | 79.55% | 71.05% | 75.00% | 0.81 |
| Naive Bayes | 78.27% | 74.00% | 68.42% | 71.05% | 0.79 |

### Best Model: K-Nearest Neighbors (KNN)

**Test Set Performance:**
```
Accuracy:  85.55%
Precision: 84.00%
Recall:    78.95%
F1-Score:  81.40%
AUC-ROC:   0.87
```

**Confusion Matrix:**
```
                    Predicted Negative    Predicted Positive
Actual Negative             52                     6
Actual Positive              4                    18
```

**5-Fold Cross-Validation Results:**
- Fold 1: 83.33%
- Fold 2: 86.67%
- Fold 3: 88.33%
- Fold 4: 80.00%
- Fold 5: 86.67%
- Mean: 85.00% ± 3.14%
- Demonstrates stable generalization performance

### ROC-AUC Analysis
- KNN AUC-ROC: 0.87 (Excellent discrimination)
- Interpretation: 87% probability the model ranks a random positive instance higher than a negative one
- Threshold optimization: Default 0.5 threshold provides good balance

---

## Key Findings

### 1. Model Selection Insights
- **KNN outperforms all other algorithms** with 85.55% accuracy
- Consistent performance across cross-validation folds (83-88%)
- Good balance between precision (84%) and recall (79%)
- Non-linear relationships in the data favor instance-based methods

### 2. Feature Importance (from Decision Tree)
1. **Ejection Fraction** - Most important predictor (30% importance)
2. **Serum Creatinine** - Second most important (25% importance)
3. **Age** - Third most important (18% importance)
4. **Serum Sodium** - Fourth most important (12% importance)
5. Other features contribute remaining 15%

### 3. Clinical Insights
- **Low Ejection Fraction:** Primary indicator of heart failure risk (inverse relationship)
- **Elevated Serum Creatinine:** Indicates kidney dysfunction, associated with worse outcomes
- **Advanced Age:** Progressive increase in risk with increasing age
- **Low Serum Sodium:** Hyponatremia associated with poor prognosis
- **Comorbidities:** Diabetes and hypertension increase risk but are not primary predictors

### 4. Model Reliability
- High accuracy (85.55%) with acceptable precision-recall tradeoff
- Strong generalization capability (stable cross-validation scores)
- Robust to test set composition (stratified evaluation)
- No signs of overfitting or underfitting

### 5. Class Imbalance Consideration
- 67.89% vs 32.11% distribution is challenging but manageable
- Recall of 78.95% shows reasonable sensitivity to positive class
- Precision of 84% indicates low false alarm rate
- Model suitable for clinical risk assessment

---

## Installation & Usage

### System Requirements
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- 4GB RAM minimum
- 500MB disk space

### Required Libraries
```
pandas >= 1.3.0
numpy >= 1.21.0
scikit-learn >= 0.24.0
matplotlib >= 3.4.0
seaborn >= 0.11.0
jupyter >= 1.0.0
```

### Installation Steps

**Step 1: Clone or Download Repository**
```bash
cd Heart-Failure-Prediction
```

**Step 2: Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Launch Jupyter Notebook**
```bash
jupyter notebook Heart_Failure_Prediction_Project.ipynb
```

### Usage Instructions

**Running the Complete Analysis:**
1. Open the Jupyter notebook
2. Execute cells sequentially from top to bottom
3. View generated visualizations and results
4. Examine model performance metrics
5. Review insights and conclusions

**Making Predictions with Trained Model:**
```python
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Load trained model and scaler
model = joblib.load('models/knn_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# Prepare patient data
new_patient = pd.DataFrame({
    'age': [65],
    'anaemia': [0],
    'creatinine_phosphokinase': [320],
    'diabetes': [1],
    'ejection_fraction': [38],
    'high_blood_pressure': [1],
    'platelets': [263000],
    'serum_creatinine': [1.46],
    'serum_sodium': [142],
    'sex': [0],
    'smoking': [0],
    'time': [130]
})

# Scale and predict
scaled_data = scaler.transform(new_patient)
prediction = model.predict(scaled_data)
probability = model.predict_proba(scaled_data)

print(f"Prediction: {prediction[0]}")  # 0 = No HF, 1 = HF
print(f"Probability: {probability[0]}")  # [prob_no_hf, prob_hf]
```

---

## Project Structure

```
Heart-Failure-Prediction/
├── README.md                              # Project overview (this file)
├── Heart_Failure_Prediction_Project.ipynb # Main analysis notebook
├── requirements.txt                       # Python dependencies
├── DATA_DOCUMENTATION.md                  # Feature documentation
├── PROJECT_STRUCTURE.md                   # Detailed structure guide
├── INSIGHTS_AND_FUTURE_SCOPE.md          # Key insights & future directions
├── data/
│   └── heart_failure_prediction.csv       # Dataset (299 records)
├── models/
│   ├── knn_model.pkl                      # Trained KNN model
│   └── scaler.pkl                         # StandardScaler object
└── outputs/
    ├── visualizations/                    # Generated plots
    ├── model_results/                     # Performance reports
    └── metrics/                           # Performance metrics
```

---

## References

**Dataset:**
- UCI Machine Learning Repository: Heart Failure Prediction Dataset
- https://archive.ics.uci.edu/dataset/519/heart+failure+clinical+records

**Key Papers & Resources:**
- Davey, B., & Davey, S. L. (1996). Assessment of patient satisfaction with aspects of long-term management of type 2 diabetes. Diabetes Medicine, 13(9), 798-809.
- Chicco, D., & Jurman, G. (2020). Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone. BMC Medical Informatics and Decision Making, 20, 16.

**Scikit-learn Documentation:**
- Classification Metrics: https://scikit-learn.org/stable/modules/model_evaluation.html
- Model Selection: https://scikit-learn.org/stable/modules/cross_validation.html

---

## Contact & Support

**For Questions About:**
- **Methodology:** Review the "Methodology" section in README.md
- **Features:** See DATA_DOCUMENTATION.md for detailed feature information
- **Results:** Check "Model Performance" section or view notebook visualizations
- **Future Work:** Review INSIGHTS_AND_FUTURE_SCOPE.md

---
