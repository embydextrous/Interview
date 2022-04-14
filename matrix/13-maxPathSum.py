# https://www.geeksforgeeks.org/maximum-path-sum-matrix/
'''
Given a matrix of N * M. Find the maximum path sum in matrix. The maximum path is sum of all elements 
from first row to last row where you are allowed to move only down or diagonally to left or right. 
You can start from any element in first row.

Examples: 

Input : mat[][] = 10 10  2  0 20  4
                   1  0  0 30  2  5
                   0 10  4  0  2  0
                   1  0  2 20  0  4
Output : 74
The maximum sum path is 20-30-4-20.

Input : mat[][] = 1 2 3
                  9 8 7
                  4 5 6
Output : 17
The maximum sum path is 3-8-6.

1   2   3
11  11  10
15  15  17
'''

def findMaxPathSum(M):
    R, C = len(M), len(M[0])
    for i in range(1, R):
        for j in range(C):
            if j == 0:
                M[i][j] += max(M[i-1][j], M[i-1][j+1])
            elif j == C - 1:
                M[i][j] += max(M[i-1][j-1], M[i-1][j])
            else:
                M[i][j] += max(M[i-1][j-1], M[i-1][j], M[i-1][j+1])
    return max(M[R-1])

mat = ([[ 10, 10, 2, 0, 20, 4 ],
        [ 1, 0, 0, 30, 2, 5 ],
        [ 0, 10, 4, 0, 2, 0 ],
        [ 1, 0, 2, 20, 0, 4 ]])

print(findMaxPathSum(mat))