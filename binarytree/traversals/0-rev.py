from tree import inorder, levelOrder
from tree import Node, preorder
from collections import deque

def iterativePreorderUsingStack(root):
    if root is None:
        return
    s = deque()
    s.append(root)
    while len(s) > 0:
        node = s.pop()
        print(node.data, end = " ")
        if node.right:
            s.append(node.right)
        if node.left:
            s.append(node.left)
    print()
    
    

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
    /
   3 
'''

root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.left.left = Node(3)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)


iterativePreorderUsingStack(root)
