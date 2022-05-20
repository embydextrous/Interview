def minCoins(a, k):
    dp = [10 ** 9] * (k + 1)
    dp[0] = 0
    for i in range(1, k + 1):
        for d in a:
            if i >= d:
                dp[i] = min(dp[i], 1 + dp[i-d])
    return dp[k]

a = [2, 3, 5, 6]
k = 17
print(minCoins(a, k))