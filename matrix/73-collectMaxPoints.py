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
MINUS_INF = -10**9

def maxPointsRecursiveUtil(M, R, C, x, y1, y2):
    # Out of Bounds Case
    if y1 < 0 or y1 >= C or y2 < 0 or y2 >= C:
        return MINUS_INF
    # Wrong Walk
    if x == R - 1 and (y1 != 0 or y2 != C - 1):
        return MINUS_INF
    # Right Walk
    if x == R - 1 and y1 == 0 and y2 == C - 1:
        return M[x][y1] + M[x][y2] if y1 != y2 else M[x][y1]
    temp = M[x][y1] + M[x][y2] if y1 != y2 else M[x][y1]
    result = MINUS_INF
    result = max(result, temp + maxPointsRecursiveUtil(M, R, C, x + 1, y1 - 1, y2 - 1))
    result = max(result, temp + maxPointsRecursiveUtil(M, R, C, x + 1, y1, y2 - 1))
    result = max(result, temp + maxPointsRecursiveUtil(M, R, C, x + 1, y1 + 1, y2 - 1))
    result = max(result, temp + maxPointsRecursiveUtil(M, R, C, x + 1, y1 - 1, y2))
    result = max(result, temp + maxPointsRecursiveUtil(M, R, C, x + 1, y1, y2))
    result = max(result, temp + maxPointsRecursiveUtil(M, R, C, x + 1, y1 + 1, y2))
    result = max(result, temp + maxPointsRecursiveUtil(M, R, C, x + 1, y1 - 1, y2 + 1))
    result = max(result, temp + maxPointsRecursiveUtil(M, R, C, x + 1, y1, y2 + 1))
    result = max(result, temp + maxPointsRecursiveUtil(M, R, C, x + 1, y1 + 1, y2 + 1))
    return result

def maxPointsRecursive(M):
    R, C = len(M), len(M[0])
    x, y1, y2 = 0, 0, C - 1
    return maxPointsRecursiveUtil(M, R, C, x, y1, y2)

def maxPointsUtil(M, R, C, x, y1, y2, dp):
    if y1 < 0 or y1 >= C or y2 < 0 or y2 >= C:
        return MINUS_INF
    if x == R - 1 and (y1 != 0 or y2 != C - 1):
        return MINUS_INF
    if x == R - 1 and y1 == 0 and y2 == C - 1:
        dp[x][y1][y2] = M[x][y1] if y1 == y2 else M[x][y1] + M[x][y2]
        return M[x][y1] if y1 == y2 else M[x][y1] + M[x][y2]
    if dp[x][y1][y2] != -1:
        return dp[x][y1][y2]
    temp = M[x][y1] if y1 == y2 else M[x][y1] + M[x][y2]
    dp[x][y1][y2] = max(dp[x][y1][y2], temp + maxPointsUtil(M, R, C, x + 1, y1 - 1, y2 - 1, dp))
    dp[x][y1][y2] = max(dp[x][y1][y2], temp + maxPointsUtil(M, R, C, x + 1, y1, y2 - 1, dp))
    dp[x][y1][y2] = max(dp[x][y1][y2], temp + maxPointsUtil(M, R, C, x + 1, y1 + 1, y2 - 1, dp))
    dp[x][y1][y2] = max(dp[x][y1][y2], temp + maxPointsUtil(M, R, C, x + 1, y1 - 1, y2, dp))
    dp[x][y1][y2] = max(dp[x][y1][y2], temp + maxPointsUtil(M, R, C, x + 1, y1, y2, dp))
    dp[x][y1][y2] = max(dp[x][y1][y2], temp + maxPointsUtil(M, R, C, x + 1, y1 + 1, y2, dp))
    dp[x][y1][y2] = max(dp[x][y1][y2], temp + maxPointsUtil(M, R, C, x + 1, y1 - 1, y2 + 1, dp))
    dp[x][y1][y2] = max(dp[x][y1][y2], temp + maxPointsUtil(M, R, C, x + 1, y1, y2 + 1, dp))
    dp[x][y1][y2] = max(dp[x][y1][y2], temp + maxPointsUtil(M, R, C, x + 1, y1 + 1, y2 + 1, dp))
    return dp[x][y1][y2]
    

def maxPoints(M):
    R, C = len(M), len(M[0])
    x, y1, y2 = 0, 0, C - 1
    dp = [[[-1 for k in range(C)] for j in range(C)] for i in range(R)]
    maxPointsUtil(M, R, C, x, y1, y2, dp)
    return dp[0][0][C-1]


M=  [[3, 6, 8, 2],
     [5, 2, 4, 3],
     [1, 1, 20, 10],
     [1, 1, 20, 10], 
     [1, 1, 20, 10]]

print(maxPoints(M))