# https://www.geeksforgeeks.org/flood-fill-algorithm-implement-fill-paint/
'''
In MS-Paint, when we take the brush to a pixel and click, the color of the region of that pixel is 
replaced with a new selected color. Following is the problem statement to do this task. 

Given a 2D screen, location of a pixel in the screen and a color, replace color of the given pixel 
and all adjacent same colored pixels with the given color.

Example: 

Input:
screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
               {1, 1, 1, 1, 1, 1, 0, 0},
               {1, 0, 0, 1, 1, 0, 1, 1},
               {1, 2, 2, 2, 2, 0, 1, 0},
               {1, 1, 1, 2, 2, 0, 1, 0},
               {1, 1, 1, 2, 2, 2, 2, 0},
               {1, 1, 1, 1, 1, 2, 1, 1},
               {1, 1, 1, 1, 1, 2, 2, 1},
               };
x = 4, y = 4, newColor = 3
The values in the given 2D screen indicate colors of the pixels. x and y are coordinates of the brush,
newColor is the color that should replace the previous color on screen[x][y] and all surrounding
pixels with same color.

Output:
Screen should be changed to following.
screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
               {1, 1, 1, 1, 1, 1, 0, 0},
               {1, 0, 0, 1, 1, 0, 1, 1},
               {1, 3, 3, 3, 3, 0, 1, 0},
               {1, 1, 1, 3, 3, 0, 1, 0},
               {1, 1, 1, 3, 3, 3, 3, 0},
               {1, 1, 1, 1, 1, 3, 1, 1},
               {1, 1, 1, 1, 1, 3, 3, 1}};
'''
from matrix import printS

def isValid(R, C, i, j):
    return i >=0 and j >=0 and i < R and j < C

def dfs(M, R, C, point, newColor, oldColor):
    x, y = point[0], point[1]
    M[x][y] = newColor
    ROW = [0, -1, 0, 1]
    COL = [-1, 0, 1, 0]
    for k in range(4):
        i, j = x + ROW[k], y + COL[k]
        if isValid(R, C, i, j) and M[i][j] == oldColor:
            dfs(M, R, C, (i, j), newColor, oldColor)

def floodFill(M, point, newColor):
    R, C = len(M), len(M[0])
    x, y = point[0], point[1]
    dfs(M, R, C, point, newColor, M[x][y])

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

