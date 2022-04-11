'''
Given a directed graph, find out if a vertex v is reachable from another vertex u for all vertex 
pairs (u, v) in the given graph. Here reachable means that there is a path from vertex u to v. 
The reachability matrix is called transitive closure of a graph.
'''
from graph import Graph, printMatrix

def dfs(g, s, t, tc):
    if(s == t):
        # Check if graph points to itself, necessary as entry function calls for same value of s and t
        if(t in g.graph[s]):
            tc[s][t] = 1
    else:
        # t is reachable from s
        tc[s][t] = 1
    # Look for deeper nodes
    for i in g.graph[t]:
        if tc[s][i] == 0:
            if i == s:
                # Simply mark because this will be anyways called by entry function
                tc[s][i] = 1
            else:
                dfs(g, s, i, tc)

'''
Same program in case a vertex is considered to be reachable from itself:

def dfs(g, s, t, tc):
    tc[s][t] = 1
    for i in g.graph[t]:
        if tc[s][i] == 0:
            dfs(g, s, i, tc)
'''
def transitiveClosure(g):
    tc = [[0 for i in range(g.V)] for j in range(g.V)]
    for i in range(g.V):
        dfs(g, i, i, tc)
    return tc

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(5, 2)
g.addEdge(5, 6)
g.addEdge(6, 4)
g.addEdge(6, 0)

printMatrix(transitiveClosure(g))