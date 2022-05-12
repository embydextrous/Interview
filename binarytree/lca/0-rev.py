from collections import deque
from re import S
from tree import Node

def pathDown(root, a, path, isLeftChild):
    if root is None:
        return False
    if root == a:
        if isLeftChild != None:
            path.appendleft("L" if isLeftChild else "R")
        return True
    hasPathDown = pathDown(root.left, a, path, True)
    if hasPathDown:
        if isLeftChild != None:
            path.appendleft("L" if isLeftChild else "R")
        return True
    hasPathDown = pathDown(root.right, a, path, False)
    if hasPathDown:
        if isLeftChild != None:
            path.appendleft("L" if isLeftChild else "R")
        return True
    return False

def pathUtil(root, a, b, result, isLeftChild):
    if root is None:
        return None
    if root == a:
        path = deque()
        if pathDown(a, b, path, None):
            result[0] = "".join(path)
        if isLeftChild is None:
            return None
        return "L" if isLeftChild else "R"
    if root == b:
        path = deque()
        if pathDown(b, a, path, None):
            result[0] = "".join(path)
        if isLeftChild is None:
            return None
        return "L" if isLeftChild else "R"
    left = pathUtil(root.left, a, b, result, True)
    right = pathUtil(root.right, a, b, result, False)
    if left and right:
        result[0] = "".join((['U'] * len(left)) + list(right))
        return result[0]
    if left is None and right is None:
        return None
    if isLeftChild is None:
        toAppend = ""
    else:
        toAppend = "L" if isLeftChild else "R"
    return toAppend + (left if left else right)

def path(root, a, b):
    result = [None]
    pathUtil(root, a, b, result, None)
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
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(11)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)

print(path(root, root.left.left, root.right.right.left))

