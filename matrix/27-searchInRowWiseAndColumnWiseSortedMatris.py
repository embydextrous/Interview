'''
Given an n x n matrix and a number x, find the position of x in the matrix if it is present in it. 
Otherwise, print “Not Found”. In the given matrix, every row and column is sorted in increasing order. 
The designed algorithm should have linear time complexity. 

Example: 

Input: mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 29
Output: Found at (2, 1)
Explanation: Element at (2,1) is 29

Input : mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 100
Output : Element not found
Explanation: Element 100 is not found
'''
def search(M, x):
    R, C = len(M), len(M[0])
    i, j = 0, C - 1
    while j >= 0 and i < R:
        if M[i][j] == x:
            return (i, j)
        elif M[i][j] < x:
            i += 1
        else:
            j -= 1
    return (-1, -1)

mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]

print(search(mat, 34))