'''
Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X. 
X is the summation of values on each face when all the dice are thrown.

n = 3
m = 6
X = 8

No. of ways = 32
'''
def diceThrow(n, m, x):
    dp = [[0 for i in range(x+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, x + 1):
            # Fix this dice value as 1 we get dp[i-1][j-1]
            # For rest values we get dp[i-1][j-2] .... dp[i][j-m] -> This sum already recorded in dp[i][j-1] 
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            # Remove number of previous ways as we may have overcounted here
            if j - m - 1 >= 0:
                dp[i][j] -= dp[i-1][j-m-1]
    return dp[n][x]

n = 3
m = 6
x = 8
print(diceThrow(n, m, x))
