# https://www.geeksforgeeks.org/binary-insertion-sort/
from random import randint

# Worst case is still O(n^2)
def binaryInsertionSort(a):
    n = len(a)
    for i in range(1, n):
        x = a[i]
        idx = floor(a, 0, i - 1, x)
        for j in range(i - 1, idx, -1):
            a[j + 1] = a[j]
        a[idx + 1] = x

def floor(a, l, r, x):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if a[m] == x:
        return m
    if a[m] < x and (r == m or a[m+1] > x):
        return m
    if a[m] < x:
        return floor(a, m + 1, r, x)
    return floor(a, l, m - 1, x)

a = [randint(1, 20) for i in range(10)]
binaryInsertionSort(a)
print(a)