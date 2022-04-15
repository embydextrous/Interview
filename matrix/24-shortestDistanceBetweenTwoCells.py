# https://www.geeksforgeeks.org/shortest-distance-two-cells-matrix-grid/
'''
Given a matrix of N*M order. Find the shortest distance from a source cell to a destination cell, 
traversing through limited cells only. Also you can move only up, down, left and right. 
If found output the distance else -1. 
s represents 'source' 
d represents 'destination'
* represents cell you can travel 
0 represents cell you can not travel 
This problem is meant for single source and destination.
Examples: 
 

Input : {'0', '*', '0', 's'},
        {'*', '0', '*', '*'},
        {'0', '*', '*', '*'},
        {'d', '*', '*', '*'}
Output : 6

Input :  {'0', '*', '0', 's'},
         {'*', '0', '*', '*'},
         {'0', '*', '*', '*'},
         {'d', '0', '0', '0'}
Output :  -1
'''

def isValid(R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C

def minDistance(M):
    ROW = [0, -1, 0, 1]
    COL = [-1, 0, 1, 0]
    R, C = len(M), len(M[0])
    sx, sy = -1, -1
    for i in range(R):
        for j in range(C):
            if M[i][j] == 's':
                sx, sy = i, j
                break
        if sx != -1:
            break
    q = [[sx, sy, 0]]
    while len(q) > 0:
        i, j, d = q.pop(0)
        for k in range(4):
            x, y = i + ROW[k], j + COL[k]
            if isValid(R, C, x, y):
                if M[x][y] == 'd':
                    return d + 1
                elif M[x][y] == '*':
                    q.append([x, y, d + 1])
                    M[x][y] = '0'
    return -1

M = [['*', '*', '*', 's'],
     ['*', '*', '0', '*'],
     ['0', '*', '0', '*'],
     ['d', '*', '*', '*']]

print(minDistance(M))