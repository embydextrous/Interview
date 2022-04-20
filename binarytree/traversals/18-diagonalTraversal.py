# https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/
from tree import Node
from collections import deque

def diagonalTraversal(root):
    if root is None:
        return
    q1, q2 = deque([root]), deque()
    while len(q1) > 0:
        while len(q1) > 0:
            node = q1.popleft()
            print(node.data, end = " ")
            if node.right:
                q1.append(node.right)
            if node.left:
                q2.append(node.left)
        print()
        q1, q2 = q2, q1

'''
        8
      /   \
     3     10
   /   \     \
  1     6     14
      /  \   /
     4    7 13
'''

root = Node(8)
root.left = Node(3)
root.right =  Node(10)
root.left.left =  Node(1)
root.left.right =  Node(6)
root.right.right =  Node(14)
root.right.right.left =  Node(13)
root.left.right.left =  Node(4)
root.left.right.right =  Node(7)

diagonalTraversal(root)
