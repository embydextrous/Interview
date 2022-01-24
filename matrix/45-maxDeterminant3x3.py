# https://www.geeksforgeeks.org/maximum-determinant-matrix-every-values-either-0-n/
from matrix import printS

def maxDet(n):
    return 2 * n * n * n

def resultMatrix(n):
    M = [[0 for i in range(3)] for j in range(3)]
    M[0][0] = M[0][1] = M[1][1] = M[1][2] = M[2][0] = M[2][2] = n
    return M

n = 3
print(maxDet(n))
printS(resultMatrix(n))