def printIsland(M, R, C):
    for i in range(R):
        for j in range(C):
            print(M[i][j], end = " ")
        print()

def isSafe(R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C

def dfs(M, R, C, i, j, count, island):
    M[i][j] = 0
    island[i][j] = 1
    count[0] += 1
    ROW = [-1, -1, -1, 0, 1, 1, 1, 0]
    COL = [-1, 0, 1, 1, 1, 0, -1, -1]
    for k in range(8):
        x, y = i + ROW[k], j + COL[k]
        if isSafe(R, C, x, y) and M[x][y] == 1:
            dfs(M, R, C, x, y, count, island)

def largestIsland(M):
    R, C = len(M), len(M[0])
    maxIsland = None
    maxCount = 0
    for i in range(R):
        for j in range(C):
            island = [[0 for i in range(C)] for j in range(R)]
            count = [0]
            if M[i][j] == 1:
                dfs(M, R, C, i, j, count, island)
                if count[0] > maxCount:
                    maxCount = count[0]
                    maxIsland = island
    return maxIsland

M = [[0, 0, 1, 1, 0],
     [0, 0, 1, 1, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 0, 0, 1]]

printIsland(largestIsland(M), len(M), len(M[0]))