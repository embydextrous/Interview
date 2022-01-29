from tree import Node

def areSiblings(root, a, b):
    if root is None:
        return False
    return (root.left == a and root.right == b) or (root.left == b and root.right == a) or areSiblings(root.left, a, b) or areSiblings(root.right, a, b)


def level(root, a, lvl):
    if root is None:
        return -1
    if root == a:
        return lvl
    l = level(root.left, a, lvl + 1)
    if l != -1:
        return l
    return level(root.right, a, lvl + 1)

def areCousins(root, a, b):
    levelA = level(root, a, 0)
    levelB = level(root, b, 0)
    if levelA == -1 or levelB == -1:
        return False
    return levelA == levelB and not areSiblings(root, a, b)

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

print(areCousins(root, root.left.left, root.right.right))