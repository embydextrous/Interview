'''
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total
value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent
values and weights associated with n items respectively. Also given an integer W which represents knapsack
capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller
than or equal to W. You cannot break an item, either pick the complete item or don't pick it (0-1 property).
'''
def knapsack(weights, value, W):
    dp = [[0 for i in range(W+1)] for j in range(2)]
    for i in range(len(weights)):
        weight = weights[i]
        for j in range(1, W + 1):
            if j < weight:
                dp[1][j] = dp[0][j]
            else:
                dp[1][j] = max(dp[0][j], value[i] + dp[0][j-weight])
        dp[0] = dp[1]
    return dp[1][W]

val = [1, 6, 10, 16]
wt = [1, 2, 3, 5]
W = 7
print (knapsack(wt, val, W))