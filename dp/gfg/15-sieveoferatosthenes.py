from math import sqrt, ceil

def printPrimes(n):
    a = [True] * n
    a[0] = False
    for i in range(2, ceil(sqrt(n))):
        if a[i-1]:
            m = 2 * i - 1
            while m < n:
                a[m] = False
                m += i
    for i in range(n):
        if a[i]:
            print(i + 1, end = " ")
    print()

printPrimes(1_00_000)
