# https://www.geeksforgeeks.org/form-coils-matrix/
from matrix import printS

def formCoils(M):
    n = len(M)
    k = n // 4
    coil1 = []
    coil2 = []
    for i in range(k):
        # add left
        for j in range(2 * i, n - 2 * i):
            x = M[j][2*i]
            coil1.append(x)
            coil2.append(n * n + 1 - x)
        # add bottom
        for j in range(2 * i + 1, n - 2 * i - 1):
            x = M[n-2*i-1][j]
            coil1.append(x)
            coil2.append(n * n + 1 - x)
        # add right
        for j in range(n - 2 * i - 2, 2 * i, -1):
            x = M[j][n - 2 * i - 2]
            coil1.append(x)
            coil2.append(n * n + 1 - x)
        # add top
        for j in range(n - 2 * i - 3, 2 * i + 1, -1):
            x = M[2*i+1][j]
            coil1.append(x)
            coil2.append(n * n + 1 - x)
    print(coil1)
    print(coil2)

n = 8
M = [[0 for i in range(n)] for j in range(n)]
for i in range(n*n):
    M[i//n][i%n] = i + 1
printS(M)
formCoils(M)


