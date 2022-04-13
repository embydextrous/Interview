'''
Given a positive integer N, the task is to find the number of ways to fill the board of dimension 2*N 
with a tile of dimensions 2 x 1, 1 x 2, (also known as domino) and an L shaped tile(also know as tromino) 
show below that can be rotated by 90 degrees.

The L shape tile:

XX
X

After rotating L shape tile by 90:

XX
 X
or
X
XX

Examples:

    Input: N = 3
    Output: 5
    Explanation:
    Below is the image to illustrate all the combinations:

    Input: N = 1
    Output: 1

Approach: The given problem can be solved based on the following observations by:

Let's define a 2 state, dynamic programming say dp[i, j] denoting one of the following arrangements in 
column index i.

1. The current column can be filled with 1, 2 x 1 dominos in state 0, if the previous column had state 0.
2. The current column can be filled with 2, 1 x 2 dominos horizontally in state 0, if the i - 2 column has state 0.
3. The current column can be filled with an L shaped domino in state 1 and state 2, if the previous column 
    had state 0.
4. The current column can be filled with 1 x 2 shaped domino in state 1 if the previous column has state 2 
    or in state 2 if the previous column has state 1.
5. Therefore, the transition of the state can be defined as the following:
    
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]+ dp[i - 2][1] + dp[i - 2][2]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
    dp[i][2] = dp[i - 1][0] + dp[i - 1][1]

Base Cases
dp[0][0] = 1, dp[0][1] = 0, dp[1][0] = 0
dp[1][0] = 1, dp[1][1] = 1, dp[1][2] = 1
'''
def tiling(n):
    if n < 3:
        return n
    dp = [[0 for i in range(3)] for j in range(n + 1)]
    dp[0][0] = dp[1][0] = dp[1][1] = dp[1][2] = 1
    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0] + dp[i-2][1] + dp[i-2][2]
        dp[i][1] = dp[i-1][0] + dp[i-1][2]
        dp[i][2] = dp[i-1][0] + dp[i-1][1]
    return dp[n][0]

print(tiling(10))