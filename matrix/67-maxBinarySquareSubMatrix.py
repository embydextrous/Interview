def maxAllOneSquareSubMatrix(M):
    R, C = len(M), len(M[0])
    maxi = 0
    for i in range(R):
        for j in range(C):
            if i != 0 and j != 0 and M[i][j] == 1:
                M[i][j] = min(M[i-1][j], M[i-1][j-1], M[i][j-1]) + 1
                maxi = max(M[i][j], maxi)
            elif M[i][j] == 1 and maxi == 0:
                maxi = 1
    return maxi

M =     [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]
print(maxAllOneSquareSubMatrix(M))
        