'''
Given N ropes, each rope has a length associated with it. At a time, only two consecutive small ropes tied at end form a large rope and cost of forming 
sum of their length. Find the minimum cost when all ropes are tied to form a single rope.

Examples: 

    Input: arr[] = {7, 6, 8, 6, 1, 1} 
    Output: 68 
    {7, 6, 8, 6, 1, 1} - {7, 6, 8, 6, 2}, cost = 2 
    {7, 6, 8, 6, 2} - {7, 6, 8, 8}, cost = 8 
    {7, 6, 8, 8} - {13, 8, 8}, cost = 13 
    {13, 8, 8} - {13, 16}, cost = 16 
    {13, 16} - {29}, cost = 29 
    2 + 8 + 13 + 16 + 29 = 68

    Input: arr[] = {10, 20, 30, 40} 
    Output: 190 
'''
# Also see, https://www.geeksforgeeks.org/minimum-cost-of-reducing-array-by-merging-any-adjacent-elements-repetitively/
def NConsecutiveRopes(a):
    n = len(a)
    pSum = [0] * (n+1)
    for i in range(n):
        pSum[i+1] = pSum[i] + a[i]
    print(pSum)
    dp = [[10 ** 9 if i != j else 0 for i in range(n)] for j in range(n)]
    for size in range(2, n + 1):
        for i in range(n-size+1):
            j = i + size - 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + pSum[j+1] - pSum[i])
    return dp[0][n-1]

a = [7, 6, 8, 6, 1, 1]
print(NConsecutiveRopes(a))