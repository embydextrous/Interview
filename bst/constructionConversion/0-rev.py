from collections import defaultdict, deque
from typing import Counter
from bst import Node, insert, search, inorder

# 1, 3, 4, 5, 6, 7, 9
# 11, 12
'''
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 
'''
def reversePath(root, key, path):
    if root is None:
        return
    path.append(root)
    if root.data == key:
        l = 0
        r = len(path) - 1
        while l < r:
            path[l].data, path[r].data = path[r].data, path[l].data
            l += 1
            r -= 1
        return
    if root.data < key:
        reversePath(root.right, key, path)
    else:
        reversePath(root.left, key, path)

root = Node(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

inorder(root)
print()
reversePath(root, 80, []) 
inorder(root)
print()