from tree import levelOrder
from tree import Node
from collections import deque

def reverseAlternateLevels(root):
    if root is None:
        return
    if root.left is None:
        return
    q = deque()
    q.append(root.left)
    q.append(root.right)
    while len(q) > 0:
        node1 = q.popleft()
        node2 = q.popleft()
        node1.data, node2.data = node2.data, node1.data
        hasNextLevel = node1.left is not None
        if hasNextLevel:
            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right)
            q.append(node2.left)      



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
reverseAlternateLevels(root)
levelOrder(root)