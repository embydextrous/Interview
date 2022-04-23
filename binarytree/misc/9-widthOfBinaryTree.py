from tree import Node
from collections import deque

def width(root):
    if root is None:
        return 0
    q = deque([(root, 0)])
    maxi = mini = 0
    while len(q) > 0:
        (node, d) = q.popleft()
        maxi = max(d, maxi)
        mini = min(d, mini)
        if node.left:
            q.append((node.left, d - 1))
        if node.right:
            q.append((node.right, d + 1))
    return maxi - mini + 1

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
print(width(root))
