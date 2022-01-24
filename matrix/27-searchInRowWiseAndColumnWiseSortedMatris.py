def search(M, x):
    R, C = len(M), len(M[0])
    i, j = 0, C - 1
    while j >= 0 and i < R:
        if M[i][j] == x:
            return (i, j)
        elif M[i][j] < x:
            i += 1
        else:
            j -= 1
    return (-1, -1)

mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]

print(search(mat, 34))