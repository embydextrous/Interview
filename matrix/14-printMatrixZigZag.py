# https://www.geeksforgeeks.org/print-matrix-in-zig-zag-fashion/

def printMatrixZigZag(M):
    n = len(M)
    d = False
    for i in range(n-1):
        L = i + 1
        for j in range(L):
            if d:
                print(M[j][L-j-1], end = " ")
            else:
                print(M[L-j-1][j], end = " ")
        d = not d
    for j in range(n):
        if d:
            print(M[j][n-j-1], end = " ")
        else:
            print(M[n-j-1][j], end = " ")
    d = not d
    sIndex = 1
    for i in range(n-1):
        L = n - i - 1
        for j in range(L):
            if d:
                print(M[sIndex + j][sIndex + L-j-1], end = " ")
            else:
                print(M[sIndex + L-j-1][sIndex + j], end = " ")
        sIndex += 1
        d = not d
    print()
        
matrix = [[1, 2, 3, 4, 5], 
          [6, 7, 8, 9, 10], 
          [11, 12, 13, 14, 15], 
          [16, 17, 18, 19, 20], 
          [21, 22, 23, 24, 25]]
printMatrixZigZag(matrix)
