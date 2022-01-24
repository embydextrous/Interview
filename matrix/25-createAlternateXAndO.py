from matrix import printS

def fillRing(M, k, c):
    R, C = len(M), len(M[0])
    # fill top row
    for i in range(k, C - k):
        M[k][i] = c
    # fill right edge
    for i in range(k + 1, R - k):
        M[i][C-k-1] = c
    # fill bottom row
    for i in range(C-k-2, k - 1, -1):
        M[R-k-1][i] = c
    # fill left row
    for i in range(R-k-2, k, -1):
        M[i][k] = c

def createMatrix(n):
    M = [['s' for _ in range(n)] for _ in range(n)]
    for k in range((n+1)//2):
        c = 'x' if k % 2 == 0 else '0'
        fillRing(M, k, c)
    return M

printS(createMatrix(10))
