from matrix import printS

# Odd Only
# For even see this: https://www.geeksforgeeks.org/magic-square-even-order/
def createMagicSquare(n):
    result = [[0 for i in range(n)] for i in range(n)]
    i, j = n // 2, n-1
    k = 1
    while True:
        if result[i][j] == 0:
            result[i][j] = k
            k += 1
            i -= 1
            j += 1
        else:
            i += 1
            j -= 2
        if i == -1 and j == n:
            i, j = 0, n - 2
        else:
            i = i % n if i >= 0 else n + i
            j = j % n if j >= 0 else n + j
        if k == n * n + 1:
            break
    return result


printS(createMagicSquare(5))