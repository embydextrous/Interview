from collections import defaultdict, deque
from graph import Graph, printMatrix, UndirectedHashGraph, UndirectedGraph
from math import sqrt, floor

def dfs(g, u, visited, dist):
    visited.add(u)
    dist[u][0] = u
    for (v, w) in g[u]:
        if v not in visited:
            dist[v][1] = dist[v-1][1] + w
            dfs(g, v, visited, dist)


def minReversals(edges):
    g = defaultdict(list)
    for (u, v) in edges:
        g[u].append([v, 0])
        g[v].append([u, 1])
    dist = [[0, 0] for i in range(len(g))]
    visited = set()
    dfs(g, 0, visited, dist)
    minReversals = len(edges)
    root = None
    for i in range(len(dist)):
        edgeToReverse = 0
        if i != 0:
            edgeToReverse += dist[i][0] - dist[i][1]
        if i != len(dist) - 1:
            edgeToReverse += dist[-1][1] - dist[i][1]
        if edgeToReverse < minReversals:
            root = i
            minReversals = edgeToReverse
        print(i, edgeToReverse)
    return (root, minReversals)


'''
        0 --> 1 <-- 2 <-- 3 --> 4 <-- 5 --> 6 <-- 7

'''

edges = [[ 0, 1 ], [ 2, 1 ], [ 3, 2 ], [ 3, 4 ], [ 5, 4 ], [ 5, 6 ], [ 7, 6 ]]
print(minReversals(edges))







