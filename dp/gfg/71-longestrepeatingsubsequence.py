'''
Given a string, find the length of the longest repeating subsequence such that the two subsequences don't have same string character at the same position, i.e., 
any i'th character in the two subsequences shouldn't have the same index in the original string. 

Input = "AABEBCDD"

Output = 3
"ABD"
'''
def lrs(s):
    n = len(s)
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i-1] == s[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]

'''
    -   A   A   B   E   B   C   D   D
-   0   0   0   0   0   0   0   0   0
A   0   0   1   1   1   1   1   1   1
A   0   1   1   1   1   1   1   1   1
B   0   1   1   1   1   2   2   2   2
E   0   1   1   1   1   2   2   2   2
B   0   1   1   2   2   2   2   2   2
C   0   1   1   2   2   2   2   2   2
D   0   1   1   2   2   2   2   2   3
D   0   1   1   2   2   2   2   3   3
'''

s = "AABEBCDD"
print(lrs(s))
