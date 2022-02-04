from tree import Node
import sys

# https://www.geeksforgeeks.org/maximum-difference-between-node-and-its-ancestor-in-binary-tree/

# Function returns minimum value
def maxDiffUtil(root, result):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    lMin = maxDiffUtil(root.left, result)
    rMin = maxDiffUtil(root.right, result)
    result[0] = max(result[0], root.data - min(lMin, rMin))
    return min(lMin, rMin, root.data)

def maxDiff(root):
    result = [-sys.maxsize-1]
    maxDiffUtil(root, result)
    return result[0]

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
root.left.right.left = Node(0)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)
print(maxDiff(root))