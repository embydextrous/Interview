from tree import Node
from collections import deque

def isPerfectTreeUtil(root, leafLevel, level):
    if root.left is None and root.right is None:
        return leafLevel == level
    if root.left is None or root.right is None:
        return False
    return isPerfectTreeUtil(root.left, leafLevel, level + 1) and isPerfectTreeUtil(root.right, leafLevel, level + 1)
    

def isPerfectTree(root):
    if root is None:
        return True
    leafLevel = 0
    current = root
    while current.left:
        current = current.left
        leafLevel += 1
    return isPerfectTreeUtil(root, leafLevel, 0)


    

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
#root.left.left = Node(1)
#root.left.right = Node(16)
#root.left.right.left = Node(4)
#root.left.right.right = Node(7)
root.right = Node(10)
#root.right.right = Node(14)
#root.right.right.left = Node(19)
#root.right.right.right = Node(2)

print(isPerfectTree(root))

root = Node(8)

root.left = Node(3)
root.right = Node(10)


root.left.left = Node(1)
root.left.right = Node(16)
root.right.left = Node(11)
root.right.right = Node(14)


root.left.left.left = Node(12)
root.left.left.right = Node(20)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.left.left = Node(13)
root.right.left.right = Node(11)
root.right.right.left = Node(19)
#root.right.right.right = Node(2)

print(isPerfectTree(root))