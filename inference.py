import numpy as np
import os
import pickle

modelPath = os.getcwd() + "/model-1627044496.525413.sav"

fakeData = np.array([[0.00632, 18, 2.31, 0, 0.538, 6.575,
                     65.2, 4.09, 1, 296, 15.3, 396.9, 4.98]], dtype = np.float64)

with open(modelPath, 'rb') as modelFile:
    model = pickle.load(modelFile)
    prediction = model.predict(fakeData)[0]
    print(prediction)