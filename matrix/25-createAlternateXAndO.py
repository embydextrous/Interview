'''
Write a code which inputs two numbers m and n and creates a matrix of size m x n (m rows and n columns) 
in which every elements is either X or 0. The Xs and 0s must be filled alternatively, the matrix should 
have outermost rectangle of Xs, then a rectangle of 0s, then a rectangle of Xs, and so on.

Examples:  

Input: m = 3, n = 3
Output: Following matrix 
X X X
X 0 X
X X X

Input: m = 4, n = 5
Output: Following matrix
X X X X X
X 0 0 0 X
X 0 0 0 X
X X X X X

Input:  m = 5, n = 5
Output: Following matrix
X X X X X
X 0 0 0 X
X 0 X 0 X
X 0 0 0 X
X X X X X

Input:  m = 6, n = 7
Output: Following matrix
X X X X X X X
X 0 0 0 0 0 X
X 0 X X X 0 X
X 0 X X X 0 X
X 0 0 0 0 0 X
X X X X X X X 
'''
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

def createMatrix(r, c):
    M = [['_' for _ in range(c)] for _ in range(r)]
    printX = True
    for k in range(min(r, c)//2):
        x = 'x' if printX else '0'
        fillRing(M, k, x)
        printX = not printX
    x = 'x' if printX else '0'
    if r % 2 == 1 and r <= c:
        for j in range(r//2, c - r//2):
            M[r//2][j] = x
    elif c % 2 == 1 and c <= r:
        for i in range(c//2, r - c//2):
            M[i][c//2] = x
    return M

printS(createMatrix(9, 5))
