import numpy as np
import pandas as pd

def findPowerToAllocateMemory(num):
    power = 0
    while (2**power) <= num:
        power += 1

    return 2**power

cols = range(4)
data = pd.read_csv('input.txt', sep="->|,", names=cols, header=None, dtype='int32')
dim = findPowerToAllocateMemory(data.max().max())

points = np.zeros((dim, dim))
data = data.to_numpy()
shape = data.shape

for i in range(shape[0]):
    if (data[i][0] != data[i][2]) & (data[i][1] != data[i][3]):
        continue
    elif data[i][0] == data[i][2]:
        start = data[i][3] if data[i][1] >= data[i][3] else data[i][1]
        end = data[i][1] if data[i][1] >= data[i][3] else data[i][3]
        for m in range(start, end + 1):
            row = data[i][0]
            column = m
            points[row][column] += 1
    else: # data[i][1] == data[i][3]
        start = data[i][2] if data[i][0] >= data[i][2] else data[i][0]
        end = data[i][0] if data[i][0] >= data[i][2] else data[i][2]
        for m in range(start, end + 1):
            row = m            
            column = data[i][1]
            points[row][column] += 1

print(points)
counts = (points >=2).sum()
print(counts)

