'''
Given a grid of size m * n, let us assume you are starting at (1, 1) and your goal is to reach (m, n). At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space are marked as 1 and 0 respectively in the grid.

Examples:  

Input: [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
Output : 2
There is only one obstacle in the middle.
'''
def numPaths(M):
    R, C = len(M), len(M[0])
    dp = [[0 for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[R-1][C-1]

M = [[0, 0, 0],
     [0, 1, 0],
     [0, 0, 0]]

M = [[0,0,0,0],
     [0,1,0,1],
     [0,0,0,0],
     [0,0,0,0]]

print(numPaths(M))