'''
Given a 2D binary matrix of N rows and M columns. The task is to check whether the matrix is horizontal symmetric, 
vertical symmetric, or both. The matrix is said to be horizontal symmetric if the first row is the same as the 
last row, the second row is the same as the second last row, and so on. And the matrix is said to be vertical 
symmetric if the first column is the same as the last column, the second column is the same as the second last 
column, and so on. Print “VERTICAL” if the matrix is vertically symmetric, “HORIZONTAL” if the matrix is 
vertically symmetric, “BOTH” if the matrix is vertical and horizontal symmetric, and “NO” if not symmetric.

Examples:  

Input: N = 3 M = 3
0 1 0
0 0 0
0 1 0
Output: Both
First and third row are same and also second row 
is in middle. So Horizontal Symmetric.
Similarly, First and third column are same and
also second column is in middle, so Vertical 
Symmetric.

Input:
0 0 1
1 1 0
0 0 1.
Output: Both 
'''
def checkVerticalSymmetry(M):
    R, C = len(M), len(M[0])
    l, r = 0, R - 1
    while l < r:
        for j in range(C):
            if M[l][j] != M[r][j]:
                return False
        l += 1
        r -= 1
    return True

def checkHorizontalSymmetry(M):
    R, C = len(M), len(M[0])
    l, r = 0, C - 1
    while l < r:
        for i in range(R):
            if M[i][l] != M[i][r]:
                return False
        l += 1
        r -= 1
    return True

def checkHorizontalVerticalSymmetry(M):
    isHorizontalSymmetric = checkHorizontalSymmetry(M)
    isVerticalSymmetric = checkVerticalSymmetry(M)
    if isHorizontalSymmetric and isVerticalSymmetric:
        print("BOTH")
    elif isHorizontalSymmetric:
        print("HORIZONTAL")
    elif isVerticalSymmetric:
        print("VERTICAL")
    else:
        print("NONE")

M = [[1, 0, 1],
     [0, 1, 0],
     [0, 0, 0]]

checkHorizontalVerticalSymmetry(M)