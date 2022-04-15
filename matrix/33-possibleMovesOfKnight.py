'''
Given a chess board of dimension m * n. Find number of possible moves where knight can be moved on a chessboard
from given position. If mat[i][j] = 1 then the block is filled by something else, otherwise empty. Assume that
board consist of all pieces of same color, i.e., there are no blocks being attacked. 

Input : mat[][] = {{1, 0, 1, 0},
                   {0, 1, 1, 1},
                   {1, 1, 0, 1},
                   {0, 1, 1, 1}}
        pos = (2, 2)
Output : 4
Knight can moved from (2, 2) to (0, 1), (0, 3), 
(1, 0) ans (3, 0).
'''
def possibleMovesKnight(M, x, y):
    count = 0
    R, C = len(M), len(M[0])
    ROW = [1, -1, -2, -2, -1, 1, 2, 2]
    COL = [-2, -2, -1, 1, 2, 2, 1, -1]
    for k in range(8):
        i, j = x + ROW[k], y + COL[k]
        if isValidMove(M, R, C, i, j):
            print(i, j)
            count += 1
    return count

def isValidMove(M, R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C and M[i][j] == 0

mat = [[1, 0, 1, 0], 
       [0, 1, 1, 1],
       [1, 1, 0, 1], 
       [0, 1, 1, 1]]
 
print(possibleMovesKnight(mat, 2, 2))