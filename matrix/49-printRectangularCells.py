# https://www.geeksforgeeks.org/print-cells-rectangular-sum-matrix/
def transform(M, R, C):
    for i in range(R):
        for j in range(C):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                M[i][j] += M[i][j-1]
            elif j == 0:
                M[i][j] += M[i-1][j]
            else:
                M[i][j] += M[i-1][j] + M[i][j-1] - M[i-1][j-1]


def printCells(M):
    R, C = len(M), len(M[0])
    transform(M, R, C)
    x = M[R-1][C-1]
    if x % 2 == 1:
        return
    for i in range(R):
        for j in range(C):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                y = M[R-1][j-1] - M[i][j-1]
                if y == x - y:
                    print(i, j)
            elif j == 0:
                y = M[i-1][C-1] - M[i-1][j]
                if y == x - y:
                    print(i, j)
            else:
                y = M[R-1][j-1] - M[i][j-1] + M[i-1][C-1] - M[i-1][j]
                if y == x - y:
                    print(i, j)



M =[[1, 2, 3, 5],
     [4, 1, 0, 2,],
     [0, 1, 2, 0],
     [7, 1, 1, 0]]

printCells(M)