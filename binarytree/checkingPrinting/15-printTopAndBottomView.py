from tree import Node
from collections import deque

def printTopView(root):
    if root is None:
        return
    d = {}
    q = deque([(root, 0)])
    mini, maxi = 0, 0
    while len(q) > 0:
        (node, vd) = q.popleft()
        mini = min(mini, vd)
        maxi = max(maxi, vd)
        if vd not in d:
            d[vd] = node.data
        if node.left:
            q.append((node.left, vd - 1))
        if node.right:
            q.append((node.right, vd + 1))
    for vd in range(mini, maxi + 1):
        print(d[vd], end = " ")
    print()

def printBottomView(root):
    if root is None:
        return
    d = {}
    q = deque([(root, 0)])
    mini, maxi = 0, 0
    while len(q) > 0:
        (node, vd) = q.popleft()
        mini = min(mini, vd)
        maxi = max(maxi, vd)
        d[vd] = node.data
        if node.left:
            q.append((node.left, vd - 1))
        if node.right:
            q.append((node.right, vd + 1))
    for vd in range(mini, maxi + 1):
        print(d[vd], end = " ")
    print()

"""
        1
       / \
      2   3
       \
        4
         \
          5
           \
            6
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
printTopView(root)
printBottomView(root)
