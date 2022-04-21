from tree import Node
from collections import deque

def checkLeavesAtSameLevel(root, firstLeafLevel, level):
    if root is None:
        return True
    if not root.left and not root.right:
        if firstLeafLevel[0] == -1:
            firstLeafLevel[0] = level
        elif firstLeafLevel[0] != level:
            return False
    return checkLeavesAtSameLevel(root.left, firstLeafLevel, level+1) and checkLeavesAtSameLevel(root.right, firstLeafLevel, level+1)

def checkLeavesAtSameLevel2(root):
    if root is None:
        return True
    q1, q2 = deque([root]), deque()
    firstLeafFound = False
    while len(q1) > 0:
        while len(q1) > 0:
            node = q1.popleft()
            if node.left is None and node.right is None:
                firstLeafFound = True
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        if firstLeafFound:
            return len(q2) == 0
        q1, q2 = q2, q1


'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
'''
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

print(checkLeavesAtSameLevel2(root))