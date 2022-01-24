class Solution:
    def __init__(self, M):
        self.R, self.C = len(M), len(M[0])
        self.sum = 0
        self.M = M
        self.rowSum = [0] * self.R
        self.colSum = [0] * self.C
        for i in range(self.R):
            for j in range(self.C):
                self.rowSum[i] += M[i][j]
                self.colSum[j] += M[i][j]
                self.sum += M[i][j]

    def findSum(self, queries):
        for (i, j) in queries:
            print(i, j, self.sum - self.rowSum[i] - self.colSum[j] + self.M[i][j])
        print()
        
mat = [[1, 1, 2],
       [3, 4, 6], 
       [5, 3, 2]]
s = Solution(mat)
queries = [(0, 0), (1, 1), (0, 1)]
s.findSum(queries)
