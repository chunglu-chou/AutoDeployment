import csv
import os
import sys

dataPath = os.path.join(os.path.abspath(os.getcwd()), 'db/boston.csv')

data = [
    [0.13004, 12.5, 8.87, 0, 0.592, 6.836, 72.9, 6.5430, 5, 331, 15.2, 299.71, 13.1, 12.9],
    [0.95204, 0, 8.14, 0, 0.882, 5.935, 87.2, 4.9013, 4, 301, 21, 452.87, 15.83, 21.2]
]

args = sys.argv
if len(args) < 2:
    print("Two arguments required")
elif len(args) > 2:
    print("Too many arguments")
else:
    numOfData = int(args[1])
    if numOfData == 1 or numOfData == 2:
        with open(dataPath, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(data[:numOfData])
    else:
        print("Not supported yet")
