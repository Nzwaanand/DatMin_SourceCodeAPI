# fastapi_app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import numpy as np

# Load scaler dan model
scaler = joblib.load("scaler-2.pkl")
model = joblib.load("xgb_best_model.pkl")  

# FastAPI instance
app = FastAPI()

# Definisikan inputan API
class InputData(BaseModel):
    pendidikan_rendah: float = Field(..., example=500000.0)
    pendidikan_menengah: float = Field(..., example=700000.0)
    pendidikan_tinggi: float = Field(..., example=300000.0)
    tahun: int = Field(..., example=2025)

@app.post("/predict")
def predict_pengangguran(data: InputData):
    try:
        # Masukkan input ke dalam array (hanya fitur numerik untuk model)
        input_features = np.array([[data.pendidikan_rendah, data.pendidikan_menengah, data.pendidikan_tinggi]])

        # Normalisasi input
        scaled_features = scaler.transform(input_features)

        # Prediksi
        prediction = model.predict(scaled_features)

        return {
            "tahun_prediksi": data.tahun,
            "predicted_total_pengangguran": int(prediction[0])
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
