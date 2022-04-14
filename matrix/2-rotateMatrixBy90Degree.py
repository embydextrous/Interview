# anti-clockwise rotation
'''
Given a square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.
Examples : 
 
Input:
Matrix:
 1  2  3
 4  5  6
 7  8  9
Output:
 3  6  9 
 2  5  8 
 1  4  7 
The given matrix is rotated by 90 degree 
in anti-clockwise direction.

Input:
 1  2  3  4 
 5  6  7  8 
 9 10 11 12 
13 14 15 16 
Output:
 4  8 12 16 
 3  7 11 15 
 2  6 10 14 
 1  5  9 13
The given matrix is rotated by 90 degree 
in anti-clockwise direction.
'''

from matrix import printS

# Complexity O(n^2)
def rotateMatrixBy90Degree2(m):
    # transpose
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]

    # reverse all columns
    for i in range(n):
        l, r = 0, n - 1
        while l < r:
            m[l][i], m[r][i] = m[r][i], m[l][i]
            l += 1
            r -= 1


matrix =[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ] 
        ]

rotateMatrixBy90Degree2(matrix)
printS(matrix)