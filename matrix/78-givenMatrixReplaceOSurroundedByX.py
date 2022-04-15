# https://www.geeksforgeeks.org/given-matrix-o-x-replace-o-x-surrounded-x/
'''
Given a matrix where every element is either 'O' or 'X', replace 'O' with 'X' if surrounded by 'X'. A 'O'
(or a set of 'O') is considered to be by surrounded by 'X' if there are 'X' at locations just below, 
just above, just left and just right of it. 
Examples: 
 

Input: mat[M][N] =  {{'X', 'O', 'X', 'X', 'X', 'X'},
                     {'X', 'O', 'X', 'X', 'O', 'X'},
                     {'X', 'X', 'X', 'O', 'O', 'X'},
                     {'O', 'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'O', 'X', 'O'},
                     {'O', 'O', 'X', 'O', 'O', 'O'},
                    };
Output: mat[M][N] =  {{'X', 'O', 'X', 'X', 'X', 'X'},
                      {'X', 'O', 'X', 'X', 'X', 'X'},
                      {'X', 'X', 'X', 'X', 'X', 'X'},
                      {'O', 'X', 'X', 'X', 'X', 'X'},
                      {'X', 'X', 'X', 'O', 'X', 'O'},
                      {'O', 'O', 'X', 'O', 'O', 'O'},
                    };
 

Input: mat[M][N] =  {{'X', 'X', 'X', 'X'}
                     {'X', 'O', 'X', 'X'}
                     {'X', 'O', 'O', 'X'}
                     {'X', 'O', 'X', 'X'}
                     {'X', 'X', 'O', 'O'}
                    };
 

Input: mat[M][N] =  {{'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'O', 'O'}
                    };
'''
from matrix import printS

def isValid(R, C, i, j):
    return i >= 0 and j >= 0 and i < R and j < C

def floodFillUtil(M, R, C, x, y, oldChar, newChar):
    M[x][y] = newChar
    ROW = [0, -1, 0, 1]
    COL = [-1, 0, 1, 0]
    for k in range(4):
        i, j = x + ROW[k], y + COL[k]
        if isValid(R, C, i, j) and M[i][j] == oldChar:
            floodFillUtil(M, R, C, i, j, oldChar, newChar)

def replaceOSurroundedByXWithX(M):
    R, C = len(M), len(M[0])
    for i in range(R):
        for j in range(C):
            if (i == 0 or j == 0 or i == R - 1 or j == C - 1) and M[i][j] == 'O':
                floodFillUtil(M, R, C, i, j, 'O', '-')
    for i in range(R):
        for j in range(C):
            if M[i][j] == 'O':
                floodFillUtil(M, R, C, i, j, 'O', 'X')
    for i in range(R):
        for j in range(C):
            if (i == 0 or j == 0 or i == R - 1 or j == C - 1) and M[i][j] == '-':
                floodFillUtil(M, R, C, i, j, '-', 'O')
                 


M = [[ 'X', 'O', 'X', 'O', 'X', 'X' ],
     [ 'X', 'O', 'X', 'X', 'O', 'X' ],
     [ 'X', 'X', 'X', 'O', 'X', 'X' ],
     [ 'O', 'X', 'X', 'X', 'X', 'X' ],
     [ 'X', 'X', 'X', 'O', 'X', 'O' ],
     [ 'O', 'O', 'X', 'O', 'O', 'O' ] ]

replaceOSurroundedByXWithX(M)
printS(M)

