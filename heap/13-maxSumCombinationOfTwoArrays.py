# https://www.geeksforgeeks.org/k-maximum-sum-combinations-two-arrays/
from heapq import heappush, heappop

def maxSumCombo(a, b, k):
    a.sort()
    b.sort()
    i = len(a) - 1
    j = len(b) - 1
    h = [[-a[i] - b[j], i, j]]
    visited = set()
    visited.add((i, j))
    for i in range(k):
        if len(h) == 0:
            return
        s, i, j = heappop(h)
        print(-s, a[i], b[j])
        if i > 0 and (i-1, j) not in visited:
            visited.add((i-1, j))
            heappush(h, [-a[i-1]-b[j], i-1, j])
        if j > 0 and (i, j - 1) not in visited:
            visited.add((i, j - 1))
            heappush(h, [-a[i]-b[j-1], i, j-1])

a = [4, 2, 5, 1]
b = [8, 0, 3, 5]
k = 3
maxSumCombo(a, b, 14)

