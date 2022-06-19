'''
Given a 2-D matrix A[N][M] where A[i][j] denotes the points available on this cell. Two persons, P1 and P2, 
start from two corners of this matrix. P1 starts from top left and needs to reach bottom right. On the other hand, 
P2 starts bottom left and needs to reach top right. P1 can move right and down. P2 can right and up. As they visit
a cell, points A[i][j] are added to their total. The task is to maximize the sum of total points collected by both
of them under the condition that they shall meet only once and the cost of this cell shall not be included in either
of their total.

Examples: 

Input : A[][] = { {100, 100, 100},
                   {100, 1, 100},
                   {100, 100, 100}};
Output : 800
P1 needs to go from (0,0) to (2,2)
P2 needs to go from (2,0) to (0,2)
Explanation: P1 goes through A[0][0]->A[0][1]->A[1][1]->
                             A[2][1]->A[2][2]. 
             P2 goes through A[2][0]->A[1][0]->A[1][1]->
                             A[1][2]->A[0][2].
They meet at A[1][1]. So total points collected: 
A[0][0] + A[0][1] + A[2][1] + A[2][2] + 
A[2][0] + A[1][0] + A[1][2] + A[0][2] = 800


Input : A[][] = {{100, 100, 100, 100},
                 {100, 100, 100, 100},
                 {100, 0, 100, 100},
                 {100, 100, 100, 100}};
Output : 1200
'''
def maxPoints(M):
    R, C = len(M), len(M[0])
    if R == 1:
        return 0
    dp = [0 for i in range(C)]
    A = [[[0, 0] for j in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if i == 0 and j == 0:
                A[i][j][0] = M[i][j]
            elif i == 0:
                A[i][j][0] = A[i][j-1][0] + M[i][j]
            elif j == 0:
                A[i][j][0] = A[i-1][j][0] + M[i][j]
            else:
                A[i][j][0] =  M[i][j] + max(A[i][j-1][0], A[i-1][j][0])
    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            if i == R-1 and j == C-1:
                A[i][j][1] = M[i][j]
            elif i == R-1:
                A[i][j][1] = A[i][j+1][1] + M[i][j]
            elif j == C-1:
                A[i][j][1] = A[i+1][j][1] + M[i][j]
            else:
                A[i][j][1] =  M[i][j] + max(A[i][j+1][1], A[i+1][j][1])
    B = [[[0, 0] for j in range(C)] for i in range(R)]
    for i in range(R-1, -1, -1):
        for j in range(C):
            if i == R-1 and j == 0:
                B[i][j][0] = M[i][j]
            elif i == R-1:
                B[i][j][0] = B[i][j-1][0] + M[i][j]
            elif j == 0:
                B[i][j][0] = B[i+1][j][0] + M[i][j]
            else:
                B[i][j][0] =  M[i][j] + max(B[i][j-1][0], B[i+1][j][0])
    for i in range(R):
        for j in range(C-1, -1, -1):
            if i == 0 and j == C-1:
                B[i][j][1] = M[i][j]
            elif i == 0:
                B[i][j][1] = B[i][j+1][1] + M[i][j]
            elif j == C-1:
                B[i][j][1] = B[i-1][j][1] + M[i][j]
            else:
                B[i][j][1] =  M[i][j] + max(B[i][j+1][1], B[i-1][j][1])
    if R % 2 == 1:
        m = R // 2
        for j in range(C):
            dp[j] = A[m-1][j][0] + B[m+1][j][0] + A[m+1][j][1] + B[m-1][j][1]
    else:
        m1 = R // 2
        m2 = m1 - 1
        for j in range(C):
            if j == C - 1:
                dp[j] = A[m2][j][0] + B[m1][j][0] + A[m1+1][j][1] + B[m2-1][j][1]
            else:
                dp[j] = A[m2][j][0] + B[m1][j][0] + max(A[m1][j+1][1], A[m1+1][j][1]) + max(B[m2][j+1][1], B[m2-1][j][1])
    return max(dp)

M = [[100, 100, 100, 100],
     [100, 100, 100, 100],
     [100, 0, 100, 100],
     [100, 100, 100, 100]]

print(maxPoints(M))