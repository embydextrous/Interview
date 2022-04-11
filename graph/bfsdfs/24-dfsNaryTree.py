'''
Since there are no cycles we can use parent info to avoid space for visited.
'''
from graph import UndirectedGraph

def dfs(g, u, parent):
    print(u, end = " ")
    for v in g.graph[u]:
        if v != parent:
            dfs(g, v, u)

'''
            0
         /  |  \   
        1   2   3
       /   / \   \
      4   5   6   7
    /              \
   9                8
'''
g = UndirectedGraph(10)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)
g.addEdge(3, 7)
g.addEdge(7, 8)
g.addEdge(4, 9)
dfs(g, 0, None)
print()