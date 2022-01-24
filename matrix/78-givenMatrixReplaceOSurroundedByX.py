# https://www.geeksforgeeks.org/given-matrix-o-x-replace-o-x-surrounded-x/
from matrix import printS

def isValid(M, R, C, i, j):
    return i >= 0 and j >= 0 and i < R and j < C and M[i][j] == '-'

def floodFillUtil(M, R, C, x, y):
    q = [[x, y]]
    while len(q) > 0:
        (i, j) = q.pop(0)
        M[i][j] = 'O'
        if isValid(M, R, C, i, j-1):
            q.append([i, j-1])
        if isValid(M, R, C, i-1, j):
            q.append([i-1, j])
        if isValid(M, R, C, i, j+1):
            q.append([i, j+1])
        if isValid(M, R, C, i+1, j):
            q.append([i+1, j])

def replaceOSurroundedByXWithX(M):
    # Replace all O's with -
    R, C = len(M), len(M[0])
    for i in range(R):
        for j in range(C):
            if M[i][j] == 'O':
                M[i][j] = '-'
    
    # Flood fill O's at boundary
    for i in range(R):
        for j in range(C):
            if (i == 0 or j == 0 or i == R - 1 or j == C-1) and M[i][j] == '-':
                floodFillUtil(M, R, C, i, j)

    # Replace all -'s with 'X'
    for i in range(R):
        for j in range(C):
            if M[i][j] == '-':
                M[i][j] = 'X'

M = [[ 'X', 'O', 'X', 'O', 'X', 'X' ],
     [ 'X', 'O', 'X', 'X', 'O', 'X' ],
     [ 'X', 'X', 'X', 'O', 'X', 'X' ],
     [ 'O', 'X', 'X', 'X', 'X', 'X' ],
     [ 'X', 'X', 'X', 'O', 'X', 'O' ],
     [ 'O', 'O', 'X', 'O', 'O', 'O' ] ]

replaceOSurroundedByXWithX(M)
printS(M)

