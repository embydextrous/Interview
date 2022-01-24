from matrix import printS
import sys

# Similar Question, https://www.geeksforgeeks.org/given-n-x-n-square-matrix-find-sum-sub-squares-size-k-x-k/

def printMaxSumSquareSubMatrix(M, k):
    R, C = len(M), len(M[0])
    V = [[0 for i in range(C)] for j in range(R-k+1)]
    for i in range(R-k+1):
        for j in range(C):
            if i == 0:
                for p in range(k):
                    V[i][j] += M[p][j]
            else:
                V[i][j] = V[i-1][j] + M[i+k-1][j] - M[i-1][j]
    S = [[0 for i in range(C-k+1)] for j in range(R-k+1)]
    x, y = -1, -1
    maxSum = -sys.maxsize-1
    for i in range(R-k+1):
        for j in range(C-k+1):
            if j == 0:
                for p in range(k):
                    S[i][j] += V[i][p]
            else:
                S[i][j] = S[i][j-1] + V[i][j+k-1] - V[i][j-1]
            if S[i][j] > maxSum:
                maxSum = S[i][j]
                x, y = i, j
    print("Maximum sum is: " + str(maxSum))
    print(x, y)
    for i in range(x, x + k):
        for j in range(y, y + k):
            print(M[i][j], end = " ")
        print()

M =    [[1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 8, 6, 7, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5],
    ]

k = 3

printMaxSumSquareSubMatrix(M, k)