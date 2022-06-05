from collections import defaultdict, deque

# Climb Stairs - Tomorrow
# Dominoes and Trominoes - Tomorrow
# Stock Problems - Today
from math import floor, sqrt

def palindromePartition(s):
    n = len(s)
    lps = [[True for i in range(n)] for j in range(n)]
    for size in range(2, n + 1):
        for i in range(n - size + 1):
            j = i + size - 1
            lps[i][j] = s[i] == s[j] and lps[i+1][j-1]
    dp = [10 ** 9] * n
    dp[0] = 0
    for i in range(1, n):
        if lps[0][i]:
            dp[i] = 0
        else:
            for j in range(i, 0, -1):
                if lps[j][i]:
                    if i == n - 1 and 1 + dp[j-1] > dp[i]:
                        print(i, j)
                    dp[i] = min(dp[i], 1 + dp[j-1])
    print(dp)
    return dp[n-1]
'''
i = 1
T F F T F
T T T F F
T T T F F
T T T T F
T T T T T
'''

s = "a|babbbab|babab"
print(palindromePartition(s))