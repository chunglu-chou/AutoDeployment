import config
import csv
import numpy as np
import os
import pickle
from sklearn.linear_model import LinearRegression
import time

def train():
    with open(config.DATAPATH, newline = '') as csvfile:
        # read data
        rows = list(csv.reader(csvfile))
        header, body = rows[0], np.array(rows[1:], dtype = np.float64)
        data, label = body[:, :-1], body[:, -1]
        # regression
        model = LinearRegression()
        model.fit(data, label)
        print(f'R square: {model.score(data, label)}')
        with open(config.MODELPATH, 'wb') as modelFile:
            pickle.dump(model, modelFile)

if "__name__" == "__main__":
    train()