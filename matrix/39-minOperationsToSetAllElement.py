# https://www.geeksforgeeks.org/minimum-operations-required-set-elements-binary-matrix/

def minOperations(M):
    R, C = len(M), len(M[0])
    c = 0
    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            if M[i][j] == 0:
                c += 1
                for x in range(i+1):
                    for y in range(j+1):
                        M[x][y] = abs(M[x][y] - 1)
    return c


M =   [[0, 0, 1, 1, 1],
       [0, 0, 0, 1, 1],
       [0, 0, 0, 1, 1],
       [1, 1, 1, 0, 1],
       [1, 1, 1, 1, 1]]
print(minOperations(M))
