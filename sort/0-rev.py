
# 12, 13, 14, 15, 16, 17, 18, 19, 20
from math import ceil
from search import binarySearchUtil

def sort(a, k):
    n = len(a)
    x = a[k]
    a.sort()
    ias = binarySearchUtil(a, 0, n - 1, x)
    if ias > k:
        for i in range(ias, k, -1):
            a[ias] = a[ias - 1]
    else:
        for i in range(ias, k):
            a[i] = a[i+1]
    a[k] = x

# 4, 6, 7, 10, 11, 20
# i = 1, j = 4
# 
a = [10, 4, 11, 7, 6, 20]
sort(a, 4)
print(a)