import re
from tree import Node

# Also see https://www.geeksforgeeks.org/find-sum-right-leaves-given-binary-tree/

def sumOfLeftLeaves(root, isLeftChild):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data if isLeftChild else 0
    return sumOfLeftLeaves(root.left, True) + sumOfLeftLeaves(root.right, False)

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

print(sumOfLeftLeaves(root, False))