
# 26, 27, 29
# 36, 39, 40
# 46, 47, 50
from typing import Counter
from search import binarySearchUtil
from heapq import heapify, heapreplace, heappop

def minSwaps(a, b):
    n = len(a)
    d = {b[i]:i for i in range(n)}
    aux = [[d[a[i]], i] for i in range(n)]
    aux.sort(key = lambda x : x[0])
    i = 0
    visited = set()
    swaps = 0
    while i < n:
        cycleSize = 0
        while i not in visited:
            cycleSize += 1
            visited.add(i)
            i = aux[i][1]
        swaps += max(0, cycleSize - 1)
        i += 1
    return swaps

a = [6, 1, 8, 4, 7, 3, 9, 5, 2]
b = [4, 9, 1, 2, 7, 5, 3, 8, 6]
print(a)
print(b)
print(minSwaps(b, a))