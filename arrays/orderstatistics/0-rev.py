from collections import deque
from heapq import heapify, heappop, heapreplace, heappush

def kMaxSumCombination(a, b, k):
    n = len(a)
    a.sort()
    b.sort()
    visited = set()
    visited.add((n-1, n-1))
    h = [[-a[n-1] - b[n-1], n-1, n-1]]
    for q in range(k):
        (s, i, j) = heappop(h)
        print(f"{a[i]} + {b[j]} = {-s}")
        if j - 1 >= 0 and (i, j - 1) not in visited:
            heappush(h, [-a[i] - b[j-1], i, j - 1])
            visited.add((i, j - 1))
        if i - 1 >= 0 and (i - 1, j) not in visited:
            heappush(h, [-a[i - 1] - b[j], i - 1, j])
            visited.add((i - 1, j))

# 1 2 4 5
# 0 3 5 8  
a = [4, 2, 5, 1]
b = [8, 0, 3, 5]
k = 14
kMaxSumCombination(a, b, k)

    

