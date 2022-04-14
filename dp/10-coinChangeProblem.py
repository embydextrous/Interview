'''
Given a value N, if we want to make change for N cents, and we have infinite supply of each of 
S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn't matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
So output should be 4. 
For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. 
So the output should be 5.

1) Optimal Substructure 
To count the total number of solutions, we can divide all set solutions into two sets. 
1) Solutions that do not contain mth coin (or Sm). 
2) Solutions that contain at least one Sm. 
Let count(S[], m, n) be the function to count the number of solutions, then it can be written as sum of count(S[], m-1, n) and count(S[], m, n-Sm).
Therefore, the problem has optimal substructure property as the problem can be solved using solutions to subproblems. 
'''
def coinChange(coins, N):
    # Row 0 when ith coin is not included. It can be used to calculate result while computing Row 1 where 
    # ith coin is included.
    dp = [[0 for i in range(N+1)] for j in range(2)]
    # Base Cases
    dp[0][0] = 1
    dp[1][0] = 1
    for coin in coins:
        # Including this coin, not including this coin are stored in dp[0]
        for i in range(coin, N+1):
            e = 1
            while coin * e <= i:
                dp[1][i] += dp[0][i - coin * e]
                e += 1
        dp[0] = dp[1][:]
    return dp[1][N]

N = 10
coins = [2, 5, 3, 6]
print(coinChange(coins, N))
