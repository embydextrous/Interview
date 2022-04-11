'''
You are given a undirected graph G(V, E) with N vertices and M edges. We need to find the minimum number
of edges between a given pair of vertices (u, v).
'''
from graph import UndirectedGraph

def minEdges(g, s, d):
    visited = set()
    visited.add(s)
    q1, q2 = [s], []
    c = 0
    while len(q1) > 0:
        while len(q1) > 0:
            u = q1.pop(0)
            if u == d:
                return c
            for v in g.graph[u]:
                if v not in visited:
                    visited.add(v)
                    q2.append(v)
        q1, q2 = q2, q1
        c += 1

g1 = UndirectedGraph(9)
g1.addEdge(0, 1)
g1.addEdge(0, 2) 
g1.addEdge(1, 2)
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
print(minEdges(g1, 0, 3))