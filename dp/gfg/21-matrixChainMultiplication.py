def matrixChainMultiplication(dimens, names):
    n = len(dimens) - 1
    M = [[10 ** 9 if i != j else 0 for i in range(n)] for j in range(n)]
    S = [[10 ** 9 if i != j else i for i in range(n)] for j in range(n)]
    for s in range(2, n+1):
        for i in range(n-s+1):
            j = i + s - 1
            for k in range(i, j):
                if M[i][k] + M[k+1][j] + dimens[i] * dimens[k+1] * dimens[j+1] < M[i][j]:
                    M[i][j] = M[i][k] + M[k+1][j] + dimens[i] * dimens[k+1] * dimens[j+1]
                    S[i][j] = k
    printBrackets(0, n - 1, S, names)
    print()
    return M[0][n-1]

def printBrackets(i, j, S, names):
    if i == j:
        print(names[i], end = "")
    else:
        print("(", end = "")
        printBrackets(i, S[i][j], S, names)
        printBrackets(S[i][j] + 1, j, S, names)
        print(")", end = "")

d = [5, 6, 4, 3, 5, 2]
names = ["A", "B", "C", "D", "E"]
# (5, 6) (6, 4) (4, 3) (3, 5) (5, 2)
print(matrixChainMultiplication(d, names))
'''
x    120   162   247    162
x     x    72    162    102
x     x     x    60     54
x     x     x     x     30        
x     x     x     x      x 

x   0   0   2   0
x   x   1   2   1
x   x   x   2   2
x   x   x   x   3
x   x   x   x   x
'''
d = [5, 4, 6, 2, 7]
names = ["A", "B", "C", "D"]
print(matrixChainMultiplication(d, names))