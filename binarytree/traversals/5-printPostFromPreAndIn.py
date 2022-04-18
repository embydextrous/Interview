def printPost(pre, ino, preIndex, inoLeft, inoRight):
    if inoLeft > inoRight or preIndex[0] < inoLeft and preIndex[0] > inoRight:
        return
    root = pre[preIndex[0]]
    preIndex[0] += 1
    inoIndex = ino.index(root, inoLeft, inoRight + 1)
    printPost(pre, ino, preIndex, inoLeft, inoIndex - 1)
    printPost(pre, ino, preIndex, inoIndex + 1, inoRight)
    print(root, end = " ")

ino = [ 4, 2, 5, 1, 3, 6 ]
pre = [ 1, 2, 4, 5, 3, 6 ]
printPost(pre, ino, [0], 0, len(ino) - 1)
print()
