'''
Given a 2D matrix and a set of cell indexes e.g., an array of (i, j) where i indicates row and j column. 
For every given cell index (i, j), find sums of all matrix elements except the elements present in i'th 
row and/or j'th column.
Example: 
 
mat[][]  = { {1, 1, 2}
             {3, 4, 6}
             {5, 3, 2} }
Array of Cell Indexes: {(0, 0), (1, 1), (0, 1)}
Output:  15, 10, 16
'''
class Solution:
    def __init__(self, M):
        R, C = len(M), len(M[0])
        self.sum = 0
        self.M = M
        self.rowSum = [0] * R
        self.colSum = [0] * C
        for i in range(R):
            for j in range(C):
                self.rowSum[i] += M[i][j]
                self.colSum[j] += M[i][j]
                self.sum += M[i][j]

    def findSum(self, query):
        i, j = query
        return self.sum - self.rowSum[i] - self.colSum[j] + self.M[i][j]

mat = [[1, 1, 2],
       [3, 4, 6], 
       [5, 3, 2]]
s = Solution(mat)
queries = [(0, 0), (1, 1), (0, 1)]
for query in queries:
    print(s.findSum(query))
