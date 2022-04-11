'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally 
connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],
               [1,0,0,0,0,1,1,0],
               [1,0,1,0,1,1,1,0],
               [1,0,0,0,0,1,0,1],
               [1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
'''
def isSafe(R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C

def dfs(M, R, C, i, j):
    M[i][j] = 1
    ROW = [-1, 0, 1, 0]
    COL = [0, 1, 0, -1]
    for k in range(4):
        x, y = i + ROW[k], j + COL[k]
        if isSafe(R, C, x, y) and M[x][y] == 0:
            dfs(M, R, C, x, y)

def countLockedIslands(M):
    R, C = len(M), len(M[0])
    # first remove all islands that lie on edge
    for j in range(C):
        if M[0][j] == 0:
            dfs(M, R, C, 0, j)
    for i in range(1, R):
        if M[i][0] == 0:
            dfs(M, R, C, i, 0)
    for j in range(1, C):
        if M[R-1][j] == 0:
            dfs(M, R, C, R - 1, j)
    for i in range(1, R-1):
        if M[i][C-1] == 0:
            dfs(M, R, C, i, C-1)
    # Now Count Islands
    count = 0
    for i in range(1, R - 1):
        for j in range(1, C - 1):
            if M[i][j] == 0:
                count += 1
                dfs(M, R, C, i, j)
                printIsland(M, R, C)
                print()
    return count

def printIsland(M, R, C):
    for i in range(R):
        for j in range(C):
            print(M[i][j], end = " ")
        print()

M = [[1,1,1,1,1,1,1,0],
     [1,0,0,0,0,1,1,0],
     [1,0,1,0,1,1,1,0],
     [1,0,0,0,0,1,0,1],
     [1,1,1,1,1,1,1,0]]

print(countLockedIslands(M))

