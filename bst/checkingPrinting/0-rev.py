from collections import defaultdict, deque
from typing import Counter
from unittest import result
from bst import Node, insert, search, inorder

# 16 17
# 23 25 27
'''
            7
          /   \
         3     12
        / \    /
       1   5  8
          /    \
         4      11
'''
# a < b, a, b exists int tree
def maxElement(root, a, b):
    if root is None:
        return
    if root.data == a:
        while root.right:
            root = root.right
        return root.data
    if root.data == b:
        return b
    if root.data > a and root.data < b:
        while root.right:
            root = root.right
        return root.data
    if root.data < a:
        return maxElement(root.right, a, b)
    return maxElement(root.left, a, b)
    

a = [18, 36, 9, 6, 12, 10, 1, 8]
root = Node(a[0])
for i in range(1, len(a)):
    insert(root, a[i])
a = 1
b = 8
print(maxElement(root, a, b))