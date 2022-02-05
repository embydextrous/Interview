from tree import Node

def isSymmetric(root):
    if root is None:
        return True
    return isSymmetricUtil(root.left, root.right)

def isSymmetricUtil(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.data == b.data and isSymmetricUtil(a.left, b.right) and isSymmetricUtil(a.right, b.left)

root = Node(1)
root.left = Node(2)
root.right = Node(2)

root.left.left = Node(3)
root.left.right = Node(4)

root.right.left = Node(4)
root.right.right = Node(3)

print(isSymmetric(root))