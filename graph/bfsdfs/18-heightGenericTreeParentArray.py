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

def findHeight(parent):
    maxH = 0
    for i in range(len(parent)):
        h = 0
        k = i
        while parent[k] != -1:
            h += 1
            k = parent[k]
        maxH = max(maxH, h)
    return maxH

parent = [-1, 0, 1, 1, 2, 3, 2, 4, 3, 5, 6]
print(findHeight(parent))

parentArray = [-1, 0, 1, 2, 3]
print(findHeight(parentArray))
