'''
Given a graph and a source vertex in the graph, find the shortest paths from the source to all vertices in the given graph.
Below are the detailed steps used in Dijkstra's algorithm to find the shortest path from a single source vertex to all other vertices in the given graph. 

Algorithm 
1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in the shortest-path tree, i.e., whose minimum distance from the source 
is calculated and finalized. Initially, this set is empty. 
2) Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so 
that it is picked first. 
3) While sptSet doesn't include all vertices 
    a) Pick a vertex u which is not there in sptSet and has a minimum distance value. 
    b) Include u to sptSet. 
    c) Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex v, if the 
    sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v. 
'''
from collections import deque
from graph import WeightedUndirectedGraph
from heapq import heapify, heappop

INF = 10 ** 9

class HeapNode:
    def __init__(self, distance, i):
        self.distance = distance
        self.i = i
        self.parent = -1

    def __lt__(self, other):
        return self.distance < other.distance

    def __lte__(self, other):
        return self.distance <= other.distance

def djikstra(g, s):
    nodeMap = { i:HeapNode(INF, i) for i in range(g.V) }
    nodeMap[s].distance = 0
    dist = [nodeMap[i] for i in range(g.V)]
    isInHeap = [True for i in range(g.V)]
    heapify(dist)
    while len(dist) > 0:
        node = heappop(dist)
        u, d = node.i, node.distance
        for (v, w) in g.graph[u]:
            if isInHeap[v] and d + w < nodeMap[v].distance:
                nodeMap[v].distance = d + w
                nodeMap[v].parent = u
        heapify(dist)
        isInHeap[u] = False
    for i in range(g.V):
        print(f"Shortest distance from node {s} to {i} is of length {nodeMap[i].distance}")
        path = deque([i])
        current = nodeMap[i]
        while current.parent != -1:
            path.appendleft(current.parent)
            current = nodeMap[current.parent]
        print(path)

g = WeightedUndirectedGraph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

djikstra(g, 0)