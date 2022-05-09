from collections import deque

ROW = [0, -1, 0, 1]
COL = [-1, 0, 1, 0]

def isSafe(R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C

def bfs(M, R, C, i, j):
    q = deque([[i, j, 0]])
    visited = set()
    visited.add((i, j))
    while len(q) > 0:
        i, j, d = q.popleft()
        if M[i][j] == 1:
            return d
        for k in range(4):
            x, y = i + ROW[k], j + COL[k]
            if isSafe(R, C, x, y) and (x, y) not in visited:
                visited.add((x, y))
                q.append([x, y, d + 1])

def nearest1(M):
    R, C = len(M), len(M[0])
    result = [[0 for j in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if M[i][j] != 1:
                result[i][j] = bfs(M, R, C, i, j)
    return result

M = [[0, 0, 0, 1], 
     [0, 0, 1, 1],
     [0, 1, 1, 0]]

print(nearest1(M))