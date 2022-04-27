'''
Given a rectangular matrix, we can move from current cell in 4 directions with equal probability. 
The 4 directions are right, left, top or bottom. Calculate the Probability that after N moves from 
a given position (i, j) in the matrix, we will not cross boundaries of the matrix at any point.
'''
def isSafe(R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C

ROW = [-1, 0, 1, 0]
COL = [0, 1, 0, -1]

def probability(R, C, i, j, n):
    if not isSafe(R, C, i, j):
        return 0.0
    if n == 0:
        return 1.0
    p = 0.0
    for k in range(4):
        x, y = i + ROW[k], j + COL[k]
        p += probability(R, C, x, y, n-1) * 0.25
    return p
    
print(probability(5, 5, 1, 1, 2))
