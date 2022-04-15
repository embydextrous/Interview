'''
Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller 
than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, 
if the length of the rod is 8 and the values of different pieces are given as the following, then the maximum 
obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
'''
def cutRod(prices, L):
    dp = [0] * (L+1)
    for i in range(1, L + 1):
        dp[i] = prices[i-1]
        for j in range(1, i//2 + 1):
            dp[i] = max(dp[i], dp[j] + dp[i-j])
    return dp[L]

prices = [3, 5, 8, 9, 10, 17, 17, 20]
L = 8
print(cutRod(prices, L))