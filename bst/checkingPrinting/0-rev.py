from collections import defaultdict, deque
from typing import Counter
from bst import Node, insert, search, inorder

# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27 28
'''
            7
          /   \
         3     12
        / \    /
       1   5  8
          /    \
         4      11
'''
def count(root, k1, k2, c):
    if root is None:
        return
    if root.data >= k1 and root.data <= k2:
        c[0] += 1
        count(root.left, k1, k2, c)
        count(root.right, k1, k2, c)
        return root
    if root.data < k1:
        count(root.right, k1, k2, c)
    if root.data > k2:
        count(root.left, k1, k2, c)

root = Node(7)
insert(root, 3)
insert(root, 12)
insert(root, 5)
insert(root, 4)
insert(root, 8)
insert(root, 11)

c = [0]
count(root, 5, 11, c)
print(c[0])