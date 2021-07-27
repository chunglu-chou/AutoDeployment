import config
import csv
import json
import os
import subprocess
import sys
import train

args = sys.argv
if len(args) < 2:
    print("Two arguments required")
elif len(args) > 2:
    print("Too many arguments")
else:
    with open(config.STATUSPATH, 'r') as statusFile:
        status = json.load(statusFile)
        currSize = status["currSize"]
    numOfData = int(args[1])
    if numOfData == 1 or numOfData == 2:
        with open(config.DATAPATH, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(config.FAKEDATA[:numOfData])
        if currSize + numOfData >= config.BATCHSIZE:
            status["currSize"] = 0
            modelPath = train.train()
            if status["host"] == "blue":
                subprocess.run(["sh", "deploy.sh", "green", modelPath])
                status["host"] = "green"
            elif status["host"] == "green":
                subprocess.run(["sh", "deploy.sh", "blue", modelPath])
                status["host"] = "blue"
            else:
                print("No host name: " + status["host"])
        else:
            status["currSize"] += numOfData
        with open(config.STATUSPATH, 'w') as statusFile:
            json.dump(status, statusFile)
    else:
        print("Not supported yet")
