def printBoundaryElements(M):
    R, C = len(M), len(M[0])
    for i in range(R):
        for j in range(C):
            if i == 0 or j == 0 or i == R - 1 or j == C - 1:
                print(M[i][j], end = " ")
            else:
                print(" ", end = " ")
        print()


a = [[ 1, 2, 3, 4 ],
     [ 5, 6, 7, 8 ],
     [ 1, 2, 3, 4 ], 
     [ 5, 6, 7, 8 ] ]
printBoundaryElements(a)
