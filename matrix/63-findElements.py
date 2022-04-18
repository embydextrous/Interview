# https://www.geeksforgeeks.org/find-k-such-that-all-elements-in-kth-row-are-0-and-kth-column-are-1-in-a-boolean-matrix/

'''
Given a square boolean matrix mat[n][n], find k such that all elements in k'th row are 0 and all 
elements in k'th column are 1. The value of mat[k][k] can be anything (either 0 or 1). 
If no such k exists, return -1.
Examples: 
 

Input: bool mat[n][n] = { {1, 0, 0, 0},
                          {1, 1, 1, 0},
                          {1, 1, 0, 0},
                          {1, 1, 1, 0},
                        };
Output: 0
All elements in 0'th row are 0 and all elements in 
0'th column are 1.  mat[0][0] is 1 (can be any value)


Input: bool mat[n][n] = {{0, 1, 1, 0, 1},
                         {0, 0, 0, 0, 0},
                         {1, 1, 1, 0, 0},
                         {1, 1, 1, 1, 0},
                         {1, 1, 1, 1, 1}};
Output: 1
All elements in 1'st row are 0 and all elements in 
1'st column are 1.  mat[1][1] is 0 (can be any value)


Input: bool mat[n][n] = {{0, 1, 1, 0, 1},
                         {0, 0, 0, 0, 0},
                         {1, 1, 1, 0, 0},
                         {1, 0, 1, 1, 0},
                         {1, 1, 1, 1, 1}};
Output: -1
There is no k such that k'th row elements are 0 and
k'th column elements are 1.
'''
def findElements(M):
    N = len(M)
    i, j = 0, N - 1
    while i != j:
        # Discard Column - Why? Because all elements in column should be 1 (except for i, i)
        if M[i][j] == 0:
            j -= 1
        # Discard Row - Why? Because all elements in row should be 0 (except for i, i)
        else:
            i += 1
    for k in range(i):
        # Check left
        if M[i][k] == 1:
            return -1
        # Check above
        if M[k][i] == 0:
            return -1
    for k in range(i+1, N):
        # Check right
        if M[i][k] == 1:
            return -1
        # check below
        if M[k][i] == 0:
            return -1
    return i


M =  [[0,1,1,0,1],
      [0,0,0,0,0],
      [1,1,1,0,0],
      [1,0,1,1,0],
      [1,1,1,1,1] ]

print(findElements(M))