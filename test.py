import json
import numpy as np
from os import pread
import pickle
import requests
import sys

# test data
data = {
    "CRIM": 0.00632, "ZN": 18, "INDUS": 2.31,
    "CHAS": 0, "NOX": 0.538, "RM": 6.575,
    "AGE": 65.2, "DIS": 4.09, "RAD": 1, "TAX": 296,
    "PTRATIO": 15.3, "B": 396.9, "LSTAT": 4.98
}

# get prediction from service
url = "http://127.0.0.1:8080/"
headers = {
    "Content-Type": "application/json"
}
response = requests.post(url, headers = headers, data = json.dumps(data))
print(response.text)

# get prediction from local
if len(sys.argv) == 2:
    with open(sys.argv[1], "rb") as modelFile:
        model = pickle.load(modelFile)
        prediction = model.predict(np.array([list(data.values())], dtype = np.float64))[0]
        print(prediction)