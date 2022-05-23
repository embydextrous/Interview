def eggDrop(n, k):
    dp = [[10**9 for i in range(n)] for j in range(k)]
    for i in range(k):
        for j in range(n):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = 1
            else:
                for x in range(j):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][x], dp[i][j-x-1]))
    print(dp)
    return dp[k-1][n-1]

n = 600
k = 8
print(eggDrop(n, k))
