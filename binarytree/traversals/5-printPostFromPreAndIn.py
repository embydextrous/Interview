def printPost(pre, ino):
    if len(pre) == 0:
        return
    root = pre[0]
    inoIndex = ino.index(root)
    printPost(pre[1:inoIndex + 1], ino[:inoIndex])
    printPost(pre[inoIndex+1:], ino[inoIndex+1:])
    print(root, end = ' ')

def printPost2(pre, ino, preIndex, inoLeft, inoRight):
    if preIndex[0] >= len(pre) or inoLeft > inoRight:
        return
    root = pre[preIndex[0]]
    inoIndex = ino.index(root, inoLeft, inoRight + 1)
    preIndex[0] += 1
    printPost2(pre, ino, preIndex, inoLeft, inoIndex - 1)
    printPost2(pre, ino, preIndex, inoIndex + 1, inoRight)
    print(root, end = ' ')

ino = [ 4, 2, 5, 1, 3, 6 ]
pre = [ 1, 2, 4, 5, 3, 6 ]

printPost(pre, ino)
print()
printPost2(pre, ino, [0], 0, len(ino) - 1)
print()
