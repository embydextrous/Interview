'''
Given a square matrix of order n*n, we need to print elements of the matrix in Z form
 

    Input: [[4, 5, 6, 8], 
            [1, 2, 3, 1], 
            [7, 8, 9, 4], 
            [1, 8, 7, 5]]
        
    Output: 4 5 6 8
                3
              8
            1 8 7 5
'''
def printMatrixInZForm(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or i + j == n - 1:
                print(M[i][j], end = " ")
            else:
                print(" ", end = " ")
        print()

M = [[4, 5, 6, 8],
     [1, 2, 3, 1],
     [7, 8, 9, 4],
     [1, 8, 7, 5]]

printMatrixInZForm(M)