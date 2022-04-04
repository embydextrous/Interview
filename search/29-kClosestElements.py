# https://www.geeksforgeeks.org/find-k-closest-elements-given-value/
from search import binarySearch

def printKClosestElements(a, x, k):
    a.sort()
    idx = binarySearch(a, x)
    i = idx - 1
    j = idx + 1
    while k > 0 and i >= 0 and j < len(a):
        if x - a[i] <= a[j] - x:
            print(a[i], end = " ")
            i -= 1
        else:
            print(a[j], end = " ")
            j += 1
        k -= 1
    while k > 0 and i >= 0:
        print(a[i], end = " ")
        i -= 1
        k -= 1
    while k > 0 and j < len(a):
        print(a[i], end = " ")
        j += 1
        k -= 1
    print()


arr = [12, 16, 22, 30, 35, 39, 42,45, 48, 50, 53, 55, 56]
x = 35
k = 4
printKClosestElements(arr, x, k)