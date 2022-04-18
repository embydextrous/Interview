from tree import Node
from collections import deque

def nthNodePostOrder(root, n):
    if root:
        nthNodePostOrder(root.left, n)
        nthNodePostOrder(root.right, n)
        n[0] -= 1
        if n[0] == 0:
            print(root.data)

# 8 3 1 16 4 3 7 10 14 19 2
# 1 3 3 4 16 7 8 10 19 14 2

# preIndex = 0, inoLeft = 0, inoRight = 10
#     preIndex = 1, inoLeft = 0, inoRight = 5
#           preIndex = 2, inoLeft = 0, inoRight = 0#
#           preIndex = 2, inoLeft = 2, inoRight = 5#
#     preIndex = 7, inoLeft = 7, inoRight = 10

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
    /
   3 
'''

root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.left.left = Node(3)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)


nthNodePostOrder(root, [7])