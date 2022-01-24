# https://www.geeksforgeeks.org/find-number-transformation-make-two-matrix-equal/

'''
Given two matrices A and B of order n*m. The task is to find the required number of transformation steps so that 
both matrices became equal, print -1 if it is not possible. 
Transformation step is as: 
i) Select any one matrix out of two matrices. 
ii) Choose either row/column of the selected matrix. 
iii) Increment every element of select row/column by 1. 

Input : 
A[2][2]: 1 1
         1 1
B[2][2]: 1 2
         3 4
Output : 3
Explanation :
1 1   ->   1 2   ->   1 2   ->   1 2
1 1   ->   1 2   ->   2 3   ->   3 4

Input :
A[2][2]: 1 1
         1 0
B[2][2]: 1 2
         3 4
Output : -1
Explanation : No transformation will make A and B equal.

https://discuss.codechef.com/t/mtrnsfrm-editorial/13867 - Very Good Explanation Here
'''
def minOperations(A, B):
    r, c = len(A), len(A[0])
    C = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            C[i][j] = A[i][j] - B[i][j]
    for i in range(r):
        for j in range(c):
            if C[0][0] - C[i][0] - C[0][j] + C[i][j] != 0:
                return -1
    result = 0
    for i in range(r):
        result += abs(C[i][0])
    for i in range(c):
        result += abs(C[0][i] - C[0][0])
    return result

A = [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
    
print(minOperations(A, B))
