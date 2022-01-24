# https://www.geeksforgeeks.org/print-cells-rectangular-sum-matrix/
def printCells(M):
    R, C = len(M), len(M[0])
    A = [[0 for i in range(C)] for j in range(R)]
    B = [[0 for i in range(C)] for j in range(R)]
    sum = 0
    if sum % 2 == 1:
        return
    for i in range(R):
        for j in range(C):
            sum += M[i][j]
    for i in range(R):
        for j in range(C):
            if i == 0 and j == 0:
                A[i][j] = M[i][j]
            elif i == 0:
                A[i][j] = M[i][j] + A[i][j-1]
            elif j == 0:
                A[i][j] = M[i][j] + A[i-1][j]
            else:
                A[i][j] = M[i][j] + A[i-1][j] + A[i][j-1] - A[i-1][j-1]
    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            if i == R-1 and j == C-1:
                B[i][j] = M[i][j]
            elif i == R - 1:
                B[i][j] = M[i][j] + B[i][j+1]
            elif j == C - 1:
                B[i][j] = M[i][j] + B[i+1][j]
            else:
                B[i][j] = M[i][j] + B[i+1][j] + B[i][j+1] - B[i+1][j+1]
    for i in range(R):
        for j in range(C):
            if A[i][j] + B[i][j] - M[i][j] == sum // 2:
                print(i, j)


M =[[1, 2, 3, 5],
     [4, 1, 0, 2,],
     [0, 1, 2, 0],
     [7, 1, 1, 0]]

printCells(M)