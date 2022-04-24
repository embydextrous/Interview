import heapq
from tree import Node
from collections import deque, defaultdict

def printNodesAtKDistanceDown(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data, end = " ")
    printNodesAtKDistanceDown(root.left, k - 1)
    printNodesAtKDistanceDown(root.right, k - 1)

# 20, 22, 24, 25, 26, 27, 28, 29 
def printNodesAtDistanceK(root, source, k):
    if root is None:
        return -1
    if root == source:
        printNodesAtKDistanceDown(root, k)
        return 0
    dl = printNodesAtDistanceK(root.left, source, k)
    if dl != -1:
        if dl + 1 == k:
            print(root.data, end = " ")
        else:
            printNodesAtKDistanceDown(root.right, k - dl - 2)
        return dl + 1
    dr = printNodesAtDistanceK(root.right, source, k)
    if dr != -1:
        if dr + 1 == k:
            print(root.data, end = " ")
        else:
            printNodesAtKDistanceDown(root.left, k - dr - 2)
        return dr + 1
    return -1






'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
'''
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)

printNodesAtDistanceK(root, root.left, 4)
print()


