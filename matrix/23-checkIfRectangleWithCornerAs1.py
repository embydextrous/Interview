def checkIfRectangleWithCornerAsOne(M):
    R = len(M)
    d = {}
    for i in range(R):
        d[i] = set()
        for j in range(len(M[0])):
            if M[i][j] == 1:
                d[i].add(j)
    for i in range(R):
        for j in range(i + 1, R):
            if len(d[i].intersection(d[j])) >= 2:
                return True
    return False


M = [[1, 0, 0, 1, 0 ],
     [0, 1, 1, 1, 1 ],
     [0, 0, 0, 1, 0 ],
     [1, 1, 1, 1, 0 ]]

print(checkIfRectangleWithCornerAsOne(M))