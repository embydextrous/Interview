'''
Given a matrix of size n x m. Print the boundary elements of the matrix. Boundary elements are those elements
which are not surrounded by elements on all four directions, i.e. elements in first row, first column,
last row and last column. 

Examples: 

Input :
        1 2 3 4  
        5 6 7 8
        1 2 3 4
        5 6 7 8
Output : 
         1 2 3 4 
         5     8 
         1     4 
         5 6 7 8
Explanation:The boundary elements of the
matrix is printed.

Input:
        1 2 3   
        5 6 7 
        1 2 3 
Output: 
        1 2 3   
        5   7 
        1 2 3 
Explanation:The boundary elements of the 
matrix is printed.
'''
def printBoundaryElements(M):
    R, C = len(M), len(M[0])
    for i in range(R):
        for j in range(C):
            if i == 0 or j == 0 or i == R - 1 or j == C - 1:
                print(M[i][j], end = " ")
            else:
                print(" ", end = " ")
        print()


a = [[ 1, 2, 3, 4 ],
     [ 5, 6, 7, 8 ],
     [ 1, 2, 3, 4 ], 
     [ 5, 6, 7, 8 ] ]
printBoundaryElements(a)
