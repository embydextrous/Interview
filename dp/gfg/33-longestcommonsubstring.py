def longestCommonSubstring(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    maxi = 0
    x = -1
    # Compare suffix of prefixes of two strings
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if 1 + dp[i-1][j-1] > maxi:
                    maxi = 1 + dp[i-1][j-1]
                    x = i - 1
    print(x)
    print(s1[x-maxi+1:x+1])
    return maxi

s1 = "pqabcxy"
s2 = "xyzabcp"
print(longestCommonSubstring(s1, s2))