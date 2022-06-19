'''
Given two arrays of positive integers of size m and n where m > n. We need to maximize the dot product by 
inserting zeros in the second array but we cannot disturb the order of elements.

Examples: 

Input : A[] = {2, 3 , 1, 7, 8} 
        B[] = {3, 6, 7}        
Output : 107
Explanation : We get maximum dot product after
inserting 0 at first and third positions in 
second array.
Maximum Dot Product : = A[i] * B[j] 
2*0 + 3*3 + 1*0 + 7*6 + 8*7 = 107

Input : A[] = {1, 2, 3, 6, 1, 4}
        B[] = {4, 5, 1}
Output : 46
'''
def maxDotProduct(a, b):
    n = len(a)
    m = len(b)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + a[i-1] * b[j-1])
    return dp[n][m]

a = [2, 3, 1, 7, 8]
b = [3, 6, 7]
print(maxDotProduct(a, b))

a = [1, 2, 3, 6, 1, 4]
b = [4, 5, 1]
print(maxDotProduct(a, b))