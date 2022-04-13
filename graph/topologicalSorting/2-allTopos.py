'''
Given a DAG, print all topological sorts of the graph.

For example, consider the below graph.

            5 ----> 0 <---- 4
            |               | 
            ↓               ↓ 
            2 ----> 3 ----> 1

All topological sorts of the given graph are:

4 5 0 2 3 1 
4 5 2 0 3 1 
4 5 2 3 0 1 
4 5 2 3 1 0 
5 2 3 4 0 1 
5 2 3 4 1 0 
5 2 4 0 3 1 
5 2 4 3 0 1 
5 2 4 3 1 0 
5 4 0 2 3 1 
5 4 2 0 3 1 
5 4 2 3 0 1 
5 4 2 3 1 0 
 
In a DAG many a times we can have vertices which are unrelated to each other because of which we can order 
them in many ways. These various topological sorting is important in many cases, for example if some 
relative weight is also available between the vertices, which is to minimize then we need to take 
care of relative ordering as well as their relative weight, which creates the need of checking 
through all possible topological ordering. 
'''
def findAndPrintAllTopos(g, V, indegrees, visited, path):
    for u in range(V):
        if indegrees[u] == 0 and not visited[u]:
            visited[u] = True
            path.append(u)
            for v in g[u]:
                indegrees[v] -= 1
            findAndPrintAllTopos(g, V, indegrees, visited, path)
            visited[u] = False
            path.pop()
            for v in g[u]:
                indegrees[v] += 1
    if len(path) == V:
        print(path)

def printAllTopos(edges, V):
    g = {i:[] for i in range(V)}
    indegrees = [0] * V
    visited = [False] * V
    for (u, v) in edges:
        indegrees[v] += 1
        g[u].append(v)
    path = []
    findAndPrintAllTopos(g, V, indegrees, visited, path)

edges = [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)]
printAllTopos(edges, 6)