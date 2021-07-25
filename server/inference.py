import json
import numpy as np
import os
import pickle
import sys

modelPath = os.path.join(os.path.abspath(os.getcwd()), 'model.sav')

if __name__ == '__main__':
    if os.path.exists(modelPath):
        with open(modelPath, 'rb') as modelFile:
            data = json.load(sys.stdin)
            model = pickle.load(modelFile)
            prediction = model.predict(data)[0]
            json.dump(prediction, sys.stdout)
    else:
        print("Invalid model path")
