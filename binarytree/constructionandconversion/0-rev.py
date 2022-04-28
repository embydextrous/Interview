from tree import Node, inorder
from collections import deque

'''
Input
       1
      /  \
     2    3
    / \  / \
   4   5 6  7
Output:
      12
     / \
    6   3
   / \   \
  4   5   6    
'''
def flip(root, parent, result):
    if root:
        flip(root.left, root, result)
        if result[0] is None:
            result[0] = root
        root.right = parent
        if parent:
            root.left = parent.right
        else:
            root.left = None         

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)

result = [None]
flip(root, None, result)
inorder(result[0])
print()