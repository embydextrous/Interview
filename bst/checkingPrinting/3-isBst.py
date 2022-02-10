from bst import Node, insert
import sys

def isBst(root, low, high):
    if root is None:
        return True
    if root.data < low or root.data > high:
        return False
    return isBst(root.left, low, root.data - 1) and isBst(root.right, root.data + 1, high)

'''
            7
          /   \
         3     12
        / \    /
       1   5  8
          /    \
         4      11
'''

root = Node(7)
insert(root, 3)
insert(root, 12)
insert(root, 5)
insert(root, 1)
insert(root, 4)
insert(root, 8)
insert(root, 11)

MAX = sys.maxsize
MIN = -sys.maxsize-1
print(isBst(root, MIN, MAX))
root.left.data = 9
print(isBst(root, MIN, MAX))
