'''
Given a square matrix, find out count of numbers that are same in same row and same in both primary and 
secondary diagonals.
Examples : 
 
Input : 1 2 1
        4 5 2
        0 5 1
Output : 2
Primary diagonal is 1 5 1
Secondary diagonal is 1 5 0
Two elements (1 and 5) match 
in two diagonals and same.

Input : 1 0 0
        0 1 0
        0 0 1
Output : 1
Primary diagonal is 1 1 1
Secondary diagonal is 0 1 0
Only one element is same.
'''
def countSame(M):
    n = len(M)
    c = 0
    for i in range(n):
        if M[i][i] == M[i][n-i-1]:
            c += 1
    return c

M = [[1, 2, 1],
     [4, 5, 2],
     [0, 5, 1]]

print(countSame(M))
