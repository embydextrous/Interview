# https://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/
from tree import Node

def printKPathUtil(root, path, k):
    if root is None:
        return
    path.append(root.data)
    printKPathUtil(root.left, path, k)
    printKPathUtil(root.right, path, k)
    f = 0
    for j in range(len(path) - 1, -1, -1):
        f += path[j]
        if (f == k):
            print(path[j:])
    path.pop()

def printKPath(root, k):
    path = []
    printKPathUtil(root, path, k)

'''
           1
        /     \
      3        -1
    /   \     /   \
   2     1   4     5                        
        /   / \     \                    
       1   1   2     6   
'''

root = Node(1)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(1)
root.left.right.left = Node(1)
root.right = Node(-1)
root.right.left = Node(4)
root.right.left.left = Node(1)
root.right.left.right = Node(2)
root.right.right = Node(5)
root.right.right.right = Node(6)
 
k = 7
printKPath(root, k)