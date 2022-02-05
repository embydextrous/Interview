from tree import Node

def isFoldableUtil(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return isFoldableUtil(a.left, b.right) and isFoldableUtil(a.right, b.left)

def isFoldable(root):
    if root is None:
        return True
    return isFoldableUtil(root.left, root.right)
    


root = Node(10)
root.left = Node(7)
root.right = Node(15)
root.left.right = Node(9)
root.right.left = Node(11)

print(isFoldable(root))
