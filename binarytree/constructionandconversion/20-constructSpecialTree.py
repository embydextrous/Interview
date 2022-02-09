# https://www.geeksforgeeks.org/construct-a-special-tree-from-given-preorder-traversal/
from tree import Node, inorder

pre = [10, 30, 20, 5, 15]
preLN = ['N', 'N', 'L', 'L', 'L']
'''
          10
         /  \
        30   15
       /  \
      20   5
'''

def construct(pre, preLN):
    if len(pre) == 0:
        return
    result = Node(pre[0])
    s = [result]
    i = 1
    while i < len(pre):
        node = Node(pre[i])
        if s[-1].left is None:
            s[-1].left = node
        else:
            s[-1].right = node
            s.pop()
        if preLN[i] == 'N':
            s.append(node)
        i += 1
    return result

root = construct(pre, preLN)
inorder(root)
print()