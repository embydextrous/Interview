# https://www.geeksforgeeks.org/count-number-nodes-given-level-using-bfs/

# Also see, https://www.geeksforgeeks.org/level-node-tree-source-node-using-bfs/
# Also see, https://www.geeksforgeeks.org/minimum-number-of-edges-between-two-vertices-of-a-graph/
from graph import Graph
from collections import deque

def numNodesAtLevel(g, root, level):
    q1, q2 = deque([root]), deque()
    lvl = 0
    while len(q1) > 0 and lvl != level:
        while len(q1) > 0:
            x = q1.popleft()
            for i in g.graph[x]:
                q2.append(i)
        q1, q2 = q2, q1
        lvl += 1
    return len(q1)

'''
        0
       / \ 
      1   2
     /  / | \
    3   4 5  8
   / \
  6   7     
'''
g = Graph(9)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)
g.addEdge(2, 8)
print(numNodesAtLevel(g, 0, 1))