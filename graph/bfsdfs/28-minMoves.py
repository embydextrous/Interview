# https://www.geeksforgeeks.org/find-minimum-numbers-moves-needed-move-one-cell-matrix-another/
'''
Given a N X N matrix (M) filled with 1 , 0 , 2 , 3 . Find the minimum numbers of moves needed to move 
from source to destination (sink) . while traversing through blank cells only. You can traverse up, down,
right and left. 
A value of cell 1 means Source. 
A value of cell 2 means Destination. 
A value of cell 3 means Blank cell. 
A value of cell 0 means Blank Wall. 

Note : there is only single source and single destination.they may be more than one path from source 
to destination(sink).E ach move in matrix we consider as '1' 

Examples: 

Input : M[3][3] = {{ 0 , 3 , 2 },
                   { 3 , 3 , 0 },
                   { 1 , 3 , 0 }};
Output : 4 

Input : M[4][4] = {{ 3 , 3 , 1 , 0 },
                   { 3 , 0 , 3 , 3 },
                   { 2 , 3 , 0 , 3 },
                   { 0 , 3 , 3 , 3 }};
Output : 4
'''
from collections import deque

def canTravel(M, N, x, y):
    return x >= 0 and x < N and y >= 0 and y < N and (M[x][y] == 2 or M[x][y] == 3)

def minMoves(M):
    ROW = [0, -1, 0, 1]
    COL = [-1, 0, 1, 0]
    N = len(M)
    x, y = -1, -1
    for i in range(N):
        for j in range(N):
            if M[i][j] == 1:
                x, y = i, j
                break
        if x != -1:
            break
    q = deque([[x, y, 0]])
    while len(q) > 0:
        (x, y, d) = q.popleft()
        for k in range(4):
            i, j = x + ROW[k], y + COL[k]
            if canTravel(M, N, i, j):
                if M[i][j] == 2:
                    return d + 1    
                M[i][j] = 0
                q.append([i, j, d + 1])
    return -1

M = [[ 3 , 3 , 1, 0 ],
     [ 0 , 0 , 3, 3 ],
     [ 2 , 3 , 0, 3 ],
     [ 0 , 3 , 3, 3 ]]

print(minMoves(M))