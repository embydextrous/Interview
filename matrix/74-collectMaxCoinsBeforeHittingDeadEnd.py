'''
# https://www.geeksforgeeks.org/collect-maximum-coins-before-hitting-a-dead-end/

Given a character matrix where every cell has one of the following values.

'C' -->  This cell has coin

'#' -->  This cell is a blocking cell. 
         We can not go anywhere from this.

'E' -->  This cell is empty. We don't get
         a coin, but we can move from here.  
Initial position is cell (0, 0) and initial direction is right.

Following are rules for movements across cells.

If face is Right, then we can move to below cells:

Move one step ahead, i.e., cell (i, j+1) and direction remains right.
Move one step down and face left, i.e., cell (i+1, j) and direction becomes left.
If face is Left, then we can move to below cells

Move one step ahead, i.e., cell (i, j-1) and direction remains left.
Move one step down and face right, i.e., cell (i+1, j) and direction becomes right.
'''
def maxCoins(M, R, C, x, y, d):
    # If Invalid Return 0
    if x < 0 or x >= R or y < 0 or y >= C or M[x][y] == '#':
        return 0
    result = 1 if M[x][y] == 'C' else 0
    # d == means current direction is right
    if d == 0:
        return result + max(maxCoins(M, R, C, x, y + 1, d), maxCoins(M, R, C, x + 1, y, 1))
    else:
        return result + max(maxCoins(M, R, C, x, y - 1, d), maxCoins(M, R, C, x + 1, y, 0))

def maxCoinsUtil(M, R, C, x, y, d, dp):
    if x < 0 or x >= R or y < 0 or y >= C or M[x][y] == '#':
        return 0
    if dp[x][y][d] != -1:
        return dp[x][y][d]
    dp[x][y][d] = 1 if M[x][y] == 'C' else 0
    # d == means current direction is right
    if d == 0:
        return dp[x][y][d] + max(maxCoinsUtil(M, R, C, x, y + 1, d, dp), maxCoinsUtil(M, R, C, x + 1, y, 1, dp))
    else:
        return dp[x][y][d] + max(maxCoinsUtil(M, R, C, x, y - 1, d, dp), maxCoinsUtil(M, R, C, x + 1, y, 0, dp))

def maxCoins2(M):
    R, C = len(M), len(M[0])
    x, y = 0, 0
    d = 0
    dp = [[[-1 for i in range(2)] for i in range(C)] for i in range(R)]
    return maxCoinsUtil(M, R, C, x, y, d, dp)
    
M =     [ ['E', 'C', 'C', 'C', 'C'],
          ['C', '#', 'C', '#', 'E'],
          ['#', 'C', 'C', '#', 'C'],
          ['C', 'E', 'E', 'C', 'E'],
          ['C', 'E', '#', 'C', 'E'] ] 
R, C = len(M), len(M[0])
x, y = 0, 0
d = 0
print(maxCoins2(M))