# https://www.geeksforgeeks.org/find-if-given-matrix-is-toeplitz-or-not/
'''
Given a square matrix, find if it's a Toeplitz matrix or not. A Toeplitz (or diagonal-constant) 
matrix is a matrix in which each descending diagonal from left to right is constant, i.e., 
all elements in a diagonal are same.
In general, any nxn matrix mat[][] is a Toeplitz matrix if every cell mat[i][j] is same as 
mat[i-1][j-1], mat[i+1][j+1], mat[i-2][j-2], mat[i+2][j+2], .. for every cell mat[i][j] and all the 
valid cells mat[i+k][j+k] or mat[i-k][j-k] 

Examples : 

Input: mat[N][N] = {{ 6, 7, 8},
                    { 4, 6, 7},
                    { 1, 4, 6}},
Output : True;
Values in all diagonals are same.

Input: mat[N][N] = {{ 6, 7, 8, 9 },
                    { 4, 6, 7, 8 },
                    { 1, 4, 6, 7 },
                    { 0, 1, 4, 6 },
                    { 2, 0, 1, 4 }};
Output : True;

Input: mat[N][N] = {{ 6, 3, 8},
                    { 4, 9, 7},
                    { 1, 4, 6}},
Output : False;
'''

def isToeplitz(M):
    R, C = len(M), len(M[0])
    for i in range(1, R):
        for j in range(1, C):
            if M[i][j] != M[i-1][j-1]:
                return False
    return True

M = [[6, 3, 8],
     [4, 6, 3],
     [1, 4, 6]]

print(isToeplitz(M))

    

