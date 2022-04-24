from tree import Node
from collections import deque, defaultdict

# 19 20 21 22 23 24 25 26 27

def sumOfHeights(root, sumHeights):
    if root is None:
        return 0
    lHeight = sumOfHeights(root.left, sumHeights)
    rHeight = sumOfHeights(root.right, sumHeights)
    height = 1 + max(lHeight, rHeight)
    print(root.data, height)
    sumHeights[0] += height
    return height


'''
        8
      /   \
     3     0
   /   \     \
  1    6      4
      /  \   /  \
     4    7 9    2
'''


root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(0)
root.right.right = Node(4)
root.right.right.left = Node(9)
root.right.right.right = Node(2)

sumHeights = [0]
sumOfHeights(root, sumHeights)
print(sumHeights[0])