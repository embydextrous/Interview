from tree import Node
from collections import deque

def populateInorderSuccessor(root, prev):
    if root:
        populateInorderSuccessor(root.left, prev)
        if prev[0]:
            prev[0].next = root
        prev[0] = root
        populateInorderSuccessor(root.right, prev)

def printInorderSuccessors(root):
    if root:
        printInorderSuccessors(root.left)
        print(root.data, None if root.next is None else root.next.data)
        printInorderSuccessors(root.right)
    
    
'''
        3
      /   \
     2     4
   /   \    \
  1     3    5    
'''

root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)

populateInorderSuccessor(root, [None])
printInorderSuccessors(root)
print()
