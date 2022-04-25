# https://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/
from tree import Node

def printKSumPaths(root, k, path, pathSum, prefixSums):
    if root is None:
        return
    pathSum += root.data
    path.append(root.data)
    if pathSum == k:
        print(path)
    if pathSum - k in prefixSums:
        print(path[prefixSums[pathSum - k] + 1:])
    prefixSums[pathSum] = len(path) - 1
    printKSumPaths(root.left, k, path, pathSum, prefixSums)
    printKSumPaths(root.right, k, path, pathSum, prefixSums)
    prefixSums.pop(pathSum)
    path.pop()

def printKPath(root, k):
    path = []
    prefixSums = {}
    printKSumPaths(root, k, path, 0, prefixSums)

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
 
k = 6
printKPath(root, k)