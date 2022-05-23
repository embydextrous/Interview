# Find lcs os string and its reverse.

# if s[i] == s[j], 1 + dp[i-1][j-1]
# else s[i], max(dp[i-1][j], dp[i][j-1])
# 
def lps(s):
    n = len(s)
    dp = [[0 for i in range(n+1)] for j in range(2)]
    for i in range(1, n+1):
        c1 = s[i-1]
        for j in range(1, n+1):
            c2 = s[n-j]
            if c1 == c2:
                dp[1][j] = dp[0][j-1] + 1
            else:
                dp[1][j] = max(dp[0][j], dp[1][j-1])
        dp[0], dp[1] = dp[1], [0] * (n + 1)
    return dp[0][n]

s = "BBABCBCAB"
print(lps(s))

