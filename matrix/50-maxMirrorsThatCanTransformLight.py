# https://www.geeksforgeeks.org/maximum-mirrors-can-transfer-light-bottom-right/
'''
A square matrix is given in which each cell represents either a blank or an obstacle. 
We can place mirrors at blank position. All mirrors will be situated at 45 degree, i.e. they can transfer 
light from bottom to right if no obstacle is there in their path. 
In this question we need to count how many such mirrors can be placed in square matrix which can transfer 
light from bottom to right. 
Examples: (1 means Obstacle, 0 means blank)

M = [[0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 1, 1, 0, 1],
     [0, 0, 0, 1, 0]]
 

Output for above example is 2.

In above diagram, mirror at (3, 1) and (5, 5) are able
to send light from bottom to right so total possible 
mirror count is 2.
'''

def maxMirrors(M):
    R, C = len(M), len(M[0])
    c = 0
    discardedColumns = set()
    for i in range(R - 1, -1, -1):
        isRowDiscarded = False
        for j in range(C - 1, -1, -1):
            if M[i][j] == 1:
                isRowDiscarded = True
                discardedColumns.add(j)
            elif not isRowDiscarded and j not in discardedColumns:
                print(i, j)
                c += 1
    return c

M = [[0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 1, 1, 0, 1],
     [0, 0, 0, 1, 0]]

print(maxMirrors(M))