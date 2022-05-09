'''
Given an undirected tree with some marked nodes and a positive number K. We need to print the count of all 
such nodes which have distance from all marked nodes less than K that means every node whose distance from 
all marked nodes is less than K, should be counted in the result. 
Examples: 
   (1)     (2)      (4)
     \      |       /
      0 --- 3 ---- 5
     /    /   \     \
    8    6     7     9
 
In above tree we can see that node with index 
0, 2, 3, 5, 6, 7 have distances less than 3
from all the marked nodes.
so answer will be 6
'''
from graph import UndirectedGraph

def getNodesWithinKDistance(g, s, k):
    result = set()
    q = [[s, 0]]
    while len(q) > 0:
        u, d = q.pop(0)
        if d <= k:
            result.add(u)
        if d < k:
            for v in g.graph[u]:
                q.append([v, d + 1])
    return result

def getNodesAtDistanceKFromMarkedNodes(g, markedNodes, k):
    result = set([i for i in range(g.V)])
    for markedNode in markedNodes:
        result = result.intersection(getNodesWithinKDistance(g, markedNode, k))
    return result

g = UndirectedGraph(10)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(0, 8)
g.addEdge(2, 3)
g.addEdge(3, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)
g.addEdge(4, 5)
g.addEdge(5, 9)
markedNodes = [1, 2, 4]
print(getNodesAtDistanceKFromMarkedNodes(g, markedNodes, 3))



