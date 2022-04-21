from tree import Node
from collections import deque

def isCompleteTree(root):
    if root is None:
        return True
    q = deque([root])
    firstIncompleteNodeGone = False
    while len(q) > 0:
        node = q.popleft()
        if firstIncompleteNodeGone:
            if node.left or node.right:
                return False
        else:
            if node.left and node.right:
                q.append(node.left)
                q.append(node.right)
                continue
            elif node.right:
                return False
            elif node.left:
                firstIncompleteNodeGone = True
                q.append(node.left)
            else:
                firstIncompleteNodeGone = True
    return True
            



'''
        1
      /   \
     2      3
   /  \      \
  4    5      7
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)


print(isCompleteTree(root))
