'''
Input

[[0, 1, 1, 0, 1],
[1, 1, 0, 1, 0],
[0, 1, 1, 1, 0],
[1, 1, 1, 1, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0]]

Output 

3
'''
def maxSizeSquareSubMatrix(M):
    R, C = len(M), len(M[0])
    maxi = 0
    for i in range(1, R):
        for j in range(1, C):
            if M[i][j] == 1:
                M[i][j] = 1 + min(M[i-1][j], M[i][j-1], M[i-1][j-1])
                maxi = max(maxi, M[i][j])
    return maxi

M = [[0, 1, 1, 0, 1],
[1, 1, 0, 1, 0],
[0, 1, 1, 1, 0],
[1, 1, 1, 1, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0]]

print(maxSizeSquareSubMatrix(M))