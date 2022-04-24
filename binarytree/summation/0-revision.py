from tree import Node
from collections import deque, defaultdict


def maxSpiralSum(root):
    if root is None:
        return 0
    maxSoFar = -10 ** 9
    maxEndingHere = 0
    s1, s2 = deque([root]), deque()
    while len(s1) > 0:
        while len(s1) > 0:
            node = s1.pop()
            maxEndingHere += node.data
            if maxSoFar < maxEndingHere:
                maxSoFar = maxEndingHere
            if maxEndingHere < 0:
                maxEndingHere = 0
            if node.left:
                s2.append(node.left)
            if node.right:
                s2.append(node.right)
        while len(s2) > 0:
            node = s2.pop()
            maxEndingHere += node.data
            if maxSoFar < maxEndingHere:
                maxSoFar = maxEndingHere
            if maxEndingHere < 0:
                maxEndingHere = 0
            if node.right:
                s1.append(node.right)
            if node.left:
                s1.append(node.left)
    return maxSoFar


'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19    2
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

print(maxSpiralSum(root))