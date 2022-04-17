# https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
'''
Given a binary matrix, find out the maximum size square sub-matrix with all 1s. 

Input Matrix: 
[[0, 1, 1, 0, 1],
 [1, 1, 0, 1, 0],
 [0, 1, 1, 1, 0],
 [1, 1, 1, 1, 0],
 [1, 1, 1, 1, 1],
 [0, 0, 0, 0, 0]]

Output = 3
'''
def maxAllOneSquareSubMatrix(M):
    R, C = len(M), len(M[0])
    maxi = 0
    for i in range(R):
        for j in range(C):
            if i != 0 and j != 0 and M[i][j] == 1:
                M[i][j] = min(M[i-1][j], M[i-1][j-1], M[i][j-1]) + 1
            maxi = max(M[i][j], maxi)
    return maxi

M =    [[0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]]

print(maxAllOneSquareSubMatrix(M))
        