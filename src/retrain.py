import os

THRESHOLD = 0.80

# Simulate current accuracy
current_accuracy = 0.75

print("Checking model performance...")

if current_accuracy < THRESHOLD:

    print("Performance dropped. Retraining model...")

    os.system("python src/train.py")

    print("Retraining completed.")

else:
    print("Model performance is good.")
