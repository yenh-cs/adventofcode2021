import pandas as pd
import numpy as np

def findAdjacents(heightmap, i, j):
    rows, columns = heightmap.shape
    if i == 0:
        if j == 0:
            return [heightmap[i][j+1], heightmap[i+1][j]]
        elif j==columns-1:
            return [heightmap[i][j-1], heightmap[i+1][j]]
        else:
            return [heightmap[i][j-1], heightmap[i][j+1], heightmap[i+1][j]]
    elif i == rows-1:
        if j == 0:
            return [heightmap[i][j+1], heightmap[i-1][j]]
        elif j==columns-1:
            return [heightmap[i][j-1], heightmap[i-1][j]]
        else:
            return [heightmap[i][j-1], heightmap[i][j+1], heightmap[i-1][j]]
    else:
        if j == 0:
            return [heightmap[i][j+1], heightmap[i-1][j], heightmap[i+1][j]]
        elif j==columns-1:
            return [heightmap[i][j-1], heightmap[i-1][j], heightmap[i+1][j]]
        else:
            return [heightmap[i][j+1], heightmap[i][j-1], heightmap[i-1][j], heightmap[i+1][j]]
    

def findLowPoint(point, adjacents):
    isLowPoint = True
    for adjacent in adjacents:
        if point >= adjacent:
            isLowPoint = False
    return isLowPoint


def main():
    data = pd.read_csv("input.txt", header=None, dtype='str')
    heightmap = data[0].str.split('', expand=True).iloc[:,1:-1].to_numpy(dtype='int32')
    rows, columns = heightmap.shape
    lowPoints = []
    for i in range(rows):
        for j in range(columns):
            adjacents = findAdjacents(heightmap, i, j)
            point = heightmap[i][j]
            isLowPoint = findLowPoint(point, adjacents)
            if isLowPoint== True:
                lowPoints.append(point)
    risk_level = sum(lowPoints) + len(lowPoints)
    print(lowPoints)
    print(risk_level)


if __name__ =='__main__':
    main()
