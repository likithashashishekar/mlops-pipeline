import time
import os

while True:

    print("Running monitoring...")

    os.system("python src/monitor.py")

    os.system("python src/retrain.py")

    print("Waiting 60 seconds...")

    time.sleep(60)
