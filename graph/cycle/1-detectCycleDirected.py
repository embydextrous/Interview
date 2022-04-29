from graph import Graph

def isCycleUtil(g, u, visited, recStack):
    visited[u] = True
    recStack[u] = True
    for v in g.graph[u]:
        if not visited[v]:
            if isCycleUtil(g, v, visited, recStack):
                return True
        elif recStack[v]:
            return True
    recStack[u] = False
    return False

def isCyclic(g):
    visited = [False] * g.V
    recStack = [False] * g.V
    for u in range(g.V):
        if not visited[u]:
            if isCycleUtil(g, u, visited, recStack):
                return True
    return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.print()

print(isCyclic(g))