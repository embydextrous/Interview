'''
Given a “2 x n” board and tiles of size “2 x 1”, count the number of ways to tile the given board using 
the 2 x 1 tiles. A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e., as 2 x 1 tile. 

Examples: 

    Input: n = 4
    Output: 5

    Explanation:

    For a 2 x 4 board, there are 5 ways

        All 4 vertical (1 way)
        All 4 horizontal (1 way)
        2 vertical and 2 horizontal (3 ways)

    Input: n = 3

    Output: 3

    Explanation:

    We need 3 tiles to tile the board of size  2 x 3.

    We can tile the board using following ways

        Place all 3 tiles vertically.
        Place 1 tile vertically and remaining 2 tiles horizontally (2 ways)
'''
def tiling2xn2x1(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

'''
Given a 3 x n board, find the number of ways to fill it with 2 x 1 dominoes.
Example 1 

Input : 2
Output : 3

Input : 8
Output : 153

Input : 12
Output : 2131

Defining Subproblems: 
At any point while filling the board, there are three possible states that the last column can be in: 
 
  xxxx      xxx     xxxx
  xxxx      xxxx    xxxx
  xxxx      xxxx    xxx
  (A)       (B)     (C)

 xxxx   xx|oo      xx|oo      xxx|o
 xxxx = xx|oo  +   xxx|o   +  xxx|o
 xxxx   xx|oo      xxx|o      xx|oo 

Why not all pairs are considered in A(n-2). Because they will form B(n-1) and C(n-1) states and are considered there.
ex : xx|oo
     xx|xo can be formed from A(n-2) and equals B(n-1).
     xx|xo

A(n) = A(n-2) + B(n-1) + C(n-1) = A(n-2) + 2 * B(n-1)

An =  No. of ways to completely fill a 3 x n board. (We need to find this)
Bn =  No. of ways to fill a 3 x n board with top corner in last column not filled.
Cn =  No. of ways to fill a 3 x n board with bottom corner in last column not filled.

Note: The following states are impossible to reach: 
 

Finding Reccurences 
Note: Even though Bn and Cn are different states, they will be equal for same n. i.e Bn = Cn 
Hence, we only need to calculate one of them.
Calculating An: 
 
A(n) = A(n-2) + 2 * B(n-1)
B(n) = A(n-1) + B(n-2)

Base Cases: 
A(0) = 1 (one way), A(1) = 0 (not possible)
B(0) = 0 (not possible), B(1) = 1 - formed by placing a tile.
'''
def tiling3xn2x1(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    a1, a2 = 1, 0
    b1, b2 = 0, 1
    for i in range(2, n + 1):
        a1, a2, b1, b2 = a2, a1 + 2 * b2, b2, a2 + b1 
    return a2

'''
Given a number n, count number of ways to fill a n x 4 grid using 1 x 4 tiles.
Examples: 
 

Input : n = 1
Output : 1

Input : n = 2
Output : 1
We can only place both tiles horizontally

Input : n = 3
Output : 1
We can only place all tiles horizontally.

Input : n = 4
Output : 2
The two ways are : 
  1) Place all tiles horizontally 
  2) Place all tiles vertically.

Input : n = 5
Output : 3
We can fill a 5 x 4 grid in following ways : 
  1) Place all 5 tiles horizontally
  2) Place first 4 vertically and 1 horizontally.
  3) Place first 1 horizontally and 4 horizontally.

 

We strongly recommend that you click here and practice it, before moving on to the solution.

This problem is mainly an extension of this tiling problem
Let “count(n)” be the count of ways to place tiles on a “n x 4” grid, following two cases arise when we place the first tile. 
 

    Place the first tile horizontally : If we place first tile horizontally, the problem reduces to “count(n-1)”
    Place the first tile vertically : If we place first tile vertically, then we must place 3 more tiles vertically. So the problem reduces to “count(n-4)”

 

grid

Therefore, count(n) can be written as below. 
 

   count(n) = 1 if n = 1 or n = 2 or n = 3   
   count(n) = 2 if n = 4
   count(n) = count(n-1) + count(n-4) 

This recurrence is similar to Fibonacci Numbers and can be solved using Dynamic programming.
'''
def tiling4xn4x1(n):
    if n <= 3:
        return 1
    if n == 4:
        return 2
    a, b, c, d = 1, 1, 1, 2
    for i in range(5, n + 1):
        a, b, c, d = b, c, d, a + d
    return d

def tilingnxmmx1(n, m):
    dp = [1] * (n + 1)
    for i in range(m, n+1):
        dp[i] = dp[i-1] + dp[i-m]
    return dp[n]

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
def trominoes(n):
    if n < 2:
        return n
    a1, a2 = 1, 1
    b1, b2 = 0, 1
    c1, c2 = 0, 1
    for i in range(2, n + 1):
        a1, a2, b1, b2, c1, c2 = a2, a1 + a2 + b1 + c1, b2, a2 + c2, c2, a2 + b2
    return a2


print(tiling2xn2x1(4))
print(tiling3xn2x1(6))
print(tiling4xn4x1(5))
print(tilingnxmmx1(7, 4))
print(trominoes(10))