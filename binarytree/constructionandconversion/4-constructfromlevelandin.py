from tree import Node, preorder, inorder

def constructUtil(level, ino, inoIndexMap):
    root = Node(level[0])
    inoIndex = inoIndexMap[root.data]
    left, right = [], []
    for i in range(1, len(level)):
        if inoIndexMap[level[i]] < inoIndex:
            left.append(level[i])
        else:
            right.append(level[i])
    if len(left) > 0:
        root.left = constructUtil(left, ino[:inoIndex], inoIndexMap)
    if len(right) > 0:
        root.right = constructUtil(right, ino[inoIndex + 1:], inoIndexMap)
    return root

def construct(level, ino):
    if len(ino) == 0:
        return None
    inoIndexMap = {}
    for i in range(len(ino)):
        inoIndexMap[ino[i]] = i
    return constructUtil(level, ino, inoIndexMap)

'''
            20
         /      \
        8        22
      /  \
     4    12
          / \
        10   14   

'''

level = [ 20, 8, 22, 4, 12, 10, 14 ]
ino = [ 4, 8, 10, 12, 14, 20, 22 ]

preorder(construct(level, ino))
print()