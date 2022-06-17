'''
Given an array arr[] of length N and an integer X, the task is to find the number of subsets with a sum equal to X.

Examples: 

    Input: arr[] = {1, 2, 3, 3}, X = 6 
    Output: 3 
    All the possible subsets are {1, 2, 3}, 
    {1, 2, 3} and {3, 3}

    Input: arr[] = {1, 1, 1, 1}, X = 1 
    Output: 4 

        0   1   2   3   4   5   6
    -   1   0   0   0   0   0   0
    3   1   0   0   1   0   0   0 
    3   1   0   0   2   0   0   1
    3   1   0   0   3   0   0   3
    3   1   0   0   4   0   0   6
'''
def countSubsetsWithSum(a, x):
    n = len(a)
    dp = [[0 for i in range(x + 1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        p = a[i-1]
        for j in range(x + 1):
            if p > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-p]
    for row in dp:
        print(row)
    return dp[n][x]

a = [3, 3, 3, 3]
x = 6
print(countSubsetsWithSum(a, x))