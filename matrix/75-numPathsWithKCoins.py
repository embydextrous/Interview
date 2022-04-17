# https://www.geeksforgeeks.org/number-of-paths-with-exactly-k-coins/
'''
Given a matrix where every cell has some number of coins. 
Count number of ways to reach bottom right from top left with exactly k coins. We can move to (i+1, j) 
and (i, j+1) from a cell (i, j).

Example: 

Input:  k = 12
        mat[][] = { {1, 2, 3},
                    {4, 6, 5},
                    {3, 2, 1}
                  };
Output:  2
There are two paths with 12 coins
1 -> 2 -> 6 -> 2 -> 1
1 -> 2 -> 3 -> 5 -> 1
'''
def numPathsRecursiveUtil(M, R, C, x, y, k):
    if x < 0 or x >= R or y < 0 or y >= C:
        return 0
    if x == 0 and y == 0 and M[x][y] == k:
        return 1
    return numPathsRecursiveUtil(M, R, C, x - 1, y, k - M[x][y]) + numPathsRecursiveUtil(M, R, C, x, y - 1, k - M[x][y])

def numPathsRecursive(M, k):
    R, C = len(M), len(M[0])
    x = R - 1
    y = C - 1
    return numPathsRecursiveUtil(M, R, C, x, y, k)

def numPathsUtil(M, R, C, x, y, k, dp):
    if x < 0 or x >= R or y < 0 or y >= C:
        return 0
    if x == 0 and y == 0 and M[x][y] == k:
        return 1
    if dp[x][y][k] != -1:
        return dp[x][y][k]
    dp[x][y][k] = numPathsUtil(M, R, C, x - 1, y, k - M[x][y], dp) + numPathsUtil(M, R, C, x, y - 1, k - M[x][y], dp)
    return dp[x][y][k]

def numPaths(M, k):
    R, C = len(M), len(M[0])
    x = R - 1
    y = C - 1
    dp = [[[-1 for x in range(k + 1)] for j in range(C)] for i in range(R)]
    numPathsUtil(M, R, C, x, y, k, dp)
    return dp[x][y][k]


k = 12
M =   [[1, 2, 3],
       [4, 6, 5],
       [3, 2, 1]]
print(numPaths(M, k))