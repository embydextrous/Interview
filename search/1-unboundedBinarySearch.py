# https://www.geeksforgeeks.org/find-the-point-where-a-function-becomes-negative/
# Similar Question

def f(x):
    return x * x - 20 * x - 50

def firstTimePositive():
    if f(0) > 0:
        return 0
    i = 1
    while f(i) <= 0:
        i *= 2
    return binarySearch(i // 2, i)

def binarySearch(l, r):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if f(m) > 0 and (m == l or f(m-1) <= 0):
        return m
    if f(m) <= 0:
        return binarySearch(m + 1, r)
    return binarySearch(l, m - 1)

print(firstTimePositive())
