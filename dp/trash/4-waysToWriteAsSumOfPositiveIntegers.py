# https://www.geeksforgeeks.org/ways-to-write-n-as-sum-of-two-or-more-positive-integers/

'''
Input : n = 5
Output : 6
Explanation : All possible six ways are :
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

Input : 4
Output : 4
Explanation : All possible four ways are :
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
'''
def numWays(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n):
        for j in range(i, n + 1):
            dp[j] += dp[j-i]
    return dp[n]

print(numWays(6))
