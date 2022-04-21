from tree import Node
from collections import deque

def checkCoveredSumEqualsUncoveredSum(root):
    if root is None:
        return True
    q1, q2 = deque([root]), deque()
    cs, ucs = 0, 0
    while len(q1) > 0:
        isFirstHandled = False
        while len(q1) > 0:
            node = q1.popleft()
            if not isFirstHandled:
                isFirstHandled = True
                ucs += node.data
            elif len(q1) == 0:
                ucs += node.data
            else:
                cs += node.data
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        q1, q2 = q2, q1
    return cs == ucs


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

print(checkCoveredSumEqualsUncoveredSum(root))