# https://www.geeksforgeeks.org/rotate-matrix-elements/
'''
Given a matrix, clockwise rotate elements in it.

Examples:

Input
1    2    3
4    5    6
7    8    9

Output:
4    1    2
7    5    3
8    9    6

For 4*4 matrix
Input:
1    2    3    4    
5    6    7    8
9    10   11   12
13   14   15   16

Output:
5    1    2    3
9    10   6    4
13   11   7    8
14   15   16   12
'''

from matrix import printS

def rotateRingClockwise(M, R, C, k):
    # rotate top
    backValue = M[k+1][k]
    for i in range(k, C - k):
        M[k][i], backValue = backValue, M[k][i]
    # rotate right
    for i in range(k + 1, R - k):
        M[i][C - k - 1], backValue = backValue, M[i][C - k - 1]
    # rotate bottom
    for i in range(C -k - 2, k - 1, -1):
        M[R - k - 1][i], backValue = backValue, M[R - k - 1][i]
    # rotate left
    for i in range(R - k - 2, k, -1):
        M[i][k], backValue = backValue, M[i][k]

def rotateMatrix(M):
    R, C = len(M), len(M)
    n = min(R, C)
    for i in range(n//2):
        rotateRingClockwise(M, R, C, i)

matrix =[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ] 
        ]

rotateMatrix(matrix)
printS(matrix)