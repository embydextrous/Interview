def findPermutedRows(M, r):
    s = set(M[r])
    p = []
    for i in range(len(M)):
        if i != r:
            isPermutation = True
            for j in range(len(M[0])):
                if M[i][j] not in s:
                    isPermutation = False
            if isPermutation:
                p.append(i)
    return p
            


M = [[3, 1, 4, 2],
       [1, 6, 9, 3],
       [1, 2, 3, 4],
       [4, 3, 2, 1]]

print(findPermutedRows(M, 3))