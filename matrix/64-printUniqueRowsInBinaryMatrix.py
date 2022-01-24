def printUniqueRows(M):
    d = {}
    R, C = len(M), len(M[0])
    for i in range(R):
        n = 0
        k = 1
        for j in range(C-1, -1, -1):
            if M[i][j] == 1:
                n = n + k * 1
            k *= 2
        if n not in d:
            d[n] = i   
    print(d)
    for i in d.values():
        for j in range(C):
            print(M[i][j], end = " ")
        print()

M =     [ [ 0, 1, 0, 0, 1 ],
          [ 1, 0, 1, 1, 0 ],
          [ 0, 1, 0, 0, 1 ],
          [ 1, 0, 1, 0, 0 ] ]

printUniqueRows(M)


