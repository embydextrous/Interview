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
def tiling(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    A = [0] * (n + 1)
    B = [0] * (n + 1)
    A[0] = 1
    A[1] = 0
    B[0] = 0
    B[1] = 1
    for i in range(2, n + 1):
        B[i] = A[i-1] + B[i-2]
        A[i] = A[i-2] + 2 * B[i-1]
    return A[n]

print(tiling(9))