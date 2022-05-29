from bst import Node, inorder
import sys
from collections import deque

def bstFromLevel(level):
    n = len(level)
    if n == 0:
        return None
    root = Node(level[0])
    q = deque([(root, -10**9, 10**9)])
    i = 1
    while i < n:
        node, low, high = q.popleft()
        if level[i] < node.data and level[i] >= low:
            node.left = Node(level[i])
            q.append((node.left, low, node.data - 1))
            i += 1
        if i < n and level[i] > node.data and level[i] <= high:
            node.right = Node(level[i])
            q.append((node.right, node.data + 1, high))
            i += 1
    return root

'''
        7        
       / \       
      4   12      
     / \  /     
    3  6 8    
   /  /   \
  1   5   10
'''

level = [7, 4, 12, 3, 6, 8, 1, 5, 10]
inorder(bstFromLevel(level))
print()