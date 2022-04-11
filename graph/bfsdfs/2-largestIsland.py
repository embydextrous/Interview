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
Output : 6

Input : M[][5] = { 0 0 1 1 0
                   0 0 1 1 0
                   0 0 0 0 0
                   0 0 0 0 1 }
Output: 4
'''
def isSafe(R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C

def dfs(M, R, C, i, j, count):
    M[i][j] = 0
    count[0] += 1
    ROW = [-1, -1, -1, 0, 1, 1, 1, 0]
    COL = [-1, 0, 1, 1, 1, 0, -1, -1]
    for k in range(8):
        x, y = i + ROW[k], j + COL[k]
        if isSafe(R, C, x, y) and M[x][y] == 1:
            dfs(M, R, C, x, y, count)

def largestIsland(M):
    R, C = len(M), len(M[0])
    maxCount = 0
    for i in range(R):
        for j in range(C):
            count = [0]
            if M[i][j] == 1:
                dfs(M, R, C, i, j, count)
                if count[0] > maxCount:
                    maxCount = count[0]
    return maxCount

M = [[0, 0, 1, 1, 0],
     [0, 0, 1, 1, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 0, 0, 1]]

print(largestIsland(M))