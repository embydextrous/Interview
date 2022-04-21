from tree import Node
from collections import deque

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

def checkIfCousins(root, a, b):
    if root is None:
        return False
    q1, q2 = deque([root]), deque()
    while len(q1) > 0:
        foundA, foundB = False, False
        while len(q1) > 0:
            node = q1.popleft()
            # are siblings
            if node.left == a and node.right == b:
                return False
            if node.right == a and node.left == b:
                return False
            if node.left:
                if node.left == a:
                    foundA = True
                elif node.left == b:
                    foundB = True
                q2.append(node.left)
            if node.right:
                if node.right == a:
                    foundA = True
                elif node.right == b:
                    foundB = True
        if foundB and foundA:
            return True
        if foundA or foundB:
            return False
        q1, q2 = q2, q1

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