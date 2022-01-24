
def flipRequired(M):
    n = len(M)
    c = 0
    for i in range(n):
        for j in range(i):
            if M[i][j] != M[j][i]:
                c += 1
    return c

mat =[[1, 1, 1, 1, 0],
      [0, 1, 0, 1, 1],
      [1, 0, 0, 0, 1],
      [0, 1, 0, 1, 0],
      [0, 1, 0, 0, 1]]

print(flipRequired(mat))