from tree import Node, inorder
from collections import deque

# 10, 15, 20, 23, 25, 28, 29, 30
# 31, 32, 33, 34, 36, 37, 38, 39

def connectNodes(root):
    if root is None:
        return
    while root:
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                


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



'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
'''
root = removesLeavesLessThanK(root, 3)
inorder(root)
print()