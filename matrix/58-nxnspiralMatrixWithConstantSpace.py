def printSpiralMatrix(n):
    for i in range(n):
        for j in range(n):
            x = min(i, j, n - i - 1, n - j - 1)
            if j >= i:
                print((n-2*x) * (n-2*x) - (i-x) - (j-x), end = " ")
            else:
                print((n-2*x-2) * (n-2*x-2) + (i-x) + (j-x), end = " ")
        print()

printSpiralMatrix(5)