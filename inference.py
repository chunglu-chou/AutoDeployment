import json
import numpy as np
import os
import pickle
import sys

modelPath = os.getcwd() + "/model-1627044496.525413.sav"

if __name__ == "__main__":
    with open(modelPath, 'rb') as modelFile:
        fakeData = json.load(sys.stdin)
        model = pickle.load(modelFile)
        prediction = model.predict(fakeData)[0]
        json.dump(prediction, sys.stdout)