# https://www.geeksforgeeks.org/print-all-possible-consecutive-numbers-with-sum-n/
from math import sqrt

def printAll(N):
    for i in range(2, int(sqrt(N))):
        if i % 2 == 0:
            if (N//i) * i + i // 2 == N:
                f = N // i + 1 - i // 2
                t = N // i + 1 + i // 2
                for j in range(f, t):
                    print(j, end = " ")
                print()
        else:
            if (N//i) * i == N:
                f = N // i - i // 2
                t = N // i + i // 2 + 1
                for j in range(f, t):
                    print(j, end = " ")
                print()

printAll(999)
