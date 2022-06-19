'''
Given two sequences A, B, find out number of unique ways in sequence A, to form a subsequence of A that is 
identical to sequence B. Transformation is meant by converting string A (by removing 0 or more characters) 
to string B.

Examples:

Input : A = "abcccdf", B = "abccdf"
Output : 3
Explanation : Three ways will be -> "ab.ccdf", 
"abc.cdf" & "abcc.df" .
"." is where character is removed. 

Input : A = "aabba", B = "ab"
Output : 4
Explanation : Four ways will be -> "a.b..",
 "a..b.", ".ab.." & ".a.b." .
"." is where characters are removed.
'''
# Convert s1 to s2, n > m
def ways(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 if j != 0 else 1 for i in range(n+1)] for j in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[j-1] != s2[i-1]:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    return dp[m][n]

s1 = "aabba"
s2 = "ab"
print(ways(s1, s2))