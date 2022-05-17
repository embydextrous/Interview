'''
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of
minimum cost path to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse
through that cell. The total cost of a path to reach (m, n) is the sum of all the costs on that path
(including both source and destination). You can only traverse down, right and diagonally lower cells
from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1), and (i+1, j+1) can be 
traversed. You may assume that all costs are positive integers.
'''
def minCostPath(M):
    R, C = len(M), len(M[0])
    dp = [[0 for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            if i == 0 and j == 0:
                dp[i][j] = M[i][j]
            elif i == 0:
                dp[i][j] = M[i][j] + dp[i][j-1]
            elif j == 0:
                dp[i][j] = M[i][j] + dp[i-1][j]
            else:
                dp[i][j] = M[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    print(dp)
    return dp[R-1][C-1]

M =  [[1, 8, 8, 1, 5],
      [4, 1, 1, 8, 1],
      [4, 2, 8, 8, 1],
      [1, 5, 8, 8, 1]]

print(minCostPath(M))
