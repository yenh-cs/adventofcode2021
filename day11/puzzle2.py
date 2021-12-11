import pandas as pd
import numpy as np

def getToBeFlashing(grid):
    queue = []
    rows, cols = grid.shape
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] > 9:
                queue.append([i, j])
    return queue


def isValidAffectedNeighbor(grid, x, y, octopuses):
    rows, cols = grid.shape
    if x<0 or x>= rows or y<0 or y>= cols or grid[x][y] > 9 or [x, y] in octopuses:
        return False
    return True


def octopuses_flash(grid, octopus_count):
    grid += 1
    octopuses = getToBeFlashing(grid) 
    if len(octopuses) == octopus_count:
        return True
    
    for octopus in octopuses: 
        x, y = octopus[0], octopus[1]
        grid[x][y] = 0
        
        neighbors = [
                        [x + 1, y], 
                        [x - 1, y], 
                        [x, y + 1], 
                        [x, y - 1], 
                        [x + 1, y - 1], 
                        [x + 1, y + 1], 
                        [x - 1, y - 1], 
                        [x - 1, y + 1], 
                    ]
        
        for neighbor in neighbors:
            if isValidAffectedNeighbor(grid, neighbor[0], neighbor[1], octopuses):
                grid[neighbor[0]][neighbor[1]] += 1
                if grid[neighbor[0]][neighbor[1]] > 9:
                    octopuses.append(neighbor)
                    if len(octopuses) == octopus_count:
                        return True

    return False 




def main():
    data = pd.read_csv("input.txt", header=None, dtype='str')
    grid = data[0].str.split('', expand=True).iloc[:,1:-1].to_numpy(dtype='int32')
    
    octopus_count = grid.shape[0] * grid.shape[1]
    print(octopus_count)
    steps = 0 
    stop = False
    while not stop:
        steps += 1
        stop = octopuses_flash(grid, octopus_count)

    print(steps)


if __name__ == '__main__':
    main()
