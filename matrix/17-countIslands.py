# https://www.geeksforgeeks.org/find-number-of-islands/
'''
Consider a matrix with rows and columns, where each cell contains either a '0' or a '1' and any cell 
containing a 1 is called a filled cell. Two cells are said to be connected if they are adjacent to 
each other horizontally, vertically, or diagonally. If one or more filled cells are also connected, 
they form a region. find the number of regions.

Examples: 

Input : M[][5] = { 0 0 1 1 0
                   1 0 1 1 0
                   0 1 0 0 0
                   0 0 0 0 1 }
Output : 2

Input : M[][5] = { 0 0 1 1 0
                   0 0 1 1 0
                   0 0 0 0 0
                   0 0 0 0 1 }
Output: 2
'''
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
