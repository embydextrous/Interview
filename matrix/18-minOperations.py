# https://www.geeksforgeeks.org/minimum-operations-required-make-row-column-matrix-equals/
'''
Given a square matrix of size n \times n . Find minimum number of operation are required such that sum of 
elements on each row and column becomes equals. In one operation, increment any value of cell of matrix by 1. 
In first line print minimum operation required and in next 'n' lines print 'n' integers representing the 
final matrix after operation. 
Example: 
 
Input: 
1 2
3 4
Output: 
4
4 3
3 4
Explanation
1. Increment value of cell(0, 0) by 3
2. Increment value of cell(0, 1) by 1
Hence total 4 operation are required

Input: 9
1 2 3
4 2 3
3 2 1
Output: 
6
2 4 3 
4 2 3 
3 3 3 
'''
from matrix import printS

def countOperations(M):
    N = len(M)
    rowSum = [0] * N
    colSum = [0] * N
    for i in range(N):
        for j in range(N):
            rowSum[i] += M[i][j]
            colSum[j] += M[i][j]
    maxSum = max(max(rowSum), max(colSum))
    operations = N * maxSum - sum(rowSum)
    for i in range(operations):
        minRowIndex = 0
        minColIndex = 0
        for k in range(N):
            if rowSum[k] < rowSum[minRowIndex]:
                minRowIndex = k
            if colSum[k] < colSum[minColIndex]:
                minColIndex = k
        M[minRowIndex][minColIndex] += 1
        rowSum[minRowIndex] += 1
        colSum[minColIndex] += 1
        print(rowSum, colSum)
    print(operations)
    printS(M)

mat = [
    [1, 2, 3],
    [4, 2, 3],
    [3, 2, 1]
]
countOperations(mat)