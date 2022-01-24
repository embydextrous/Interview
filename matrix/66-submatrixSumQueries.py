from matrix import printS

class Solution:
    def __init__(self, M):
        self.R = len(M)
        self.C = len(M[0])
        self.sumMatrix = self.createSumMatrix(M, self.R, self.C)

    def createSumMatrix(self, M, R, C):
        A = [[M[i][j] for j in range(C)] for i in range(R)]
        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    A[i][j] = M[i][j]
                elif i == 0:
                    A[i][j] = A[i][j-1] + M[i][j]
                elif j == 0:
                    A[i][j] = A[i-1][j] + M[i][j]
                else:
                    A[i][j] = A[i-1][j] + A[i][j-1] - A[i-1][j-1] + M[i][j]
        return A

    def query(self, topLeft, bottomRight):
        (i, j) = topLeft
        (x, y) = bottomRight
        if i == 0 and j == 0:
            return self.sumMatrix[x][y]
        elif i == 0:
            return self.sumMatrix[x][y] - self.sumMatrix[x][j-1]
        elif j == 0:
            return self.sumMatrix[x][y] - self.sumMatrix[i-1][y]
        else:
            return self.sumMatrix[x][y] - self.sumMatrix[i-1][y] - self.sumMatrix[x][j-1] + self.sumMatrix[i-1][j-1]

mat = [[1, 2, 3, 4, 6],
       [5, 3, 8, 1, 2],
       [4, 6, 7, 5, 5],
       [2, 4, 8, 9, 4]]

s = Solution(mat)
printS(s.sumMatrix)
print(s.query([1, 1], [3, 3]))
