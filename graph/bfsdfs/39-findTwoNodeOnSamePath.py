# https://www.geeksforgeeks.org/check-if-two-nodes-are-on-same-path-in-a-tree/
'''
Given a tree (not necessarily a binary tree) and a number of queries such that every query takes 
two nodes of the tree as parameters. For every query pair, find if two nodes are on the same path 
from the root to the bottom.

For example, consider the below tree, if given queries are (1, 5), (1, 6), and (2, 6), then answers 
should be true, true, and false respectively. 
'''
from graph import UndirectedGraph

class Solution:
    def __init__(self, g, root):
        self.root = root
        self.timeMap = {}
        self.g = g
        self.fillTimeMap(root, [0], set())

    def fillTimeMap(self, u, time, visited):
        visited.add(u)
        self.timeMap[u] = [time[0], -1]
        time[0] += 1
        for v in self.g.graph[u]:
            if v not in visited:
                self.fillTimeMap(v, time, visited)
                time[0] += 1
        self.timeMap[u][1] = time[0]

    def areOnSamePath(self, u, v):
        return self.timeMap[v][0] > self.timeMap[u][0] and self.timeMap[v][1] < self.timeMap[u][1]or self.timeMap[u][0] > self.timeMap[v][0] and self.timeMap[u][1] < self.timeMap[v][1]


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

