def possibleMovesKnight(M, x, y):
    count = 0
    R, C = len(M), len(M[0])
    if isValidMove(M, R, C, x - 2, y - 1):
        count += 1
    if isValidMove(M, R, C, x - 2, y + 1):
        count += 1
    if isValidMove(M, R, C, x - 1, y - 2):
        count += 1
    if isValidMove(M, R, C, x + 1, y - 2):
        count += 1
    if isValidMove(M, R, C, x + 2, y - 1):
        count += 1
    if isValidMove(M, R, C, x + 2, y + 1):
        count += 1
    if isValidMove(M, R, C, x - 1, y + 2):
        count += 1
    if isValidMove(M, R, C, x + 1, y + 2):
        count += 1
    return count

def isValidMove(M, R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C and M[i][j] == 0

mat = [[1, 0, 1, 0], 
       [0, 1, 1, 1],
       [1, 1, 0, 1], 
       [0, 1, 1, 1]]
 
print(possibleMovesKnight(mat, 2, 2))