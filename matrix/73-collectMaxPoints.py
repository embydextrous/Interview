'''
# https://www.geeksforgeeks.org/collect-maximum-points-in-a-grid-using-two-traversals/

Given a matrix where every cell represents points. How to collect maximum points using two traversals 
under following conditions?
Let the dimensions of given grid be R x C.
1) The first traversal starts from top left corner, i.e., (0, 0) and should reach left bottom corner, i.e., 
(R-1, 0). The second traversal starts from top right corner, i.e., (0, C-1) and should reach bottom right corner, 
i.e., (R-1, C-1)/
2) From a point (i, j), we can move to (i+1, j+1) or (i+1, j-1) or (i+1, j)
3) A traversal gets all points of a particular cell through which it passes. If one traversal has already 
collected points of a cell, then the other traversal gets no points if goes through that cell again.
 

Input :
    int arr[R][C] = {{3, 6, 8, 2},
                     {5, 2, 4, 3},
                     {1, 1, 20, 10},
                     {1, 1, 20, 10},
                     {1, 1, 20, 10},
                    };

     Output: 73

Explanation :

First traversal collects total points of value 3 + 2 + 20 + 1 + 1 = 27

Second traversal collects total points of value 2 + 4 + 10 + 20 + 10 = 46.
Total Points collected = 27 + 46 = 73.
'''
# Recursion Based Algo
# Check If cell is valid or not - in case of invalid return -inf
# Check is last row but invalid columns - return -inf
# Check if traversal complete - return sum of cells if columns different else just return column
# Otherwise init result as 0 and save columns sum if different, else just column value
# check max of 9 conditions, row + 1 -> (col1-1, col1, col1+1) * (col2-1, col2, col2+1)
# add it to result and return it

import sys

def maxPoints(M, R, C, x, y1, y2):
    # Cell is invalid
    if x < 0 or x >= R or y1 < 0 or y1 >= C or y2 < 0 or y2 >= C:
        return -sys.maxsize-1
    # Traversal not to proper destination
    if x == R - 1 and (y1 != 0 or y2 != C-1):
        return -sys.maxsize-1
    # Traversal Complete
    if x == R - 1 and y1 == 0 and y2 == C-1:
        return M[x][y1] if y1 == y2 else M[x][y1] + M[x][y2]
    result = M[x][y1] if y1 == y2 else M[x][y1] + M[x][y2]
    # maxPoints results can be remembered using a 3d matrix of size [R][C][C]
    result += max(
                    maxPoints(M, R, C, x + 1, y1 - 1, y2 - 1),
                    maxPoints(M, R, C, x + 1, y1, y2 - 1),
                    maxPoints(M, R, C, x + 1, y1 + 1, y2 - 1),
                    maxPoints(M, R, C, x + 1, y1 - 1, y2),
                    maxPoints(M, R, C, x + 1, y1, y2),
                    maxPoints(M, R, C, x + 1, y1 + 1, y2),
                    maxPoints(M, R, C, x + 1, y1 - 1, y2 + 1),
                    maxPoints(M, R, C, x + 1, y1, y2 + 1),
                    maxPoints(M, R, C, x + 1, y1 + 1, y2 + 1)
                )
    return result

def maxPointsUtil(M, R, C, x, y1, y2, dp):
    # Cell is invalid
    if x < 0 or x >= R or y1 < 0 or y1 >= C or y2 < 0 or y2 >= C:
        return -sys.maxsize-1
    # Traversal not to proper destination
    if x == R - 1 and (y1 != 0 or y2 != C-1):
        return -sys.maxsize-1
    # Traversal Complete
    if x == R - 1 and y1 == 0 and y2 == C-1:
        return M[x][y1] if y1 == y2 else M[x][y1] + M[x][y2]
    # Check is subproblem is already solved
    if dp[x][y1][y2] != -1:
        return dp[x][y1][y2]
    result = -sys.maxsize-1
    temp = M[x][y1] if y1 == y2 else M[x][y1] + M[x][y2]
    result = max(result, temp + maxPointsUtil(M, R, C, x + 1, y1 - 1, y2 - 1, dp))
    result = max(result, temp + maxPointsUtil(M, R, C, x + 1, y1 - 1, y2, dp))
    result = max(result, temp + maxPointsUtil(M, R, C, x + 1, y1 - 1, y2 + 1, dp))
    result = max(result, temp + maxPointsUtil(M, R, C, x + 1, y1, y2 - 1, dp))
    result = max(result, temp + maxPointsUtil(M, R, C, x + 1, y1, y2, dp))
    result = max(result, temp + maxPointsUtil(M, R, C, x + 1, y1, y2 + 1, dp))
    result = max(result, temp + maxPointsUtil(M, R, C, x + 1, y1 + 1, y2 - 1, dp))
    result = max(result, temp + maxPointsUtil(M, R, C, x + 1, y1 + 1, y2, dp))
    result = max(result, temp + maxPointsUtil(M, R, C, x + 1, y1 + 1, y2 + 1, dp))
    dp[x][y1][y2] = result
    return result

def maxPoints2(M):
    R, C = len(M), len(M[0])
    x = 0
    y1, y2 = 0, C - 1
    dp = [[[-1 for i in range(C)] for i in range(C)] for i in range(R)]
    return maxPointsUtil(M, R, C, x, y1, y2, dp)

M=  [[3, 6, 8, 2],
     [5, 2, 4, 3],
     [1, 1, 20, 10],
     [1, 1, 20, 10], 
     [1, 1, 20, 10]]
R, C = len(M), len(M[0])
x = 0
y1, y2 = 0, C-1

print(maxPoints2(M))