import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

# Load model
model = joblib.load("model/model.pkl")

# Load dataset
data = pd.read_csv("data/data.csv")

X = data.drop("target", axis=1)
y = data["target"]

# Predict
predictions = model.predict(X)

accuracy = accuracy_score(y, predictions)

print("Current accuracy:", accuracy)

# Save monitoring log
with open("data/monitoring_log.txt", "a") as f:
    f.write(f"Accuracy: {accuracy}\n")

# Alert if accuracy drops
if accuracy < 0.80:
    print("ALERT: Accuracy dropped. Retraining required.")
