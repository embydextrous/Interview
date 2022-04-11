from graph import HashGraph

def transpose(g):
    tp = HashGraph(g.V)
    for u in range(g.V):
        for v in g.graph[u]:
            tp.addEdge(v, u)
    return tp

g = HashGraph(5)
g.addEdge(0, 1) 
g.addEdge(0, 4) 
g.addEdge(0, 3) 
g.addEdge(2, 0) 
g.addEdge(3, 2) 
g.addEdge(4, 1) 
g.addEdge(4, 3)
g.print()
print()
transpose(g).print()