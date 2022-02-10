# https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/
# https://www.geeksforgeeks.org/applications-of-depth-first-search/

class GraphNode:
    def __init__(self, data):
        self.data = data
        self.next = []

    def __str__(self) -> str:
        return "{} -> {}".format(self.data, self.next)

    def __repr__(self) -> str:
        return str(self.data)

class Graph:
    def __init__(self):
        self.vertices = []

    def addVertex(self, data):
        vertex = GraphNode(data)
        self.vertices.append(vertex)
        return vertex

    def addEdge(self, u, v):
        u.next.append(v)

    def print(self):
        for vertex in self.vertices:
            print(vertex)

class UndirectedGraph:
    def __init__(self):
        self.vertices = []

    def addVertex(self, data):
        vertex = GraphNode(data)
        self.vertices.append(vertex)
        return vertex

    def addEdge(self, u, v):
        u.next.append(v)
        v.next.append(u)

    def print(self):
        for vertex in self.vertices:
            print(vertex)

def bfs(vertex):
    if vertex is None:
        return
    visited = set()
    q = [vertex]
    visited.add(vertex)
    while len(q) > 0:
        u = q.pop(0)
        print(u.data, end = " ")
        for v in u.next:
            if v not in visited:
                q.append(v)
                visited.add(v)
    print()

def dfsUtil(vertex, visited):
    visited.add(vertex)
    print(vertex.data, end = " ")
    for neighbor in vertex.next:
        if neighbor not in visited:
            dfsUtil(neighbor, visited)

def dfs(vertex):
    visited = set()
    dfsUtil(vertex, visited)
    print()