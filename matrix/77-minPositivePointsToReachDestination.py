# https://www.geeksforgeeks.org/minimum-positive-points-to-reach-destination/
'''
Given a grid with each cell consisting of positive, negative or no points i.e, zero points. 
We can move across a cell only if we have positive points ( > 0 ). 
Whenever we pass through a cell, points in that cell are added to our overall points. 
We need to find minimum initial points to reach cell (m-1, n-1) from (0, 0).

Constraints :

From a cell (i, j) we can move to (i+1, j) or (i, j+1).
We cannot move from (i, j) if your overall points at (i, j) is <= 0.
We have to reach at (n-1, m-1) with minimum positive points i.e., > 0.
Example:

Input: points[m][n] = { {-2, -3,   3}, 
                        {-5, -10,  1}, 
                        {10,  30, -5} 
                      };
Output: 7
Explanation: 
7 is the minimum value to reach destination with 
positive throughout the path. Below is the path.

(0,0) -> (0,1) -> (0,2) -> (1, 2) -> (2, 2)

We start from (0, 0) with 7, we reach(0, 1) 
with 5, (0, 2) with 2, (1, 2) with 5, (2, 2)
with and finally we have 1 point (we needed 
greater than 0 points at the end). 
7   5   2
6   11   5
1   1   6
'''
from matrix import printS

def minPositivePoints(M):
    R, C = len(M), len(M[0])
    dp = [[0 for x in range(C)] for y in range(R)]
    # Fill dp for bottom right point
    if M[R-1][C-1] > 0:
        dp[R-1][C-1] = 1
    else:
        dp[R-1][C-1] = 1 - M[R-1][C-1]
    # Fill dp for last row
    for j in range(C-2, -1, -1):
        dp[R-1][j] = max(dp[R-1][j+1] - M[R-1][j], 1)
    # Fill dp for last column
    for i in range(R-2, -1, -1):
        dp[i][C-1] = max(dp[i+1][C-1] - M[i][C-1], 1)
    # Fill rest of cells
    for i in range(R-2, -1, -1):
        for j in range(C-2, -1, -1):
            minPointsOnExit = min(dp[i+1][j], dp[i][j+1])
            dp[i][j] = max(minPointsOnExit - M[i][j], 1)
    printS(dp)

M = [[-2, -3, 3],
     [-5, -10, 1],
     [10, 30, -5]]

minPositivePoints(M)