import config
import csv
import json
import os
import sys
import train

args = sys.argv
if len(args) < 2:
    print("Two arguments required")
elif len(args) > 2:
    print("Too many arguments")
else:
    with open(config.SIZEPATH, 'r') as sizeFile:
        sizeData = json.load(sizeFile)
        currSize = sizeData["currSize"]
    numOfData = int(args[1])
    if numOfData == 1 or numOfData == 2:
        with open(config.DATAPATH, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(config.FAKEDATA[:numOfData])
            if currSize + numOfData >= config.BATCHSIZE:
                sizeData["currSize"] = 0
                train.train()
            else:
                sizeData["currSize"] += numOfData
            with open(config.SIZEPATH, 'w') as sizeFile:
                json.dump(sizeData, sizeFile)
    else:
        print("Not supported yet")
