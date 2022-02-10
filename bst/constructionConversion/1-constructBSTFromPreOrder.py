from bst import Node, inorder
import sys

MIN = -sys.maxsize-1
MAX = sys.maxsize

def constructUtil(pre, mini, maxi, idx):
    if idx[0] >= len(pre):
        return None
    if pre[idx[0]] < mini or pre[idx[0]] > maxi:
        return None
    root = Node(pre[idx[0]])
    idx[0] += 1
    root.left = constructUtil(pre, mini, root.data - 1, idx)
    root.right = constructUtil(pre, root.data + 1, maxi, idx)
    return root

def construct(pre):
    if len(pre) == 0:
        return None
    return constructUtil(pre, MIN, MAX, [0])
    

'''
          10
        /    \
       5     40
      / \      \
     1   7      50  
'''

pre = [10, 5, 1, 7, 40, 50]
inorder(construct(pre))
print()