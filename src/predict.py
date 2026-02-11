import joblib
import numpy as np
import pandas as pd
import datetime

# Load model
model = joblib.load("model/model.pkl")

# Simulate input data
input_data = np.array([[5.1, 3.5, 1.4, 0.2]])

# Predict
prediction = model.predict(input_data)[0]

# Log prediction
log = {
    "timestamp": datetime.datetime.now(),
    "feature1": input_data[0][0],
    "feature2": input_data[0][1],
    "feature3": input_data[0][2],
    "feature4": input_data[0][3],
    "prediction": int(prediction)
}

# Save log
df = pd.DataFrame([log])

df.to_csv("data/prediction_logs.csv", mode="a", header=False, index=False)

print("Prediction logged:", prediction)
