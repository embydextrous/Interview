from tree import Node

def areIdentical(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.data == b.data and areIdentical(a.left, b.left) and areIdentical(a.right, b.right)

def isSubTree(a, b):
    if b is None:
        return True
    if a is None:
        return False
    if areIdentical(a, b):
        return True
    return isSubTree(a.left, b) or isSubTree(a.right, b)


'''
        1
      /   \
     2      3
   /  \      \
  4    5      7
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print(isSubTree(root.left, root.left))