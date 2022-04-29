# https://www.geeksforgeeks.org/construct-a-special-tree-from-given-preorder-traversal/
from tree import Node, inorder

pre = [1, 2, 3, 4, 5]
preLN = ['N', 'L', 'N', 'L', 'L']
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

def construct2(pre, preLN, preIndex):
    if preIndex[0] >= len(pre):
        return None
    root = Node(pre[preIndex[0]])
    if preLN[preIndex[0]] == 'N':
        preIndex[0] += 1
        root.left = construct2(pre, preLN, preIndex)
        preIndex[0] += 1
        root.right = construct2(pre, preLN, preIndex)
    return root

root = construct2(pre, preLN, [0])
inorder(root)
print()