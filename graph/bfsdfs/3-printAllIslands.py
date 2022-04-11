def isSafe(R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C

def dfs(M, R, C, i, j, island):
    M[i][j] = 0
    island[i][j] = 1
    ROW = [-1, -1, -1, 0, 1, 1, 1, 0]
    COL = [-1, 0, 1, 1, 1, 0, -1, -1]
    for k in range(8):
        x, y = i + ROW[k], j + COL[k]
        if isSafe(R, C, x, y) and M[x][y] == 1:
            dfs(M, R, C, x, y, island)

def printIsland(M, R, C):
    for i in range(R):
        for j in range(C):
            print(M[i][j], end = " ")
        print()

def printAllIslands(M):
    R, C = len(M), len(M[0])
    for i in range(R):
        for j in range(C):
            island = [[0 for i in range(C)] for j in range(R)]
            if M[i][j] == 1:
                dfs(M, R, C, i, j, island)
                printIsland(island, R, C)
                print()

M = [[0, 0, 1, 1, 0],
     [0, 0, 1, 1, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 0, 0, 1]]

printAllIslands(M)