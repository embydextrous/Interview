from tree import Node
from collections import deque

# https://www.geeksforgeeks.org/maximum-sum-tree-adjacent-levels-not-allowed/

def maxSumAdjacentLevelsNotAllowed(root):
    if root is None:
        return 0
    q1, q2 = deque([root]), deque()
    incl = excl = 0
    while len(q1) > 0:
        levelSum = 0
        while len(q1) > 0:
            node = q1.popleft()
            levelSum += node.data
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        temp = incl
        incl = max(incl, excl + levelSum)
        excl = max(temp, excl)
        q1, q2 = q2, q1
    return max(incl, excl)
        
'''
        8
      /   \
     3     -10
   /   \     \
  1    -16    14
      /  \   /  \
     4    1 1    2
'''
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(-16)
root.left.right.left = Node(4)
root.left.right.right = Node(1)
root.right = Node(-10)
root.right.right = Node(14)
root.right.right.left = Node(1)
root.right.right.right = Node(2)

print(maxSumAdjacentLevelsNotAllowed(root))


