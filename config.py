import os

# global constants
DATAPATH = os.path.join(os.path.abspath(os.getcwd()), 'db/boston.csv')
MODELPATH = os.path.join(os.path.abspath(os.getcwd()), 'server/model.sav')
SIZEPATH = os.path.join(os.path.abspath(os.getcwd()), 'currSize.json')
BATCHSIZE = 2
FAKEDATA = [
    [0.13004, 12.5, 8.87, 0, 0.592, 6.836, 72.9,
        6.5430, 5, 331, 15.2, 299.71, 13.1, 12.9],
    [0.95204, 0, 8.14, 0, 0.882, 5.935, 87.2,
        4.9013, 4, 301, 21, 452.87, 15.83, 21.2]
]