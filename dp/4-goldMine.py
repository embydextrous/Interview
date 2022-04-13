'''
Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is the amount of 
gold in tons. Initially the miner is at first column but can be at any row. He can move only (right->,right up /,
right down\) that is from a given cell, the miner can move to the cell diagonally up towards the right or right
 or diagonally down towards the right. Find out maximum amount of gold he can collect. 
Examples: 
 
Input : mat[][] = {{1, 3, 3},
                   {2, 1, 4},
                  {0, 6, 4}};
Output : 12 
{(1,0)->(2,1)->(1,2)}

Input: mat[][] = { {1, 3, 1, 5},
                   {2, 2, 4, 1},
                   {5, 0, 2, 3},
                   {0, 6, 1, 2}};
Output : 16
(2,0) -> (1,1) -> (1,2) -> (0,3) OR
(2,0) -> (3,1) -> (2,2) -> (2,3)

Input : mat[][] = {{10, 33, 13, 15},
                  {22, 21, 04, 1},
                  {5, 0, 2, 3},
                  {0, 6, 14, 2}};
Output : 83
'''
def goldMine(M):
    R, C = len(M), len(M[0])
    for j in range(1, C):
        for i in range(R):
            if i == 0:
                M[i][j] += max(M[i][j-1], M[i+1][j-1])
            elif i == R - 1:
                M[i][j] += max(M[i][j-1], M[i-1][j-1])
            else:
                M[i][j] += max(M[i][j-1], M[i-1][j-1], M[i+1][j-1])
    maxi = M[0][C-1]
    for i in range(1, R):
        maxi = max(maxi, M[i][C-1])
    return maxi

M = [[10, 33,13, 15], 
     [21, 21, 4, 1],
     [5, 0, 2, 3],
     [0, 6, 14, 2]]

print(goldMine(M))
