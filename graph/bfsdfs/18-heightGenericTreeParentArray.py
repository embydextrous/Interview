'''
We are given a tree of size n as array parent[0..n-1] where every index i in the parent[] represents 
a node and the value at i represents the immediate parent of that node. For root node value will be -1. 
Find the height of the generic tree given the parent links.

Examples: 

Input : parent[] = {-1, 0, 0, 0, 3, 1, 1, 2}
Output : 2

Height of a generic tree from parent array 1
'''
from graph import Graph

def findHeight(parentArray):
    n = len(parentArray)
    g = Graph(n)
    root = None
    for i in range(n):
        if parentArray[i] == -1:
            root = i
            continue
        g.addEdge(parentArray[i], i)
    h = 0
    q1, q2 = [root], []
    while len(q1) > 0:
        while len(q1) > 0:
            u = q1.pop(0)
            for v in g.graph[u]:
                q2.append(v)
        q1, q2 = q2, q1
        if len(q1) == 0:
            return h
        h += 1

parentArray = [-1, 0, 1, 2, 3]
print(findHeight(parentArray))
