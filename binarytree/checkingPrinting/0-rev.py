from tree import Node
from collections import deque, defaultdict

def printBottomView(root):
    if root is None:
        return
    q = deque([(root, 0)])
    d = {}
    maxi, mini = 0, 0
    while len(q) > 0:
        (node, vd) = q.popleft()
        d[vd] = node.data
        maxi = max(maxi, vd)
        mini = min(mini, vd)
        if node.left:
            q.append((node.left, vd - 1))
        if node.right:
            q.append((node.right, vd + 1))
    for vd in range(mini, maxi + 1):
        print(d[vd], end = " ")
    print()






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

printBottomView(root)

