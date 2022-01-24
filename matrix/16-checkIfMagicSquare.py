
# should also check that all elements are distinct
def checkMagicSquare(M):
    sumSet = set()
    elementSet = set()
    R, C = len(M), len(M[0])
    for row in M:
        s = 0
        for i in row:
            s += i
            elementSet.add(i)
        sumSet.add(s)
    for i in range(C):
        s = 0
        for j in range(R):
            s += M[j][i]
        sumSet.add(s)
    s1 = s2 = 0
    for i in range(R):
        s1 += M[i][i]
        s2 += M[i][R-i-1]
    sumSet.add(s1)
    sumSet.add(s2)
    return len(sumSet) == 1 and len(elementSet) ==  R * R


M = [[9, 3, 22, 16, 15],
[2, 21, 20, 14, 8],
[25, 19, 13, 7, 1],
[18, 12, 6, 5, 24],
[11, 10, 4, 23, 17]]

print(checkMagicSquare(M))