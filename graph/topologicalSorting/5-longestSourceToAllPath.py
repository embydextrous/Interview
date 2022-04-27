'''
Given a Weighted Directed Acyclic Graph (DAG) and a source vertex s in it, find the longest distances 
from s to all other vertices in the given graph.
'''
from collections import defaultdict, deque

def dfs(g, u, ts, visited):
    visited.add(u)
    for (v, w) in g[u]:
        if v not in visited:
            dfs(g, v, ts, visited)
    ts.appendleft(u)
    
def topologicalSorting(g):
    ts = deque()
    visited = set()
    for u in g:
        if u not in visited:
            dfs(g, u, ts, visited)
    return ts

def longestPath(edges, source):
    g = defaultdict(list)
    for (u, v, w) in edges:
        g[u].append([v, w])
        g[v]
    topo = topologicalSorting(g)
    dist = {}
    for u in g:
        if u == source:
            dist[u] = 0
        else:
            dist[u] = -10 ** 9
    for u in topo:
        for (v, w) in g[u]:
            if dist[v] < dist[u] + w:
                dist[v] = dist[u] + w
    print(dist)

edges = [(0, 1, 5), (0, 2, 3), (1, 3, 6), (1, 2, 2), (2, 4, 4), (2, 5, 2), (2, 3, 7), (3, 5, 1), (3, 4, -1), (4, 5, -2)]
longestPath(edges, 0)