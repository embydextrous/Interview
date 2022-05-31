# https://www.geeksforgeeks.org/print-all-possible-consecutive-numbers-with-sum-n/
from math import sqrt

def printAll(N):
    for i in range(2, int(sqrt(N)+ 1)):
        if i % 2 == 0 and N == (N // i) * i + i // 2:
            first = N // i - i // 2 + 1
            last = N // i + i // 2
            for x in range(first, last + 1):
                print(x, end = " ")
            print()
        elif i % 2 == 1 and N % i == 0:
            first = N // i - i // 2
            last = N // i + i // 2
            for x in range(first, last + 1):
                print(x, end = " ")
            print()

printAll(1000)