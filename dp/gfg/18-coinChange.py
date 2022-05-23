'''
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn't matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2},
{2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.

Same as number of solutions for linear equations of n variables. See 27.

Also see, https://www.geeksforgeeks.org/count-number-ways-reach-given-score-game/
'''
def coinChange(a, k):
    dp = [0] * (k + 1)
    dp[0] = 1
    for d in a:
        for i in range(d, k+1):
            dp[i] += dp[i-d]
    return dp[k]

a = [2, 3, 5, 6]
k = 10
print(coinChange(a, k))
