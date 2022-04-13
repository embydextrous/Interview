# https://www.geeksforgeeks.org/rotate-matrix-180-degree/
'''
Given a square matrix, the task is that we turn it by 180 degrees in an anti-clockwise direction without 
using any extra space. 

Examples : 

Input :  1  2  3
         4  5  6
         7  8  9
Output : 9 8 7 
         6 5 4 
         3 2 1

Input :  1 2 3 4 
         5 6 7 8 
         9 0 1 2 
         3 4 5 6 
Output : 6 5 4 3 
         2 1 0 9 
         8 7 6 5 
         4 3 2 1
'''
from matrix import printS

def rotateBy180(m):
    n = len(m)
    l, r = 0, n -1
    while l < r:
        m[l], m[r] = m[r], m[l]
        l, r = l + 1, r - 1
    for i in range(len(m)):
        m[i] = m[i][::-1]

matrix =[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ] 
        ]

rotateBy180(matrix)
printS(matrix)