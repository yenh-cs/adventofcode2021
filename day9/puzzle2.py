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


def isValid(heightmap, rows, cols, x, y, lowPoint):
        if x<0 or x>= rows\
           or y<0 or y>= cols\
           or heightmap[x][y] == 9\
           or heightmap[x][y] < lowPoint:
            return False
        return True


def findBasinSize(heightmap, x, y):
    size = 0
    rows, cols = heightmap.shape
    lowPoint = heightmap[x][y]
    queue = []
    queue.append([x, y])
    while queue:
        current = queue.pop()
        posX, posY = current[0], current[1]

        if heightmap[posX][posY] == 9:
            continue

        heightmap[posX][posY] = 9
        size += 1
                
        if isValid(heightmap, rows, cols, posX + 1, posY, lowPoint):
            queue.append([posX + 1, posY])
            
        if isValid(heightmap, rows, cols, posX - 1, posY, lowPoint):
            queue.append([posX - 1, posY])

        if isValid(heightmap, rows, cols, posX, posY + 1, lowPoint):
            queue.append([posX, posY + 1])

        if isValid(heightmap, rows, cols, posX, posY - 1, lowPoint):
            queue.append([posX, posY - 1])

    return size, heightmap


def main():
    data = pd.read_csv("input.txt", header=None, dtype='str')
    heightmap = data[0].str.split('', expand=True).iloc[:,1:-1].to_numpy(dtype='int32')
    rows, columns = heightmap.shape
    lowPoints = []
    basins = []
    for i in range(rows):
        for j in range(columns):
            adjacents = findAdjacents(heightmap, i, j)
            point = heightmap[i][j]
            isLowPoint = findLowPoint(point, adjacents)
            if isLowPoint== True:
                lowPoints.append({ 'lowPoint': point, 
                                   'x': i, 
                                   'y': j
                                  })
        
    for lowPoint in lowPoints:
        size, heightmap = findBasinSize(heightmap, lowPoint['x'], lowPoint['y'])
        basins.append(size)
    print(sorted(basins, reverse=True)[0:3])


if __name__ =='__main__':
    main()
