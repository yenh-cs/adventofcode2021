import numpy as np
import pandas as pd

def read_data(file_name):
    with open(file_name) as file:
       data = file.readlines()
       data = [[int(char) for char in line.rstrip('\n')] for line in data]
       risk_map = np.array(data)

    return risk_map



def find_min_dist(dist, keys):
    min_dist = float('inf') 
    vertex = (0, 0)
    for key in keys:
        if dist[key] <= min_dist:
            min_dist = dist[key]
            vertex = key
    return vertex


def find_least_risk_path(risk_map):
    rows, cols = risk_map.shape
    dist = np.zeros((rows, cols))
    Q = [] 

    for i in range(rows):
        for j in range(cols):
            if i!= 0 or j!= 0:
                dist[(i,j)] = float('inf')
            Q.append((i, j))
    
    while Q:
        vertex = find_min_dist(dist, Q)
        vertex_x, vertex_y = vertex

        # remove vertex from Q
        Q.remove(vertex)
        if vertex_x < rows - 1:
            if  vertex_y < cols - 1:
                neighbors = [(vertex_x, vertex_y + 1), (vertex_x + 1, vertex_y)]
            else:
                neighbors = [(vertex_x + 1, vertex_y)]
        else:
            if  vertex_y < cols - 1:
                neighbors = [(vertex_x, vertex_y + 1)]
            else:
                neighbors = []
                dist[vertex] = dist[(vertex_x, vertex_y - 1)] + risk_map[vertex_x][vertex_y] if dist[(vertex_x, vertex_y - 1)] < dist[(vertex_x - 1, vertex_y)] else dist[(vertex_x - 1, vertex_y)] + risk_map[vertex_x][vertex_y] 

        for neighbor in neighbors:
            alt = dist[vertex] + risk_map[neighbor[0]][neighbor[1]] 
            if alt < dist[neighbor]:
                dist[neighbor] = alt
            
    print(dist) 
    
   

def main():
    risk_map = read_data('input.txt')
    find_least_risk_path(risk_map)


if __name__ == '__main__':
    main()
