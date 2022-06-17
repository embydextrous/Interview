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
    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            if i == R - 1 and j == C - 1:
                M[i][j] = max(1, 1 - M[i][j])
            elif i == R - 1:
                M[i][j] = max(1, M[i][j+1] - M[i][j])
            elif j == C - 1:
                M[i][j] = max(1, M[i+1][j] - M[i][j])
            else:
                M[i][j] = max(1, min(M[i+1][j], M[i][j+1]) - M[i][j])
    return M[0][0]

M = [[-2, -3, 3],
     [-5, -10, 1],
     [10, 30, -5]]

print(minPositivePoints(M))