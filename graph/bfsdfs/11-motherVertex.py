'''
What is a Mother Vertex? 
A mother vertex in a graph G = (V, E) is a vertex v such that all other vertices in G can be reached 
by a path from v.
'''
from graph import Graph, dfs

def dfsUtil(graph, v, visited):
    visited[v] = True
    for u in graph.graph[v]:
        if not visited[u]:
            dfsUtil(graph, u, visited)
    

def motherVertex(graph):
    visited = [False] * graph.V
    v = 0
    for i in range(graph.V):
        if not visited[i]:
            dfsUtil(graph, i, visited)
            v = i
    visited = [False] * graph.V
    dfsUtil(graph, v, visited)
    if all(i == True for i in visited):
        return v
    return -1
    

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(5, 2)
g.addEdge(5, 6)
g.addEdge(6, 4)
g.addEdge(6, 0)

g.print()
print(motherVertex(g))