'''
Given a matrix of size N*M, and a number K. We have to rotate the matrix K times to the right side. 
Examples: 
 

Input :  N = 3, M = 3, K = 2
         12 23 34
         45 56 67
         78 89 91 

Output : 23 34 12
         56 67 45
         89 91 78 


Input :  N = 2, M = 2, K = 2
         1 2
         3 4
         
Output : 1 2
         3 4
'''
from matrix import printS

def rotateMatrix(m, k):
    for a in m:
        rotate(a, k % len(a))

def rotate(a, k):
    r = len(a) - 1
    reverse(a, 0, r)
    reverse(a, 0, k - 1)
    reverse(a, k, r)

def reverse(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

M = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
rotateMatrix(M, 3)
printS(M)