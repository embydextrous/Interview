from matrix import printS

def longestPathUtil(M, N, x, y, dp):
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
    if dp[x][y] != -1:
        return dp[x][y]
    l = u = r = d = -1
    if y > 0 and M[x][y] + 1 == M[x][y-1]:
        l = 1 + longestPathUtil(M, N, x, y - 1, dp)
    if x > 0 and M[x][y] + 1 == M[x-1][y]:
        u = 1 + longestPathUtil(M, N, x-1, y, dp)
    if y < N-1 and M[x][y] + 1 == M[x][y+1]:
        r = 1 + longestPathUtil(M, N, x, y + 1, dp)
    if x < N-1 and M[x][y] + 1 == M[x+1][y]:
        d = 1 + longestPathUtil(M, N, x+1, y, dp)
    dp[x][y] = max(1, l, u, r, d)
    return dp[x][y]

def longestPath(M):
    N = len(M)
    dp = [[-1 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                longestPathUtil(M, N, i, j, dp)
    maxPath = -1
    for row in dp:
        maxPath = max(maxPath, max(row))
    return maxPath

M = [[1, 2, 9],
     [5, 3, 8],
     [4, 6, 7]]

print(longestPath(M))

