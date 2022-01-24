# https://www.geeksforgeeks.org/maximum-path-sum-matrix/

def findMaxPathSum(M):
    R, C = len(M), len(M[0])
    for i in range(1, R):
        for j in range(C):
            if j == 0:
                M[i][j] += max(M[i-1][j], M[i-1][j+1])
            elif j == C - 1:
                M[i][j] += max(M[i-1][j-1], M[i-1][j])
            else:
                M[i][j] += max(M[i-1][j-1], M[i-1][j], M[i-1][j+1])
    return max(M[R-1])

mat = ([[ 10, 10, 2, 0, 20, 4 ],
        [ 1, 0, 0, 30, 2, 5 ],
        [ 0, 10, 4, 0, 2, 0 ],
        [ 1, 0, 2, 20, 0, 4 ]])

print(findMaxPathSum(mat))