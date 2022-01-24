def getRing(M, R, C, k, s):
    if len(s) == R * C:
        return
    # fill top row
    for i in range(k, C-k):
        x = M[k][i]
        s.append(x)
        if len(s) == R * C:
            return
    # fill right edge
    for i in range(k + 1, R-k):
        x = M[i][C-k-1]        
        s.append(x)
        if len(s) == R * C:
            return
    # fill bottom row
    for i in range(C-k-2, k, -1):
        x = M[R-k-1][i]
        s.append(x)
        if len(s) == R * C:
            return
    # fill left edge
    for i in range(R-k-1, k, -1):
        x = M[i][k]
        s.append(x)
        if len(s) == R * C:
            return


def printAntiSpiral(M):
    R, C = len(M), len(M[0])
    s = []
    for k in range((min(R, C) + 1)//2):
        getRing(M, R, C, k, s)
    while len(s) > 0:
        print(s.pop(), end = " ")
    print()

M = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]

printAntiSpiral(M)