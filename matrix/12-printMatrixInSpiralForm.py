def printClockWiseRing(M, k, R, C):
    # print top row
    for i in range(k, C - k):
        print(M[k][i], end = " ")
    # print right edge
    for i in range(k + 1, R - k):
        print(M[i][C-k-1], end = " ")
    # print bottom row
    for i in range(C-k-2, k - 1, -1):
        print(M[R-k-1][i], end = " ")
    # print left edge
    for i in range(R-k-2, k, -1):
        print(M[i][k], end = " ")

def printMatrixInClockwiseSpiralForm(M):
    R, C = len(M), len(M[0])
    for i in range(min(R, C) // 2):
        printClockWiseRing(M, i, R, C)
    if R % 2 == 1 and R <= C:
        for j in range(R//2, C - R//2):
            print(M[R//2][j], end = " ")
    elif C % 2 == 1 and C <= R:
        for i in range(C//2, R - C//2):
            print(M[i][C//2], end = " ")
    print()

def printAntiClockWiseRing(M, k, R, C):
    for i in range(k, R-k):
        print(M[i][k], end = " ")
    for i in range(k+1, C-k):
        print(M[R-k-1][i], end = " ")
    for i in range(R-k-2, k - 1, -1):
        print(M[i][C-k-1], end = " ")
    for i in range(C-k-2, k, -1):
        print(M[k][i], end = " ")
    
def printMatrixInAntiClockwiseSpiralForm(M):
    R, C = len(M), len(M[0])
    for i in range(min(R, C) // 2):
        printAntiClockWiseRing(M, i, R, C)
    if R % 2 == 1 and R <= C:
        for j in range(R//2, C - R//2):
            print(M[R//2][j], end = " ")
    elif C % 2 == 1 and C <= R:
        for i in range(C//2, R - C//2):
            print(M[i][C//2], end = " ")
    print()
    

M = [[1, 2, 3],
      ['&', '/', '*'],
     [5, 6, 7],
     [-1, -2, -3]]

printMatrixInClockwiseSpiralForm(M)
printMatrixInAntiClockwiseSpiralForm(M)