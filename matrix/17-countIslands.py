# https://www.geeksforgeeks.org/find-number-of-islands/
from matrix import printS

def dfs(M, i, j):
    if i < 0 or i >= len(M):
        return
    if j < 0 or j >= len(M[0]):
        return
    if M[i][j] != 1:
        return
    M[i][j] = -1
    dfs(M, i-1, j-1)
    dfs(M, i-1, j)
    dfs(M, i-1, j+1)
    dfs(M, i, j-1)
    dfs(M, i, j+1)
    dfs(M, i+1, j-1)
    dfs(M, i+1, j)
    dfs(M, i+1, j+1)

def countIslands(M):
    R, C = len(M), len(M[0])
    count = 0
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1:
                dfs(M, i, j)
                count += 1
    return count

def isValid(M, R, C, i, j):
    return i >= 0 and j >= 0 and i < R and j < C and M[i][j] == 1

def countIslandsBfsSolution(M):
    R, C = len(M), len(M[0])
    count = 0
    for i in range(R):
        for j in range(C):
            if M[i][j] == 0:
                continue
            count += 1
            q = [[i, j]]
            while len(q) > 0:
                (x, y) = q.pop(0)
                M[x][y] = 0
                if isValid(M, R, C, x - 1, y - 1):
                    q.append([x-1, y-1])
                if isValid(M, R, C, x - 1, y):
                    q.append([x-1, y])
                if isValid(M, R, C, x - 1, y + 1):
                    q.append([x-1, y+1])
                if isValid(M, R, C, x, y + 1):
                    q.append([x, y+1])
                if isValid(M, R, C, x + 1, y + 1):
                    q.append([x+1, y+1])
                if isValid(M, R, C, x + 1, y):
                    q.append([x+1, y])
                if isValid(M, R, C, x + 1, y - 1):
                    q.append([x+1, y-1])
                if isValid(M, R, C, x - 1, y):
                    q.append([x-1, y])
    return count



graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

print(countIslandsBfsSolution(graph))
