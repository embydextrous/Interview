# https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/

'''
Given a n*n matrix where all numbers are distinct, find the maximum length path (starting from any cell) 
such that all cells along the path are in increasing order with a difference of 1. 
We can move in 4 directions from a given cell (i, j), i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j)
or (i, j-1) with the condition that the adjacent cells have a difference of 1.
Example: 
 

Input:  mat[][] = {{1, 2, 9}
                   {5, 3, 8}
                   {4, 6, 7}}
Output: 4
The longest path is 6-7-8-9. 

Reco
'''
from matrix import printS

def longestPathUtil(M, N, x, y, dp):
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
    if dp[x][y] != -1:
        return dp[x][y]
    l = u = r = d = -1
    if y > 0 and M[x][y] + 1 == M[x][y-1]:
        l = 1 + longestPathUtil(M, N, x, y - 1, dp)
    if x > 0 and M[x][y] + 1 == M[x-1][y]:
        u = 1 + longestPathUtil(M, N, x-1, y, dp)
    if y < N-1 and M[x][y] + 1 == M[x][y+1]:
        r = 1 + longestPathUtil(M, N, x, y + 1, dp)
    if x < N-1 and M[x][y] + 1 == M[x+1][y]:
        d = 1 + longestPathUtil(M, N, x+1, y, dp)
    dp[x][y] = max(1, l, u, r, d)
    return dp[x][y]

def isSafe(R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C

def dfs(M, R, C, i, j, pathLen, visited):
    visited.add((i, j))
    pathLen[0] += 1
    ROW = [0, -1, 0, 1]
    COL = [-1, 0, 1, 0]
    for k in range(4):
        x, y = i + ROW[k], j + COL[k]
        if isSafe(R, C, x, y) and (x, y) not in visited and abs(M[x][y] - M[i][j]) == 1:
            dfs(M, R, C, x, y, pathLen, visited)

def longestPath2(M):
    R, C = len(M), len(M[0])
    visited = set()
    maxLen = 0
    for i in range(R):
        for j in range(C):
            pathLen = [0]
            if (i, j) not in visited:
                dfs(M, R, C, i, j, pathLen, visited)
                maxLen = max(maxLen, pathLen[0])
    return maxLen

    

M = [[1, 2, 9],
     [5, 3, 8],
     [4, 6, 7]]

print(longestPath2(M))

