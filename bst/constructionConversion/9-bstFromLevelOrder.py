from bst import Node, inorder
import sys

def bstFromLevel(level):
    if len(level) == 0:
        return
    root = Node(level[0])
    MIN = -sys.maxsize-1
    MAX = sys.maxsize
    q = [(root, MIN, MAX)]
    i = 1
    while i < len(level):
        (node, low, high) = q.pop(0)
        if level[i] < node.data and level[i] >= low:
            node.left = Node(level[i])
            q.append((node.left, low, node.data - 1))
            i += 1
        if i < len(level) and level[i] > node.data and level[i] <= high:
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