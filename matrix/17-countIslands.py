# https://www.geeksforgeeks.org/find-number-of-islands/
from matrix import printS

def isSafe(R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C

def dfs(M, R, C, i, j):
    M[i][j] = 0
    ROW = [-1, -1, -1, 0, 1, 1, 1, 0]
    COL = [-1, 0, 1, 1, 1, 0, -1, -1]
    for k in range(8):
        x, y = i + ROW[k], j + COL[k]
        if isSafe(R, C, x, y) and M[x][y] == 1:
            dfs(M, R, C, x, y)

def countIslands(M):
    R, C = len(M), len(M[0])
    count = 0
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1:
                count += 1
                dfs(M, R, C, i, j)
    return count

graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

print(countIslands(graph))
