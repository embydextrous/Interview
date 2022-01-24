# https://www.geeksforgeeks.org/find-2-d-array-completely-traversed-not-following-cell-values/

def traverse(M):
    R, C = len(M), len(M[0])
    visited = [[False for i in range(C)] for j in range(R)]
    visitedCount = 0
    i, j = 0, 0
    while True:
        if visited[i][j]:
            return False
        visitedCount += 1
        if visitedCount == R * C:
            return True
        if M[i][j] is None:
            return False
        i, j = M[i][j][0], M[i][j][1]

cell = [[[] for j in range(2)] for i in range(3)]
cell[0][0] = [1, 0]
cell[0][1] = [2, 0]
cell[1][0] =  None
cell[1][1] = [1, 0]
cell[2][0] = [2, 1]
cell[2][1] = [1, 1]  

print(traverse(cell))
