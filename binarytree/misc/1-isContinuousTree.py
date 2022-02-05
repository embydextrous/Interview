from tree import Node


def isContinuousTree(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is None:
        return abs(root.data - root.right.data) == 1 and isContinuousTree(root.right)
    if root.right is None:
        return abs(root.data - root.left.data) == 1 and isContinuousTree(root.left)
    return abs(root.data - root.left.data) == 1 and abs(root.data - root.right.data) == 1 and isContinuousTree(root.left) and isContinuousTree(root.right)


root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)

print(isContinuousTree(root))
