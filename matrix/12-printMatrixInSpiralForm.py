def printClockWiseRing(M, k, R, C, n):
    # print top row
    if n[0] == R*C:
        return
    for i in range(k, C - k):
        print(M[k][i], end = " ")
        n[0] += 1
        if n[0] == R*C:
            return
    # print right edge
    for i in range(k + 1, R - k):
        print(M[i][C-k-1], end = " ")
        n[0] += 1
        if n[0] == R*C:
            return
    # print bottom row
    for i in range(C-k-2, k - 1, -1):
        print(M[R-k-1][i], end = " ")
        n[0] += 1
        if n[0] == R*C:
            return
    # print left edge
    for i in range(R-k-2, k, -1):
        print(M[i][k], end = " ")
        n[0] += 1
        if n[0] == R*C:
            return

def printMatrixInClockwiseSpiralForm(M):
    R, C, n = len(M), len(M[0]), [0]
    for i in range(min(R, C) // 2 + 1):
        printClockWiseRing(M, i, R, C, n)
    print()

def printAntiClockWiseRing(M, k, R, C, n):
    if n[0] == R*C:
        return
    # print left edge
    for i in range(k, R-k):
        print(M[i][k], end = " ")
        n[0] += 1
        if n[0] == R*C:
            return
    # print bottom row
    for i in range(k+1, C-k):
        print(M[R-k-1][i], end = " ")
        n[0] += 1
        if n[0] == R*C:
            return
    # print right edge
    for i in range(R-k-2, k - 1, -1):
        print(M[i][C-k-1], end = " ")
        n[0] += 1
        if n[0] == R*C:
            return
    # print top row
    for i in range(C-k-2, k, -1):
        print(M[k][i], end = " ")
        n[0] += 1
        if n[0] == R*C:
            return
    
    

def printMatrixInAntiClockwiseSpiralForm(M):
    R, C, n = len(M), len(M[0]), [0]
    for i in range(min(R, C) // 2 + 1):
        printAntiClockWiseRing(M, i, R, C, n)
    print()
    

M = [[1, 2, 3],
      ['&', '/', '*'],
     [5, 6, 7],
     [-1, -2, -3]]

printMatrixInClockwiseSpiralForm(M)
printMatrixInAntiClockwiseSpiralForm(M)