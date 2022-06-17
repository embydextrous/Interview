def countPathsUtil(x, y, k, d, dp):
    if x < 0 or y < 0 or k < 0:
        return 0
    if x == 0 and y == 0:
        return 1
    if k == 0:
        if d == 0 and x == 0:
            return 1
        if d == 1 and y == 0:
            return 1
        return 0
    if dp[x][y][k][d] != -1:
        return dp[x][y][k][d]
    if d == 0:
        dp[x][y][k][d] = countPathsUtil(x, y - 1, k, d, dp) + countPathsUtil(x - 1, y, k - 1, abs(d-1), dp)
    else:
        dp[x][y][k][d] = countPathsUtil(x, y - 1, k - 1, abs(d-1), dp) + countPathsUtil(x - 1, y, k, d, dp)
    return dp[x][y][k][d]

def countPaths(n, m, k):
    if n == 0 and m == 0:
        return 1
    x = n - 1
    y = m - 1
    dp = [[[[-1 for _ in range(2)]
            for _ in range(k+1)]
            for _ in range(m)]
            for _ in range(n)]
    return countPathsUtil(x - 1, y, k, 1, dp) + countPathsUtil(x, y - 1, k, 0, dp)
    

n = 3
m = 3
k = 2
print(countPaths(n, m, k))