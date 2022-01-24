def findPairs(M, x):
    d = {}
    for i in range(len(M)):
        for j in range(len(M[0])):
            d[M[i][j]] = (i, j)
    for i in range(len(M)):
        for j in range(len(M[0])):
            if x - M[i][j] in d and i < d[x - M[i][j]][0]:
                print(M[i][j], x - M[i][j])
    
sum = 11
mat = [[1, 3, 2, 4],
       [5, 8, 7, 6],
       [9, 10, 13, 11],
       [12, 0, 14, 15]]

findPairs(mat, sum)
