'''
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for 
every directed edge (u, v), vertex u comes before v in the ordering. 

Topological Sorting for a graph is not possible if the graph is not a DAG.

            5 ----> 0 <---- 4
            |               | 
            ↓               ↓ 
            2 ----> 3 ----> 1
                   

For example, a topological sorting of the following graph is “5 4 2 3 1 0”. 
There can be more than one topological sorting for a graph. 
For example, another topological sorting of the following graph is “4 5 2 3 1 0”. 
The first vertex in topological sorting is always a vertex with in-degree as 0 (a vertex with no incoming edges).
'''

'''
Algorithm to find Topological Sorting -> Use Recursion Stack
'''
from graph import Graph

def dfs(g, u, ts, visited):
    visited[u] = True
    for v in g.graph[u]:
        if not visited[v]:
            dfs(g, v, ts, visited)
    ts.append(u)

def topo(g):
    ts = [] # Used as stack
    visited = [False] * g.V
    for v in range(g.V):
        if not visited[v]:
            dfs(g, v, ts, visited)
    return ts[::-1]

g = Graph(6)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(5, 0)
g.addEdge(5, 2)

print(topo(g))