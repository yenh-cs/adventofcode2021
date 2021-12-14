from collections import defaultdict
import pandas as pd
import numpy as np

def create_graph(edges):
    graph = defaultdict(list)
    vertices = []
    for edge in edges:
        start, end = edge.split('-')
        graph[start].append(end)
        graph[end].append(start)
        if start not in vertices:
            vertices.append(start)

        if end not in vertices:
            vertices.append(end)

    return graph, vertices


def categorise_caves(vertices):
    big_caves = []
    small_caves = []
    for vertice in vertices:
        #if vertice != 'start' and vertice != 'end':
        if vertice.islower():
            small_caves.append(vertice)
        else:
            big_caves.append(vertice)

    return big_caves, small_caves


def get_all_paths_util(path, graph, paths, visited, small_caves, start='start', end='end'):
    visited[start] = True
    path.append(start)

    if start == end:
        paths.append(path.copy())
    else:
        for node in graph[start]:
            if visited[node] == False or (node not in small_caves):
                get_all_paths_util(path, graph, paths, visited, small_caves, node, end)
    path.pop()
    visited[start] = False


def get_all_paths(graph, vertices, paths, start='start', end='end'):
    visited = dict.fromkeys(vertices, False)
    path = []
    big_caves, small_caves = categorise_caves(vertices)
    get_all_paths_util(path, graph, paths, visited, small_caves)


def main():
    edges = pd.read_csv('input.txt', header=None).to_numpy().flatten()
    graph, vertices  = create_graph(edges)
    paths = []
    get_all_paths(graph, vertices, paths)
    print(len(paths)) 

if __name__ == '__main__':
    main()
