def printS(M):
    R, C = len(M), len(M[0])
    for i in range(R):
        for j in range(C):
            print(M[i][j], end = " ")
        print()