'''
Given two strings str1 and str2, the task is to find the length of the shortest string that has both str1 
and str2 as subsequences.

Examples : 

Input:   str1 = "geek",  str2 = "eke"
Output: 5
Explanation: 
String "geeke" has both string "geek" 
and "eke" as subsequences.

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  9
Explanation: 
String "AGXGTXAYB" has both string 
"AGGTAB" and "GXTXAYB" as subsequences.
'''
from collections import deque


def lcs(s1, s2):
    n, m = len(s1), len(s2)
    a, b = (s1, s2) if n > m else (s2, s1)
    dp = [[0 for i in range(min(n, m) + 1)] for j in range(2)]
    for c1 in a:
        for j in range(1, min(n, m) + 1):
            c2 = b[j-1]
            if c1 == c2:
                dp[1][j] = dp[0][j-1] + 1
            else:
                dp[1][j] = max(dp[0][j], dp[1][j-1])
        dp[0] = dp[1]
    return dp[1][min(n, m)]

def printScs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        c1 = s1[i-1]
        for j in range(m + 1):
            c2 = s2[j-1]
            if c1 == c2:
                dp[i][j] = dp[i][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    for row in dp:
        print(row)
    i = n
    j = m
    q = deque()
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            q.appendleft(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] < dp[i][j-1]:
            q.appendleft(s2[j-1])
            j -= 1
        else:
            q.appendleft(s1[i-1])
            i -= 1
    while i > 0:
        q.appendleft(s1[i-1])
        i -= 1
    while j > 0:
        q.appendleft(s2[j-1])
        j -= 1
    return "".join(q)


def scs(s1, s2):
    return len(s1) + len(s2) - lcs(s1, s2)

s1 = "AGGTAB"
s2 = "GXTXAYB"
print(scs(s1, s2))
print(printScs(s1, s2))