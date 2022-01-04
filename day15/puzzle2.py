import numpy as np
import pandas as pd
from collections import defaultdict

class Heap():
    def __init__(self):
        self.heap = [None]
        self.pos = {}        


    def add(self, vertex, weight):
        self.heap.append([vertex, weight])
        #self.pos.append(vertex)
        index = len(self.heap) - 1
        self.pos[vertex] = index
        self.heapify(index)


    def heapify(self, index):
        parent = int(index/2)
        if parent != 0 and self.heap[parent][1] > self.heap[index][1]:
            parent_vertex = self.heap[parent][0]
            child_vertex = self.heap[index][0]

            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.pos[parent_vertex], self.pos[child_vertex] = self.pos[child_vertex], self.pos[parent_vertex]

            self.heapify(parent)

    def get_min(self):
        return self.heap[1]


    def extract_min(self):
        size = len(self.heap)
        self.heap[1], self.heap[size - 1] = self.heap[size - 1], self.heap[1] 
        self.pos[self.heap[1][0]], self.pos[self.heap[size - 1][0]] = self.pos[self.heap[size - 1][0]], self.pos[self.heap[1][0]]
        min = self.heap.pop()
        min_pos = self.pos.pop(min[0])
        self.sink(1)
        return min, min_pos


    def decrease_key(self, vertex, weight):
        index = self.pos[vertex]
        self.heap[index][1] = weight 
        self.heapify(index)


    def sink(self, index):
        left = index * 2
        right = index * 2 + 1
        smallest = index
        

        if left < len(self.heap) and self.heap[left][1] < self.heap[smallest][1]:
            smallest = left

        if right < len(self.heap) and self.heap[right][1] < self.heap[smallest][1]:
            smallest = right

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.pos[self.heap[smallest][0]], self.pos[self.heap[index][0]] = self.pos[self.heap[index][0]], self.pos[self.heap[smallest][0]]
            self.sink(smallest)


class Graph():
    def __init__(self, risk_map):
        self.V = len(risk_map)
        self.graph = defaultdict(list)
        self.add_edges(risk_map)
        

    def add_edges(self, risk_map):
        rows = int(np.sqrt(self.V))
        for i in range(self.V):
            r = (int)(i / rows)
            c = (int)(i % rows)

            if r == rows - 1 and c == rows - 1:
                continue

            if c < rows - 1:
                self.graph[i].insert(0, [i + 1, risk_map[i + 1]])

            if r < rows - 1:
                self.graph[i].insert(0, [i + rows, risk_map[i + rows]])

            if r > 0:
                self.graph[i].insert(0, [i - rows, risk_map[i - rows]])

            if c > 0:
                self.graph[i].insert(0, [i - 1, risk_map[i - 1]])


            # right most column
            #if (i + 1)%rows == 0:
            #    if int(i/rows) != (rows - 1):
            #        self.graph[i].insert(0, [i + rows, risk_map[i + rows]])
            ## last row 
            #elif int(i/rows) == rows - 1:
            #    self.graph[i].insert(0, [i + 1, risk_map[i + 1]])
            #else:
            #    self.graph[i].insert(0, [i + rows, risk_map[i + rows]])
            #    self.graph[i].insert(0, [i + 1, risk_map[i + 1]])

    
    def dijkstra(self):
        V = self.V
        dist = []
        min_heap = Heap()
        for v in range(V):
            if v == 0:
                dist.append(0)
            else: 
                dist.append(float('inf'))
            min_heap.add(v, dist[v])

        while len(min_heap.heap) > 1:
            min_vertice, min_dist = min_heap.get_min()

            for neighbor in self.graph[min_vertice]:
                neighbor_vertice, neighbor_weight = neighbor
                if dist[min_vertice] + neighbor_weight < dist[neighbor_vertice]:
                    dist[neighbor_vertice] = dist[min_vertice] + neighbor_weight 
                    min_heap.decrease_key(neighbor_vertice, dist[neighbor_vertice])

            min_heap.extract_min()

        print(dist)
                    
            




def create_next_piece(piece, n=1):
    rows, cols = piece.shape
    next_piece = np.zeros((rows, cols))    
    for i in range(rows):
        for j in range(cols):
            if piece[i][j] + n == 10:
                next_piece[i][j] = 1
            elif (piece[i][j] + n) > 10:
                next_piece[i][j] = int(piece[i][j] + n - 9)
            else:
                next_piece[i][j] = int(piece[i][j] + n)
    return next_piece

    
def create_full_map( piece):
    rows, cols = piece.shape
    full_risk_map = []
    pieces = [piece]

    for n in range(1, 9):
        pieces.append(create_next_piece(piece, n))
    
    count = 0
    for i in range(5):
        temp = []
        for j in range(i, i + 5):
            temp.append(pieces[j])
        full_risk_map.append(np.hstack(tuple(temp)))

    full_risk_map = np.vstack(tuple(full_risk_map))
    full_risk_map = np.array(full_risk_map, dtype='int32')
    return full_risk_map
   

def main():
    with open('input.txt') as file:
       data = file.readlines()
       data = [[int(char) for char in line.rstrip('\n')] for line in data]
       risk_map = np.array(data)

    full_risk_map = create_full_map(risk_map)
    print(full_risk_map)
    graph = Graph(full_risk_map.flatten())
    print(graph.graph)
    graph.dijkstra()
    


if __name__ == '__main__':
    main()
