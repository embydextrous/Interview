# https://www.geeksforgeeks.org/minimum-operations-required-make-row-column-matrix-equals/
from matrix import printS

def countOperations(M):
    rowSum = []
    colSum = []
    R, C = len(M), len(M[0])
    for i in range(R):
        s = 0
        for j in range(C):
            s += M[i][j]
        rowSum.append(s)
    for i in range(C):
        s = 0
        for j in range(R):
            s += M[j][i]
        colSum.append(s)
    maxSum = max(max(rowSum), max(colSum))
    count = 0
    for i in range(R):
        for j in range(C):
            toAdd = min(maxSum - rowSum[i], maxSum - colSum[j])
            print(i, j, toAdd)
            count += toAdd
            rowSum[i] += toAdd
            colSum[j] += toAdd
    return count

mat = [
    [1, 2, 3],
    [4, 2, 3],
    [3, 2, 1]
]

print(countOperations(mat))