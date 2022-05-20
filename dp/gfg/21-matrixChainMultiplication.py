def matrixChainMultiplication(dimens):
    n = len(dimens) - 1
    M = [[10 ** 9 for i in range(n)] for j in range(n)]
    S = [[10 ** 9 for i in range(n)] for j in range(n)]
    for i in range(n):
        M[i][i] = 0
        S[i][i] = i
    for s in range(2, n+1):
        i = 0
        j = i + s - 1
        while j < n:
            for k in range(i, j):
                if M[i][k] + M[k+1][j] + dimens[i] * dimens[k+1] * dimens[j+1] < M[i][j]:
                    M[i][j] = M[i][k] + M[k+1][j] + dimens[i] * dimens[k+1] * dimens[j+1]
                    S[i][j] = k
            i += 1
            j += 1
    printBrackets(M, S, n)
    return M[0][n-1]

def printBrackets(M, S, n):
    s = []
    i = 0
    j = n - 1
    visited = set()
    while i != j:
        s.append(f"M{S[i][j]}")
        visited.add(S[i][j])
        if M[i+1][j] < M[i][j-1]:
            i += 1
        else:
            j -= 1
    print(visited)
    for i in range(n):
        if i not in visited:
            s.append(f"M{i}")
    while len(s) > 1:
        a = s.pop()
        b = s.pop()
        s.append(f"({b}*{a})")
    print(s[0])


d = [5, 6, 4, 3, 5, 2]
# (5, 6) (6, 4) (4, 3) (3, 5) (5, 2)
print(matrixChainMultiplication(d))
'''
x   120    162   237    162
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
print(matrixChainMultiplication(d))