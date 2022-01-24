# https://www.geeksforgeeks.org/find-if-given-matrix-is-toeplitz-or-not/

def isToeplitz(M):
    R, C = len(M), len(M[0])
    for k in range(C-1, 0, -1):
        i = 0
        j = k
        x = M[i][j]
        i += 1
        j += 1
        while i < R and j < C:
            if M[i][j] != x:
                return False
            i += 1
            j += 1
    for k in range(R):
        i = k
        j = 0
        x = M[i][j]
        i += 1
        j += 1
        while i < R and j < C:
            if M[i][j] != x:
                return False
            i += 1
            j += 1
    return True

M = [[6, 3, 8],
     [4, 9, 7],
     [1, 4, 6]]

print(isToeplitz(M))

    

