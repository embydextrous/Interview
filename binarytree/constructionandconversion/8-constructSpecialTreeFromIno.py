# https://www.geeksforgeeks.org/construct-binary-tree-from-inorder-traversal/
from tree import Node, preorder

'''
Input: inorder[] = {1, 5, 10, 40, 30, 15, 28, 20}
Output: root of following tree
          40
        /   \
       10     30
      /         \
     5          28
    /          /  \
   1         15    20
'''

def construct(ino):
    if len(ino) == 0:
        return None
    data = max(ino)
    root = Node(data)
    inoIndex = ino.index(data)
    root.left = construct(ino[:inoIndex])
    root.right = construct(ino[inoIndex+1:])
    return root

ino = [1, 5, 10, 40, 30, 15, 28, 20]
preorder(construct(ino))
print()