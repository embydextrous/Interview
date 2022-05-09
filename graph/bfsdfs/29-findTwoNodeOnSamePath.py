# https://www.geeksforgeeks.org/check-if-two-nodes-are-on-same-path-in-a-tree/
'''
Given a tree (not necessarily a binary tree) and a number of queries such that every query takes 
two nodes of the tree as parameters. For every query pair, find if two nodes are on the same path 
from the root to the bottom.

For example, consider the below tree, if given queries are (1, 5), (1, 6), and (2, 6), then answers 
should be true, true, and false respectively. 
'''
from collections import defaultdict
from email.policy import default
from graph import UndirectedGraph

class Solution:
    def __init__(self, g, root):
        self.timeMap = defaultdict(list)
        self.fillTimeMap(g, root, None, [0])

    def fillTimeMap(self, g, root, parent, time):
        time[0] += 1
        self.timeMap[root].append(time[0])
        for v in g.graph[root]:
            if v != parent:
                self.fillTimeMap(g, v, root, time)
        time[0] += 1
        self.timeMap[root].append(time[0])

    def areOnSamePath(self, u, v):
        enterU, exitU = self.timeMap[u]
        enterV, exitV = self.timeMap[v]
        return (enterV > enterU and exitV < exitU) or (enterU > enterV and exitU < exitV)


g = UndirectedGraph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
g.print()
solution = Solution(g, 0)
print(solution.areOnSamePath(2, 5))

