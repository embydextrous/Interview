'''
Given a Binary Matrix of size N X N, consisting of 1s and 0s. The task is to find the minimum flips 
required to make the matrix symmetric along main diagonal.
Examples : 
 

Input : mat[][] = { { 0, 0, 1 },
                    { 1, 1, 1 },
                    { 1, 0, 0 } };
Output : 2
Value of mat[1][0] is not equal to mat[0][1].
Value of mat[2][1] is not equal to mat[1][2].
So, two flip are required.

Input : mat[][] = { { 1, 1, 1, 1, 0 },
                    { 0, 1, 0, 1, 1 },
                    { 1, 0, 0, 0, 1 },
                    { 0, 1, 0, 1, 0 },
                    { 0, 1, 0, 0, 1 } };                  
Output : 3
'''
def flipRequired(M):
    n = len(M)
    c = 0
    for i in range(n):
        for j in range(i):
            if M[i][j] != M[j][i]:
                c += 1
    return c

mat =[[1, 1, 1, 1, 0],
      [0, 1, 0, 1, 1],
      [1, 0, 0, 0, 1],
      [0, 1, 0, 1, 0],
      [0, 1, 0, 0, 1]]

print(flipRequired(mat))