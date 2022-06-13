'''
Same as min remove.
Find length of longest palindromic subsequence.
'''
def minInsertions(s):
    n = len(s)
    lps = [[0 for i in range(n+1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        c1 = s[i-1]
        for j in range(1, n + 1):
            c2 = s[-j]
            if c1 == c2:
                lps[i][j] = 1 + lps[i-1][j-1]
            else:
                lps[i][j] = max(lps[i-1][j], lps[i][j-1])
    return n - lps[n][n]

s = "abcaa"
print(minInsertions(s))
