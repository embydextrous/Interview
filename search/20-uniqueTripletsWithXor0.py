# array is sorted, elements are distinct
# O(n^2)
from search import binarySearchUtil

def findUniqueTriplets(a):
    n = len(a)
    s = set(a)
    c = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] ^ a[j] in s:
                c += 1
    return c // 3

a = [4, 7, 5, 8, 3, 9]
print(findUniqueTriplets(a))
