# https://www.geeksforgeeks.org/distance-nearest-cell-1-binary-matrix/
def isValid(M, R, C, i, j):
    return i >= 0 and j >= 0 and i < R and j < C and M[i][j] == 0


def findNearestOne(M):
    R, C = len(M), len(M[0])
    visited = [[False for i in range(C)] for j in range(R)]
    q = []
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1:
                q.append((i, j, 0))
    while len(q) > 0:
        (i, j, d) = q.pop(0)
        visited[i][j] = True
        M[i][j] = d
        if isValid(M, R, C, i - 1, j) and not visited[i-1][j]:
            M[i - 1][j] = 1
            q.append((i - 1, j, d + 1))
        if isValid(M, R, C, i, j - 1) and not visited[i][j-1]:
            M[i][j - 1] = 1
            q.append((i, j - 1, d + 1))
        if isValid(M, R, C, i + 1, j) and not visited[i+1][j]:
            M[i + 1][j] = 1
            q.append((i + 1, j, d + 1))
        if isValid(M, R, C, i, j + 1) and not visited[i][j+1]:
            M[i][j+1] = 1
            q.append((i, j + 1, d + 1))
    print(M)

mat = [[0, 0, 0, 1], 
       [0, 0, 1, 1],
       [0, 1, 1, 0]]

findNearestOne(mat)




