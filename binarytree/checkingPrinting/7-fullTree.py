from tree import Node

def isFullTree(root):
    if root is None:
        return True
    if not root.left and not root.right:
        return True
    if root.left is None or root.right is None:
        return False
    return isFullTree(root.left) and isFullTree(root.right)

root = Node(8)

root.left = Node(3)
root.right = Node(10)


root.left.left = Node(1)
root.left.right = Node(16)
root.right.left = Node(11)
root.right.right = Node(14)


root.left.left.left = Node(12)
root.left.left.right = Node(20)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.left.left = Node(13)
root.right.left.right = Node(11)
root.right.right.left = Node(19)
root.right.right.right = Node(2)


print(isFullTree(root))