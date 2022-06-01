from collections import defaultdict
from math import sqrt, ceil
from search import binarySearchUtil

def check(a):
    n = len(a)
    a.sort()
    missCount = 0
    for i in range(a[0] + 1, a[0] + n):
        if binarySearchUtil(a, 0, n - 1, i) == -1:
            missCount += 1
    if missCount == 0:
        return "AC"
    if missCount == 1:
        return a[n-1]
    missCount = 0
    for i in range(a[n-1] - 1, a[0] - n, -1):
        if binarySearchUtil(a, 0, n - 1, i) == -1:
            missCount += 1
    if missCount == 1:
        return a[0]
    return -1

a = [5, 6, 7, 9, 10]
print(check(a))
