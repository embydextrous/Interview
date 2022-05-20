def coinChange(a, k):
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(1, k + 1):
        for d in a:
            if i >= d:
                dp[i] += dp[i-d]
    return dp[k]

a = [2, 3, 5, 6]
k = 10
print(coinChange(a, k))