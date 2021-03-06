from tree import Node
from collections import deque

def printCousins(root, target):
    if root is None or root == target:
        return
    q1, q2 = deque([root]), deque()
    targetFound = False
    while len(q1) > 0:
        while len(q1) > 0:
            node = q1.popleft()
            if node.left == target or node.right == target:
                targetFound = True
                continue
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        if targetFound:
            while len(q2) > 0:
                print(q2.popleft().data, end = " ")
            break
        q1, q2 = q2, q1
    print()

root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)
root.right.right.left.left = Node(30)
root.right.right.left.left.left = Node(32)
root.right.right.left.right = Node(31)

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
           /  \
          30   31
         /
        32 
'''

printCousins(root, root.right.right)