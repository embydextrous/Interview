from tree import inorder, levelOrder
from tree import Node, preorder
from collections import deque

def diagonalTraversal(root):
    if root is None:
        return
    q1 = deque()
    q2 = deque()
    q1.append(root)
    while len(q1) > 0:
        while len(q1) > 0:
            node = q1.popleft()
            print(node.data, end = " ")
            if node.left:
                q2.append(node.left)
            if node.right:
                q1.append(node.right)
        print()
        q1, q2 = q2, q1        
        

    
    

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


diagonalTraversal(root)
