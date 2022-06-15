'''
Given a matrix that is filled with 'O', 'G', and 'W' where 'O' represents open space, 'G' represents guards and 'W' represents walls in a Bank. 
Replace all of the O's in the matrix with their shortest distance from a guard, without being able to go through any walls. Also, replace the guards 
with 0 and walls with -1 in output matrix.
Expected Time complexity is O(MN) for a M x N matrix.

Expected Auxiliary Space is O(MN) for a M x N matrix.

Examples:

O ==> Open Space
G ==> Guard
W ==> Wall

Input: 
  O  O  O  O  G
  O  W  W  O  O
  O  O  O  W  O
  G  W  W  W  O
  O  O  O  O  G

Output:  
  3  3  2  1  0
  2 -1 -1  2  1
  1  2  3 -1  2
  0 -1 -1 -1  1
  1  2  2  1  0
'''
from collections import deque

INF = 10 ** 9

ROW = [0, -1, 0, 1]
COL = [-1, 0, 1, 0]

def isSafe(R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C

def bfs(M, R, C, i, j, dist):
    q = deque([[i, j, 0]])
    visited = set()
    while len(q) > 0:
        x, y, d = q.popleft()
        dist[x][y] = min(dist[x][y], d)
        for k in range(4):
            i, j = x + ROW[k], y + COL[k]
            if isSafe(R, C, i, j) and M[i][j] != 'W' and (i, j) not in visited:
                visited.add((i, j))
                q.append([i, j, d + 1])
                
def minDistance(M):
    R, C = len(M), len(M[0])
    dist = [[10 ** 9 for i in range(C)] for j in range(R)]
    source = []
    for i in range(R):
        for j in range(C):
            if M[i][j] == 'W':
                dist[i][j] = -1
            elif M[i][j] == 'G':
                source.append([i, j])
    for (i, j) in source:
        bfs(M, R, C, i, j, dist)
    for row in dist:
        print(row)

M = [['O', 'O', 'O', 'O', 'G'],
     ['O', 'W', 'W', 'O', 'O'],
     ['O', 'O', 'O', 'W', 'O'],
     ['G', 'W', 'W', 'W', 'O'],
     ['O', 'O', 'O', 'O', 'G']]

minDistance(M)