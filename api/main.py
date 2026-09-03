from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "models" / "heart_failure_pipeline.joblib"

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

app = FastAPI(
    title="Heart Failure Prediction API",
    version="1.0.0",
    description=(
        "Educational machine-learning demonstration using the UCI Heart Failure "
        "Clinical Records dataset. This API is not for diagnosis, treatment, or "
        "clinical decision-making."
    ),
)

model = None


class PatientInput(BaseModel):
    age: float = Field(..., ge=18, le=120)
    anaemia: int = Field(..., ge=0, le=1)
    creatinine_phosphokinase: float = Field(..., ge=0)
    diabetes: int = Field(..., ge=0, le=1)
    ejection_fraction: float = Field(..., ge=0, le=100)
    high_blood_pressure: int = Field(..., ge=0, le=1)
    platelets: float = Field(..., ge=0)
    serum_creatinine: float = Field(..., ge=0)
    serum_sodium: float = Field(..., ge=0)
    sex: int = Field(..., ge=0, le=1)
    smoking: int = Field(..., ge=0, le=1)
    time: float = Field(..., ge=0)


@app.on_event("startup")
def load_model():
    global model

    if not MODEL_PATH.exists():
        raise RuntimeError(
            "Model is missing. Run this command first: python src\\train.py"
        )

    model = joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return {
        "message": "Heart Failure Prediction API is running.",
        "documentation": "/docs",
        "warning": "Educational demo only; not medical advice or a clinical tool.",
    }


@app.get("/health")
def health():
    model_name = None

    if model is not None:
        if hasattr(model, "named_steps") and "model" in model.named_steps:
            model_name = type(model.named_steps["model"]).__name__
        else:
            model_name = type(model).__name__

    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "model_name": model_name,
    }


@app.post("/predict")
def predict(patient: PatientInput):
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not loaded.")

    patient_df = pd.DataFrame(
        [patient.model_dump()],
        columns=FEATURE_COLUMNS,
    )

    prediction = int(model.predict(patient_df)[0])
    probability = float(model.predict_proba(patient_df)[0][1])

    return {
        "prediction": prediction,
        "risk_label": (
            "Higher predicted risk in this model"
            if prediction == 1
            else "Lower predicted risk in this model"
        ),
        "heart_failure_probability": round(probability, 4),
        "disclaimer": (
            "Educational ML demonstration only. This is not medical advice, "
            "a diagnosis, or a treatment recommendation."
        ),
    }
