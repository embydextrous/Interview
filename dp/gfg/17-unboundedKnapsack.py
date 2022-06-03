# Repeteition of Items is allowed
def unboundedKnapsack(W, weights, values):
    dp = [0] * (W + 1)
    for i in range(1, W + 1):
        for j in range(len(weights)):
            weight = weights[j]
            if i >= weight:
                dp[i] = max(dp[i], dp[i-weight] + values[j])
    return dp[W]

values = [1, 4, 1, 6, 5, 4]
weights = [2, 3, 1, 6, 4, 5]
W = 10   
print(unboundedKnapsack(W, weights, values))
