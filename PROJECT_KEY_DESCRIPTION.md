# Heart Failure Prediction with Machine Learning

## Key Project Description (4 Lines)

**Aim:** Develop a machine-learning classification system to estimate heart-failure outcome risk from clinical and demographic variables in the UCI Heart Failure Clinical Records dataset.

**Methodology:** Analyzed 299 patient records containing 12 input variables and the `DEATH_EVENT` target. Performed exploratory data analysis, stratified 80/20 train-test splitting, five-fold stratified cross-validation, and comparative evaluation of Logistic Regression, Decision Tree, Random Forest, K-Nearest Neighbors, and Support Vector Machine classifiers.

**Results:** In the latest reproducible experiment, Random Forest was selected as the strongest overall model. It achieved 83.33% test accuracy, 80.00% precision, 63.16% recall, 70.59% F1-score, and 0.8909 ROC-AUC. Five-fold cross-validation produced 84.56% mean accuracy with 6.63% standard deviation.

**Impact:** Demonstrates an end-to-end machine-learning workflow, from exploratory analysis and model comparison to a reusable training pipeline, FastAPI prediction service, and locally tested Docker container. The project is an educational and research demonstration, not a clinical diagnostic tool.

---

## Alternative Short Version (1–2 Lines)

Built and evaluated five classification models on 299 UCI heart-failure clinical records, selecting Random Forest based on final comparative results. The selected model achieved 83.33% accuracy and 0.8909 ROC-AUC, and was packaged as a locally tested FastAPI and Docker prediction service.

---

## Resume Version

**Heart Failure Prediction API — ML Engineering Upgrade**  
*Python, pandas, scikit-learn, Random Forest, FastAPI, Docker*

- Evaluated five classification models on the UCI Heart Failure Clinical Records dataset and selected Random Forest based on the final held-out test and cross-validation results.
- Achieved 83.33% test accuracy and 0.8909 ROC-AUC; reported precision, recall, F1-score, confusion matrix, and five-fold cross-validation for robust evaluation.
- Refactored notebook analysis into a reusable training workflow, serialized the model for inference, and built FastAPI `/health` and `/predict` endpoints.
- Containerized and locally tested the ML API using Docker; AWS deployment is in progress.

---

## Academic Registration Form Version

Developed a machine-learning classification project using 299 UCI Heart Failure Clinical Records. The project performed exploratory data analysis and compared Logistic Regression, Decision Tree, Random Forest, K-Nearest Neighbors, and Support Vector Machine models using stratified evaluation and five-fold cross-validation. Random Forest was selected in the final experiment, achieving 83.33% test accuracy and 0.8909 ROC-AUC. The model was then integrated into a FastAPI prediction API and locally tested in a Docker container.

---

## Key Statistics Summary

| Metric | Final Result |
|---|---|
| **Selected Model** | Random Forest Classifier |
| **Test Accuracy** | 83.33% |
| **Precision** | 80.00% |
| **Recall** | 63.16% |
| **F1-score** | 70.59% |
| **ROC-AUC** | 0.8909 |
| **Cross-Validation** | 84.56% ± 6.63% (5-fold stratified CV on training data) |
| **Dataset** | 299 patient records |
| **Input Features** | 12 clinical and demographic variables |
| **Target** | `DEATH_EVENT` |
| **Models Evaluated** | Logistic Regression, Decision Tree, Random Forest, KNN, SVM |
| **Local Deployment** | FastAPI API + Docker container tested locally |
| **AWS Status** | Deployment in progress |

---

## Important Limitations

- The dataset contains only 299 records and requires validation on independent data before generalization claims can be made.
- The `time` feature represents patient follow-up duration. It is retained to reproduce the current experiment, but it may introduce temporal leakage for an initial-risk prediction use case.
- Model feature importance reflects the trained model and dataset; it does not establish clinical causality.
- This project is an educational/research demonstration only and must not be used for diagnosis, treatment, or clinical decision-making.
