import numpy as np
import pandas as pd
import math

def findPowerToAllocateMemory(num):
    power = 0
    while (2**power) <= num:
        power += 1
    return 2**power

def degree(coordinates):
    slope = (coordinates[3] - coordinates[1])/(coordinates[2] - coordinates[0])
    degree = math.degrees(math.atan(slope))
    return degree 

def mark_diagonal(coordinates, points):
    x1 = coordinates[0]
    y1 = coordinates[1]
    x2 = coordinates[2]
    y2 = coordinates[3]

    min_x = min([x1,x2])
    max_x = max([x1,x2])
    min_y = min([y1,y2])
    max_y = max([y1,y2])

    if degree(coordinates) == 45:
        diff_xy = y1 - x1
        for m in range(min_x, max_x + 1):
            points[m][m + diff_xy] += 1
    elif degree(coordinates) == -45:
        sum = x1 + y1
        for m in range(min_x, max_x + 1):
            points[m][sum - m] += 1

def mark_horizontal(coordinates, points):
    start = min([coordinates[3], coordinates[1]])
    end = max([coordinates[3], coordinates[1]])
    for m in range(start, end + 1):
        points[coordinates[0]][m] += 1

def mark_vertical(coordinates, points):
    start = min([coordinates[0], coordinates[2]])
    end = max([coordinates[0], coordinates[2]])
    for m in range(start, end + 1):
        points[m][coordinates[1]] += 1

def main():
    cols = range(4)
    data = pd.read_csv('input.txt', sep="->|,", names=cols, header=None, dtype='int32')
    dim = findPowerToAllocateMemory(data.max().max())

    points = np.zeros((dim, dim))
    data = data.to_numpy()
    shape = data.shape

    for i in range(shape[0]):
        # Diagonal
        if (data[i][0] != data[i][2]) & (data[i][1] != data[i][3]):
            mark_diagonal(data[i], points)
        elif data[i][0] == data[i][2]:
            mark_horizontal(data[i], points)
        else: # data[i][1] == data[i][3]
            mark_vertical(data[i], points)

    counts = (points >=2).sum()
    print(counts)

main()
#points = np.zeros((10, 10))
#mark_diagonal([4,1,6,3], points)
#mark_diagonal([3,1,0,4], points)
#mark_horizontal([1,1,1,4], points)
#mark_vertical([9,7,7,7], points)
#print(points)
