def countSame(M):
    n = len(M)
    c = 0
    for i in range(n):
        if M[i][i] == M[i][n-i-1]:
            c += 1
    return c

M = [[1, 2, 1],
     [4, 5, 2],
     [0, 5, 1]]

print(countSame(M))
