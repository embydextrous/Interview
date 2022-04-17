# https://www.geeksforgeeks.org/given-matrix-o-x-find-largest-subsquare-surrounded-x/
'''
Given a matrix where every element is either 'O' or 'X', find the largest subsquare surrounded by 'X'. 
In the below article, it is assumed that the given matrix is also a square matrix. The code given below 
can be easily extended for rectangular matrices.

Examples: 

Input: mat[N][N] = { {'X', 'O', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'O', 'X', 'O'},
                     {'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'O', 'O'},
                    };
Output: 3
The square submatrix starting at (1, 1) is the largest
submatrix surrounded by 'X'

Input: mat[M][N] = { {'X', 'O', 'X', 'X', 'X', 'X'},
                     {'X', 'O', 'X', 'X', 'O', 'X'},
                     {'X', 'X', 'X', 'O', 'O', 'X'},
                     {'X', 'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'O', 'X', 'O'},
                    };
Output: 4
The square submatrix starting at (0, 2) is the largest
submatrix surrounded by 'X'
'''
from matrix import printS

def createHMatrix(M, R, C):
    H = [[0 for j in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            if M[i][j] == 'X':
                if j == 0:
                    H[i][j] = 1
                else:
                    H[i][j] = H[i][j-1] + 1
    return H

def createVMatrix(M, R, C):
    V = [[0 for j in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            if M[i][j] == 'X':
                if i == 0:
                    V[i][j] = 1
                else:
                    V[i][j] = V[i-1][j] + 1
    return V

def findLargestSubsquare(M):
    R, C = len(M), len(M[0])
    H = createHMatrix(M, R, C)
    V = createVMatrix(M, R, C)
    maxVal = 0
    for i in range(R):
        for j in range(C):
            if i == 0 or j == 0:
                maxVal = max(maxVal, min(H[i][j], V[i][j]))
            elif M[i][j] == 'X':
                k = min(H[i][j], V[i][j])
                while k > 1:
                    if H[i-k+1][j] >= k and V[i][j-k+1] >= k:
                        break
                    k -= 1
                maxVal = max(maxVal, k)
                print(i, j, k)
    return maxVal

mat = [['X', 'O', 'X', 'X', 'X', 'X'],
       ['X', 'O', 'X', 'X', 'O', 'X'],
       ['X', 'X', 'X', 'O', 'O', 'X'],
       ['O', 'X', 'X', 'X', 'X', 'X'],
       ['X', 'X', 'X', 'O', 'X', 'O'],
       ['O', 'O', 'X', 'O', 'O', 'O']]

print(findLargestSubsquare(mat))



