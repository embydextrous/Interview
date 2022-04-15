def findPairs(M, x):
    s = set(M[0])
    R, C = len(M), len(M[0])
    for i in range(1, R):
        rowSet = set()
        for j in range(C):
            if x - M[i][j] in s:
                print(M[i][j], x - M[i][j])
            rowSet.add(M[i][j])
        s = s.union(rowSet)

sum = 11
mat = [[1, 3, 2, 4],
       [5, 8, 7, 6],
       [9, 10, 13, 11],
       [12, 0, 14, 15]]

findPairs(mat, sum)
