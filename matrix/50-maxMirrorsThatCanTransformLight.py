# https://www.tutorialspoint.com/maximum-mirrors-which-can-transfer-light-from-bottom-to-right-in-cplusplus
# https://www.geeksforgeeks.org/maximum-mirrors-can-transfer-light-bottom-right/
def maxMirrors(M):
    R, C = len(M), len(M[0])
    c = 0
    discardedRows = set()
    discardedColumns = set()
    for i in range(R - 1, -1, -1):
        for j in range(C - 1, -1, -1):
            if M[i][j] == 1:
                discardedRows.add(i)
                discardedColumns.add(j)
            elif i not in discardedRows and j not in discardedColumns:
                print(i, j)
                c += 1
    return c

M = [[0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 1, 1, 0, 1],
     [0, 0, 0, 1, 0]]

print(maxMirrors(M))