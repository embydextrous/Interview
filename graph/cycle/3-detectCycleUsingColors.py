# 0 means white, 1 means grey, 2 means black
from graph import Graph

WHITE = 0
GREY = 1
BLACK = 2

def isCyclicUtil(g, u, color):
    color[u] = GREY
    for v in g.graph[u]:
        if color[v] == WHITE:
            if isCyclicUtil(g, v, color):
                return True
        elif color[v] == GREY:
            return True
    color[u] = BLACK
    return False

def isCyclic(g):
    color = [WHITE] * g.V
    for u in range(g.V):
        if color[u] == WHITE:
            if isCyclicUtil(g, u, color):
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