from tree import Node

def checkSum(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is None:
        return root.data == root.right.data and checkSum(root.right)
    if root.right is None:
        return root.data == root.left.data and checkSum(root.left)
    return root.data == root.left.data + root.right.data and checkSum(root.left) and checkSum(root.right)

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

print(checkSum(root))