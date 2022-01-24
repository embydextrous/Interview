# https://www.geeksforgeeks.org/find-k-such-that-all-elements-in-kth-row-are-0-and-kth-column-are-1-in-a-boolean-matrix/

from cgitb import reset


def findElements(M):
    n = len(M)
    rowSum = [0 for i in range(n)]
    colSum = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                rowSum[i] += 1
                colSum[j] += 1
    res = []
    for i in range(n):
        if M[i][i] == 0:
            if rowSum[i] == 0 and colSum[i] == n - 1:
                res.append(i)
        else:
            if rowSum[i] == 1 and colSum[i] == n:
                res.append(i)
    return res

M =     [[0,0,1,1,0],
         [0,0,0,1,0],
         [1,1,1,1,0],
         [0,0,0,0,0],
         [1,1,1,1,1] ]

print(findElements(M))