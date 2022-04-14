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

def isValid(M, R, C, i, j):
    return i < R and j < C and i >= 0 and j >= 0 and M[i][j] != '0'

def minDistance(M):
    source = None
    R, C = len(M), len(M[0])
    for i in range(R):
        for j in range(C):
            if M[i][j] == 's':
                source = (i, j, 0)
                break
        if source:
            break
    visited = [[False for _ in range(len(M[0]))]
               for _ in range(len(M))]
    q = [source]
    while len(q) > 0:
        (i, j, d) = q.pop(0)
        visited[i][j] = True
        if M[i][j] == 'd':
            return d
        if isValid(M, R, C, i - 1, j) and not visited[i-1][j]:
            q.append((i - 1, j, d + 1))
        if isValid(M, R, C, i, j - 1) and not visited[i][j-1]:
            q.append((i, j - 1, d + 1))
        if isValid(M, R, C, i + 1, j) and not visited[i+1][j]:
            q.append((i + 1, j, d + 1))
        if isValid(M, R, C, i, j + 1) and not visited[i][j + 1]:
            q.append((i, j + 1, d + 1))
    return -1

M = [['*', '*', '*', 's'],
     ['*', '*', '0', '*'],
     ['0', '0', '0', '*'],
     ['d', '*', '0', '*']]

print(minDistance(M))