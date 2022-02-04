from tree import Node

class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

def level(root, a, lvl):
    if root is None:
        return -1
    if root == a:
        return lvl
    l = level(root.left, a, lvl + 1)
    if l != -1:
        return l
    return level(root.right, a, lvl + 1)

def lca(root, a, b):
    if root is None:
        return None
    lvlA = level(root, a, 0)
    if lvlA == -1:
        return None
    lvlB = level(root, b, 0)
    if lvlB == -1:
        return None
    if lvlA - lvlB > 0:
        i = 0
        while i < lvlA - lvlB:
            a = a.parent
            i += 1
    elif lvlB - lvlA > 0:
        i = 0
        while i < lvlB - lvlA:
            b = b.parent
            i += 1
    while a != b:
        a = a.parent
        b = b.parent
    return a

root = Node(1, None)
root.left = Node(2, root)
root.right = Node(3, root)
root.left.left = Node(4, root.left)
root.left.right = Node(5, root.left)
root.right.left = Node(6, root.right)
root.right.right = Node(7, root.right)

print(lca(root, root.left, Node(10, None)).data)