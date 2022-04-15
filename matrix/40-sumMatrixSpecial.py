# https://www.geeksforgeeks.org/sum-matrix-element-absolute-difference-row-column-numbers/

'''
Given a positive integer n. Consider a matrix of n rows and n columns, in which each element contain 
absolute difference of its row number and numbers. The task is to calculate sum of each element of the matrix.
Examples : 
 
Input : n = 2
Output : 2
Matrix formed with n = 2 with given constraint:
0 1
1 0
Sum of matrix = 2.

Input : n = 3
Output : 8
Matrix formed with n = 3 with given constraint:
0 1 2
1 0 1
2 1 0
Sum of matrix = 8.

Input : n = 4
Output : 20
Matrix formed with n = 3 with given constraint:
0 1 2 3
1 0 1 2
2 1 0 1
3 2 1 0
Sum of matrix = 20.
'''
def findSum(n):
    if n == 1:
        return 0
    return n * (n - 1) + findSum(n-1)

print(findSum(7))