from matrix import printS

def fillRing(M, R, C, k, startValue):
    if startValue > R * C:
        return startValue
    # fill top row
    for i in range(k, C-k):
        M[k][i] = startValue
        startValue += 1
        if startValue > R * C:
            return startValue
    # fill right edge
    for i in range(k + 1, R-k):
        M[i][C-k-1] = startValue
        startValue += 1
        if startValue > R * C:
            return startValue
    # fill bottom row
    for i in range(C-k-2, k, -1):
        M[R-k-1][i] = startValue
        startValue += 1
        if startValue > R * C:
            return startValue
    # fill left edge
    for i in range(R-k-1, k, -1):
        M[i][k] = startValue
        startValue += 1
        if startValue > R * C:
            return startValue
    return startValue


def createMatrix(n, m):
    k = min(n, m)
    M = [[0 for i in range(m)] for i in range(n)]
    startValue = 1
    for i in range((k + 1) // 2):
        startValue = fillRing(M, n, m, i, startValue)
    return M


printS(createMatrix(4, 3))