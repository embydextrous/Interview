'''
There is a m*n rectangular matrix whose top-left(start) location is (1, 1) and bottom-right(end) location is (m*n). 
There are k circles each with radius r. Find if there is any path from start to end without touching any circle.
The input contains values of m, n, k, r and two array of integers X and Y, each of length k. 
(X[i], Y[i]) is the center of ith circle.

Input : m = 5, n = 5, k = 2, r = 1, 
         X = {1, 3}, Y = {3, 3}
Output : Possible

Input : m = 5, n = 5, k = 2, r = 1, 
         X = {1, 1}, Y = {2, 3}.
Output : Not Possible
'''
def constructMatrix(m, n, circles, r):
    M = [[0 for i in range(n)] for j in range(m)]
    for circle in circles:
        x, y = circle[0] - 1, circle[1] - 1
        for i in range(max(0, x - r), min(m, x + r + 1)):
            for j in range(max(0, y - r), min(m, y + r + 1)):
                M[i][j] = 2
    return M

def isSafe(R, C, i, j):
    return i >= 0 and i < R and j >=0 and j < C

def dfs(M, R, C, i, j):
    M[i][j] = 1
    ROW = [-1, -1, -1, 0, 1, 1, 1, 0]
    COL = [-1, 0, 1, 1, 1, 0, -1, -1]
    for k in range(8):
        x, y = i + ROW[k], j + COL[k]
        if isSafe(R, C, x, y) and M[x][y] == 0:
            dfs(M, R, C, x, y)
            if M[R-1][C-1] == 1:
                break

def hasPath(m, n, circles, r):
    M = constructMatrix(m, n, circles, r)
    if M[0][0] == 1:
        return False
    dfs(M, m, n, 0, 0)
    return M[m-1][n-1] == 1

m = 5
n = 5
r = 2
circles = [[2, 4]]
print(hasPath(m, n, circles, r))