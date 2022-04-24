from tree import Node
from collections import deque

def maxLevelSum(root):
    if root is None:
        return 0
    q1, q2 = deque([root]), deque()
    maxSum = root.data
    while len(q1) > 0:
        sum = 0
        while len(q1):
            node = q1.popleft()
            sum += node.data
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        maxSum = max(maxSum, sum)
        q1, q2 = q2, q1
    return maxSum

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
print(maxLevelSum(root))