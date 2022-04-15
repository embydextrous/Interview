# https://www.geeksforgeeks.org/maximum-determinant-matrix-every-values-either-0-n/
'''
We have given a positive number n, and we have to find a 3*3 matrix which can be formed with combination of 
0 or n and has maximum determinant.

Examples : 

Input : n = 3 
Output : Maximum determinant = 54
Resultant Matrix :
3 3 0
0 3 3
3 0 3

Input : n = 13 
Output : Maximum determin sant = 4394
Resultant Matrix :
13 13  0
0  13 13
13  0 13

'''
from matrix import printS

def maxDet(n):
    return 2 * n * n * n

def resultMatrix(n):
    M = [[0 for i in range(3)] for j in range(3)]
    M[0][0] = M[0][1] = M[1][1] = M[1][2] = M[2][0] = M[2][2] = n
    return M

n = 3
print(maxDet(n))
printS(resultMatrix(n))