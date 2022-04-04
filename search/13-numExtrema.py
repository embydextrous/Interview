# Extrema  - if two neighbors and both greater or smaller

def numExtrema(a):
    n = len(a)
    c = 0
    for i in range(1, n - 1):
        if (a[i - 1] - a[i]) * (a[i + 1] - a[i]) > 0:
            c += 1
    return c

a = [1, 3, 2]
print(numExtrema(a))