# array is sorted, elements are distinct
# O(nlogn) -> can be done in O(n) via hashing
from search import binarySearchUtil

def findUniqueTriplets(a):
    n = len(a)
    for i in range(n - 2):
        if i != 0 and a[i] == a[i-1]:
            continue
        for j in range(i + 1, n - 1):
            xor = a[i] ^ a[j]
            if xor < a[j]:
                continue
            idx = binarySearchUtil(a, j + 1, n - 1, xor)
            if idx != -1:
                print(a[i], a[j], a[idx])

a = [2, 6, 9, 12, 17, 22, 31, 32, 35, 42]
findUniqueTriplets(a)
