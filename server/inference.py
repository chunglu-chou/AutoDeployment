from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import json
import numpy as np
import os
import pickle
import sys

# Define data model
class Data(BaseModel):
    data: List[List[float]]

# Load model
modelPath = os.path.join(os.path.abspath(os.getcwd()), 'model.sav')
if os.path.exists(modelPath):
    with open(modelPath, 'rb') as modelFile:
        model = pickle.load(modelFile)
else:
    print("Invalid model path")
    model = None

# Start app
app = FastAPI()

# Define inference API
@app.post("/inference")
async def inference(body: Data):
    if model:
        prediction = model.predict(np.array(body.data, dtype = np.float64))
        return {"Price": prediction[0]}
    return None