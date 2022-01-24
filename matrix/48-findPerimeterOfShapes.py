# https://www.geeksforgeeks.org/find-perimeter-shapes-formed-1s-binary-matrix/
'''
Given a matrix of N rows and M columns, consist of 0s and 1s. 
The task is to find the perimeter of subfigure consisting only 1s in the matrix. 
Perimeter of single 1 is 4 as it can be covered from all 4 side. Perimeter of double 11 is 6. 

     
   __                __  __         
|  1  |           |  1    1  |
   __                __  __         
Examples:  

Input : mat[][] = 
               {
                 1, 0,
                 1, 1,
               }
Output : 8
Cell (1,0) and (1,1) making a L shape whose perimeter is 8.
'''
def addBoundaryUnit(M, R, C, i, j):
    if i < 0 or i >= R or j < 0 or j >= C or M[i][j] == 0:
        return 1
    return 0

def findPerimeter(M):
    R, C = len(M), len(M[0])
    perimeter = 0
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1:
                perimeter += addBoundaryUnit(M, R, C, i - 1, j)
                perimeter += addBoundaryUnit(M, R, C, i, j - 1)
                perimeter += addBoundaryUnit(M, R, C, i + 1, j)
                perimeter += addBoundaryUnit(M, R, C, i, j + 1)
    return perimeter


M = [ [0, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0] ]

print(findPerimeter(M))