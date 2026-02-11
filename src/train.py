import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

os.makedirs("model", exist_ok=True)

data = pd.read_csv("data/data.csv")

X = data.drop("target", axis=1)
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

mlflow.set_experiment("mlops_project")

with mlflow.start_run():
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")

joblib.dump(model, "model/model.pkl")

print("Model saved successfully")
