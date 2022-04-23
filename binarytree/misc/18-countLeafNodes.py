from tree import Node

def countLeaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return countLeaves(root.left) + countLeaves(root.right)

def countNonLeaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return 1 + countNonLeaves(root.left) + countNonLeaves(root.right)

def countFullNodes(root):
    if root is None:
        return 0
    if root.left is None:
        return countFullNodes(root.right)
    if root.right is None:
        return countFullNodes(root.left)
    return 1 + countFullNodes(root.left) + countFullNodes(root.right)

def countHalfNodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    if root.left is None:
        return 1 + countHalfNodes(root.right)
    if root.right is None:
        return 1 + countHalfNodes(root.left)
    return countHalfNodes(root.left) + countHalfNodes(root.right)
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
print(countLeaves(root))
print(countNonLeaves(root))
print(countFullNodes(root))
print(countHalfNodes(root))


