'''
Given three strings A, B and C. Write a function that checks whether C is an interleaving of A and B. C is said to be interleaving A and B, if it contains all and only 
characters of A and B and order of all characters in individual strings is preserved. 

Example: 

Input: strings: "XXXXZY", "XXY", "XXZ"
Output: XXXXZY is interleaved of XXY and XXZ
The string XXXXZY can be made by 
interleaving XXY and XXZ
String:    XXXXZY
String 1:    XX Y
String 2:  XX  Z

Input: strings: "XXY", "YX", "X"
Output: XXY is not interleaved of YX and X
XXY cannot be formed by interleaving YX and X.
The strings that can be formed are YXX and XYX.
'''
def checkInterleaved(A, B, C):
    n, m = len(A), len(B)
    if n + m != len(C):
        return False
    dp = [[False for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = B[j-1] == C[j-1] and dp[i][j-1]
            elif j == 0:
                dp[i][j] = A[i-1] == C[i-1] and dp[i-1][j]
            elif C[i+j-1] == A[i-1] and C[i+j-1] != B[j-1]:
                dp[i][j] = dp[i-1][j]
            elif C[i+j-1] != A[i-1] and C[i+j-1] == B[j-1]:
                dp[i][j] = dp[i][j-1]
            elif C[i+j-1] == A[i-1] and C[i+j-1] == B[j-1]:
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
    for row in dp:
        print(row)
    return dp[n][m]

'''
T   T   T   F
T   T   T   F
T   T   T   T
F   F   F   T
'''

A = "XXY"
B = "XXZ"
C = "XXXXZY"
print(checkInterleaved(A, B, C))


