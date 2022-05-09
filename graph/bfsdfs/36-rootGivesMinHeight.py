'''
Given an undirected graph, which has tree characteristics. It is possible to choose any node as root, 
the task is to find those nodes only which minimize the height of tree. 

Example: 
In below diagram all node are made as root one by one, we can see that when 3 and 4 are root, height of tree 
is minimum(2) so {2, 3} is our answer. 
 
          0 -- (2) -- 1 -- 7
                |
          6 -- (3) -- 4 -- 5
                      |    |
                      9    8
'''
from graph import UndirectedGraph

def findRoot(g):
    degrees = [len(g.graph[i]) for i in range(g.V)]
    q1, q2 = [], []
    for i in range(g.V):
        if degrees[i] == 1:
            q1.append(i)
    nodesLeft = g.V
    while len(q1) > 0 and nodesLeft > 2:
        while len(q1) > 0:
            u = q1.pop(0)
            degrees[u] = 0
            nodesLeft -= 1
            for v in g.graph[u]:
                if degrees[v] != 0:
                    degrees[v] -= 1
                    if degrees[v] == 1:
                        q2.append(v)
        q1, q2 = q2, q1
    return q1

g = UndirectedGraph(10)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(1, 7)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(3, 6)
g.addEdge(4, 5)
g.addEdge(4, 9)
g.addEdge(5, 8)

print(findRoot(g))