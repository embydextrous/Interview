'''
Given a graph G and an integer K, K-cores of the graph are connected components that are left after
all vertices of degree less than k have been removed
'''
from graph import UndirectedHashGraph

def dfs(g, s, visited, degrees, k):
    visited.add(s)
    for v in g.graph[s]:
        if degrees[s] < k:
            degrees[v] -= 1
        if v not in visited:
            dfs(g, v, visited, degrees, k)

def printKCores(g, k):
    visited = set()
    degrees = [len(g.graph[i]) for i in range(g.V)]
    for i in range(g.V):
        if i not in visited:
            dfs(g, i, visited, degrees, k)
    for i in range(g.V):
        if degrees[i] >= k:
            adj = g.graph[i].copy()
            for v in g.graph[i]:
                if degrees[v] < k:
                    adj.remove(v)
            print("{} -> {}".format(i, adj))

def dfsUtil(g, s, visited, k):
    visited[s] = True
    adj = g.graph[s].copy()
    for v in adj:
        if len(g.graph[s]) < k:
            g.removeEdge(s, v)
            if len(g.graph[v]) < k:
                visited[v] = False
        if not visited[v]:
            dfsUtil(g, v, visited, k)
    if len(g.graph[s]) == 0:
        g.graph.pop(s)

def kCores(g, k):
    visited = [False] * g.V
    for i in range(g.V):
        if not visited[i]:
            dfsUtil(g, i, visited, k)

k = 3
g1 = UndirectedHashGraph(9)
g1.addEdge(0, 1) #1
g1.addEdge(0, 2) 
g1.addEdge(1, 2) #2
g1.addEdge(1, 5)
g1.addEdge(2, 3)
g1.addEdge(2, 4)
g1.addEdge(2, 5)
g1.addEdge(2, 6)
g1.addEdge(3, 4)
g1.addEdge(3, 6)
g1.addEdge(3, 7)
g1.addEdge(4, 6)
g1.addEdge(4, 7)
g1.addEdge(5, 6)
g1.addEdge(5, 8)
g1.addEdge(6, 7)
g1.addEdge(6, 8)
g1.print()
print()
kCores(g1, k)
g1.print()