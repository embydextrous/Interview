# https://www.geeksforgeeks.org/flood-fill-algorithm-implement-fill-paint/
from matrix import printS

def isValid(M, R, C, i, j, x):
    return i >=0 and j >=0 and i < R and j < C and M[i][j] == x

def floodFill(M, point, newColor):
    R, C = len(M), len(M[0])
    q = [point]
    oldColor = M[point[0]][point[1]]
    #visited = [[False for i in range(C)] for j in range(R)]
    while len(q) > 0:
        (i, j) = q.pop(0)
        M[i][j] = newColor
        if isValid(M, R, C, i, j-1, oldColor):
            q.append([i, j-1])
        if isValid(M, R, C, i-1, j, oldColor):
            q.append([i-1, j])
        if isValid(M, R, C, i, j+1, oldColor):
            q.append([i, j+1])
        if isValid(M, R, C, i+1, j, oldColor):
            q.append([i+1, j])

data = [
  [ 1, 1, 1, 1, 1, 1, 1, 1 ],
  [ 1, 1, 1, 1, 1, 1, 0, 0 ],
  [ 1, 0, 0, 1, 1, 0, 1, 1 ],
  [ 1, 2, 2, 2, 2, 0, 1, 0 ],
  [ 1, 1, 1, 2, 2, 0, 1, 0 ],
  [ 1, 1, 1, 2, 2, 2, 2, 0 ],
  [ 1, 1, 1, 1, 1, 2, 1, 1 ],
  [ 1, 1, 1, 1, 1, 2, 2, 1 ],
]

floodFill(data, [4, 4], 3)
printS(data)

