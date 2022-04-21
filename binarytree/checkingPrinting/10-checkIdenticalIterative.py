from tree import Node
from collections import deque

def areIdentical(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    q1, q2 = deque([a]), deque([b])
    while len(q1) > 0 and len(q2) > 0:
        n1, n2 = q1.pop(0), q2.pop(0)
        print(n1, n2)
        if n1.data != n2.data:
            return False
        if n1.left and n2.left:
            q1.append(n1.left)
            q2.append(n2.left)
        elif n1.left or n2.left:
            return False
        if n1.right and n2.right:
            q1.append(n1.right)
            q2.append(n2.right)
        elif n1.right or n2.right:
            return False
    return True

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

print(areIdentical(root.left, root.left))