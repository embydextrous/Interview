# https://www.geeksforgeeks.org/a-boolean-matrix-question/

'''
Given a boolean matrix mat[M][N] of size M X N, modify it such that if a matrix cell mat[i][j] is 1 (or true) 
then make all the cells of ith row and jth column as 1. 
 
Example 1
The matrix
1 0
0 0
should be changed to following
1 1
1 0
'''
from matrix import printS

def transformMatrix(M):
    R, C = len(M), len(M[0])
    rowSet = set()
    colSet = set()
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1:
                rowSet.add(i)
                colSet.add(j)
    for i in range(R):
        for j in range(C):
            if i in rowSet or j in colSet:
                M[i][j] = 1


mat = [ [1, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0] ]

transformMatrix(mat)
printS(mat)