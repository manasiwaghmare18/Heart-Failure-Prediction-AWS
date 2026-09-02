from pathlib import Path
import json

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_ROOT / "heart_failure_prediction.csv"
MODEL_DIR = PROJECT_ROOT / "models"

MODEL_PATH = MODEL_DIR / "heart_failure_pipeline.joblib"
METRICS_PATH = MODEL_DIR / "model_metrics.json"


TARGET_COLUMN = "DEATH_EVENT"

FEATURE_COLUMNS = [
    "age",
    "anaemia",
    "creatinine_phosphokinase",
    "diabetes",
    "ejection_fraction",
    "high_blood_pressure",
    "platelets",
    "serum_creatinine",
    "serum_sodium",
    "sex",
    "smoking",
    "time",
]


def main():

    # ---------------------------------------------------------
    # 1. Check whether dataset exists
    # ---------------------------------------------------------
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}"
        )

    # ---------------------------------------------------------
    # 2. Load dataset
    # ---------------------------------------------------------
    df = pd.read_csv(DATA_PATH)

    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

    # ---------------------------------------------------------
    # 3. Validate required columns
    # ---------------------------------------------------------
    required_columns = FEATURE_COLUMNS + [TARGET_COLUMN]

    missing_columns = set(required_columns) - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Dataset is missing columns: {missing_columns}"
        )

    # ---------------------------------------------------------
    # 4. Separate features and target
    # ---------------------------------------------------------
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    # ---------------------------------------------------------
    # 5. Train-test split
    # ---------------------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    # ---------------------------------------------------------
    # 6. Create Random Forest model
    # ---------------------------------------------------------
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight=None,
    )

    # ---------------------------------------------------------
    # 7. Train model
    # ---------------------------------------------------------
    model.fit(X_train, y_train)

    # ---------------------------------------------------------
    # 8. Make predictions
    # ---------------------------------------------------------
    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]

    # ---------------------------------------------------------
    # 9. Calculate evaluation metrics
    # ---------------------------------------------------------
    metrics = {
        "model_name": "RandomForestClassifier",
        "n_estimators": 100,
        "random_state": 42,
        "feature_columns": FEATURE_COLUMNS,

        "accuracy": round(
            float(accuracy_score(y_test, predictions)),
            4,
        ),

        "precision": round(
            float(precision_score(y_test, predictions)),
            4,
        ),

        "recall": round(
            float(recall_score(y_test, predictions)),
            4,
        ),

        "f1_score": round(
            float(f1_score(y_test, predictions)),
            4,
        ),

        "roc_auc": round(
            float(roc_auc_score(y_test, probabilities)),
            4,
        ),

        "training_rows": int(len(X_train)),
        "test_rows": int(len(X_test)),
    }

    # ---------------------------------------------------------
    # 10. Calculate feature importance
    # ---------------------------------------------------------
    feature_importance = pd.DataFrame(
        {
            "feature": FEATURE_COLUMNS,
            "importance": model.feature_importances_,
        }
    ).sort_values(
        "importance",
        ascending=False,
    )

    metrics["feature_importance"] = {
        row["feature"]: round(float(row["importance"]), 6)
        for _, row in feature_importance.iterrows()
    }

    # ---------------------------------------------------------
    # 11. Create models directory
    # ---------------------------------------------------------
    MODEL_DIR.mkdir(exist_ok=True)

    # ---------------------------------------------------------
    # 12. Save trained model
    # ---------------------------------------------------------
    joblib.dump(model, MODEL_PATH)

    # ---------------------------------------------------------
    # 13. Save metrics
    # ---------------------------------------------------------
    with open(
        METRICS_PATH,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            metrics,
            file,
            indent=2,
        )

    # ---------------------------------------------------------
    # 14. Print results
    # ---------------------------------------------------------
    print("\n" + "=" * 70)
    print("RANDOM FOREST MODEL TRAINING COMPLETE")
    print("=" * 70)

    print(f"\nModel saved to:")
    print(MODEL_PATH)

    print(f"\nMetrics saved to:")
    print(METRICS_PATH)

    print("\nMODEL PERFORMANCE:")
    print(f"Accuracy:  {metrics['accuracy']:.2%}")
    print(f"Precision: {metrics['precision']:.2%}")
    print(f"Recall:    {metrics['recall']:.2%}")
    print(f"F1-Score:  {metrics['f1_score']:.2%}")
    print(f"ROC-AUC:   {metrics['roc_auc']:.4f}")

    print("\nTOP FEATURES:")
    for _, row in feature_importance.head(7).iterrows():
        print(
            f"   - {row['feature']}: "
            f"{row['importance']:.6f}"
        )

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()