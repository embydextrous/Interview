'''
Given a 2D array, the task is to print matrix in anti spiral form:
Examples: 

spiral

Output: 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
 

Input : arr[][4] = {1, 2, 3, 4
                    5, 6, 7, 8
                    9, 10, 11, 12
                    13, 14, 15, 16};
Output : 10 11 7 6 5 9 13 14 15 16 12 8 4 3 2 1

Input :arr[][6] = {1, 2, 3, 4, 5, 6
                  7, 8, 9, 10, 11, 12
                  13, 14, 15, 16, 17, 18};
Output : 11 10 9 8 7 13 14 15 16 17 18 12 6 5 4 3 2 1
'''
def getRing(M, R, C, k, s):
    # fill top row
    for j in range(k, C-k):
        s.append(M[k][j])
    # fill right column
    for i in range(k + 1, R-k):
        s.append(M[i][C-k-1])     
    # fill bottom row
    for j in range(C-k-2, k - 1, -1):
        s.append(M[R-k-1][j])
    # print top row
    for i in range(R-k-2, k, -1):
        s.append(M[i][k])

def printAntiSpiral(M):
    R, C = len(M), len(M[0])
    s = []
    for k in range(min(R, C)//2):
        getRing(M, R, C, k, s)
    if R % 2 == 1 and R <= C:
        for j in range(R//2, C - R//2):
            s.append(M[R//2][j])
    elif C % 2 == 1 and C <= R:
        for i in range(C//2, R - C//2):
            s.append(M[i][C//2]) 
    while len(s) > 0:
        print(s.pop(), end = " ")       
    print()

M = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]

printAntiSpiral(M)