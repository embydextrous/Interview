from tree import Node, preorder

def construct(level, ino):
    if len(level) == 0:
        return None
    data = level[0]
    root = Node(data)
    inoIndex = ino.index(data)
    left, right = [], []
    for x in level:
        if ino.index(x) < inoIndex:
            left.append(x)
        elif ino.index(x) > inoIndex:
            right.append(x)
    root.left = construct(left, ino[:inoIndex])
    root.right = construct(right, ino[inoIndex+1:])
    return root

level = [20, 8, 22, 4, 12, 10, 14]
ino = [4, 8, 10, 12, 14, 20, 22]

preorder(construct(level, ino))
print()