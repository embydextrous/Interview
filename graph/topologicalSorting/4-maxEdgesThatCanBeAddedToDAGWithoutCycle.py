# https://www.geeksforgeeks.org/maximum-edges-can-added-dag-remains-dag/

'''
            5 ----> 0 <---- 4
            |               | 
            ↓               ↓ 
            2 ----> 3 ----> 1

Solution 

1. Find topo.
2. For every u, v pair in topo if there is not already an edge count for it.
'''
from graph import HashGraph

def dfs(g, u, ts, visited):
    visited[u] = True
    for v in g.graph[u]:
        if not visited[v]:
            dfs(g, v, ts, visited)
    ts.append(u)

def topo(g):
    visited = [False] * g.V
    ts = []
    for i in range(g.V):
        if not visited[i]:
            dfs(g, i, ts, visited)
    return ts[::-1]

def maxEdges(g):
    ts = topo(g)
    c = 0
    for i in range(g.V - 1):
        u = ts[i]
        for j in range(i + 1, g.V):
            v = ts[j]
            if v not in g.graph[u]:
                c += 1
    return c
            
g = HashGraph(6)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(5, 0)
g.addEdge(5, 2)

print(maxEdges(g))
