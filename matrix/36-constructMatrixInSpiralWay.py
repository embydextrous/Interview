'''
Given two values m and n, fill a matrix of size n * m in a spiral (or circular) fashion (clockwise) with 
natural numbers from 1 to n*m.

Examples:  

Input : n = 4, m = 4
Output :  1  2  3  4
         12 13 14  5
         11 16 15  6
         10  9  8  7 

Input : n = 3, m = 4
Output :  1  2  3  4
          10 11 12 5
          9  8  7  6     
'''

from matrix import printS

def fillRing(M, R, C, k, startValue):
    # fill top row
    for i in range(k, C-k):
        M[k][i] = startValue
        startValue += 1
    # fill right edge
    for i in range(k + 1, R-k):
        M[i][C-k-1] = startValue
        startValue += 1
    # fill bottom row
    for i in range(C-k-2, k, -1):
        M[R-k-1][i] = startValue
        startValue += 1
    # fill left edge
    for i in range(R-k-1, k, -1):
        M[i][k] = startValue
        startValue += 1
    return startValue

def createMatrix(n, m):
    k = min(n, m)
    M = [[0 for i in range(m)] for i in range(n)]
    startValue = 1
    for i in range(k// 2):
        startValue = fillRing(M, n, m, i, startValue)
    if n % 2 == 1 and n <= m:
        for j in range(n//2, m - n//2):
            M[n//2][j] = startValue
            startValue += 1
    elif m % 2 == 1 and m <= n:
        for i in range(m//2, n - m//2):
            M[i][m//2] = startValue
            startValue += 1
    return M


printS(createMatrix(5, 7))