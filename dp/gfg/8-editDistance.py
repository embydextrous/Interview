'''
    s   u   n   d   a   y
s   0   1   2   3   4   5
a   1   1   2   3   3   4
t   2   2   2   3   4   4
u   3   2   3   3   4   5
r   4   3   3   4   4   5
d   5   4   4   3   4   5
a   6   5   5   4   3   4   
y   4   5   6   5   4   3

Given two strings str1 and str2 and below operations that can be performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.  

    Insert
    Remove
    Replace

All of the above operations are of equal cost. 

Examples: 

Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations. 
Replace 'n' with 'r', insert t, insert a
'''
def editDistance(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[n][m]

s2 = "saturday"
s1 = "sunday"
print(editDistance(s2, s1))