from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model/model.pkl")

@app.get("/")
def home():
    return {"message": "MLOps system running"}

@app.get("/predict")
def predict(feature1: float, feature2: float, feature3: float, feature4: float):

    features = np.array([[feature1, feature2, feature3, feature4]])

    prediction = model.predict(features)

    return {"prediction": int(prediction[0])}
