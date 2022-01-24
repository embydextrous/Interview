from matrix import printS
import sys

def createMinMatrix(M, R, C):
    A = [[M[i][j] for j in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if i == 0 and j == 0:
                A[i][j] = M[i][j]
            elif i == 0:
                A[i][j] = min(A[i][j-1], M[i][j])
            elif j == 0:
                A[i][j] = min(A[i-1][j], M[i][j])
            else:
                A[i][j] = min(A[i-1][j], A[i][j-1], M[i][j])
    return A

def createMaxMatrix(M, R, C):
    A = [[M[i][j] for j in range(C)] for i in range(R)]
    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            if i == R - 1 and j == C - 1:
                A[i][j] = M[i][j]
            elif i == R - 1:
                A[i][j] = max(A[i][j+1], M[i][j])
            elif j == C - 1:
                A[i][j] = max(A[i+1][j], M[i][j])
            else:
                A[i][j] = max(A[i+1][j], A[i][j+1], M[i][j])
    return A

def specificPair(M):
    R, C = len(M), len(M[0])
    minMatrix = createMinMatrix(M, R, C)
    maxMatrix = createMaxMatrix(M, R, C)
    maxDiff = -sys.maxsize-1
    for i in range(R-1):
        for j in range(C-1):
            maxDiff = max(maxMatrix[i+1][j+1] - minMatrix[i][j], maxDiff)
    return maxDiff

M =   [[ 1, 2, -1, -4, -20 ],
       [-8, -3, 4, 2, 1 ],
       [ 3, 8, 6, 1, 3 ],
       [ -4, -1, 1, 7, -6] ,
       [0, -4, 10, -5, 1 ]]
print(specificPair(M))