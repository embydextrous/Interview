def checkIfInorderTraversalCanBeBST(ino):
    n = len(ino)
    for i in range(n-1):
        if ino[i] >= ino[i+1]:
            return False
    return True

a = [1, 2, 3, 4, 5, 7, 6, 8]
print(checkIfInorderTraversalCanBeBST(a))