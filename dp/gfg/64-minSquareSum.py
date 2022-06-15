'''
A number can always be represented as a sum of squares of other numbers. Note that 1 is a square and we can always break a number as (1*1 + 1*1 + 1*1 + …). 
Given a number n, find the minimum number of squares that sum to X.

Examples : 

    Input:  n = 100
    Output: 1
    Explanation:
    100 can be written as 102. Note that 100 can also be written as 52 + 52 + 52 + 52, but this representation requires 4 squares.

    Input:  n = 6
    Output: 3
'''
from math import floor, sqrt

def minSquares(n):
    dp = [10 ** 9] * (n + 1)
    dp[0] = 0
    for i in range(1, n+1):
        for j in range(1, floor(sqrt(i)) + 1):
            dp[i] = min(dp[i], 1 + dp[i - j * j])
    return dp[n]

n = 32
print(minSquares(n))