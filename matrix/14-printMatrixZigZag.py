# https://www.geeksforgeeks.org/print-matrix-in-zig-zag-fashion/
'''
Given a matrix of 2D array of n rows and m columns. Print this matrix in ZIG-ZAG fashion as shown in figure. 
matrix_zag-zag

Example: 
 

Input: 
1 2 3
4 5 6
7 8 9
Output: 
1 2 4 7 5 3 6 8 9
'''

def printMatrixZigZag(M):
    R, C = len(M), len(M[0])
    goingUp = True
    i, j = 0, 0
    while True:
        print(M[i][j], end = " ")
        if i == R - 1 and j == C - 1:
            break
        if goingUp:
            if j == C - 1:
                i += 1
                goingUp = not goingUp
            elif i == 0:
                j += 1
                goingUp = not goingUp
            else:
                i, j = i - 1, j + 1
        else:
            if i == R - 1:
                j += 1
                goingUp = not goingUp
            elif j == 0:
                i += 1
                goingUp = not goingUp
            else:
                i, j = i + 1, j - 1
    print()
        
matrix = [[1, 2, 3, 4, 5], 
          [6, 7, 8, 9, 10], 
          [11, 12, 13, 14, 15], 
          [16, 17, 18, 19, 20], 
          [21, 22, 23, 24, 25]]
printMatrixZigZag(matrix)
