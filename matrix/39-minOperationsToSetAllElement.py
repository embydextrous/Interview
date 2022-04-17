# https://www.geeksforgeeks.org/minimum-operations-required-set-elements-binary-matrix/
'''
Given a binary matrix of N rows and M columns. The operation allowed on the matrix is to choose any 
index (x, y) and toggle all the elements between the rectangle having top-left as (0, 0) and bottom-right
as (x-1, y-1). 
Toggling the element means changing 1 to 0 and 0 to 1. The task is to find minimum operations required 
to make set all the elements of the matrix i.e make all elements as 1.
Examples: 
 

Input : mat[][] =  0 0 0 1 1
                   0 0 0 1 1
                   0 0 0 1 1
                   1 1 1 1 1
                   1 1 1 1 1
Output : 1
In one move, choose (3, 3) to make the
whole matrix consisting of only 1s.

Input : mat[][] =  0 0 1 1 1
                   0 0 0 1 1
                   0 0 0 1 1
                   1 1 1 1 1
                   1 1 1 1 1
Output : 3
'''
# Time Complexity is O(n * m)
def isAffectedByFlip(i, j, x, y):
    return i <= x and j <= y

def minOperations(M):
    R, C = len(M), len(M[0])
    c = 0
    flipIndex = None
    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            if flipIndex is None and M[i][j] == 0:
                c += 1
                flipIndex = (i, j)
            elif flipIndex is not None:
                isAffected = isAffectedByFlip(i, j, flipIndex[0], flipIndex[1])
                if isAffected:
                    if M[i][j] == 1:
                        c += 1
                        flipIndex = None
                else:
                    if M[i][j] == 0:
                        c += 1
                        flipIndex = None
    return c


M =   [[0, 0, 0, 1, 1],
       [0, 0, 0, 1, 1],
       [0, 0, 0, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]]
print(minOperations(M))
