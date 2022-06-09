'''
Given a 2D matrix, find the largest rectangular sub-matrix whose sum is 0. for example consider the following N x M input matrix 
 

Examples: 
 

Input :  1,  2,  3
        -3, -2, -1          
         1,  7,  5

Output : 1,  2,  3          
        -3, -2, -1

Input :  9,  7, 16,  5
         1, -6, -7,  3          
         1,  8,  7,  9          
         7, -2,  0, 10

Output :-6, -7
          8,  7          
         -2,  0    
'''
# Also see, https://www.geeksforgeeks.org/largest-area-rectangular-sub-matrix-equal-number-1s-0s/ [Convert all 0 to -1 and find zero sum]
def maxZeroSumArray(a):
    n = len(a)
    lSum = 0
    start = end = -1
    size = 0
    d = {}
    for i in range(n):
        lSum += a[i]
        if lSum == 0 and i + 1 >= size:
            size = i + 1
            start, end = 0, i
        elif lSum in d:
            if i - d[lSum] >= size:
                size = i - d[lSum]
                start, end = d[lSum] + 1, i
        else:
            d[lSum] = i
    return (size, start, end)
        

def largestMatrixWithZeroSum(M):
    R, C = len(M), len(M[0])
    maxSize = 0
    fl = fr = ft = fb = -1
    for left in range(C):
        temp = [0] * R
        for right in range(left, C):
            for i in range(R):
                temp[i] += M[i][right]
            size, top, bottom = maxZeroSumArray(temp)
            if size * (right - left + 1) > maxSize:
                maxSize = size * (right - left + 1)
                fl = left
                fr = right
                ft = top
                fb = bottom
    for i in range(ft, fb + 1):
        for j in range(fl, fr + 1):
            print(M[i][j], end = " ")
        print()

M = [[9, 7, 16, 5],
     [1, -6, -7, 3],
     [1, 8, 7, 9],
     [7, -2, 0, 10]]

largestMatrixWithZeroSum(M)