import json
import requests
import sys
import time

# test data
jsonData = {
    "CRIM": 0.00632, "ZN": 18, "INDUS": 2.31,
    "CHAS": 0, "NOX": 0.538, "RM": 6.575,
    "AGE": 65.2, "DIS": 4.09, "RAD": 1, "TAX": 296,
    "PTRATIO": 15.3, "B": 396.9, "LSTAT": 4.98
}

data = list(jsonData.values())

url = "http://127.0.0.1:3001/inference"
headers = {
    "Content-Type": "application/json"
}

fail = True
start = time.time()
while time.time() - start < 10:
    try:
        response = requests.post(
            url=url, headers=headers, data=json.dumps({"data": [data]}))
        print(response.text)
        print("Health check passed")
        fail = False
        break
    except:
        continue
if fail:
    print("Error")
