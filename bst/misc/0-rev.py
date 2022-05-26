from collections import defaultdict, deque
from typing import Counter
from bst import Node, insert, search, inorder

# 4, 5
def correctUtil(root, prev, a, b):
    if root:
        correctUtil(root.left, prev, a, b)
        if prev[0]:
            if a[0]:
                if root.data < prev[0].data:
                    b[0] = root
            else:
                if root.data < prev[0].data:
                    a[0] = prev[0]
        prev[0] = root
        correctUtil(root.right, prev, a, b)

def correct(root):
    if root is None:
        return
    a = [None]
    b = [None]
    correctUtil(root, [None], a, b)
    a[0].data, b[0].data = b[0].data, a[0].data


'''
#      6
#     /   \
#   10    2
#  / \   / \
# 1   3 7   12
 
# 1 10 3 6 7 2 12
'''
root = Node(6)
root.left = Node(10)
root.right = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(7)
root.right.right = Node(12)

inorder(root)
print()
correct(root)
inorder(root)
print()