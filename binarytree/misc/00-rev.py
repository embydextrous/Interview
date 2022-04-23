from tree import Node, inorder
from collections import deque

def checkSortedLevels(root):
    if root is None:
        return True
    q1, q2 = deque([root]), deque()
    maxLastLevel = root.data
    while len(q1) > 0:
        maxCurrentLevel = q1[0].data
        while len(q1) > 0:
            node = q1.popleft()
            if node.data < maxLastLevel:
                return False
            maxCurrentLevel = max(maxCurrentLevel, node.data)
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        q1, q2 = q2, q1
        maxLastLevel = maxCurrentLevel


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

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
'''
print(checkSortedLevels(root))