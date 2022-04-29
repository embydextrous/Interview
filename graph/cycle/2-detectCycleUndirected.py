from graph import UndirectedGraph

def isCyclicUtil(g, u, visited, parent):
    visited[u] = True
    for v in g.graph[u]:
        if v != parent:
            if not visited[v]:
                if isCyclicUtil(g, v, visited, u):
                    return True
            else:
                return True
    return False

def isCyclic(g):
    visited = [False] * g.V
    for u in range(g.V):
        if not visited[u]:
            print(u)
            if isCyclicUtil(g, u, visited, None):
                return True
    return False

'''
g = UndirectedGraph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
 
print(isCyclic(g))
'''

g1 = UndirectedGraph(3)
g1.addEdge(0,1)
g1.addEdge(1,2)
g1.print()
print(isCyclic(g1))
