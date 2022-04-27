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

def construct(ino, inoLeft, inoRight):
    if inoLeft > inoRight:
        return None
    maxIndex = inoLeft
    for i in range(inoLeft + 1, inoRight + 1):
        if ino[maxIndex] < ino[i]:
            maxIndex = i
    root = Node(ino[maxIndex])
    root.left = construct(ino, inoLeft, maxIndex - 1)
    root.right = construct(ino, maxIndex + 1, inoRight)
    return root

ino = [1, 5, 10, 40, 30, 15, 28, 20]
preorder(construct(ino, 0, len(ino) - 1))
print()