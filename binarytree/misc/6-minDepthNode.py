from tree import Node
from collections import deque

# Level order traversal is better here as it does not traverse entire tree
def minDepth(root):
    if root is None:
        return 0
    q1, q2 = deque([root]), deque()
    depth = 0
    while len(q1) > 0:
        while len(q1) > 0:
            node = q1.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        depth += 1
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
print(minDepth(root))
