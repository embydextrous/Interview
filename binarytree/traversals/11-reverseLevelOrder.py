from tree import Node
from collections import deque

# Also contains possible solution for level order traversal line by line

def reverseLevelOrder(root):
    if root is None:
        return
    q, s = deque([root]), []
    while len(q) > 0:
        node = q.popleft()
        s.append(node.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    while len(s) > 0:
        print(s.pop(), end = " ")
    print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)

root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)
reverseLevelOrder(root)