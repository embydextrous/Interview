'''
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number. 
A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion. 
Find the longest chain which can be formed from a given set of pairs. 
For example, if the given pairs are {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} }, 
then the longest chain that can be formed is of length 3, and the chain is {{5, 24}, {27, 40}, {50, 90}}
'''
def maxLengthChain(a):
    n = len(a)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i][0] < a[j][1] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    return max(dp)

a = [[5, 24], [39, 60], [15, 28], [27, 40], [50, 90]]
print(maxLengthChain(a))