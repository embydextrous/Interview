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

Input 

[ 
    ['E', 'C', 'C', 'C', 'C'],
    ['C', '#', 'C', '#', 'E'],
    ['#', 'C', 'C', '#', 'C'],
    ['C', 'E', 'E', 'C', 'E'],
    ['C', 'E', '#', 'C', 'E'] 
] 


Output

8

'''
def isSafe(R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C

def maxCoins(M):
    R, C = len(M), len(M[0])
    # direction 1 is right -1 is left
    q = [[0, 0, 1, 1 if M[0][0] == 'C' else 0]]
    maxCoins = 0
    while len(q) > 0:
        i, j, d, c = q.pop(0)
        maxCoins = max(maxCoins, c)
        # can go right and down
        if d == 1:
            # Go Right
            if isSafe(R, C, i, j + 1) and M[i][j+1] != '#':
                # direction will remain right
                x = c + 1 if M[i][j+1] == 'C' else c
                q.append([i, j + 1, 1, x])
            # Go Down
            if isSafe(R, C, i + 1, j) and M[i+1][j] != '#':
                # direction will change to left
                x = c + 1 if M[i+1][j] == 'C' else c
                q.append([i+1, j, -1, x])
        else:
            # Go Left
            if isSafe(R, C, i, j - 1) and M[i][j-1] != '#':
                # direction will remain left
                x = c + 1 if M[i][j-1] == 'C' else c
                q.append([i, j - 1, -1, x])
            # Go Down
            if isSafe(R, C, i + 1, j) and M[i+1][j] != '#':
                # direction will change to right
                x = c + 1 if M[i+1][j] == 'C' else c
                q.append([i+1, j, 1, x])
    return maxCoins
    
M =     [ ['E', 'C', 'C', 'C', 'C'],
          ['C', '#', 'C', '#', 'E'],
          ['#', 'C', 'C', '#', 'C'],
          ['C', 'E', 'E', 'C', 'E'],
          ['C', 'E', '#', 'C', 'E'] ] 

print(maxCoins(M))