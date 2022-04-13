'''
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. 
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included. 
Given a number n, the task is to find n'th Ugly number.

Examples:  

Input  : n = 7
Output : 8

Input  : n = 10
Output : 12

Input  : n = 15
Output : 24

Input  : n = 150
Output : 5832
'''
def ugly(n):
    dp = [0] * n
    dp[0] = 1
    i2 = i3 = i5 = 0
    for i in range(1, n):
        next2, next3, next5 = dp[i2] * 2, dp[i3] * 3, dp[i5] * 5
        dp[i] = min(next2, next3, next5)
        if next2 == dp[i]:
            i2 += 1
        if next3 == dp[i]:
            i3 += 1
        if next5 == dp[i]:
            i5 += 1
    return dp[n-1]

print(ugly(150))