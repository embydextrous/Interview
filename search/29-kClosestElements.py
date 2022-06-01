# https://www.geeksforgeeks.org/find-k-closest-elements-given-value/
from search import binarySearch

def printKClosestElements(a, x, k):
    n = len(a)
    idx = findClosestElementIndex(a, 0, n - 1, x)
    i, j = idx - 1, idx + 1
    if a[idx] != x:
        i = idx
    while i >= 0 and j < n and k > 0:
        if abs(x - a[i]) <= abs(x - a[j]):
            print(a[i], end = " ")
            i -= 1
        else:
            print(a[j], end = " ")
            j += 1
        k -= 1
    while i >= 0 and k > 0:
        print(a[i], end = " ")
        i -= 1
        k -= 1
    while j < n and k > 0:
        print(a[j], end = " ")
        j += 1
        k -= 1
    print()

def findClosestElementIndex(a, l, r, x):
    if l == r:
        return l
    if l + 1 == r:
        return l if abs(x - a[l]) <= abs(x - a[r]) else r
    m = l + (r - l) // 2
    if a[m] == x:
        return m
    if a[m] > x:
        if a[m-1] < x:
            return m if abs(x - a[m]) <= abs(x - a[m-1]) else m-1
        return findClosestElementIndex(a, l, m - 1, x)
    else:
        if a[m+1] > x:
            return m if abs(x - a[m]) <= abs(x - a[m+1]) else m+1
        return findClosestElementIndex(a, m + 1, r, x)


arr = [12, 16, 22, 30, 35, 39, 42,45, 48, 50, 53, 55, 56]
x = 17
k = 9
printKClosestElements(arr, x, k)


arr = [12, 16, 22, 30, 35, 39, 42,45, 48, 50, 53, 55, 56]
x = 35
k = 4
printKClosestElements(arr, x, k)