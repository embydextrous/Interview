# https://www.geeksforgeeks.org/rotate-matrix-elements/

from matrix import printS

def rotateRingClockwise(m, n, k):
    # rotate top
    backValue = m[k+1][k]
    for i in range(k, n - k):
        m[k][i], backValue = backValue, m[k][i]
    # rotate right
    for i in range(k+1, n - k):
        m[i][n-k-1], backValue = backValue, m[i][n-k-1]
    # rotate bottom
    for i in range(n-k-2, k - 1, -1):
        m[n-k-1][i], backValue = backValue, m[n-k-1][i]
    # rotate left
    for i in range(n - k - 2, k, -1):
        m[i][k], backValue = backValue, m[i][k]

def rotateMatrix(m):
    n = len(m)
    for i in range(n//2):
        rotateRingClockwise(m, n, i)

matrix =[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ] 
        ]

rotateMatrix(matrix)
printS(matrix)