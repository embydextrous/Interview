# Unique Cells in Binary Matrix
# https://www.geeksforgeeks.org/unique-cells-binary-matrix/

'''
Given a matrix of size n x m consisting of 0;s and 1's. We need to find the number of unique cells with 
value 1 such that the corresponding entire row and the entire column do not have another 1. Return the 
number of unique cells.

Examples: 

Input : mat[][] = {0, 1, 0, 0
                   0, 0, 1, 0
                   1, 0, 0, 1}
Answer : 2
The two 1s that are unique
in their rows and columns
are highlighted.

Input : mat[][] = { 
{0, 0, 0, 0, 0, 0, 1}
{0, 1, 0, 0, 0, 0, 0}
{0, 0, 0, 0, 0, 1, 0}
{1, 0, 0, 0, 0, 0, 0}
{0, 0, 1, 0, 0, 0, 1}
Output : 3
'''
def countUniqueCells(M):
    R, C = len(M), len(M[0])
    rowSum = [0] * R
    colSum = [0] * C
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1:
                rowSum[i] += 1
                colSum[j] += 1
    count = 0
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1 and rowSum[i] == 1 and colSum[j] == 1:
                count += 1
    return count

mat = [[0, 0, 0, 0, 0, 0, 1],
       [0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0],
       [1, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 1]]

print(countUniqueCells(mat))
