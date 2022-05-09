# https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/
# https://www.geeksforgeeks.org/applications-of-depth-first-search/
from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[] for i in range(V)]

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def print(self):
        for i in range(self.V):
            print("{} -> {}".format(i, self.graph[i]))

class HashGraph:
    def __init__(self, V):
        self.graph = {}
        self.V = V
        for i in range(V):
            self.graph[i] = set()

    def addEdge(self, u, v):
        self.graph[u].add(v)

    def removeEdge(self, u, v):
        self.graph[u].remove(v)

    def print(self):
        for i in self.graph.keys():
            print("{} -> {}".format(i, self.graph[i]))

class UndirectedHashGraph:
    def __init__(self, V):
        self.graph = {}
        self.V = V
        for i in range(V):
            self.graph[i] = set()

    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def removeEdge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def print(self):
        for i in self.graph:
            print("{} -> {}".format(i, self.graph[i]))

class UndirectedGraph:
    def __init__(self, V):
        self.V = V
        self.graph = [[] for i in range(V)]

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def print(self):
        for i in range(self.V):
            print("{} -> {}".format(i, self.graph[i]))

def bfs(graph, s):
    visited = [False] * graph.V
    q = [s]
    visited[s] = True
    while len(q) > 0:
        u = q.pop(0)
        print(u, end = " ")
        for v in graph.graph[u]:
            if not visited[v]:
                q.append(v)
                visited[v] = True
    print()

def dfsUtil(graph, u, visited):
    visited[u] = True
    print(u, end = " ")
    for v in graph.graph[u]:
        if not visited[v]:
            dfsUtil(graph, v, visited)

def dfs(graph):
    visited = [False] * graph.V
    for i in range(graph.V):
        if not visited[i]:
            dfsUtil(graph, i, visited)
    print()

def iterativeDfs(graph):
    visited = [False] * graph.V
    for i in range(graph.V):
        if not visited[i]:
            s = [[i, 0]]
            while len(s) > 0:
                (u, idx) = s[-1]
                if not visited[u]:
                    print(u, end = " ")
                    visited[u] = True
                while idx < len(graph.graph[u]) and visited[graph.graph[u][idx]]:
                    idx += 1
                if idx == len(graph.graph[u]):
                    s.pop()
                else:
                    s[-1][1] = idx + 1
                    s.append([graph.graph[u][idx], 0])
    print()

'''
i -> 0
s -> 
u -> 1
idx 
0 -> {1, 2} - T
1 -> {0, 2, 5} - T
2 -> {0, 1, 3, 4, 5, 6} - T
3 -> {2, 4, 6, 7} - T
4 -> {2, 3, 6, 7} - T
5 -> {8, 1, 2, 6} - T
6 -> {2, 3, 4, 5, 7, 8} - T
7 -> {3, 4, 6} - T
8 -> {5, 6} - T

0 1 2 3 4 6 5 8 7
'''

def printMatrix(M):
    R, C = len(M), len(M[0])
    for i in range(R):
        for j in range(C):
            print(M[i][j], end = " ")
        print()

'''
g1 = UndirectedGraph(9)
g1.addEdge(0, 1) #1
g1.addEdge(0, 2) 
g1.addEdge(1, 2) #2
g1.addEdge(1, 5)
g1.addEdge(2, 3)
g1.addEdge(2, 4)
g1.addEdge(2, 5)
g1.addEdge(2, 6)
g1.addEdge(3, 4)
g1.addEdge(3, 6)
g1.addEdge(3, 7)
g1.addEdge(4, 6)
g1.addEdge(4, 7)
g1.addEdge(5, 6)
g1.addEdge(5, 8)
g1.addEdge(6, 7)
g1.addEdge(6, 8)
g1.print()
iterativeDfs(g1)
'''